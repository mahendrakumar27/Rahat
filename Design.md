# Rahat Design Notes

## Patient journey
1. Home → Login / Sign up.
2. Sign up with full name, email, mobile number, and password.
3. Sign in with email and password.
4. Successful authentication opens the patient dashboard.
5. Dashboard shows the patient's name and their own uploaded prescriptions.
6. Patient uploads a PDF or supported image; the list refreshes from the backend.
7. Patient can open/download or delete their own file.
8. Logout clears the session token and returns to the home page.

## UI rules
- Use existing Rahat blue/white visual language.
- Never show a fake OTP or claim a message was sent.
- Show clear loading, success, validation, and API-unavailable states.
- Hide the old patient-facing "create prescription draft" form; patients cannot author clinician prescriptions.
- Label this milestone as a prototype and warn against real patient data until production controls are verified.
- Empty state: "No prescriptions are linked to this account yet."

## Accessibility
Use associated labels, visible errors, keyboard-accessible controls, and responsive layouts.
