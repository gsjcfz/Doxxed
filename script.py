import requests
import time
from requests.exceptions import ReadTimeout, ConnectTimeout, SSLError
import sys, os
import base64
#import pdfkit
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from requests import HTTPError
from email import encoders

class colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'  # Reset color


def run(username):
    web = [
        f'https://www.instagram.com/{username}', f'https://www.facebook.com/{username}',
        f'https://www.twitter.com/{username}', f'https://www.youtube.com/{username}',
        f'https://{username}.blogspot.com', f'https://plus.google.com/s/{username}/top',
        f'https://www.reddit.com/user/{username}', f'https://{username}.wordpress.com',
        f'https://www.pinterest.com/{username}', f'https://www.github.com/{username}',
        f'https://{username}.tumblr.com', f'https://www.flickr.com/people/{username}',
        f'https://steamcommunity.com/id/{username}', f'https://vimeo.com/{username}',
        f'https://soundcloud.com/{username}', f'https://disqus.com/by/{username}',
        f'https://medium.com/@{username}', f'https://{username}.deviantart.com',
        f'https://vk.com/{username}', f'https://about.me/{username}',
        f'https://imgur.com/user/{username}', f'https://flipboard.com/@{username}',
        f'https://slideshare.net/{username}', f'https://fotolog.com/{username}',
        f'https://open.spotify.com/user/{username}', f'https://www.mixcloud.com/{username}',
        f'https://www.scribd.com/{username}', f'https://www.badoo.com/en/{username}',
        f'https://www.patreon.com/{username}', f'https://bitbucket.org/{username}',
        f'https://www.dailymotion.com/{username}', f'https://www.etsy.com/shop/{username}',
        f'https://cash.me/{username}', f'https://www.behance.net/{username}',
        f'https://www.goodreads.com/{username}', f'https://www.instructables.com/member/{username}',
        f'https://keybase.io/{username}', f'https://kongregate.com/accounts/{username}',
        f'https://{username}.livejournal.com', f'https://angel.co/{username}',
        f'https://last.fm/user/{username}', f'https://dribbble.com/{username}',
        f'https://www.codecademy.com/{username}', f'https://en.gravatar.com/{username}',
        f'https://pastebin.com/u/{username}', f'https://foursquare.com/{username}',
        f'https://www.roblox.com/user.aspx?username={username}', f'https://www.gumroad.com/{username}',
        f'https://{username}.newgrounds.com', f'https://www.wattpad.com/user/{username}',
        f'https://www.canva.com/{username}', f'https://creativemarket.com/{username}',
        f'https://www.trakt.tv/users/{username}', f'https://500px.com/{username}',
        f'https://buzzfeed.com/{username}', f'https://tripadvisor.com/members/{username}',
        f'https://{username}.hubpages.com', f'https://{username}.contently.com',
        f'https://houzz.com/user/{username}', f'https://blip.fm/{username}',
        f'https://www.wikipedia.org/wiki/User:{username}', f'https://news.ycombinator.com/user?id={username}',
        f'https://www.codementor.io/{username}', f'https://www.reverbnation.com/{username}',
        f'https://www.designspiration.net/{username}', f'https://www.bandcamp.com/{username}',
        f'https://www.colourlovers.com/love/{username}', f'https://www.ifttt.com/p/{username}',
        f'https://www.ebay.com/usr/{username}', f'https://{username}.slack.com',
        f'https://www.okcupid.com/profile/{username}', f'https://www.trip.skyscanner.com/user/{username}',
        f'https://ello.co/{username}', f'https://tracky.com/user/~{username}',
        f'https://{username}.basecamphq.com/login'
    ]

    detected_urls = []
    undetected_urls = []
  

    count = 0
    match = True
    for url in web:
        try:
            r = requests.get(url, timeout=3)
            if r.status_code == 200:
                if match:
                    
                    match = False
                
                if username in r.text:
                    print(colors.GREEN + f'[PM] Username:{username} - text has been detected in url.' + colors.END)
                    detected_urls.append((url, username))
                    count += 1
                else:
                    
                    undetected_urls.append((url, username))
            else:
                undetected_urls.append((url, username))

        except ReadTimeout:
            undetected_urls.append((url, username))
        except ConnectTimeout:
            undetected_urls.append((url, username))
        except SSLError:
            undetected_urls.append((url, username))
        except Exception as e:
            undetected_urls.append((url, username))

    total = len(web)

    return print_output_data(detected_urls, undetected_urls)


def print_output_data(detected_urls, undetected_urls):
    result_string = '<div style="text-align: center;">'  # Container for centering the content

    result_string += "<h3>Detected URLs - Publicly Visible:</h3>"
    result_string += '<table style="margin: 0 auto;"><tr><th>Username</th><th>URL</th></tr>'  # Centered table

    for url, username in detected_urls:
        result_string += f"<tr><td>{username}</td><td><a href='{url}' target='_blank'>{url}</a></td></tr>"
    result_string += "</table>"

    result_string += "<h3>Undetected URLs - Safe:</h3>"
    result_string += '<table style="margin: 0 auto;"><tr><th>Username</th><th>URL</th></tr>'  # Centered table

    for url, username in undetected_urls:
        result_string += f"<tr><td>{username}</td><td><a href='{url}' target='_blank'>{url}</a></td></tr>"
    result_string += "</table>"

    result_string += "</div>"  # Close the container

    return result_string
    
    
def email_sender(to_addr, file_to_send, first_name, last_name, ip_addr):
    print('entered')
    from_addr = 'capstonetest8@gmail.com'
    subject = 'Doxxed Information Report'

    SCOPES = ["https://www.googleapis.com/auth/gmail.send"]
            
    flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
    creds = flow.run_local_server(port=0)

    service = build('gmail', 'v1', credentials=creds)

    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = subject
    file_path = 'Data/' + ip_addr + '.txt'
    with open(file_path) as f:
        body = f.readlines()
    body = body[1:]
    body = '-'.join(body)
    body = 'Here is a report of your digital footprint:  \n\n' + "The following information was found from your ip-address:" + '\n-' + body + '\n\n' + "The attached file below shows a graphical representation of your online presence. The file must be downloaded to be viewed properly.\n"

    msg.attach(MIMEText(body, 'plain'))
    attachment = open(file_to_send, 'rb')
    print('HERE: ', file_to_send)
   
    p = MIMEBase('application', 'octet-stream')
    p.set_payload(attachment.read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % file_to_send)

    msg.attach(p)

    create_message = {'raw': base64.urlsafe_b64encode(msg.as_bytes()).decode()}

    service.users().messages().send(userId="me", body=create_message).execute()
    return
# runs all open source doxing tools using as many args as provided
     
def osint_gather_and_send(email: str = None, username: str = None, phone_number: str = None, ip_addr: str = None, firstname: str = None, lastname: str = None):
	#if email is not None:
		# not working properly, do not remove comment
		#os.system("python vector/vector.py {}".format(email))
    
    try:
        if username is not None:
            os.system(f"python vector/vector.py {username}")
        if ip_addr is not None:
            os.system(f"python vector/vector.py {ip_addr}")
   

        temp = 'Data/' + username + '.html'
        email_sender(to_addr=email, file_to_send=temp, first_name=firstname, last_name=lastname, ip_addr=ip_addr)

        return "Please check your email for results"
    except Exception as e:
        return f"Error in Python script: {str(e)}"


	
def main():
    username = "supahtripp"
    ip_addr = "172.59.171.136"
    osint_gather_and_send(username = username, ip_addr = ip_addr)




if __name__ == "__main__":
	main()
    
