# Rahat Project Memory

## Repository
- GitHub: mahendrakumar27/Rahat
- Default branch: main
- Frontend entry point: index.html
- Published frontend: https://mahendrakumar27.github.io/Rahat/
- Current prescription demo: static HTML/CSS/JavaScript with IndexedDB.
- Earlier Flask backend files remain in the repository but are not required by the current GitHub Pages demo.

## Collaboration
- Project developers listed in README: Mahendrakumar Surana and Ayush Jadhav.
- User is a beginner in backend development; explain setup in small, ordered steps.

## Public demo credentials
- Patient email: patient@rahat.demo
- Patient password: Patient@123
- Doctor email: doctor@rahat.demo
- Doctor password: Doctor@123
- These credentials are intentionally public demo credentials, not secure authentication.

## Prescription workflow
- Patient can upload PDF/JPEG/PNG/WebP files up to 8 MB.
- Doctor can create text-based demo prescription records for the sample patient.
- Digital records include patient, doctor, diagnosis, medicines/dosage, optional instructions, and timestamp.
- Both roles see relevant records only within the same browser profile's local IndexedDB.

## Safety and accuracy
- Prescription data is stored only in the current browser profile using IndexedDB.
- Do not describe local browser storage as a secure patient record system or backup.
- Do not encourage real medical documents or real medication instructions to be entered.
- Doctor identity is not verified; demo prescriptions are not signed or clinically valid.
- Never claim OTP, email verification, real doctor verification, or server synchronization unless implemented and tested.
