# Rahat Design Notes

## Patient demo journey
1. Home → Patient Prescription Management.
2. Patient selects Patient Login and uses the published sample patient credentials.
3. Successful login opens My Prescriptions.
4. Patient uploads a PDF or supported image (maximum 8 MB).
5. Patient sees uploaded copies and digital records created for the sample patient.
6. Patient can download records or delete uploaded copies.
7. Logout ends the patient demo session.

## Doctor demo journey
1. Home → Doctor Login.
2. Doctor uses the published sample doctor credentials.
3. Successful login opens Doctor Dashboard.
4. Doctor enters patient name/email, diagnosis, medicines and dosage, and optional instructions.
5. Saving creates a browser-local digital prescription linked to the sample patient email.
6. Doctor sees records created by that demo account and can download them.
7. Logout ends the doctor demo session.

## UI rules
- Use the existing Rahat blue/white visual language.
- Keep patient and doctor login paths visibly separate.
- Clearly label both roles and prescription workflow as a browser-only demo.
- Explain that IndexedDB data is local to the current browser and can be cleared.
- Never claim the sample logins are secure, doctor identity is verified, or files are uploaded to a server.
- Do not encourage real patient records or real medication instructions.
- Show visible loading, validation, success, and storage error messages.
- Empty states should explain when no records exist.

## Accessibility
Use associated labels, visible errors, keyboard-accessible controls, and responsive layouts.
