import streamlit as st
import requests

# ==========================
# Replace with your Make.com Webhook URL
# ==========================
WEBHOOK_URL = st.text_input("Your Webhook URL")

st.title("Lead Capture Form")

st.write("Please fill in your details below.")

with st.form("lead_form"):

    name = st.text_input("Name")
    email = st.text_input("Email")
    company = st.text_input("Company")
    message = st.text_area("Service Needed")
    budget = st.text_input("Budget")
    timeline = st.text_input("Timeline")
    contact_no = st.text_input("Contact No.")
    
    
    submit = st.form_submit_button("Submit")

if submit:

    if not all([name, company, budget, timeline, message, contact_no, email]):
        st.warning("Please fill all required fields.")

    else:
        payload = {
            "name": name,
            "email": email,
            "company": company,
            "message": message,
            "budget": budget,
            "timeline": timeline,
            "contact_no": contact_no
        }

        try:
            response = requests.post(
                WEBHOOK_URL,
                json=payload,
                timeout=10
            )

            if response.status_code in [200, 201, 202]:
                st.success("Your information has been submitted successfully.")
            else:
                st.error("Failed to submit your information.")

        except Exception as e:
            st.error(f"An error occurred: {e}")
