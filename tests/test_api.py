import io

import pytest

from app import create_app, db


@pytest.fixture()
def client():
    app = create_app({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite://",
        "JWT_SECRET_KEY": "test-jwt-secret",
        "SECRET_KEY": "test-secret",
    })
    with app.app_context():
        db.drop_all()
        db.create_all()
    with app.test_client() as test_client:
        yield test_client
    with app.app_context():
        db.session.remove()
        db.drop_all()


def register(client, email):
    response = client.post("/api/auth/register", json={
        "full_name": "Test Patient",
        "email": email,
        "mobile": "9876543210",
        "password": "StrongPass123",
    })
    assert response.status_code == 201
    return response.get_json()["access_token"]


def auth(token):
    return {"Authorization": f"Bearer {token}"}


def test_patient_can_register_login_and_view_profile(client):
    token = register(client, "patient1@example.com")
    response = client.get("/api/me", headers=auth(token))
    assert response.status_code == 200
    assert response.get_json()["user"]["email"] == "patient1@example.com"

    login = client.post("/api/auth/login", json={
        "email": "patient1@example.com",
        "password": "StrongPass123",
    })
    assert login.status_code == 200
    assert login.get_json()["access_token"]


def test_patient_only_sees_own_prescriptions(client):
    token_a = register(client, "patienta@example.com")
    token_b = register(client, "patientb@example.com")
    upload = client.post(
        "/api/prescriptions",
        headers=auth(token_a),
        data={"file": (io.BytesIO(b"%PDF-1.4\nexample"), "test.pdf", "application/pdf")},
        content_type="multipart/form-data",
    )
    assert upload.status_code == 201
    prescription_id = upload.get_json()["prescription"]["id"]

    list_a = client.get("/api/prescriptions", headers=auth(token_a))
    list_b = client.get("/api/prescriptions", headers=auth(token_b))
    assert len(list_a.get_json()["prescriptions"]) == 1
    assert list_b.get_json()["prescriptions"] == []

    denied_download = client.get(f"/api/prescriptions/{prescription_id}/file", headers=auth(token_b))
    denied_delete = client.delete(f"/api/prescriptions/{prescription_id}", headers=auth(token_b))
    assert denied_download.status_code == 404
    assert denied_delete.status_code == 404


def test_prescriptions_require_login(client):
    assert client.get("/api/prescriptions").status_code == 401


def test_rejects_non_pdf_file_with_pdf_extension(client):
    token = register(client, "patient@example.com")
    response = client.post(
        "/api/prescriptions",
        headers=auth(token),
        data={"file": (io.BytesIO(b"not a pdf"), "fake.pdf", "application/pdf")},
        content_type="multipart/form-data",
    )
    assert response.status_code == 400
