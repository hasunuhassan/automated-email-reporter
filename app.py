from email.message import EmailMessage
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()
EMAIL_USER = os.getenv("EMAIL_USER")
APP_PASSWORD = os.getenv("EMAIL_PASSWORD")

business_contacts = [
    {
        "name": "Rick",
        "email": "rick.recipient@example.com",
        "project": "AI world Domination System",
        "report": "rick_report.pdf",
        "known_issues": "the agents forming a union and asking for better working conditions."
    },
    {
        "name": "Marcus",
        "email": "marcus.recipient@example.com",
        "project": "GPU-powered battle bots",
        "report": "marcus_report.pdf",
        "known_issues": "an alarming increase in the number of failed battles."
    }
]

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as email_server:
    email_server.login(EMAIL_USER, APP_PASSWORD)

    for contact in business_contacts:
        message = EmailMessage()

        message['Subject'] = contact["project"] + " Status Update"
        message['From'] = EMAIL_USER
        message['To'] = contact['email']

        message.set_content(
            f"""
Hi {contact["name"]},
I have an update on the {contact["project"]}.

Everything is running according to the plan.
However, we're currently dealing with {contact["known_issues"]}

I'd appreciate your input on the matter.
PS. Full report is attached.
Chicago
"""
        )

        # Safely open and read the PDF file using a context manager
        with open(contact["report"], 'rb') as f:
            report_pdf = f.read()

        message.add_attachment(
            report_pdf, 
            maintype='application',
            subtype='pdf',
            filename=contact["report"]
        )

        email_server.send_message(message)  
        print("Email sent to", contact["name"])