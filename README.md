# AI-Powered Patient Triage & Lab Report Explainer

A real-time patient triage web application built with Streamlit. Patients or
intake staff submit symptoms or lab report metrics, and a serverless AI
backend classifies the case into a triage level (HIGH / MEDIUM / LOW), then
returns a plain-English explanation and recommended next steps. Physicians
can view a live, priority-sorted queue of all submitted cases.

The application runs entirely on live, real-time data. There is no local
dataset — every request is processed on demand through the backend.

## How It Works

1. A patient enters an anonymous ID and describes their symptoms or lab
   values in the intake form.
2. The app sends this data as JSON to an AWS Lambda Function URL.
3. The Lambda function runs the AI classification and returns a triage
   level, an explanation, and a recommended action.
4. The physician dashboard polls the same backend to display a live,
   priority-ordered list of all cases (HIGH risk shown first).

## Tech Stack

- Python
- Streamlit (frontend/UI)
- Requests (HTTP client)
- AWS Lambda Function URL (backend/AI inference, deployed separately)

## Project Structure

```
ai-patient-triage/
├── app.py              Main Streamlit application
├── requirements.txt    Python dependencies
├── .env.example         Example environment configuration
├── .gitignore
├── LICENSE
└── README.md
```

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/<your-username>/ai-patient-triage.git
   cd ai-patient-triage
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Configure the backend URL. Copy `.env.example` to `.env` and set your
   own Lambda Function URL, or export it directly:
   ```
   export LAMBDA_URL="https://your-lambda-function-url.on.aws/"
   ```

4. Run the app:
   ```
   streamlit run app.py
   ```

## Notes

- The backend endpoint is never hardcoded in source. It is read from the
  `LAMBDA_URL` environment variable at runtime.
- The AI inference and storage layer (Lambda + backend logic) are deployed
  separately and are outside the scope of this repository.

## License

This project is licensed under the MIT License. See `LICENSE` for details.
