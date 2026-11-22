# Rahat Product Requirements Document

## Product goal
Rahat is a rural-health access prototype. This milestone provides a browser-only prescription upload demonstration that can run on GitHub Pages without a deployed backend.

## Users and scope
- Demo patient: signs in with the published sample credentials and manages prescription file copies stored locally in their own browser.
- Doctor: clinician-authored prescriptions and doctor accounts are not part of this milestone.
- Administrator: not implemented.

## Functional requirements
1. The demo patient can sign in using the sample credentials displayed on the login screen.
2. The patient can upload PDF, JPEG, PNG, or WebP prescription copies up to 8 MB.
3. Prescription files and metadata are stored in browser IndexedDB.
4. The patient can list, view/download, and delete their local prescription copies.
5. Records remain available in the same browser profile after refresh, subject to browser storage remaining intact.
6. The app clearly explains that this is a public demo, not secure authentication or medical-record storage.
7. The static site must not require a Flask API URL for the prescription demo.

## Non-functional requirements
- Keep the frontend compatible with static GitHub Pages hosting.
- Use IndexedDB for binary file storage; do not store uploaded file bytes in localStorage.
- Do not claim that the sample login protects records. The demo credentials are public.
- Do not encourage real patient records or medical documents to be uploaded.
- Do not allow patients to create clinician-authored prescriptions or medication instructions.

## Acceptance criteria
- The live GitHub Pages site can open the prescription section without a deployed API.
- The displayed sample patient credentials sign in successfully.
- Uploading an allowed file adds it to the prescription list.
- Refreshing the page preserves the uploaded item in the same browser profile.
- View/download returns the stored file and delete removes it from the local list.
- Invalid file types and files over 8 MB are rejected with a visible message.
- Signed-out visitors are redirected to the demo login before accessing the prescription view.

## Out of scope
Secure multi-user authentication, server-side storage, cloud synchronization, verified doctor accounts, clinician-authored prescriptions, real OTP delivery, appointment booking integration, and production clinical use.
