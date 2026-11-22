# Rahat Architecture

## Current prescription demo
- Frontend: static HTML, CSS, and JavaScript in `index.html`.
- Hosting: GitHub Pages.
- Authentication: fixed public demo credentials; a sessionStorage flag identifies the current demo session. This is navigation for demonstration only, not security.
- Prescription files: browser IndexedDB stores file blobs and metadata. Each record is associated with the demo patient's email.
- No backend URL or Flask API is required for the live prescription demo.

## Data flow
1. The visitor enters the sample patient credentials.
2. The frontend checks the entered values against the published demo credentials.
3. The upload form validates file type and the 8 MB size limit.
4. IndexedDB stores the file blob, filename, MIME type, owner email, and upload timestamp.
5. The dashboard reads records for the current demo email and supports download and delete.

## Existing backend files
The repository retains an earlier Flask API implementation (`app.py`, `requirements.txt`, tests, and deployment notes), but the current GitHub Pages prescription demo does not call or require that API. Do not describe the backend as deployed or active.

## Limitations
- The demo password is public and must never be treated as secure authentication.
- IndexedDB data stays in the current browser profile and does not sync across devices or users.
- Browser storage can be cleared or evicted; it is not a backup.
- Browser-local storage is not suitable for real patient records or confidential medical documents.
- Doctor accounts and clinician-authored prescriptions are not implemented.

## Future architecture
A future production-oriented version would need a separately deployed API, secure authentication, verified roles, private persistent storage, access-control enforcement, HTTPS, backups, monitoring, and privacy/security review before real patient data is considered.
