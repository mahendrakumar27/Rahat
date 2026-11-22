# Rahat – AI-Powered Rural Health Triage & Referral Assistant

**Rahat** is a web-based healthcare support platform designed to improve access to healthcare information and services in rural areas.

The project aims to help people find healthcare services, understand preliminary symptom information, discover doctors and diagnostic services, and request appointments through a simple interface.

**Live Website:** https://mahendrakumar27.github.io/Rahat/

## 🎯 Project Objectives

- Improve access to healthcare information in rural communities.
- Help users understand preliminary symptom-related information.
- Make doctor and diagnostic service discovery easier.
- Support appointment requests through a digital interface.
- Build a foundation for a scalable rural healthcare referral platform.

## ✨ Key Features

- **Symptom Assessment:** Interface for entering symptoms and viewing preliminary health guidance.
- **Doctor Discovery:** Browse doctor information and availability.
- **Diagnostic Services:** Explore diagnostic services such as blood tests, blood sugar and blood pressure checks.
- **Appointment Requests:** Interface for selecting preferred appointment dates and times.
- **Health History:** Interface for viewing previous health check-ins.
- **My Prescriptions:** Browser-only demo login with prescription upload, local history, download, and delete using IndexedDB.

*Note: The prescription feature is a browser-only demonstration. The sample login is public and not secure authentication; files stay in the current browser and must not contain real patient data. Doctor accounts, clinician-authored prescriptions, OTP verification and confirmed appointment booking are not implemented.*

## 🛠️ Technology Stack

- HTML5
- CSS3
- JavaScript
- IndexedDB (browser-local prescription file storage)
- GitHub Pages (static frontend hosting)
- Earlier Flask API prototype files remain in the repository but are not used by the live prescription demo.

## 🏗️ Project Structure

```text
Rahat/
├── index.html
├── config.js
├── app.py
├── requirements.txt
├── tests/
│   └── test_api.py
├── .github/workflows/backend-tests.yml
├── prd.md
├── architecture.md
├── Design.md
├── Memory.md
├── Rules.md
├── Tracker.md
├── DEPLOYMENT.md
└── README.md
```

The frontend remains a static single-page site. The Flask API is deployed separately.

## 🚀 Run Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/mahendrakumar27/Rahat.git
   ```

2. Open the project folder:

   ```bash
   cd Rahat
   ```

3. Follow `DEPLOYMENT.md` to start the Flask API and serve the frontend locally.

The live prescription demo does not require a backend. Use the sample patient login shown on the website. Prescription files remain in the browser profile where they were uploaded.

## 🌐 Live Deployment

The project is hosted using GitHub Pages.

Visit: https://mahendrakumar27.github.io/Rahat/

## 🔮 Future Enhancements

- Add verified doctor onboarding and clinician-authored prescriptions.
- Add email/mobile verification and account recovery.
- Add verified government healthcare facilities across Satara district.
- Integrate location-based hospital and PHC discovery.
- Implement real appointment request and tracking functionality.
- Develop a clinically validated symptom triage and referral workflow.
- Add Marathi language support.
- Improve mobile responsiveness and accessibility.

## ⚠️ Disclaimer

Rahat is a healthcare technology prototype and is not a replacement for professional medical advice, diagnosis or treatment.

Users should consult qualified healthcare professionals for medical decisions. Emergency symptoms require immediate medical attention.

## 👨‍💻 Project Information

## 👨‍💻 Project Developers

This project was collaboratively developed by:

1. **Mahendrakumar Surana**
2. **Ayush Jadhav**

Both developers contributed to the design and development of Rahat.

## 📌 Project Information

- **Project Name:** Rahat
- **Project Domain:** Healthcare Technology
- **Focus Area:** Rural Healthcare Access and Referral Support
- **Development:** Collaborative Project
- **Repository:** https://github.com/mahendrakumar27/Rahat
- **Live Website:** https://mahendrakumar27.github.io/Rahat/
---

⭐ If you find this project interesting, consider exploring the repository and following its development.


## Patient accounts and prescriptions (development milestone)

The current live prescription feature is a frontend-only demonstration. It uses a public sample patient login and IndexedDB to keep uploaded prescription copies in the current browser. The older Flask API implementation remains in the repository but is not connected to the live frontend.

- Backend: `app.py`
- Dependencies: `requirements.txt`
- Automated API tests: `tests/test_api.py`
- Deployment guide: `DEPLOYMENT.md`
- Frontend API setting: `config.js`

**Important:** The sample login is public and is not secure authentication. IndexedDB is local browser storage, not a private server or backup. Do not upload real patient documents. The demo supports patient-uploaded copies only; clinician-authored prescriptions are not implemented.

Earlier backend files (`app.py`, `requirements.txt`, `tests/`, `config.js`, and `DEPLOYMENT.md`) are retained for future development and are not required to run the current GitHub Pages demo.

**Important:** This is a development prototype. Email/mobile OTP verification and doctor accounts are not implemented. Do not upload real patient records until the backend is deployed with a persistent database, HTTPS, secure secrets, backups, access controls, and an appropriate privacy/security review.
