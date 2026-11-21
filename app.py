import os
import re
from datetime import timedelta
from io import BytesIO

from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity, jwt_required
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select
from werkzeug.security import check_password_hash, generate_password_hash
from PIL import Image, UnidentifiedImageError

db = SQLAlchemy()
jwt = JWTManager()

ALLOWED_IMAGE_TYPES = {"image/jpeg", "image/png", "image/webp"}
ALLOWED_EXTENSIONS = {".pdf", ".jpg", ".jpeg", ".png", ".webp"}


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(254), unique=True, nullable=False, index=True)
    mobile = db.Column(db.String(10), nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), nullable=False, default="patient")
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())


class Prescription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False, index=True)
    original_filename = db.Column(db.String(180), nullable=False)
    mime_type = db.Column(db.String(80), nullable=False)
    file_data = db.Column(db.LargeBinary, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())


def create_app(test_config=None):
    app = Flask(__name__)
    database_url = os.getenv("DATABASE_URL", "sqlite:///rahat.db")
    if database_url.startswith("postgres://"):
        database_url = database_url.replace("postgres://", "postgresql://", 1)

    app.config.update(
        SECRET_KEY=os.getenv("SECRET_KEY", "local-development-secret-change-this"),
        JWT_SECRET_KEY=os.getenv("JWT_SECRET_KEY", "local-jwt-secret-change-this"),
        JWT_ACCESS_TOKEN_EXPIRES=timedelta(hours=2),
        SQLALCHEMY_DATABASE_URI=database_url,
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        MAX_CONTENT_LENGTH=8 * 1024 * 1024,
    )
    if test_config:
        app.config.update(test_config)

    if os.getenv("RAHAT_ENV") == "production":
        if not os.getenv("SECRET_KEY") or not os.getenv("JWT_SECRET_KEY"):
            raise RuntimeError("Set SECRET_KEY and JWT_SECRET_KEY before production startup.")
        if app.config["SQLALCHEMY_DATABASE_URI"].startswith("sqlite"):
            raise RuntimeError("Production must use a persistent PostgreSQL DATABASE_URL.")

    db.init_app(app)
    jwt.init_app(app)
    origins = os.getenv("CORS_ORIGINS", "https://mahendrakumar27.github.io").split(",")
    CORS(app, resources={r"/api/*": {"origins": [item.strip() for item in origins if item.strip()]}})

    @app.get("/api/health")
    def health():
        return jsonify(status="ok", service="Rahat API")

    @app.post("/api/auth/register")
    def register():
        data = request.get_json(silent=True) or {}
        full_name = str(data.get("full_name", "")).strip()
        email = str(data.get("email", "")).strip().lower()
        mobile = re.sub(r"\D", "", str(data.get("mobile", "")))
        password = str(data.get("password", ""))

        if not full_name or len(full_name) > 100:
            return jsonify(error="Enter your name (up to 100 characters)."), 400
        if not re.fullmatch(r"[^\s@]+@[^\s@]+\.[^\s@]+", email) or len(email) > 254:
            return jsonify(error="Enter a valid email address."), 400
        if not re.fullmatch(r"\d{10}", mobile):
            return jsonify(error="Enter a valid 10-digit mobile number."), 400
        if len(password) < 10 or len(password) > 128:
            return jsonify(error="Password must be 10 to 128 characters long."), 400
        if db.session.scalar(select(User).where(User.email == email)):
            return jsonify(error="An account with this email already exists."), 409

        user = User(
            full_name=full_name,
            email=email,
            mobile=mobile,
            password_hash=generate_password_hash(password),
            role="patient",
        )
        db.session.add(user)
        db.session.commit()
        token = create_access_token(identity=str(user.id))
        return jsonify(message="Account created.", access_token=token, user=user_payload(user)), 201

    @app.post("/api/auth/login")
    def login():
        data = request.get_json(silent=True) or {}
        email = str(data.get("email", "")).strip().lower()
        password = str(data.get("password", ""))
        user = db.session.scalar(select(User).where(User.email == email))
        if not user or not check_password_hash(user.password_hash, password):
            return jsonify(error="Email or password is incorrect."), 401
        token = create_access_token(identity=str(user.id))
        return jsonify(message="Signed in.", access_token=token, user=user_payload(user))

    @app.get("/api/me")
    @jwt_required()
    def me():
        user = current_user()
        if not user:
            return jsonify(error="Account not found."), 404
        return jsonify(user=user_payload(user))

    @app.get("/api/prescriptions")
    @jwt_required()
    def list_prescriptions():
        user = current_user()
        if not user:
            return jsonify(error="Account not found."), 404
        rows = db.session.scalars(
            select(Prescription).where(Prescription.patient_id == user.id).order_by(Prescription.created_at.desc())
        ).all()
        return jsonify(prescriptions=[prescription_payload(row) for row in rows])

    @app.post("/api/prescriptions")
    @jwt_required()
    def upload_prescription():
        user = current_user()
        if not user:
            return jsonify(error="Account not found."), 404
        uploaded = request.files.get("file")
        if not uploaded or not uploaded.filename:
            return jsonify(error="Choose a prescription file."), 400
        filename = uploaded.filename.rsplit("/", 1)[-1].rsplit("\\", 1)[-1]
        extension = os.path.splitext(filename)[1].lower()
        if extension not in ALLOWED_EXTENSIONS:
            return jsonify(error="Only PDF, JPG, PNG, and WebP files are allowed."), 400

        raw = uploaded.read()
        if not raw or len(raw) > 8 * 1024 * 1024:
            return jsonify(error="File must be between 1 byte and 8 MB."), 400
        mime_type = uploaded.mimetype or ""
        if extension == ".pdf":
            if not raw.startswith(b"%PDF-"):
                return jsonify(error="The file does not look like a valid PDF."), 400
            mime_type = "application/pdf"
        else:
            if mime_type not in ALLOWED_IMAGE_TYPES:
                return jsonify(error="Unsupported image type."), 400
            try:
                image = Image.open(BytesIO(raw))
                image.verify()
                expected = {".jpg": "JPEG", ".jpeg": "JPEG", ".png": "PNG", ".webp": "WEBP"}[extension]
                if image.format != expected:
                    return jsonify(error="The image content does not match its file extension."), 400
            except (UnidentifiedImageError, OSError, ValueError):
                return jsonify(error="The uploaded image could not be validated."), 400

        row = Prescription(
            patient_id=user.id,
            original_filename=filename[:180],
            mime_type=mime_type,
            file_data=raw,
        )
        db.session.add(row)
        db.session.commit()
        return jsonify(message="Prescription uploaded.", prescription=prescription_payload(row)), 201

    @app.get("/api/prescriptions/<int:prescription_id>/file")
    @jwt_required()
    def download_prescription(prescription_id):
        user = current_user()
        row = db.session.scalar(
            select(Prescription).where(
                Prescription.id == prescription_id,
                Prescription.patient_id == user.id if user else False,
            )
        )
        if not row:
            return jsonify(error="Prescription not found."), 404
        return send_file(
            BytesIO(row.file_data),
            mimetype=row.mime_type,
            as_attachment=True,
            download_name=row.original_filename,
            max_age=0,
        )

    @app.delete("/api/prescriptions/<int:prescription_id>")
    @jwt_required()
    def delete_prescription(prescription_id):
        user = current_user()
        row = db.session.scalar(
            select(Prescription).where(
                Prescription.id == prescription_id,
                Prescription.patient_id == user.id if user else False,
            )
        )
        if not row:
            return jsonify(error="Prescription not found."), 404
        db.session.delete(row)
        db.session.commit()
        return jsonify(message="Prescription deleted.")

    @app.errorhandler(413)
    def too_large(_error):
        return jsonify(error="File is too large. Maximum size is 8 MB."), 413

    with app.app_context():
        db.create_all()

    return app


def current_user():
    identity = get_jwt_identity()
    try:
        return db.session.get(User, int(identity))
    except (TypeError, ValueError):
        return None


def user_payload(user):
    return {
        "id": user.id,
        "full_name": user.full_name,
        "email": user.email,
        "mobile": user.mobile,
        "role": user.role,
    }


def prescription_payload(row):
    return {
        "id": row.id,
        "filename": row.original_filename,
        "mime_type": row.mime_type,
        "created_at": row.created_at.isoformat() if row.created_at else None,
    }


app = create_app()

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=int(os.getenv("PORT", "5000")), debug=os.getenv("FLASK_DEBUG") == "1")
