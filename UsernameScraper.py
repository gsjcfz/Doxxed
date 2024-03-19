import requests
import time
from requests.exceptions import ReadTimeout, ConnectTimeout


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


username = input('[?] username : ')
  
instagram = f'https://www.instagram.com/{username}'
facebook = f'https://www.facebook.com/{username}'
twitter = f'https://www.twitter.com/{username}'
youtube = f'https://www.youtube.com/{username}'
blogger = f'https://{username}.blogspot.com'
google_plus = f'https://plus.google.com/s/{username}/top'
reddit = f'https://www.reddit.com/user/{username}'
wordpress = f'https://{username}.wordpress.com'
pinterest = f'https://www.pinterest.com/{username}'
github = f'https://www.github.com/{username}'
tumblr = f'https://{username}.tumblr.com'
flickr = f'https://www.flickr.com/people/{username}'
steam = f'https://steamcommunity.com/id/{username}'
vimeo = f'https://vimeo.com/{username}'
soundcloud = f'https://soundcloud.com/{username}'
disqus = f'https://disqus.com/by/{username}'
medium = f'https://medium.com/@{username}'
deviantart = f'https://{username}.deviantart.com'
vk = f'https://vk.com/{username}'
aboutme = f'https://about.me/{username}'
imgur = f'https://imgur.com/user/{username}'
flipboard = f'https://flipboard.com/@{username}'
slideshare = f'https://slideshare.net/{username}'
fotolog = f'https://fotolog.com/{username}'
spotify = f'https://open.spotify.com/user/{username}'
mixcloud = f'https://www.mixcloud.com/{username}'
scribd = f'https://www.scribd.com/{username}'
badoo = f'https://www.badoo.com/en/{username}'
patreon = f'https://www.patreon.com/{username}'
bitbucket = f'https://bitbucket.org/{username}'
dailymotion = f'https://www.dailymotion.com/{username}'
etsy = f'https://www.etsy.com/shop/{username}'
cashme = f'https://cash.me/{username}'
behance = f'https://www.behance.net/{username}'
goodreads = f'https://www.goodreads.com/{username}'
instructables = f'https://www.instructables.com/member/{username}'
keybase = f'https://keybase.io/{username}'
kongregate = f'https://kongregate.com/accounts/{username}'
livejournal = f'https://{username}.livejournal.com'
angellist = f'https://angel.co/{username}'
last_fm = f'https://last.fm/user/{username}'
dribbble = f'https://dribbble.com/{username}'
codecademy = f'https://www.codecademy.com/{username}'
gravatar = f'https://en.gravatar.com/{username}'
pastebin = f'https://pastebin.com/u/{username}'
foursquare = f'https://foursquare.com/{username}'
roblox = f'https://www.roblox.com/user.aspx?username={username}'
gumroad = f'https://www.gumroad.com/{username}'
newsground = f'https://{username}.newgrounds.com'
wattpad = f'https://www.wattpad.com/user/{username}'
canva = f'https://www.canva.com/{username}'
creative_market = f'https://creativemarket.com/{username}'
trakt = f'https://www.trakt.tv/users/{username}'
five_hundred_px = f'https://500px.com/{username}'
buzzfeed = f'https://buzzfeed.com/{username}'
tripadvisor = f'https://tripadvisor.com/members/{username}'
hubpages = f'https://{username}.hubpages.com'
contently = f'https://{username}.contently.com'
houzz = f'https://houzz.com/user/{username}'
blipfm = f'https://blip.fm/{username}'
wikipedia = f'https://www.wikipedia.org/wiki/User:{username}'
hackernews = f'https://news.ycombinator.com/user?id={username}'
codementor = f'https://www.codementor.io/{username}'
reverb_nation = f'https://www.reverbnation.com/{username}'
designspiration = f'https://www.designspiration.net/{username}'
bandcamp = f'https://www.bandcamp.com/{username}'
colourlovers = f'https://www.colourlovers.com/love/{username}'
ifttt = f'https://www.ifttt.com/p/{username}'
ebay = f'https://www.ebay.com/usr/{username}'
slack = f'https://{username}.slack.com'
okcupid = f'https://www.okcupid.com/profile/{username}'
trip = f'https://www.trip.skyscanner.com/user/{username}'
ello = f'https://ello.co/{username}'
tracky = f'https://tracky.com/user/~{username}'
basecamp = f'https://{username}.basecamphq.com/login'



