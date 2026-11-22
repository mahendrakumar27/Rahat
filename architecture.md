# Rahat Architecture

## Current prescription demo
- Frontend: static HTML, CSS, and JavaScript in `index.html`.
- Hosting: GitHub Pages.
- Authentication: separate fixed public demo credentials for patient and doctor; sessionStorage keeps each role's current demo session. This is navigation for demonstration only, not security.
- Prescription data: browser IndexedDB database `rahat_prescriptions_demo`, object store `prescriptions`.
- Patient uploads: store file blob and metadata with `ownerEmail`.
- Doctor-authored records: store patient name/email, doctor name/email, diagnosis, medicines/dosage, instructions, and timestamp with `recordType: doctor-authored`.
- No backend URL or Flask API is required for the live prescription demo.

## Data flow
1. Patient or doctor chooses the corresponding login entry point.
2. Frontend checks entered values against that role's published demo credentials.
3. Patient uploads are validated for supported type and 8 MB maximum, then stored in IndexedDB.
4. Doctor enters a digital prescription for the sample patient; the record is stored in IndexedDB.
5. Both role dashboards filter records by patient email or creating doctor email.
6. Digital prescription records can be downloaded as text files; uploaded patient files can be downloaded in their original format.

## Existing backend files
The repository retains an earlier Flask API implementation (`app.py`, `requirements.txt`, tests, and deployment notes), but the current GitHub Pages prescription demo does not call or require that API. Do not describe the backend as deployed or active.

## Limitations
- Both demo passwords are public and are not secure authentication.
- The doctor account is not verified; anyone can use its public credentials.
- IndexedDB data stays in the current browser profile. It is not shared across devices, browsers, or users.
- Browser storage can be cleared or evicted; it is not a backup.
- This workflow is not clinically valid or appropriate for real prescribing or patient records.
- Digital prescriptions are demo text records, not signed, verified, regulated e-prescriptions.

## Future architecture
A production-oriented version requires a separately deployed API, secure authentication, verified clinician identity and role-based access control, private persistent storage, audit logs, backups, HTTPS, monitoring, and privacy/security and regulatory review before real patient data or prescribing is considered.
