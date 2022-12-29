# CONCLUSION
"""
- Use function to develop AWS SES solution for sending news in email using AWS SDK. 
- Import from dealflow-scraper/awstranslate for more info.
"""

 
# Source
# https://djangocentral.com/sending-emails-with-csv-attachment-using-python/

# Untouched-CODE
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
import smtplib


def send_mail():
    """
    
    """
    
    # Create a multipart message
    msg = MIMEMultipart()
    body_part = MIMEText(MESSAGE_BODY, 'plain')
    msg['Subject'] = EMAIL_SUBJECT
    msg['From'] = EMAIL_FROM
    msg['To'] = EMAIL_TO
    # Add body to email
    msg.attach(body_part)
    # open and read the CSV file in binary
    with open(FILE_PATH,'rb') as file:
# Attach the file with filename to the email    
        msg.attach(MIMEApplication(file.read(), Name=FILE_NAME))

    # Create SMTP object
    smtp_obj = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    # Login to the server
    smtp_obj.login(SMTP_USERNAME, SMTP_PASSWORD)

    # Convert the message to a string and send it
    smtp_obj.sendmail(msg['From'], msg['To'], msg.as_string())
    smtp_obj.quit()