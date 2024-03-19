import requests
import time
from requests.exceptions import ReadTimeout, ConnectTimeout, SSLError


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
    unreachable_urls = []

    count = 0
    match = True
    for url in web:
        try:
            r = requests.get(url, timeout=10)
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
                unreachable_urls.append((url, username))

        except ReadTimeout:
            unreachable_urls.append((url, username))
        except ConnectTimeout:
            unreachable_urls.append((url, username))
        except SSLError:
            unreachable_urls.append((url, username))
        except Exception as e:
            unreachable_urls.append((url, username))

    total = len(web)

    return print_output_data(detected_urls, undetected_urls, unreachable_urls)


def print_output_data(detected_urls, undetected_urls, unreachable_urls):
    result_string = 'Detected URLs - Publicly Visible:\n' +'\n'
    for url, username in detected_urls:
        result_string += f'{username} : {url}\n'

    result_string += '\nUnreachable URLs - Probably Fine:\n' + '\n'
    for url, username in unreachable_urls:
        result_string += f'{username} : {url}\n'

    result_string += '\nUndetected URLs - Safe:\n' +'\n'
    for url, username in undetected_urls:
        result_string += f'{username} : {url}\n'

    return result_string
