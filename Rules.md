# Rahat Development Rules

1. Read prd.md, architecture.md, Design.md, Memory.md, Rules.md, and Tracker.md before planning or changing project code.
2. Inspect current repository files before editing; do not overwrite unseen content.
3. Keep the current live frontend compatible with GitHub Pages static hosting.
4. Keep secrets, real credentials, tokens, and real patient data out of Git.
5. Public demo credentials are not authentication and must not be presented as secure.
6. Use IndexedDB for browser-local prescription file blobs; do not put file bytes in localStorage.
7. Clearly explain that browser-local files can be cleared and do not sync or back up.
8. Do not encourage real patient records or medical documents to be uploaded to the demo.
9. Do not let patients create clinician prescriptions or medication advice.
10. Do not claim the Flask backend is deployed or used by the live frontend unless that changes and is verified.
11. Clearly label prototype limitations; do not present demo features as production-ready.
12. Use simple, beginner-readable code and explain deployment steps in sequence.
13. Do not make real clinical safety claims or populate unverified facility/doctor data as facts.
