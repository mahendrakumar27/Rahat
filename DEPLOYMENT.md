# Rahat backend setup and deployment

## 1. Run the API locally

Use Python 3.11 or newer.

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
$env:CORS_ORIGINS="http://127.0.0.1:8000,http://localhost:8000"
python app.py
```

The API starts at `http://127.0.0.1:5000`. Its local SQLite database is created as `rahat.db`.

In a second terminal, serve the website from the repository root:

```bash
python -m http.server 8000
```

Open `http://127.0.0.1:8000`. The local `config.js` must temporarily contain:

```javascript
window.RAHAT_API_BASE_URL = "http://127.0.0.1:5000";
```

Do not commit local secrets or real patient data.

## 2. Run automated tests

```bash
pip install -r requirements.txt
pytest -q
```

The tests cover patient registration/login, protected routes, upload validation, and prescription ownership isolation.

## 3. Deploy the API

The GitHub Pages website cannot run Flask. Deploy this repository as a separate Python web service (for example, on Render) and provision a persistent PostgreSQL database.

For a Render web service:
- Build command: `pip install -r requirements.txt`
- Start command: `gunicorn app:app`
- Health check path: `/api/health`

Set these environment variables in the backend host:
- `RAHAT_ENV` = `production`
- `DATABASE_URL` = the PostgreSQL connection URL supplied by the host
- `SECRET_KEY` = a newly generated long random secret
- `JWT_SECRET_KEY` = a different newly generated long random secret
- `CORS_ORIGINS` = `https://mahendrakumar27.github.io`

Use the provider's internal PostgreSQL connection URL where supported. Do not paste secrets into GitHub files, screenshots, or chat messages. Confirm that the database plan provides persistent storage and backups; a temporary/free database may expire.

## 4. Connect GitHub Pages to the deployed API

After deployment, copy the backend's HTTPS service URL. Edit `config.js`:

```javascript
window.RAHAT_API_BASE_URL = "https://YOUR-ACTUAL-API-HOST";
```

Commit the real service URL (not a secret) and wait for GitHub Pages to publish. Then test registration, logout, login, upload, refresh, download, and delete.

## Important limitations

- This milestone has email/password registration, not email or SMS OTP verification.
- Doctor registration and clinician-authored prescriptions are not implemented. Patients can upload copies of prescriptions they already have; they cannot create a medical prescription.
- The API stores uploaded file bytes in PostgreSQL for this small prototype. A larger production service should use private object storage, malware scanning, audit logging, rate limiting, database migrations, backups, monitoring, and a formal security/privacy review.
- Do not use real patient data until those safeguards and applicable legal requirements have been reviewed and verified.
