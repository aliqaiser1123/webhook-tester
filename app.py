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
    city = st.text_input("City")
    contact = st.text_input("Contact No.")
    email = st.text_input("Email")
    message = st.text_area("Message")

    submit = st.form_submit_button("Submit")

if submit:

    if not all([name, city, contact, email]):
        st.warning("Please fill all required fields.")

    else:
        payload = {
            "name": name,
            "city": city,
            "contact": contact,
            "email": email,
            "message": message
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