web = [
instagram, facebook, twitter, youtube, blogger, google_plus, reddit,
wordpress, pinterest, github, tumblr, flickr, steam, vimeo, soundcloud, disqus, 
medium, deviantart, vk, aboutme, imgur, flipboard, slideshare, fotolog, spotify,
mixcloud, scribd, badoo, patreon, bitbucket, dailymotion, etsy, cashme, behance,
goodreads, instructables, keybase, kongregate, livejournal, angellist, last_fm,
dribbble, codecademy, gravatar, pastebin, foursquare, roblox, gumroad, newsground,
wattpad, canva, creative_market, trakt, five_hundred_px, buzzfeed, tripadvisor, hubpages,
contently, houzz, blipfm, wikipedia, hackernews, reverb_nation, designspiration,
bandcamp, colourlovers, ifttt, ebay, slack, okcupid, trip, ello, tracky, basecamp,
]

def search():
    print(f'[+] searching for username : {username}')
    time.sleep(0.5)
    print('------------')
    time.sleep(0.5)
    print('------------\n')
    time.sleep(0.5)

    print(f'[+] SKAT v0.5 is working\n')
    time.sleep(0.5)
    print('------------')
    time.sleep(0.5)
    print('------------\n')
    time.sleep(0.5)

    time.sleep(1)

    detected_urls = []
    undetected_urls = []
    unreachable_urls = []

    count = 0
    match = True
    for url in web:
        try:
            r = requests.get(url, timeout=10)
            if r.status_code == 200:
                if match == True:
                    print(f'[+] found matches')
                    match = False
                print(f'\n[-] link : {url} \n[-] status : {r.status_code}')
                if username in r.text:
                    print(colors.GREEN + f'[PM] Username:{username} - text has been detected in url.' + colors.END)
                    detected_urls.append((url, username))
                else:
                    print(colors.YELLOW + f'[PM] Username:{username} - text has not been detected in url, could be a false positive.' + colors.END)
                    undetected_urls.append((url, username))
            else:
                unreachable_urls.append((url, username))
                
            count += 1
        except ReadTimeout:
            print(colors.RED + f'[ERROR] Timeout occurred while accessing URL: {url}' + colors.END)
            unreachable_urls.append((url, username))
        except ConnectTimeout:
            print(colors.RED + f'[ERROR] Connection to {url} timed out.' + colors.END)
            unreachable_urls.append((url, username))
            
    total = len(web)
    print(colors.CYAN + f'a total of {count} matches found out of {total} websites.' + colors.END)
    
    return detected_urls, undetected_urls, unreachable_urls


def print_output_data(detected_urls, undetected_urls, unreachable_urls):
    print(colors.RED + '\nDetected URLs - Publicly Visible:' + colors.END)
    print('-' * 50)
    for url, username in detected_urls:
        print(colors.RED + f'{username} : {url}' + colors.END)
        
    print(colors.YELLOW + '\nUnreachable URLs - Probably Fine:' + colors.END)
    print('-' * 50)
    for url, username in unreachable_urls:
        print(colors.YELLOW + f'{username} : {url}' + colors.END)
        
    print(colors.GREEN + '\nUndetected URLs - Probably Fine:' + colors.END)
    print('-' * 50)
    for url, username in undetected_urls:
        print(colors.GREEN + f'{username} : {url}' + colors.END)

def main():
	detected_urls, undetected_urls, unreachable_urls = search()
	print_output_data(detected_urls, undetected_urls, unreachable_urls)

if __name__=='__main__':
    main()
