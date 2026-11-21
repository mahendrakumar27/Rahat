# Rahat Product Requirements Document

## Product goal
Rahat is a rural-health access prototype. This milestone adds real patient accounts and a private prescription area. It is not a production medical-record system.

## Users and scope
- Patient: can register, sign in, view only prescriptions owned by their account, upload an existing prescription, and download/delete their own uploaded copy.
- Doctor: not publicly self-registering in this milestone. A future verified doctor workflow may create clinician-authored prescriptions.
- Administrator: not implemented in this milestone.

## Functional requirements
1. Patient registration requires name, email, mobile number, and a password.
2. Email is unique; passwords are hashed by the backend and never stored as plaintext.
3. Patient login returns a short-lived signed access token.
4. Authenticated patient can view their profile.
5. Authenticated patient can upload PDF/JPEG/PNG/WebP prescriptions (maximum 8 MB).
6. Every prescription is linked server-side to the authenticated patient ID; the API must never accept a patient ID from the browser for ownership.
7. Patient can list, download, and delete only their own uploaded prescriptions.
8. Signed-out users cannot access the patient dashboard or prescription endpoints.
9. UI must clearly state that the current build is a prototype and must not receive real patient records until hosting, secrets, database persistence, HTTPS, access controls, backups, and privacy/legal review are verified.

## Non-functional requirements
- Use Flask, SQLAlchemy, PostgreSQL in hosted deployment, and password hashing.
- CORS must be restricted to the published frontend origin.
- Enforce request size and file-type checks on the server.
- No real OTP claim: email/mobile verification is not included.
- Do not allow patients to create clinician prescriptions or issue medication instructions.

## Acceptance criteria
- Registration and login work against the Flask API.
- Patient A cannot list, download, or delete Patient B's prescription, even by changing an ID in the URL.
- Prescription records survive app restarts when a persistent PostgreSQL database is configured.
- Missing backend configuration produces a clear unavailable message, not fake success.
- Automated tests cover auth, ownership isolation, upload validation, and unauthenticated access.

## Out of scope
Real OTP delivery, doctor onboarding/verification, clinician prescription authoring, appointment booking integration, symptom-history synchronization, and production clinical use.
