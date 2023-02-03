import webbrowser, requests, ctypes , re, sys, random, time, os, os.path, platform, hashlib, warnings, threading, argparse, urllib, shlex, json, colorama, phonenumbers, concurrent.futures
from phonenumbers import geocoder
from phonenumbers import carrier
from  mechanize import Browser
from getpass import getpass
from json import dumps
from sys import argv, exit
from easygui import fileopenbox
from requests import get, post, Session
from urllib3 import disable_warnings
from multiprocessing.dummy import Pool, Lock
from ctypes import windll
from colorama import Fore, init, Back, Style
from threading import Thread
from time import sleep, strftime
from bs4 import BeautifulSoup
from os import  mkdir, path, name, _exit, system
from subprocess import check_output
from random import choice, randint
from discord_webhook import DiscordWebhook, DiscordEmbed
from urllib.parse import quote
from urllib.request import Request, urlopen
from base64 import b64decode
from json import JSONDecodeError
from prettytable import PrettyTable

proxies = get("https://raw.githubusercontent.com/PlatiGold/Proxy/main/proxy.txt").text
proxies = proxies.split("\n")
ptype = get("https://raw.githubusercontent.com/PlatiGold/Proxy/main/proxy_type.txt").text
ptype = ptype.replace("\n", "")

time1 = strftime("(%d-%m-%Y-%H-%M)")

API = 'https://bins-su-api.now.sh/api/'
brblue = '\x1b[94m'
white = '\x1b[37m'

def clear():
    system('cls' if name == 'nt' else 'clear')


def plasmamotd():
        system('cls' if name == 'nt' else 'clear')
        print(Fore.RED+CENTER("""\n
 /$$$$$$$$ /$$ /$$           /$$$$$$$                    
|_____ $$ |__/| $$          | $$__  $$                   
     /$$/  /$$| $$  /$$$$$$ | $$  \ $$ /$$$$$$   /$$$$$$ 
    /$$/  | $$| $$ /$$__  $$| $$$$$$$//$$__  $$ /$$__  $$
   /$$/   | $$| $$| $$  \ $$| $$____/| $$  \__/| $$  \ $$
  /$$/    | $$| $$| $$  | $$| $$     | $$      | $$  | $$
 /$$$$$$$$| $$| $$|  $$$$$$/| $$     | $$      |  $$$$$$/
|________/|__/|__/ \______/ |__/     |__/       \______/                                                                                                                   
""").replace("█", Fore.RESET+"█"+Fore.LIGHTCYAN_EX)+Fore.RESET)
        print("\n"+Fore.RESET+CENTER("""~ t.me/zilopro ~ Made by @lespamer & ZiloPro  ~""").replace("~", Fore.LIGHTCYAN_EX+"~"+Fore.RESET) + "\n")

def plasmamotd():
    print(f'''{Fore.LIGHTCYAN_EX}

 /$$$$$$$$ /$$ /$$           /$$$$$$$                    
|_____ $$ |__/| $$          | $$__  $$                   
     /$$/  /$$| $$  /$$$$$$ | $$  \ $$ /$$$$$$   /$$$$$$ 
    /$$/  | $$| $$ /$$__  $$| $$$$$$$//$$__  $$ /$$__  $$
   /$$/   | $$| $$| $$  \ $$| $$____/| $$  \__/| $$  \ $$
  /$$/    | $$| $$| $$  | $$| $$     | $$      | $$  | $$
 /$$$$$$$$| $$| $$|  $$$$$$/| $$     | $$      |  $$$$$$/
|________/|__/|__/ \______/ |__/     |__/       \______/
                    

                     {Fore.WHITE}''')


def CENTER(var:str, space:int=None): 
        if not space:space = (os.get_terminal_size().columns - len(var.splitlines()[int(len(var.splitlines())/2)])) / 2        
        return "\n".join((' ' * int(space)) + var for var in var.splitlines())

def bincheckermotd():
        system('cls' if name == 'nt' else 'clear')
        print(Fore.RED+CENTER("""\n
██████╗ ██╗███╗   ██╗ ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
██╔══██╗██║████╗  ██║██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██████╔╝██║██╔██╗ ██║██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
██╔══██╗██║██║╚██╗██║██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
██████╔╝██║██║ ╚████║╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝                                                                                                                      
""").replace("█", Fore.RESET+"█"+Fore.LIGHTCYAN_EX)+Fore.RESET)
        print("\n"+Fore.RESET+CENTER("""~ t.me/zilopro ~ Made by @lespamer & ZiloPro  ~""").replace("~", Fore.LIGHTCYAN_EX+"~"+Fore.RESET) + "\n")
