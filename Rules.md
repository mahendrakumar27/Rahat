# Rahat Development Rules

1. Read prd.md, architecture.md, Design.md, Memory.md, Rules.md, and Tracker.md before planning or changing project code.
2. Inspect current repository files before editing; do not overwrite unseen content.
3. Keep the frontend compatible with GitHub Pages (static hosting).
4. Keep secrets, credentials, tokens, and real patient data out of Git.
5. Never store plaintext passwords. Never trust patient IDs supplied by the frontend.
6. Every patient prescription query, download, and delete must enforce ownership on the server.
7. Do not expose patient uploads through public static URLs.
8. Do not let patients create clinician prescriptions or medical advice.
9. Clearly label prototype limitations; do not present demo features as production-ready.
10. Add/update tests and documentation when backend behavior changes.
11. Use simple, beginner-readable code and explain deployment steps in sequence.
12. Do not make real clinical safety claims or populate unverified facility/doctor data as facts.
