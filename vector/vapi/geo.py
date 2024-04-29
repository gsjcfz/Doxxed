import requests
import json
from vapi.poor import color
import os

def write_to_file(ip, data):
    with open("Data/{}.txt".format(ip), 'w') as file:
        file.write(data["status"] + "\n")
        file.write(data["country"] + "\n")
        file.write(data["timezone"] + "\n")
        file.write(data["city"] + "\n")
        file.write(data["org"] + "\n")
        file.write(data["zip"] + "\n")
        file.write("https://www.google.com/maps/search/{}+{}".format(data["lat"], data["lon"]))
        

def run(ip):
    req = requests.get(f"http://ip-api.com/json/{ip}").text
    data = json.loads(req)
    print(f'''
{color.CBLUE}[*]{color.CWHITE} IP Information :
{color.CWHITE}IP Adress  : [{color.CWHITE2}{ip}{color.CWHITE}]
{color.CWHITE}Status     : [{color.CWHITE2}{data["status"]}{color.CWHITE}]
{color.CWHITE}Country    : [{color.CWHITE2}{data["country"]}{color.CWHITE}]
{color.CWHITE}TimeZone   : [{color.CWHITE2}{data["timezone"]}{color.CWHITE}]
{color.CWHITE}City       : [{color.CWHITE2}{data["city"]}{color.CWHITE}]
{color.CWHITE}ORG Name   : [{color.CWHITE2}{data["org"]}{color.CWHITE}]
{color.CWHITE}ZIP        : [{color.CWHITE2}{data["zip"]}{color.CWHITE}]
{color.CWHITE}[{color.CWHITE2}Potantial{color.CWHITE}] Map  : [{color.CWHITE2}https://www.google.com/maps/search/{data["lat"]}+{data["lon"]}{color.CWHITE}]
    ''')
    
    write_to_file(ip, data)
    
