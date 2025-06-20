import streamlit as st
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
EMAIL = os.getenv("EMAIL").strip()
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD").strip()


st.title("Contact Me")

with st.form("contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Anything you wanna talk about?")
    submitted = st.form_submit_button("Send")

    if submitted:
        if name and email and message:
            try:
                msg = EmailMessage()
                msg.set_content(f"From: {name} <{email}>\n\n{message}")
                msg["Subject"] = f"New Contact Form Submission from {name}"
                msg["From"] = EMAIL
                msg["To"] = EMAIL

                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login(EMAIL, EMAIL_PASSWORD)
                server.send_message(msg)
                server.quit()

                st.success("Message sent successfully!")
            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.warning("Please fill in all fields.")
