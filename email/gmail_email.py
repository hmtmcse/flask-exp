import smtplib, ssl


class Mail:

    def __init__(self):
        self.port = 465
        self.smtp_server_domain_name = "smtp.gmail.com"
        self.sender_mail = "GMAIL_ADDRESS"
        self.password = "SECURE_PASSWORD"

    def send(self, emails, subject, content):
        ssl_context = ssl.create_default_context()
        service = smtplib.SMTP_SSL(self.smtp_server_domain_name, self.port, context=ssl_context)
        service.login(self.sender_mail, self.password)

        for email in emails:
            result = service.sendmail(self.sender_mail, email, f"Subject: {subject}\n{content}")

        service.quit()


if __name__ == '__main__':
    mails = "hmtmcse@gmail.com"
    subject = "Test Email"
    content = "Test Email Context"

    mail = Mail()
    mail.send(mails, subject, content)
