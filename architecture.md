# Rahat Architecture

## Current deployment shape
- Frontend: static HTML/CSS/JavaScript on GitHub Pages.
- Backend: Flask REST API, deployed separately (for example, Render).
- Database: PostgreSQL for hosted use; SQLite is supported for local development only.
- Prescription file bytes: stored in the database for this small prototype, behind authenticated download routes. A production-scale service should move files to private object storage with signed, short-lived access.

## Authentication
- Public patient registration creates role `patient` only.
- Passwords are stored as Werkzeug password hashes.
- Login returns a short-lived JWT access token.
- Frontend keeps the token in sessionStorage (cleared when the browser tab session ends).
- Every protected route validates the JWT.
- The server derives patient ownership from JWT identity; client-supplied owner IDs are never trusted.
- Doctor accounts are not self-service and are out of scope until a verified onboarding process exists.

## Data model
- User: id, full_name, email (unique), mobile, password_hash, role, created_at.
- Prescription: id, patient_id foreign key, original filename, MIME type, binary file data, created_at.
- The patient_id foreign key is assigned from the authenticated token on upload.

## API
- POST /api/auth/register
- POST /api/auth/login
- GET /api/me
- GET /api/prescriptions
- POST /api/prescriptions (multipart upload)
- GET /api/prescriptions/{id}/file
- DELETE /api/prescriptions/{id}
- GET /api/health

## Deployment requirements
Set SECRET_KEY, JWT_SECRET_KEY, DATABASE_URL, and CORS_ORIGINS as environment variables. Use HTTPS and a persistent PostgreSQL database. Never commit real secrets or patient records. The GitHub Pages frontend needs the deployed API URL in js/config.js.