# output watcher
def output():
    if os.path.exists(pathTextFile):
        os.remove(pathTextFile)
    elif not os.path.exists(pathTextFile):
        with open(pathTextFile, 'w'): pass

class bin(object):

    @classmethod
    def check(cls, bins):
        if bins == '':
            EXT('[!] Bin Not Found!')
        else:
            cls.main(bins)
    @classmethod
    def main(cls, x):
        BINS = x
        x = {
            'author': 'X-MrG3P5',
            'url': 'https://bins-su-api.now.sh/api/'+x,
            'version': '0.1.1'
        }
        req = requests.get(x['url'])
        requests_json = req.json()
        if requests_json['result'] == 'false':
            EXT('[!] Bins Error!')
        elif requests_json['message'] == 'Request failed with status code 404':
            EXT('[!] API Timeout!')
        else:
            r = requests_json['data']
            cls.main_check(r)
    @classmethod
    def main_check(cls, r):
        full_data = r
        data = {
            'Bin': full_data['bin'],
            'Vendor': full_data['vendor'],
            'Type': full_data['type'],
            'Level': full_data['level'],
            'Bank': full_data['bank'],
            'Country': full_data['country'],
        }
        clear()
        bincheckermotd()
        print(f'''                                                                        
{Fore.WHITE}[{Fore.LIGHTCYAN_EX}Bin{Fore.WHITE}] {data['Bin']}
{Fore.WHITE}[{Fore.LIGHTCYAN_EX}Vendor{Fore.WHITE}] {data['Vendor']}
{Fore.WHITE}[{Fore.LIGHTCYAN_EX}Type{Fore.WHITE}] {data['Type']}
{Fore.WHITE}[{Fore.LIGHTCYAN_EX}Level{Fore.WHITE}] {data['Level']}
{Fore.WHITE}[{Fore.LIGHTCYAN_EX}Bank{Fore.WHITE}] {data['Bank']}
{Fore.WHITE}[{Fore.LIGHTCYAN_EX}Country{Fore.WHITE}] {data['Country']}''')




