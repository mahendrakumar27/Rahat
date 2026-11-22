# Rahat Development Tracker

## Completed
- [x] Static Rahat website deployed with GitHub Pages.
- [x] Browser-local patient prescription upload, list, download, and delete.
- [x] Patient demo login with clear storage/security warnings.
- [x] Added separate doctor demo login and doctor dashboard.
- [x] Added doctor-authored digital prescription records with patient, diagnosis, medicines/dosage, and instructions.
- [x] Linked doctor-created demo records to the sample patient account in IndexedDB.
- [x] Added patient access to doctor-created records and text download.
- [x] Updated project documentation for the two-role browser-only workflow.

## Current demo limitations
- [ ] Secure patient and doctor authentication.
- [ ] Verified doctor identity and clinical authorization.
- [ ] Server-side/private prescription storage and cross-device synchronization.
- [ ] Signed/regulated e-prescription workflow and audit trail.
- [ ] Hosted backend and persistent database deployment.
- [ ] Production privacy/security, clinical, and regulatory review.

## Manual verification still required
- [ ] Test patient login and patient upload on the published GitHub Pages site.
- [ ] Test doctor login and creation of a digital prescription.
- [ ] Confirm the created record appears in the doctor list and patient account in the same browser profile.
- [ ] Download and inspect the doctor-created text prescription.
- [ ] Test patient view/download/delete for uploaded files.
- [ ] Confirm invalid file types and files larger than 8 MB are rejected.
- [ ] Confirm role logout and login guards work.
