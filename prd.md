# Rahat Product Requirements Document

## Product goal
Rahat is a rural-health access prototype. This milestone demonstrates patient-uploaded prescription copies and clinician-authored digital prescription records in a browser-only workflow on GitHub Pages.

## Users and scope
- Demo patient: signs in with the published sample patient credentials, uploads prescription copies, and views/downloads patient-linked records.
- Demo doctor: signs in with separate public sample credentials, creates digital prescription records for the sample patient, and views/downloads records created by that demo account.
- Administrator: not implemented.

## Functional requirements
1. Patient and doctor have separate login screens and separate demo sessions.
2. Patient can upload PDF, JPEG, PNG, or WebP prescription copies up to 8 MB.
3. Patient-uploaded files and prescription metadata are stored in browser IndexedDB.
4. Doctor can create a digital prescription with patient name/email, diagnosis, medicines/dosage, and additional instructions.
5. Doctor-created records are linked to the sample patient email and the creating demo doctor account.
6. Patient can view/download own uploaded copies and doctor-created records.
7. Doctor can list and download records created by the current demo doctor.
8. Patient and doctor can log out independently.
9. The app clearly explains that this is a public browser-only demo, not secure authentication or clinical record storage.
10. The static site must not require a Flask API URL for the prescription demo.

## Non-functional requirements
- Keep the frontend compatible with static GitHub Pages hosting.
- Use IndexedDB for binary file storage and prescription records.
- Public demo credentials are not authentication and must not be presented as secure.
- Browser-local data is not shared across devices or different browser profiles.
- Do not encourage real patient records or real medication instructions to be entered.
- The demo must not be presented as a clinically valid prescribing system.

## Acceptance criteria
- Patient sample login opens My Prescriptions.
- Doctor sample login opens Doctor Dashboard.
- Doctor can create a prescription linked to patient@rahat.demo.
- Created record appears in the doctor's list and the patient's list in the same browser profile.
- Patient can download the digital record as a text file.
- Doctor can download a record created by that doctor demo account.
- Patient can upload, view/download, and delete their own uploaded files.
- Invalid file types and files over 8 MB are rejected.
- Signed-out users are redirected to the correct role login.

## Out of scope
Verified doctor identity, secure multi-user authentication, server-side storage, cross-device synchronization, real clinical prescribing, e-prescription regulatory compliance, real OTP delivery, and production clinical use.