class AmazonNum:
    valid = 0
    invalid = 0
    checked = 0
    invalid = 0
    loaded = 0
    cpm = 0
    timeout = 0
    numlist = []

    def CENTER(var:str, space:int=None): 
        if not space:space = (os.get_terminal_size().columns - len(var.splitlines()[int(len(var.splitlines())/2)])) / 2        
        return "\n".join((' ' * int(space)) + var for var in var.splitlines())

    def banner():
        system('cls' if name == 'nt' else 'clear')
        print(Fore.RED+OperatorChecker.CENTER("""\n
 █████╗ ███╗   ███╗ █████╗ ███████╗ ██████╗ ███╗   ██╗
██╔══██╗████╗ ████║██╔══██╗╚══███╔╝██╔═══██╗████╗  ██║
███████║██╔████╔██║███████║  ███╔╝ ██║   ██║██╔██╗ ██║
██╔══██║██║╚██╔╝██║██╔══██║ ███╔╝  ██║   ██║██║╚██╗██║
██║  ██║██║ ╚═╝ ██║██║  ██║███████╗╚██████╔╝██║ ╚████║
╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝                                                
""").replace("█", Fore.RESET+"█"+Fore.LIGHTCYAN_EX)+Fore.RESET)
        print("\n"+Fore.RESET+OperatorChecker.CENTER("""~ t.me/zilopro ~ Made by @lespamer & ZiloPro  ~""").replace("~", Fore.LIGHTCYAN_EX+"~"+Fore.RESET) + "\n")

    def console_title():
        while True:
            windll.kernel32.SetConsoleTitleW(f"ZiloPro Amazon Numlist Checker {AmazonNum.checked}/{AmazonNum.loaded} - {AmazonNum.valid} Valids - {AmazonNum.invalid} Invalids - {AmazonNum.cpm} CPM")

    def cpm_counter():
        while True:
            now = AmazonNum.checked
            sleep(1)
            AmazonNum.cpm = (AmazonNum.checked - now) * 60


    def AmazonNum(numlist):
        data = {'appActionToken': 'Yq2mhgfDpdFgAc7Q0195zsKMhMgj3D',
        'appAction': 'SIGNIN_PWD_COLLECT',
        'subPageType': 'SignInClaimCollect',
        'openid.return_to': 'ape:aHR0cHM6Ly93d3cuYW1hem9uLmZyLz9yZWZfPW5hdl9zaWduaW4=',
        'prevRID': 'ape:MDU0NEE2SjhFRlFRUTYyN1dKVjQ=',
        'workflowState': 'eyJ6aXAiOiJERUYiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiQTI1NktXIn0.82kD-hdrp3qMJkrTTdkc7Kc08KLPQBHL_iQoQ2pjIS8D31IZSfbInA.90U5VKcKctZvMWjr.o5bTk4T5fy7FanxrQ70Wd9a7Yeg7j8PwNCf31MdIe_tCA2xU4aDIeFto4vZZ_WOuNIRDKX3wCSfPtNeRwWKZSYEf9iy5STM6hyqrBd8dn6HAj2scs056iFAFf6nbuTvZzZ4PMNkbe9XAlm49L9UhlE2WhNYp9J1C4v_BKloM8634tt3qqr6TJmE7sF2ALES8v27bQGYVbC0TT7gnvRhbd2J9KiXpNRw3ksFN9hxvbOmHSMd5yQ4LS9h8BxNWmO0d5_687P05l20JZ6TJHdY1-JD2aNnK4Gp96DGTQu2WYKexFuz0-wo3RJVqcJJUGQTTIKz9._B41CuwhGFlx-f0Rgma_bA',
        'email': numlist,
        'password': '',
        'create': '0',
        'metadata1': 'ECdITeCs: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'
        }
        headers = {"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "fr,en-US;q=0.9,en;q=0.8",
        "cache-control": "max-age=0",
        "content-length": "9702",
        "content-type": "application/x-www-form-urlencoded",
        "cookie": 'signin-sso-state-fr=9a588507-c1d0-47d2-9b4e-24660962a172; session-id=259-0765909-8490911; ubid-acbfr=257-0984503-1653536; s_cc=true; s_nr=1628038460339-New; s_vnum=2060038460339%26vn%3D1; s_dslv=1628038460342; s_sq=%5B%5BB%5D%5D; s_ppv=28; lc-acbfr=fr_FR; sst-acbfr=Sst1|PQF8-IR2JwMpPCYbuYCWXsn0CUByhtpw3G-ru2dOH1cCAwob0wV9_PHM53N5vhYwOh_10q-TmrnyJiDIubhN1vQRwdPX6zr81XepEK4gwVCPuknVsOTraJuLC0KTDLWGpSH1zA7fOq5sI8sp8fDRlnH1nLMf1LgfkKNoSMXBG-bfJLJhyF5VfnhJ_ARRFXOqeEDXqYsSFjZOevjChkRdY4s7xdFORfxpv-R00B-KXv6bpxR5aMOjnQqHGWrJlldWQaAaFYqSpQ-DsuQfb4D5C1_Mrnc7AKc8KU9WPCsuxnvlu1w; i18n-prefs=EUR; session-token="79xix76gKPVVnFiaW9dcHSh+Um4/4J7yi5BR0BAjliXf2Cun5JLeD2BpFKgO1kZsu6ialy8NtAj9qauNFQgn7fHycrZVdsrloQ80RCMZAHbt/T1mWOxDYofcMLA46ZrcaBo1ad7d4dhlfpsZpeEYXjY6OrkE2oZJXv8GCZ3b64qVcmNDT6GuNEdiQSApa9f1CWCU/DwpfDeFd96cXaZltct5FJuJJ1PCv5++TQHAXogh56Hp4H6dkOetF2AAXHzc2cHoMDZFvQ0="; session-id-time=2259697171l; csm-hit=tb:CCFXXEQY6J81PR2CX5JM+b-1QVH157HS0JKGH9N9B30|1628977179563&t:1628977179563&adb:adblk_yes',
        "downlink": "10",
        "ect": "4g",
        "origin": "https://www.amazon.fr",
        "referer": "https://www.amazon.fr/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.fr%2F%3Fref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=frflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&",
        "rtt": "150",
        "sec-ch-ua": '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
        "sec-ch-ua-mobile": "?0",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
        }

        proxy = choice(proxies)
        if proxy.count(':') == 3:
            spl = proxy.split(':')
            proxy = f'{spl[2]}:{spl[3]}@{spl[0]}:{spl[1]}'
        else:
            return_proxy = proxy
        return_proxy = {"http": f"{ptype}://{proxy}","https": f"{ptype}://{proxy}"}

        try:
            req = post(f"https://www.amazon.fr/ap/signin", data=data, headers=headers, timeout=10).text
            if req.__contains__("Numéro de téléphone incorrect"):
                AmazonNum.invalid += 1
                AmazonNum.checked += 1
                print(f"{Fore.LIGHTRED_EX} [-] {numlist}")
                open(f"results/AmazonNumlist-{time1}/Invalids.txt", "a+", encoding="utf-8", errors="ignore").write(f"{numlist}\n")
            elif req.__contains__("Mot de passe oublié"):
                AmazonNum.valid += 1
                AmazonNum.checked += 1
                print(f"{Fore.LIGHTGREEN_EX} [+] {numlist}")
                open(f"results/AmazonNumlist-{time1}/Valids.txt", "a+", encoding="utf-8", errors="ignore").write(f"{numlist}\n")
            elif req.__contains__("Envoyer un code de connexion sur votre téléphone"):
                AmazonNum.valid += 1
                AmazonNum.checked += 1
                print(f"{Fore.LIGHTGREEN_EX} [+] {numlist}")
                open(f"results/AmazonNumlist-{time1}/Valids.txt", "a+", encoding="utf-8", errors="ignore").write(f"{numlist}\n")
            else:
                AmazonNum.recheck += 1
                AmazonNum.checked += 1
                print(f"{Fore.YELLOW} [RECHECK] {numlist}")
                open(f"results/AmazonNumlist-{time1}/Rechecks.txt", "a+", encoding="utf-8", errors="ignore").write(f"{numlist}\n")
        except:
                AmazonNum.recheck += 1
                AmazonNum.checked += 1
                print(f"{Fore.YELLOW} [RECHECK] {numlist}")
                open(f"results/Operateur-Checker-{time1}/Recheck.txt", "a+", encoding='utf-8', errors='ignore').write(f"{numlist}\n")

    def start():
        try:
            AmazonNum.banner()
            print(f" \n[{Fore.LIGHTCYAN_EX}#{Fore.WHITE}]  Please import your Combolist...")
            numlist = open(fileopenbox(title="Select your Combolist !", default="*.txt"), "r", encoding="utf8",errors="ignore").read().split('\n')
            AmazonNum.loaded = len(numlist)
            try:

                threads = int(input("\nThreads : "))
            except:
                print(f"\n{Fore.LIGHTRED_EX}Invalid threads !")
                sleep(3)
                AmazonNum.start()
            Thread(target=AmazonNum.console_title, daemon=False).start()
            Thread(target=AmazonNum.cpm_counter, daemon=False).start()
            if not path.exists("results"):
                mkdir("results")
            if not path.exists(f"results/AmazonNumlist-{time1}"):
                mkdir(f"results/AmazonNumlist-{time1}")
            if not path.exists(f"results/AmazonNumlist-{time1}/Capture"):
                mkdir(f"results/AmazonNumlist-{time1}/Capture")
            mainpool = Pool(processes=threads)
            mainpool.imap_unordered(AmazonNum.AmazonNum, numlist)
            mainpool.close()
            mainpool.join()
            if AmazonNum.checked == AmazonNum.loaded:
                print("\nTerminé !")
            input(f'Appuie sur une touche pour retourner au menu')
            menu()
        except Exception as e:
            try:
                pass
            finally:
                e = None
                del e

