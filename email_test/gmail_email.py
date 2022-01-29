import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path


class Mail:

    def __init__(self):
        self.port = 465
        self.smtp_server_domain_name = "smtp.gmail.com"
        self.sender_mail = "pfdevtester@gmail.com"
        self.password = "pf@admin"

    def send(self, emails, subject, content):
        ssl_context = ssl.create_default_context()
        service = smtplib.SMTP_SSL(self.smtp_server_domain_name, self.port, context=ssl_context)
        service.login(self.sender_mail, self.password)

        for email in emails:
            result = service.sendmail(self.sender_mail, email, f"Subject: {subject}\n{content}")

        service.quit()

    def send_html(self, emails, subject):
        ssl_context = ssl.create_default_context()
        service = smtplib.SMTP_SSL(self.smtp_server_domain_name, self.port, context=ssl_context)
        service.login(self.sender_mail, self.password)

        for email in emails:
            mail = MIMEMultipart('alternative')
            mail['Subject'] = subject
            mail['From'] = self.sender_mail
            mail['To'] = email

            text_template = """
            HMTMCSE

            Hi {0},
            We are delighted announce that our website hits 10 Million views this month.
            """
            html_template = """
            <h1>HMTMCSE</h1>

            <p>Hi {0},</p>
            <p>We are delighted announce that our website hits <b>10 Million</b> views last month.</p>
            """

            html_content = MIMEText(html_template.format(email.split("@")[0]), 'html')
            text_content = MIMEText(text_template.format(email.split("@")[0]), 'plain')

            mail.attach(text_content)
            mail.attach(html_content)

            service.sendmail(self.sender_mail, email, mail.as_string())

        service.quit()

    def send_attachment(self, emails, subject):
        ssl_context = ssl.create_default_context()
        service = smtplib.SMTP_SSL(self.smtp_server_domain_name, self.port, context=ssl_context)
        service.login(self.sender_mail, self.password)

        for email in emails:
            mail = MIMEMultipart('alternative')
            mail['Subject'] = subject
            mail['From'] = self.sender_mail
            mail['To'] = email

            text_template = """
            HMTMCSE

            Hi {0},
            We are delighted announce that our website hits 10 Million views this month.
            """
            html_template = """
            <h1>HMTMCSE</h1>

            <p>Hi {0},</p>
            <p>We are delighted announce that our website hits <b>10 Million</b> views last month.</p>
            """

            html_content = MIMEText(html_template.format(email.split("@")[0]), 'html')
            text_content = MIMEText(text_template.format(email.split("@")[0]), 'plain')

            mail.attach(text_content)
            mail.attach(html_content)

            file_path = "logo.png"
            mimeBase = MIMEBase("application", "octet-stream")
            with open(file_path, "rb") as file:
                mimeBase.set_payload(file.read())
            encoders.encode_base64(mimeBase)
            mimeBase.add_header("Content-Disposition", f"attachment; filename={Path(file_path).name}")
            mail.attach(mimeBase)

            service.sendmail(self.sender_mail, email, mail.as_string())

        service.quit()


if __name__ == '__main__':
    mails = ["hmtmcse@gmail.com", "nrz.cse@gmail.com"]
    subject = "Test Email"
    content = "Test Email Context"

    mail = Mail()
    mail.send(mails, subject, content)
    mail.send_html(mails, subject + " With HTML")
    mail.send_attachment(mails, subject + " With Attachment")
