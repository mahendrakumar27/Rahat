# Rahat Development Tracker

## Completed
- [x] Static Rahat website deployed with GitHub Pages.
- [x] Browser-local prescription upload and draft prototype explored earlier.
- [x] Replaced backend-dependent prescription login and API calls in the live frontend with a browser-only patient demo.
- [x] Added IndexedDB storage for uploaded prescription files and metadata.
- [x] Added local list, view/download, and delete actions.
- [x] Added sample patient demo login and clear storage/security warnings.
- [x] Updated project documentation to describe the current frontend-only demo.

## Current demo limitations
- [ ] Secure patient authentication.
- [ ] Server-side/private prescription storage and cross-device synchronization.
- [ ] Verified doctor onboarding and clinician-authored prescriptions.
- [ ] Hosted backend and persistent database deployment.
- [ ] Production privacy/security review, backups, monitoring, and incident response.

## Manual verification still required
- [ ] Test sample login on the published GitHub Pages site.
- [ ] Upload a small sample PDF/image and confirm it appears.
- [ ] Refresh and confirm the record remains in the same browser.
- [ ] Test view/download and delete.
- [ ] Confirm invalid file types and files larger than 8 MB are rejected.