class OperatorChecker:
    valid = 0
    invalid = 0
    checked = 0
    recheck = 0
    loaded = 0
    cpm = 0
    timeout = 0
    numlist = []

    def CENTER(var:str, space:int=None): 
        if not space:space = (os.get_terminal_size().columns - len(var.splitlines()[int(len(var.splitlines())/2)])) / 2        
        return "\n".join((' ' * int(space)) + var for var in var.splitlines())

    def banner():
        system('cls' if name == 'nt' else 'clear')
        print(Fore.RED+OperatorChecker.CENTER("""\n
 ██████╗ ██████╗ ███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗ 
██╔═══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██║   ██║██████╔╝█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝
██║   ██║██╔═══╝ ██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗
╚██████╔╝██║     ███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║
 ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝                                                                                                             
""").replace("█", Fore.RESET+"█"+Fore.LIGHTCYAN_EX)+Fore.RESET)
        print("\n"+Fore.RESET+OperatorChecker.CENTER("""~ t.me/zilopro ~ Made by @lespamer & ZiloPro  ~""").replace("~", Fore.LIGHTCYAN_EX+"~"+Fore.RESET) + "\n")

    def console_title():
        while True:
            windll.kernel32.SetConsoleTitleW(f"ZiloPro Debouncer Operator {OperatorChecker.checked}/{OperatorChecker.loaded} - {OperatorChecker.valid} Valids - {OperatorChecker.invalid} Invalids - {OperatorChecker.cpm} CPM")

    def cpm_counter():
        while True:
            now = OperatorChecker.checked
            sleep(1)
            OperatorChecker.cpm = (OperatorChecker.checked - now) * 60


    def OperatorChecker(numlist):
        try:
            r = requests.get(f"https://messente.com/messente-api/number-lookup/?phone_number=%2B{numlist}").text
            if r.__contains__("error"):
                OperatorChecker.invalid += 1
                OperatorChecker.checked += 1
                print(Fore.RED+f"Mauvais num : {numlist}")
            elif r.__contains__("e*Message"):
                OperatorChecker.valid += 1
                OperatorChecker.checked += 1
                req = requests.get(f"https://messente.com/messente-api/number-lookup/?phone_number=%2B{numlist}").json()
                cap = print(f"{Fore.GREEN} [+] {numlist} {Fore.WHITE} | Country: {req['countryName']} | Operateur: {req['originalCarrierName']} | TimeZone: {req['timeZone']}")
                open(f"results/Operateur/eMessage-{time1}.txt", "a+").write(f"{n}\n")
            elif not r.__contains__('originalCarrierName":""'):
                OperatorChecker.valid += 1
                OperatorChecker.checked += 1
                req = requests.get(f"https://messente.com/messente-api/number-lookup/?phone_number=%2B{numlist}").json()
                cap = print(f"{Fore.GREEN} [+] {numlist} {Fore.WHITE} | Country: {req['countryName']} | Operateur: {req['originalCarrierName']} | TimeZone: {req['timeZone']}")
                open(f"results/Operateur/{req['originalCarrierName']}-{time1}.txt", "a+").write(f"{numlist}\n")
            else:
                OperatorChecker.invalid += 1
                OperatorChecker.checked += 1
                print(f"{Fore.RED} [-] {numlist}")
        except:
                OperatorChecker.recheck += 1
                OperatorChecker.checked += 1
                print(f"{Fore.YELLOW} [RECHECK] {numlist}")

    def start():
        try:
            OperatorChecker.banner()
            print(f" \n[{Fore.LIGHTCYAN_EX}#{Fore.WHITE}] Please import your Combolist...")
            numlist = open(fileopenbox(title="Select your Combolist !", default="*.txt"), "r", encoding="utf8",errors="ignore").read().split('\n')
            OperatorChecker.loaded = len(numlist)
            try:
                threads = int(input("\nThreads : "))
            except:
                print(f"\n{Fore.LIGHTRED_EX}Invalid threads !")
                sleep(3)
                OperatorChecker.start()
            Thread(target=OperatorChecker.console_title, daemon=False).start()
            Thread(target=OperatorChecker.cpm_counter, daemon=False).start()
            if not path.exists("results"):
                mkdir("results")
            if not path.exists(f"results/Operateur"):
                mkdir(f"results/Operateur")
            mainpool = Pool(processes=threads)
            mainpool.imap_unordered(OperatorChecker.OperatorChecker, numlist)
            mainpool.close()
            mainpool.join()
            if OperatorChecker.checked == OperatorChecker.loaded:
                print("\nTerminé !")
            input(f'Appuie sur une touche pour retourner au menu')
            menu()
        except Exception as e:
            try:
                pass
            finally:
                e = None
                del e


