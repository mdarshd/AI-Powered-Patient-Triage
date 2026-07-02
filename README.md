<div align="center">

# 🏥 AI-Powered Patient Triage & Lab Report Explainer

### Intelligent Healthcare Triage System using Generative AI, Serverless Computing, and Real-Time Clinical Decision Support

<p align="center">

An AI-powered healthcare application that enables real-time patient triage by analyzing symptoms and laboratory reports, automatically determining patient risk levels, generating explainable medical summaries, and assisting healthcare professionals with intelligent case prioritization.

</p>

<p align="center">

<img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white">

<img src="https://img.shields.io/badge/Streamlit-Web%20Application-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white">

<img src="https://img.shields.io/badge/AWS-Lambda-Serverless-FF9900?style=for-the-badge&logo=amazonaws">

<img src="https://img.shields.io/badge/Generative-AI-blueviolet?style=for-the-badge">

<img src="https://img.shields.io/badge/Real--Time-Healthcare-success?style=for-the-badge">

<img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge">

</p>

</div>

---

# 📖 Overview

Efficient patient triage is essential for delivering timely healthcare, particularly in emergency departments and telemedicine platforms where clinicians must rapidly prioritize patients based on the severity of their condition.

This project presents an **AI-powered Patient Triage & Lab Report Explainer**, designed to automate the initial patient assessment process through real-time symptom analysis and laboratory report interpretation.

The application leverages a **serverless AI backend** deployed on AWS Lambda to classify patient cases into appropriate triage levels, generate human-readable medical explanations, and recommend suitable next steps. Healthcare professionals can simultaneously monitor a live dashboard that automatically prioritizes patients according to clinical urgency.

The system demonstrates how Artificial Intelligence can enhance clinical workflows by improving decision support, reducing response time, and increasing operational efficiency.

---

# 🎯 Objectives

- Automate patient triage using AI.
- Prioritize patients based on clinical severity.
- Generate explainable medical summaries.
- Provide recommended clinical actions.
- Demonstrate scalable serverless healthcare AI architecture.

---

# ✨ Key Features

## 🩺 Intelligent Patient Triage

Analyzes patient symptoms and laboratory findings to classify cases into clinical priority levels.

Supported classifications:

- 🔴 High Risk
- 🟡 Medium Risk
- 🟢 Low Risk

---

## 📄 Lab Report Interpretation

Processes laboratory metrics alongside patient symptoms to improve risk assessment accuracy and provide contextual medical explanations.

---

## 🤖 Explainable AI

Instead of returning only a prediction, the AI generates a patient-friendly explanation describing:

- Clinical reasoning
- Risk assessment
- Medical interpretation
- Suggested next steps

This improves transparency and supports informed healthcare decisions.

---

## 📋 Clinical Recommendations

Each prediction is accompanied by AI-generated recommendations such as:

- Immediate emergency consultation
- Physician appointment
- Home observation
- Follow-up monitoring

---

## 📊 Real-Time Physician Dashboard

Healthcare professionals can monitor an automatically updating dashboard that displays all submitted cases ordered by clinical priority.

Dashboard capabilities include:

- Live patient queue
- Risk-based prioritization
- Case tracking
- Clinical summary display

---

## ☁️ Serverless Architecture

The application utilizes AWS Lambda for scalable, on-demand AI inference without requiring dedicated infrastructure.

Benefits include:

- Automatic scaling
- Reduced operational cost
- Low maintenance
- High availability

---

# 🏗 System Workflow

```text
Patient Symptoms / Lab Report
              │
              ▼
      Streamlit Web Interface
              │
              ▼
      AWS Lambda Function URL
              │
              ▼
───────────────────────────────────────
│ AI Risk Classification              │
│ Clinical Explanation Generation     │
│ Recommended Next Action             │
───────────────────────────────────────
              │
              ▼
      Structured JSON Response
              │
              ▼
   Physician Dashboard (Live Queue)
```

---

# ⚙ Technology Stack

| Category | Technologies |
|------------|-------------|
| Programming Language | Python |
| Frontend | Streamlit |
| Backend Communication | Requests |
| Cloud Platform | AWS Lambda |
| Deployment Model | Serverless Architecture |
| Environment Management | python-dotenv |
| Version Control | Git & GitHub |

---

# 📂 Repository Structure

```text
ai-patient-triage/
│
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
├── LICENSE
└── README.md
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-patient-triage.git
```

Navigate into the project

```bash
cd ai-patient-triage
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

Install project dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 Environment Configuration

Create a local environment file

```bash
cp .env.example .env
```

Configure your backend endpoint

```env
LAMBDA_URL=https://your-lambda-function-url.on.aws/
```

The backend endpoint is securely loaded from environment variables and is excluded from version control.

---

# ▶ Running the Application

Launch the Streamlit application

```bash
streamlit run app.py
```

---

# ☁️ Deployment Architecture

The application follows a serverless deployment model.

- **Frontend:** Streamlit Web Application
- **Backend:** AWS Lambda Function URL
- **Communication:** REST API over HTTPS
- **Inference:** Real-Time AI Processing

This architecture enables scalable, cost-effective deployment suitable for cloud-native healthcare applications.

---

# 📊 AI Capabilities

| Component | Purpose |
|-----------|----------|
| AI Backend | Patient Risk Classification |
| Explainable AI | Clinical Interpretation |
| Recommendation Engine | Suggested Medical Action |
| Dashboard Logic | Priority-Based Patient Queue |

---

# 💼 Engineering Skills Demonstrated

This project demonstrates expertise in:

- Healthcare AI System Design
- Real-Time Decision Support Systems
- Serverless Cloud Architecture
- Streamlit Web Development
- AWS Lambda Deployment
- REST API Integration
- Prompt Engineering
- Explainable AI
- Clinical Workflow Automation
- Secure Environment Configuration
- Cloud-Native Application Development
- Modular Python Development

---

# 📈 Future Enhancements

- Electronic Health Record (EHR) Integration
- OCR-Based Lab Report Upload
- PDF Medical Report Analysis
- Multi-Language Support
- Voice-Based Patient Intake
- AI Chat Assistant
- Docker Containerization
- CI/CD Pipeline
- Kubernetes Deployment
- Analytics Dashboard

---

# ⚠ Disclaimer

This project is intended solely for educational, research, and demonstration purposes.

It is **not** a certified medical diagnostic system and should not replace professional medical advice, diagnosis, or treatment.

---

# 👨‍💻 Author

## **Md Arshad**

**Artificial Intelligence,Machine Learning, AWS Enthusiast**

### Areas of Interest

- Artificial Intelligence
- Generative AI
- Healthcare AI
- Machine Learning
- Cloud Computing
- Serverless Architecture
- Python Development
- Intelligent Automation

---

<div align="center">

### ⭐ If you found this project useful, consider giving it a Star.

</div>
