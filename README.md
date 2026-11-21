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
- **User Authentication Interface:** Login and registration screens.

*Note: The availability of backend services, real OTP verification, persistent health records and confirmed appointment booking must be verified separately. Interface availability does not necessarily mean these services are operational.*

## 🛠️ Technology Stack

- HTML5
- CSS3
- JavaScript
- GitHub Pages (deployment and hosting)

## 🏗️ Project Structure

```text
Rahat/
│
├── index.html
└── README.md
```

The current website is maintained as a single HTML file. Its structure can be modularized as the project develops.

## 🚀 Run Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/mahendrakumar27/Rahat.git
   ```

2. Open the project folder:

   ```bash
   cd Rahat
   ```

3. Open `index.html` in your web browser.

No additional server is required for the static website.

## 🌐 Live Deployment

The project is hosted using GitHub Pages.

Visit: https://mahendrakumar27.github.io/Rahat/

## 🔮 Future Enhancements

- Integrate a reliable backend and database.
- Develop verified OTP-based authentication.
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

The repository now includes a Flask API for patient registration, login, and account-linked prescription uploads. The static website remains on GitHub Pages; the API must be deployed separately.

- Backend: `app.py`
- Dependencies: `requirements.txt`
- Automated API tests: `tests/test_api.py`
- Deployment guide: `DEPLOYMENT.md`
- Frontend API setting: `config.js`

Patient accounts use password hashes and short-lived JWT access tokens. Prescription ownership is assigned by the backend from the authenticated account, not from a patient ID sent by the browser. Patients can list, download, and delete only their own uploaded files.

**Important:** This is a development prototype. Email/mobile OTP verification and doctor accounts are not implemented. Do not upload real patient records until the backend is deployed with a persistent database, HTTPS, secure secrets, backups, access controls, and an appropriate privacy/security review.