class AntiDuplicate:
    def start():
        system('cls' if name == 'nt' else 'clear')
        print(Fore.RED+CENTER("""\n
 /$$$$$$$$ /$$ /$$           /$$$$$$$                    
|_____ $$ |__/| $$          | $$__  $$                   
     /$$/  /$$| $$  /$$$$$$ | $$  \ $$ /$$$$$$   /$$$$$$ 
    /$$/  | $$| $$ /$$__  $$| $$$$$$$//$$__  $$ /$$__  $$
   /$$/   | $$| $$| $$  \ $$| $$____/| $$  \__/| $$  \ $$
  /$$/    | $$| $$| $$  | $$| $$     | $$      | $$  | $$
 /$$$$$$$$| $$| $$|  $$$$$$/| $$     | $$      |  $$$$$$/
|________/|__/|__/ \______/ |__/     |__/       \______/                                                          
\n""").replace("█", Fore.RESET+"█"+Fore.LIGHTCYAN_EX)+Fore.RESET)
        print(Fore.RESET+CENTER("""~ t.me/zilopro ~ Made by @lespamer & ZiloPro  ~""").replace("~", Fore.LIGHTCYAN_EX+"~"+Fore.RESET))
        print(f" \n[{Fore.LIGHTCYAN_EX}#{Fore.WHITE}] Please import your Numlist...")
        inputf = input('> ')
        if not path.exists("results"):
            mkdir("results")
        with open(inputf, 'r+', encoding='latin-1') as linesf:
            output_file = f'results/Duplicates_Removed-{time1}.txt'
            open(output_file, 'w', encoding='latin-1').writelines(set(linesf.readlines()))
            afterremove = open(output_file, 'r', encoding='u8', errors='ignore').read().split('\n')
            beforeremove = open(inputf, 'r', encoding='u8',errors='ignore').read().split('\n')
            nigga = (len(beforeremove) - len(afterremove))
            print(f'\nAvant: {len(beforeremove)} Après: {len(afterremove)} ({nigga} Lignes supprimés)\n')
        input(f'Appuie sur une touche pour retourner au menu')
        menu()

