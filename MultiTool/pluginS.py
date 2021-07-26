import requests, os, platform, time
from colorama import Fore, Back, Style
import os
from colorama import Fore
from colorama.ansi import clear_screen
import sys



def Design():
    print(f''' 
    
    
    
  ______            _        __  __       _ _   _   _______          _ 
  | ____|          | |      |  \/  |     | | | (_) |__   __|        | |
   | |__   __ _  __ _| | ___  | \  / |_   _| | |_ _     | | ___   ___ | |
   |  __| / _` |/ _` | |/ _ \ | |\/| | | | | | __| |    | |/ _ \ / _ \| |
  | |___| (_| | (_| | |  __/ | |  | | |_| | | |_| |    | | (_) | (_) | |
  |______\__,_|\__, |_|\___| |_|  |_|\__,_|_|\__|_|    |_|\___/ \___/|_|
               __/ |                                                 
               
                By Stoned.eagle#0003
                discord.gg/beamz


               ''')   
               
               
               
               


Design()



webhook = input(">>Please enter the Webhook: ") # input for webhook url
text = input(">>Please enter the Message that should be spammed: ") # asks for message

if platform.system() == "Windows": # checking the OS of the device running the tool
    clearcmd = "cls"
else:
    clearcmd = "clear"

os.system(clearcmd)

data = {
    "content": text # data for webhook as json
}
def send(i):
    res = requests.post(webhook, data=data) # sends data to webhook
    try:
        print(Fore.RED + 'getting ratelimited, waiting ' + str(res.json()["retry_after"]) + 'ms.')
        # response: {'global': False, 'message': 'You are being rate limited.', 'retry_after': 12345)}
        time.sleep(res.json()["retry_after"]/1000)
        res = 'waited ' + Fore.RED + str(res.json()["retry_after"]) + 'ms.'
    except:
        i += 1
        res = "Sent message " + text + " successful."
    print(Fore.MAGENTA + res + Fore.MAGENTA + ' Amount of messages already sent: ' + Fore.CYAN + str(i)) # message for feedback lol
    return i
i = 0
while True: #loop
   i = send(i)
