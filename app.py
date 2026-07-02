import json
import os
import requests
import streamlit as st
LAMBDA_URL = os.environ.get("LAMBDA_URL", "")
PRIORITY_ORDER = {"HIGH": 0, "MEDIUM": 1, "LOW": 2}
def configure_page() -> None:
    st.set_page_config(page_title="AI Healthcare Triage Portal", layout="wide")
    st.title("AI-Powered Patient Triage & Lab Report Explainer")
    st.markdown("---")
def is_backend_configured() -> bool:
    return bool(LAMBDA_URL)
def submit_triage_request(patient_id: str, symptom_text: str) -> dict:
    """Send patient data to the backend and return the parsed response."""
    payload = {"patient_id": patient_id, "symptom_text": symptom_text}
    response = requests.post(
        LAMBDA_URL,
        data=json.dumps(payload),
        headers={"Content-Type": "application/json"},
        timeout=15,
    )
    response.raise_for_status()
    res_data = response.json()

    if "body" in res_data:
        body = res_data["body"]
        data = json.loads(body)["data"] if isinstance(body, str) else body["data"]
    else:
        data = res_data["data"]
    return data
def fetch_patient_logs() -> list:
    """Retrieve the current patient queue/logs from the backend."""
    response = requests.get(LAMBDA_URL, timeout=15)
    response.raise_for_status()
    res_data = response.json()
    if "body" in res_data:
        body = res_data["body"]
        items = json.loads(body)["items"] if isinstance(body, str) else body["items"]
    else:
        items = res_data.get("items", [])
    return items
def render_patient_entry_tab() -> None:
    st.header("Submit Lab Summary or Symptoms")
    with st.form("patient_form"):
        patient_id = st.text_input("Patient ID (Anonymous)", placeholder="e.g., P-102")
        symptom_text = st.text_area(
            "Describe symptoms or paste lab report metrics here:",
            placeholder="e.g., Blood test shows Hemoglobin 8g/dL and feeling very tired...",
        )
        submit_btn = st.form_submit_button("Analyze & Triage")
    if not submit_btn:
        return
    if not patient_id or not symptom_text:
        st.error("Please fill in both fields.")
        return
    if not is_backend_configured():
        st.error("Backend not configured. Set the LAMBDA_URL environment variable.")
        return
    with st.spinner("AI is analyzing metrics and calculating triage level..."):
        try:
            data = submit_triage_request(patient_id, symptom_text)
        except Exception as exc:
            st.error(f"Connection error: {exc}")
            return
    st.success("Analysis complete.")
    level = data.get("triage_level", "LOW")
    if level == "HIGH":
        st.error(f"Triage Level: {level} (critical alert sent to medical team)")
    elif level == "MEDIUM":
        st.warning(f"Triage Level: {level}")
    else:
        st.info(f"Triage Level: {level}")
    st.subheader("Plain-English Medical Explanation")
    st.write(data.get("explanation", "N/A"))
    st.subheader("Recommended Next Steps")
    st.write(data.get("recommended_action", "N/A"))
def render_physician_dashboard_tab() -> None:
    st.header("Real-Time Patient Queue & Risk Factor Logs")
    if st.button("Refresh Dashboard Data"):
        st.rerun()
    if not is_backend_configured():
        st.error("Backend not configured. Set the LAMBDA_URL environment variable.")
        return
    with st.spinner("Fetching logs from the backend..."):
        try:
            items = fetch_patient_logs()
        except Exception as exc:
            st.error(f"Dashboard connection error: {exc}")
            return
    if not items:
        st.info("No patient logs found.")
        return
    sorted_items = sorted(
        items, key=lambda x: PRIORITY_ORDER.get(x.get("triage_level", "LOW"), 3)
    )
    for item in sorted_items:
        level = item.get("triage_level", "LOW")
        label = {"HIGH": "CRITICAL", "MEDIUM": "MODERATE RISK", "LOW": "STABLE"}.get(
            level, "UNKNOWN"
        )
        st.markdown(f"### Patient ID: {item.get('patient_id')} — {label}")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"**Submitted Symptoms:**\n{item.get('symptom_text')}")
            st.markdown(f"**AI Explanation:**\n{item.get('explanation')}")
        with col2:
            st.markdown(f"**Action Plan:**\n{item.get('recommended_action')}")
        st.markdown("---")
def main() -> None:
    configure_page()
    tab1, tab2 = st.tabs(["Patient Symptoms Entry", "Physician Dashboard"])
    with tab1:
        render_patient_entry_tab()
    with tab2:
        render_physician_dashboard_tab()


if __name__ == "__main__":
    main()
