# Rahat Development Rules

1. Read prd.md, architecture.md, Design.md, Memory.md, Rules.md, and Tracker.md before planning or changing project code.
2. Inspect current repository files before editing; do not overwrite unseen content.
3. Keep the current live frontend compatible with GitHub Pages static hosting unless a backend migration is explicitly planned.
4. Keep secrets, real credentials, tokens, and real patient data out of Git.
5. Public patient and doctor demo credentials are not authentication and must not be presented as secure.
6. Use IndexedDB for browser-local prescription file blobs and records; do not put file bytes in localStorage.
7. Clearly explain that browser-local files can be cleared and do not sync or back up.
8. Do not encourage real patient records or real medication instructions to be entered into the demo.
9. Clearly label doctor-created records as demo records, not signed or clinically valid prescriptions.
10. Do not claim doctor identity verification, secure role-based access, or server-side access control in this frontend-only prototype.
11. Do not claim the Flask backend is deployed or used by the live frontend unless that changes and is verified.
12. Clearly label prototype limitations; do not present demo features as production-ready.
13. Use simple, beginner-readable code and explain deployment steps in sequence.
14. Do not make real clinical safety claims or populate unverified facility/doctor data as facts.
