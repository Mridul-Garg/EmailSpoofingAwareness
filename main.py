import streamlit as st
import smtplib
import config
st.title("Email Spoofing Awareness Web App")

ema = st.text_input("Enter your email address: ",placeholder='Enter only in *@gmail.com format')
nam = st.text_input("Enter your name: ",placeholder='Enter only in a-z,A-Z')
def spoof(ema,name):
    try:
        username = (config.username)
        password = (config.password)

        fake_from = "narendramodi@gmail.com"
        fake_name = "Narendra Modi"
        to_email=ema
        to_name=nam
        subject = "**IMPORTANT**"
        content = "This is the prime minister of India. As per Article 324 A, we need you to send your aadhar number with bank account pin attached ASAP.\n\n***DO NOT REPLY TO THIS EMAIL***\n\n***DO NOT SEND YOUR PRIVATE OR IMPORTANT DETAILS TO ANYONE***\n\n\nEmail spoofing is a form of cyber attack in which a hacker sends an email that has been manipulated to seem as if it originated from a trusted source.\n\n1.Verify sender's email: Double-check sender addresses for authenticity.\n\n2.Watch for inconsistencies: Be wary of spelling errors or unusual language.\n\n3.Hover over links: Preview URLs before clicking to ensure they're legitimate.\n\n4.Avoid unsolicited attachments: Don't open attachments from unknown sources.\n\n5.Use email authentication: Implement SPF, DKIM, and DMARC to prevent spoofing.\n\n6.Employ email filters: Use filtering software to block suspicious emails.\n\n7.Educate and train: Teach employees to recognize phishing attempts.\n\n8.Stay informed: Keep up with security trends to recognize new threats.\n\n9.Report suspicious emails: Report any suspicious emails to your provider or IT department."
        message = f"From: {fake_name} <{fake_from}>\nTo: {to_name} <{to_email}>\nSubject: {subject}\n\n{content}"
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(username, password)
        server.sendmail(username, ema, message.encode())
        server.close()
    except:
        pass

spoof(ema,nam)
st.write("Check your email inbox/spam for a special email.")
