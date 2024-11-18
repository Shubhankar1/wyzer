import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailNotifier:
    def __init__(self, sender_email, sender_password):
        """
        Initialize the email notifier with sender credentials.
        """
        self.sender_email = sender_email
        self.sender_password = sender_password

    def send_email(self, recipient_email, subject, message):
        """
        Send an email notification.
        """
        try:
            msg = MIMEMultipart()
            msg["From"] = self.sender_email
            msg["To"] = recipient_email
            msg["Subject"] = subject
            msg.attach(MIMEText(message, "plain"))

            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.send_message(msg)
                print(f"Email sent to {recipient_email}")
        except Exception as e:
            print(f"Error sending email: {e}")

    def notify_undervalued_stocks(self, stocks, threshold):
        """
        Notify users about undervalued stocks based on threshold.
        """
        try:
            undervalued = [
                stock for stock in stocks
                if stock["NPV"] - stock["Current Price"] > threshold
            ]
            for stock in undervalued:
                subject = f"Undervalued Stock Alert: {stock['Ticker']}"
                message = (
                    f"Stock {stock['Ticker']} is undervalued.\n"
                    f"Net Present Value: {stock['NPV']}\n"
                    f"Current Price: {stock['Current Price']}\n"
                    f"Difference: {stock['NPV'] - stock['Current Price']}\n"
                )
                self.send_email(stock["Recipient"], subject, message)
        except Exception as e:
            print(f"Error in notifying undervalued stocks: {e}")