class NumGen:
    generated = 0
    numnumber = 0
    cpm = 0

    def cpm_counter(self):
        while True:
            now = NumGen.generated
            sleep(1)
            NumGen.cpm = (NumGen.generated - now) * 60

    def console_title(self):
        while True:
            windll.kernel32.SetConsoleTitleW(f"ZiloPro Num Generator {NumGen.generated}/{NumGen.numnumber} - {NumGen.cpm} CPM")
            sleep(0.07)

    def start(self):
        kirikou = False
        windll.kernel32.SetConsoleTitleW(f"ZiloPro Num Generator")
        system('cls' if name == 'nt' else 'clear')
        print(Fore.RED+CENTER("""\n
 ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗ 
██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝
██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗
╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║
 ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝                                                                         
""").replace("█", Fore.RESET+"█"+Fore.LIGHTCYAN_EX)+Fore.RESET)
        print(Fore.RESET+CENTER("""~ t.me/zilopro ~ Made by @lespamer & ZiloPro  ~""").replace("~", Fore.LIGHTCYAN_EX+"~"+Fore.RESET))
        print("\nQuel type de numéros tu veux générer ? (07 ou 06):")
        basic = int(input(" > "))
        print("Combien de num tu veux générer ? ")
        NumGen.numnumber = int(input("> "))
        print("Generating...")
        Thread(target=self.console_title, daemon=False).start()
        Thread(target=self.cpm_counter, daemon=False).start()
        if not path.exists("results"):
            mkdir("results")
        mkdir(f"results/Num-Generator-{time1}")
        for x in range(NumGen.numnumber):
            addon = randint(10000000,99999999)
            open(f"results/Num-Generator-{time1}/Generated.txt", "a", encoding="utf-8", errors="ignore").write(f"0{basic}{addon}\n")
            NumGen.generated += 1
        print(f"{Fore.WHITE}\n{NumGen.generated} Numéros ont été générer !")
        if NumGen.generated == NumGen.numnumber:
            print("\nTerminé !")
        input(f'Appuie sur une touche pour retourner au menu')
        menu()


