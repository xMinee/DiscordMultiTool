import os
from colorama import Fore
from colorama.ansi import clear_screen
import sys
import requests
import colorama
import threading
import os
import ctypes
from colorama import Fore, Style
from threading import Thread
from sys import stdout
from requests import Session
from time import strftime, gmtime






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

print(f'{Fore.RED}[{Fore.LIGHTCYAN_EX}1{Fore.LIGHTWHITE_EX}] {Fore.RED} Webhook Spammer ')
print(f'{Fore.RED}[{Fore.LIGHTCYAN_EX}2{Fore.LIGHTWHITE_EX}] {Fore.RED} Webhook Deleter')
print(f'{Fore.RED}[{Fore.LIGHTCYAN_EX}3{Fore.LIGHTWHITE_EX}] {Fore.RED} Mass Report Bot')






answer = input("> ")

if answer == "1":
    exec(open('pluginS.py').read())
else:
    print("Not an answer lol?")


if answer == "2":
    os.system('pluginD.exe')




if answer == "3":
    sent = 0
session = Session()
b = Style.BRIGHT
os = os.system
os('cls')

ctypes.windll.kernel32.SetConsoleTitleW(f"discord.gg/beamz ")

print(f"""

 {Fore.RED}______            _       {Fore.BLUE} __  __       _ _   _  {Fore.RED} _______          _ 
 {Fore.RED}| ____|          | |      {Fore.BLUE}|  \/  |     | | | (_) {Fore.RED}|__   __|        | |
 {Fore.RED} | |__   __ _  __ _| | ___{Fore.BLUE}  | \  / |_   _| | |_ _{Fore.RED}     | | ___   ___ | |
 {Fore.RED} |  __| / _` |/ _` | |/ _ \{Fore.BLUE} | |\/| | | | | | __| |{Fore.RED}    | |/ _ \ / _ \| |
 {Fore.RED}| |___| (_| | (_| | |  __/ {Fore.BLUE}| |  | | |_| | | |_| | {Fore.RED}   | | (_) | (_) | |
 {Fore.RED}|______\__,_|\__, |_|\___| {Fore.BLUE}|_|  |_|\__,_|_|\__|_| {Fore.RED}   |_|\___/ \___/|_|


{b+Fore.RED} > {Fore.RESET}discord.gg/beamz. report bot by Dropout

{b+Fore.BLUE} > {Fore.RESET}Options

{b+Fore.BLUE} > {Fore.RESET}illegal Content {b+Fore.BLUE}::{Fore.RESET} 1
{b+Fore.BLUE} > {Fore.RESET}Harrassment {b+Fore.BLUE}::{Fore.RESET} 2
{b+Fore.BLUE} > {Fore.RESET}Spam or Phishing Links {b+Fore.BLUE}::{Fore.RESET} 3
{b+Fore.BLUE} > {Fore.RESET}Self harm {b+Fore.BLUE}::{Fore.RESET} 4
{b+Fore.BLUE} > {Fore.RESET}NSFW Content {b+Fore.BLUE}::{Fore.RESET} 5
""")

token = input(f"{b+Fore.BLUE} > Alt Account Token{Fore.RESET}: ")
headers = {'Authorization': token, 'Content-Type':  'application/json'}  
r = requests.get('https://discord.com/api/v6/users/@me', headers=headers)
if r.status_code == 200:
        pass
else:
        print(f"{b+Fore.RED} > Invalid Token")
        input()
guild_id1 = input(f"{b+Fore.BLUE} > Server ID{Fore.RESET}: ")
channel_id1 = input(f"{b+Fore.BLUE} > Channel ID{Fore.RESET}: ")
message_id1 = input(f"{b+Fore.BLUE} > Message ID{Fore.RESET}: ")
reason1 = input(f"{b+Fore.BLUE} > Option{Fore.RESET}: ")


def Main():
  global sent
  headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36',
        'Authorization': token,
        'Content-Type': 'application/json'
      }

  payload = {
    'channel_id': channel_id1,
    'guild_id': guild_id1,
    'message_id': message_id1,
    'reason': reason1
  }

  while True:
    r = requests.post('https://discord.com/api/v6/report', headers=headers, json=payload)
    if r.status_code == 201:
      print(f"{Fore.GREEN} > Sent Report {b+Fore.BLUE}::{Fore.GREEN} ID {message_id1}")
      ctypes.windll.kernel32.SetConsoleTitleW(f"[REPORT BOT] By Dropout | Sent: %s" % sent)
      sent += 1
      
    elif r.status_code == 401:
      print(f"{Fore.RED} > Invalid token")
      input()
      exit()
    else:
      print(f"{Fore.RED} > Error")


print()
for i in range(500, 1000):
    Thread(target=Main).start()













def Design():
    print(f''' 
    
    


    
 {Fore.RED}______            _       {Fore.BLUE} __  __       _ _   _  {Fore.RED} _______          _ 
 {Fore.RED}| ____|          | |      {Fore.BLUE}|  \/  |     | | | (_) {Fore.RED}|__   __|        | |
 {Fore.RED} | |__   __ _  __ _| | ___{Fore.BLUE}  | \  / |_   _| | |_ _{Fore.RED}     | | ___   ___ | |
 {Fore.RED} |  __| / _` |/ _` | |/ _ \{Fore.BLUE} | |\/| | | | | | __| |{Fore.RED}    | |/ _ \ / _ \| |
 {Fore.RED}| |___| (_| | (_| | |  __/ {Fore.BLUE}| |  | | |_| | | |_| | {Fore.RED}   | | (_) | (_) | |
 {Fore.RED}|______\__,_|\__, |_|\___| {Fore.BLUE}|_|  |_|\__,_|_|\__|_| {Fore.RED}   |_|\___/ \___/|_|
               __/ |                                                 
               
               {Fore.YELLOW} By Stoned.eagle#0003 & kojimu#1916
               {Fore.WHITE} discord.gg/beamz


               ''')           

Design()



os.system


