#FIXME: crashes after sending.... why???
#       try on windows and see what happens

import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from requests import HTTPError

#idk
SCOPES = ["https://www.googleapis.com/auth/gmail.send"]
flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
creds = flow.run_local_server(port=0)
service = build('gmail', 'v1', credentials=creds)

#ik
message = MIMEText('')
message['to'] = 'capstonetest8@gmail.com'
message['subject'] = 'Email Subject'

file_name = 'test.pdf'
msg = MIMEMultipart()
msg.attach(message)
msg.attach(MIMEText(open(file_name).read()))

create_message = {'raw': base64.urlsafe_b64encode(msg.as_bytes()).decode()}
#idk
service.users().messages().send(userId="me", body=create_message).execute()
#message = (service.users().messages().send(userId="me", body=create_message).execute())
#try:
    #message = (service.users().messages().send(userId="me", body=create_message).execute())
    #print(F'sent message to {message} Message Id: {message["id"]}')
#except HTTPError as error:
    #print(F'An error occurred: {error}')
    #message = None
print('done')
input()
