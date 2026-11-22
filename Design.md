# Rahat Design Notes

## Patient demo journey
1. Home → Patient Login.
2. Demo login screen displays the sample patient email and password.
3. Successful demo login opens My Prescriptions.
4. Dashboard displays the demo patient's locally stored prescription copies.
5. Patient uploads a PDF or supported image (maximum 8 MB).
6. Patient can view/download or delete each saved file.
7. Logout ends the current demo session and returns to the home page.

## UI rules
- Use the existing Rahat blue/white visual language.
- Clearly label the feature as a browser-only demo.
- Explain that IndexedDB data is local to the current browser and can be cleared.
- Never claim the sample login is secure or that files are uploaded to a server.
- Do not encourage real patient records or medical document uploads.
- Do not expose a patient-facing clinician prescription creation form.
- Show visible loading, validation, success, and storage error messages.
- Empty state: "No prescriptions are linked to this account yet."

## Accessibility
Use associated labels, visible errors, keyboard-accessible controls, and responsive layouts.