def othermodule():
    windll.kernel32.SetConsoleTitleW(f"ZiloPro Others Modules")
    system('cls' if name == 'nt' else 'clear')
    print(Fore.RED+CENTER("""\n
 /$$$$$$$$ /$$ /$$           /$$$$$$$                    
|_____ $$ |__/| $$          | $$__  $$                   
     /$$/  /$$| $$  /$$$$$$ | $$  \ $$ /$$$$$$   /$$$$$$ 
    /$$/  | $$| $$ /$$__  $$| $$$$$$$//$$__  $$ /$$__  $$
   /$$/   | $$| $$| $$  \ $$| $$____/| $$  \__/| $$  \ $$
  /$$/    | $$| $$| $$  | $$| $$     | $$      | $$  | $$
 /$$$$$$$$| $$| $$|  $$$$$$/| $$     | $$      |  $$$$$$/
|________/|__/|__/ \______/ |__/     |__/       \______/
\n""").replace("█", Fore.RESET+"█"+Fore.LIGHTCYAN_EX)+Fore.RESET)
    print(Fore.RESET+CENTER("""~ t.me/zilopro ~ Made by @lespamer & ZiloPro  ~""").replace("~", Fore.LIGHTCYAN_EX+"~"+Fore.RESET))
    print(f'''{Fore.WHITE}
[{Fore.LIGHTCYAN_EX}1{Fore.WHITE}] Telegram Scrapper
[{Fore.LIGHTCYAN_EX}2{Fore.WHITE}] OnOff Sender
[{Fore.LIGHTCYAN_EX}3{Fore.WHITE}] SenderId
[{Fore.LIGHTCYAN_EX}4{Fore.WHITE}] Bin Checker

[{Fore.LIGHTRED_EX}X{Fore.WHITE}] Retour 
''')
    mod = input("> Select your number: ")
    if mod == "1":
        NumGen().start()
    elif mod == "2":
        NumChecker.start()
    elif mod == "3":
        NumChecker.start()
    elif mod == "4":
        clear()
        bincheckermotd()
        while True:
            try:
                BINS = input('\n > Enter the first 6 numbers : ')
                bin.check(BINS)
            except KeyboardInterrupt:
                menu()
    else:
        menu()

def emailmodule():
    windll.kernel32.SetConsoleTitleW(f"ZiloPro Emails Modules")
    system('cls' if name == 'nt' else 'clear')
    print(Fore.RED+CENTER("""\n
 /$$$$$$$$ /$$ /$$           /$$$$$$$                    
|_____ $$ |__/| $$          | $$__  $$                   
     /$$/  /$$| $$  /$$$$$$ | $$  \ $$ /$$$$$$   /$$$$$$ 
    /$$/  | $$| $$ /$$__  $$| $$$$$$$//$$__  $$ /$$__  $$
   /$$/   | $$| $$| $$  \ $$| $$____/| $$  \__/| $$  \ $$
  /$$/    | $$| $$| $$  | $$| $$     | $$      | $$  | $$
 /$$$$$$$$| $$| $$|  $$$$$$/| $$     | $$      |  $$$$$$/
|________/|__/|__/ \______/ |__/     |__/       \______/
\n""").replace("█", Fore.RESET+"█"+Fore.LIGHTCYAN_EX)+Fore.RESET)
    print(Fore.RESET+CENTER("""~ t.me/zilopro ~ Made by @lespamer & ZiloPro  ~""").replace("~", Fore.LIGHTCYAN_EX+"~"+Fore.RESET))
    print(f'''{Fore.WHITE}
[{Fore.LIGHTCYAN_EX}1{Fore.WHITE}] Debouncer
[{Fore.LIGHTCYAN_EX}2{Fore.WHITE}] Checker Paypal
[{Fore.LIGHTCYAN_EX}3{Fore.WHITE}] Checker Amazon
[{Fore.LIGHTCYAN_EX}4{Fore.WHITE}] Checker Netlix
[{Fore.LIGHTCYAN_EX}5{Fore.WHITE}] Checker Disney+

[{Fore.LIGHTRED_EX}X{Fore.WHITE}] Retour 
''')
    mod = input("> Select your number: ")
    if mod == "1":
        NumGen().start()
    elif mod == "2":
        NumChecker.start()
    elif mod == "3":
        OperateurCapture.start()
    else:
        menu()

