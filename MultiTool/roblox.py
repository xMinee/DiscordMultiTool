import os
from colorama import Fore
from colorama.ansi import clear_screen
import sys
from time import sleep


try:

    import requests
    import colorama
    import sys, os
    import time
    import random
    import string
    import threading
except:
    print('You dont have the required modules installed! Trying to install required modules..')
    try:
        import os
        os.system('cmd /k "pip install colorama --quiet"')
        os.system('cmd /k "pip install time --quiet"')
        os.system('cmd /k "pip install requests --quiet"')
        os.system('cmd /k "pip install random --quiet"')
        os.system('cmd /k "pip install string --quiet"')
        import colorama, time, requests, random, string, threading

    except:
        print('Pip is not installed! Please reinstall python with pip and restart the multitool!')

colorama.init(autoreset=True)
#Continung l8ter
session = requests.Session()






os.system("cls && title Eagle Multi Tool")




def Design():
    print(f''' 
    
    
    
 {Fore.RED}______            _       {Fore.BLUE} __  __       _ _   _  {Fore.RED} _______          _ 
 {Fore.RED}| ____|          | |      {Fore.BLUE}|  \/  |     | | | (_) {Fore.RED}|__   __|        | |
 {Fore.RED} | |__   __ _  __ _| | ___{Fore.BLUE}  | \  / |_   _| | |_ _{Fore.RED}     | | ___   ___ | |
 {Fore.RED} |  __| / _` |/ _` | |/ _ \{Fore.BLUE} | |\/| | | | | | __| |{Fore.RED}    | |/ _ \ / _ \| |
 {Fore.RED}| |___| (_| | (_| | |  __/ {Fore.BLUE}| |  | | |_| | | |_| | {Fore.RED}   | | (_) | (_) | |
 {Fore.RED}|______\__,_|\__, |_|\___| {Fore.BLUE}|_|  |_|\__,_|_|\__|_| {Fore.RED}   |_|\___/ \___/|_|
               __/ |                                                 
               
               {Fore.YELLOW} By Stoned.eagle#0001
               {Fore.WHITE} discord.gg/beamz


               ''')           






Design()



print(f'{Fore.RED}[{Fore.LIGHTCYAN_EX}1{Fore.LIGHTWHITE_EX}] {Fore.RED} Cookie Checker')
print(f'{Fore.RED}[{Fore.LIGHTCYAN_EX}2{Fore.LIGHTWHITE_EX}] {Fore.RED} Group Sniper')
print("gay uwu baka")













answer = input("> ")

if answer == "1":
    import requests, os
req = requests.Session()
cookiefilefolder = os.path.dirname(__file__)
cookiefile = (cookiefilefolder + "\cookies.txt")
cookie = open(cookiefile).read().splitlines()
validcount = 0
invalidcount = 0

if len(cookie) > 0:
    print(str(len(cookie)) + " Cookie(s) Found")
    print(" ")
    pathnameforvalid = os.path.join(os.path.dirname(__file__), "validcookies.txt")
    newfileforvalid = open(pathnameforvalid, "w")
    newfileforvalid.truncate(0)
    pathnameforinvalid = os.path.join(os.path.dirname(__file__), "invalidcookies.txt")
    newfileforinvalid = open(pathnameforinvalid, "w")
    newfileforinvalid.truncate(0)
    for line in cookie:
        check = req.get('https://api.roblox.com/currency/balance', cookies={'.ROBLOSECURITY': str(line)})
        if check.status_code == 200:
            newfileforvalid.write(str(line) + "\n")
            validcount += 1
        else:
            newfileforinvalid.write(str(line) + "\n")
            invalidcount += 1
    print("Valid Cookie(s): " + str(validcount) + "\nInvalid Cookie(s):" + str(invalidcount))
else:
    print("Put Cookies In Cookies.txt")
    os.system("pause")







if answer == "2":
     print('Running Group Sniper.')
     while True:
        id = ''.join(random.choice(string.digits) for i in range(8))
        group = requests.get('https://groups.roblox.com/v1/groups/' + id)
        if group.status_code == 200:
            if group.json()['owner'] == None and group.json()['publicEntryAllowed'] == True:
                    print(colorama.Fore.GREEN + "https://www.roblox.com/groups/" + str(id))

            else:
                pass

        elif group.status_code == 400:
            pass

        else:
            pass












def Design():
    print(f''' 
    
    


    
 {Fore.RED}______            _       {Fore.BLUE} __  __       _ _   _  {Fore.RED} _______          _ 
 {Fore.RED}| ____|          | |      {Fore.BLUE}|  \/  |     | | | (_) {Fore.RED}|__   __|        | |
 {Fore.RED} | |__   __ _  __ _| | ___{Fore.BLUE}  | \  / |_   _| | |_ _{Fore.RED}     | | ___   ___ | |
 {Fore.RED} |  __| / _` |/ _` | |/ _ \{Fore.BLUE} | |\/| | | | | | __| |{Fore.RED}    | |/ _ \ / _ \| |
 {Fore.RED}| |___| (_| | (_| | |  __/ {Fore.BLUE}| |  | | |_| | | |_| | {Fore.RED}   | | (_) | (_) | |
 {Fore.RED}|______\__,_|\__, |_|\___| {Fore.BLUE}|_|  |_|\__,_|_|\__|_| {Fore.RED}   |_|\___/ \___/|_|
               __/ |                                                 
               
               {Fore.YELLOW} By Stoned.eagle#0003
               {Fore.WHITE} discord.gg/beamz


               ''')           

Design()



os.system


fh = open("resources" + "cookes.txt")
print(fh.readline())


