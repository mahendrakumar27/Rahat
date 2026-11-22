# Rahat – AI-Powered Rural Health Triage & Referral Assistant

**Rahat** is a web-based healthcare support platform designed to improve access to healthcare information and services in rural areas.

**Live Website:** https://mahendrakumar27.github.io/Rahat/

## Key Features
- Symptom assessment interface and preliminary guidance.
- Doctor discovery and diagnostic service discovery.
- Appointment request interface.
- Symptom history.
- Patient prescription management: upload, view/download, and delete prescription copies.
- Doctor demo login: create and review digital prescription records for the sample patient.
- Patient dashboard can view/download doctor-created demo records.

## Prescription demo credentials

**Patient**
- Email: `patient@rahat.demo`
- Password: `Patient@123`

**Doctor**
- Email: `doctor@rahat.demo`
- Password: `Doctor@123`

These are public sample credentials for demonstration only. They do not provide secure authentication or verify a doctor's identity.

## Technology
- HTML5, CSS3, JavaScript
- IndexedDB for browser-local prescription records and uploaded file blobs
- GitHub Pages static hosting
- Earlier Flask API prototype files remain in the repository but are not connected to the live prescription demo.

## Important limitations
The prescription workflow is a frontend-only demonstration. Patient uploads and doctor-created demo records are stored in IndexedDB in the current browser profile. They do not sync across devices or browser profiles and may be cleared by browser storage cleanup.

Doctor-created records are unsigned text-based demo records, not valid clinical prescriptions. Doctor identity is not verified. Do not enter real patient data or real medication instructions. A production system would require secure authentication, verified clinician onboarding, server-side private storage, access controls, audit logs, backups, HTTPS, and privacy/security and regulatory review.

## Project structure
```text
Rahat/
├── index.html
├── config.js
├── app.py
├── requirements.txt
├── tests/
├── prd.md
├── architecture.md
├── Design.md
├── Memory.md
├── Rules.md
├── Tracker.md
├── DEPLOYMENT.md
└── README.md
```

## Run locally
1. Clone `https://github.com/mahendrakumar27/Rahat.git`.
2. Open the repository folder.
3. Open `index.html` in a browser for the static frontend demo.
4. The live prescription demo does not require a backend.

## Project developers
1. Mahendrakumar Surana
2. Ayush Jadhav

## Disclaimer
Rahat is a healthcare technology prototype and is not a replacement for professional medical advice, diagnosis, or treatment. Emergency symptoms require immediate medical attention.