def nummodule():
    windll.kernel32.SetConsoleTitleW(f"ZiloPro Nums Modules")
    system('cls' if name == 'nt' else 'clear')
    print(Fore.RED+CENTER("""\n
 /$$$$$$$$ /$$ /$$           /$$$$$$$                    
|_____ $$ |__/| $$          | $$__  $$                   
     /$$/  /$$| $$  /$$$$$$ | $$  \ $$ /$$$$$$   /$$$$$$ 
    /$$/  | $$| $$ /$$__  $$| $$$$$$$//$$__  $$ /$$__  $$
   /$$/   | $$| $$| $$  \ $$| $$____/| $$  \__/| $$  \ $$
  /$$/    | $$| $$| $$  | $$| $$     | $$      | $$  | $$
 /$$$$$$$$| $$| $$|  $$$$$$/| $$     | $$      |  $$$$$$/
|________/|__/|__/ \______/ |__/     |__/       \______/ 
\n""").replace("█", Fore.RESET+"█"+Fore.LIGHTCYAN_EX)+Fore.RESET)
    print(Fore.RESET+CENTER("""~ t.me/zilopro ~ Made by @lespamer & ZiloPro  ~""").replace("~", Fore.LIGHTCYAN_EX+"~"+Fore.RESET))
    print(f'''{Fore.WHITE}
[{Fore.LIGHTCYAN_EX}1{Fore.WHITE}] Anti Duplicate
[{Fore.LIGHTCYAN_EX}2{Fore.WHITE}] Nums Generator
[{Fore.LIGHTCYAN_EX}3{Fore.WHITE}] Operators Checker - Debouncer
[{Fore.LIGHTCYAN_EX}4{Fore.WHITE}] Amazon Checker

[{Fore.LIGHTRED_EX}X{Fore.WHITE}] Retour 
''')
    mod = input("> Select your number: ")
    if mod == "1":
        AntiDuplicate.start()
    elif mod == "2":
        NumGen().start()
    elif mod == "3":
        OperatorChecker.start()
    elif mod == "4":
        AmazonNum.start()
    elif mod == "5":
        PaypalNum.start()
    else:
        menu()

def menu():
    windll.kernel32.SetConsoleTitleW(f"ZiloPro Menu")
    system('cls' if name == 'nt' else 'clear')
    print(Fore.RED+CENTER("""\n
 /$$$$$$$$ /$$ /$$           /$$$$$$$                    
|_____ $$ |__/| $$          | $$__  $$                   
     /$$/  /$$| $$  /$$$$$$ | $$  \ $$ /$$$$$$   /$$$$$$ 
    /$$/  | $$| $$ /$$__  $$| $$$$$$$//$$__  $$ /$$__  $$
   /$$/   | $$| $$| $$  \ $$| $$____/| $$  \__/| $$  \ $$
  /$$/    | $$| $$| $$  | $$| $$     | $$      | $$  | $$
 /$$$$$$$$| $$| $$|  $$$$$$/| $$     | $$      |  $$$$$$/
|________/|__/|__/ \______/ |__/     |__/       \______/                                                        
\n""").replace("█", Fore.RESET+"█"+Fore.LIGHTCYAN_EX)+Fore.RESET)

    syms = [f'                                  {Fore.RESET}', f'{Fore.LIGHTCYAN_EX}~', f'{Fore.RESET} ', 't', '.', 'm', 'e', '/', 'l', 'e', 's', 'p', 'a', 'm', 'e','r', '  ', f'{Fore.LIGHTCYAN_EX}~', f'{Fore.RESET} ', 'M', 'a', 'd', 'e', ' ', 'b', 'y', ' ', '@', 'l', 'e', 's', 'p', 'a', 'm', 'e', 'r',' ', '&', ' ', 'Z', 'i', 'l', 'o', 'P', 'r', 'o', '  ', f'{Fore.LIGHTCYAN_EX}~']
    for _ in range(1):
        for sym in syms:
            sys.stdout.write("%s" % sym)
            sys.stdout.flush()
            sleep(0.04)
    print(f'''{Fore.WHITE}

[{Fore.LIGHTCYAN_EX}1{Fore.WHITE}] Nums Modules
[{Fore.LIGHTCYAN_EX}2{Fore.WHITE}] Emails Modules
[{Fore.LIGHTCYAN_EX}3{Fore.WHITE}] Others Modules                                                  
''')
    mod = input("> Select your number: ")
    if mod == "1":
        nummodule()
    elif mod == "2":
        emailmodule()
    elif mod == "3":
        othermodule()
    else:
        print("Invalid input !")
        sleep(3)
        menu()

clear()

on = 'on'
off = 'off'
get_on = get("https://raw.githubusercontent.com/K7MTV/checker/main/onoff.txt").text
get_off = get("https://raw.githubusercontent.com/K7MTV/checker/main/onoff.txt").text
get_on = get_on.replace("\n", "")
get_off = get_off.replace("\n", "")
if on == get_on:
    pass
menu()
