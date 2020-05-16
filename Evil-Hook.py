import re
from bs4 import BeautifulSoup as bs
import requests
import sys
import argparse
from colorama import Fore


print("""
 _______________________________________________
|############## EVIL - HOOK ###################|
|        |                                     |
|        |              __,                    |
|        |           .-'_-'`                   |
|        |         .' {`                       |
|        |     .-'````'-.    .-'``'.           |
|        |   .'(0)       '._/ _.-.  `\         |
|        ¿  }     '. ))    _<`    )`  |        |
|            `-.,\'.\_,.-\` \`---; .' /         |
|               )  )       '-.  '--:           |
|                ( ' (          ) '.  \        |
|                 '.  )      .'(   /   )       |
|                   )/      (   '.    /        |
|                            '._( ) .'         |
|                                ( (           |
|                                 `-.          |
|                                              |
|______________________________________________|
|          Last Updated:16/05/2020             |
|   Author:SAGAR;@ http://github.com/S4GAR/    |
|______________________________________________|
""")

parser = argparse.ArgumentParser()
parser.add_argument("-u",action="store",metavar="URL",help="eg:https://example.com/")
args = parser.parse_args()

class evil:
    def __init__(self,url):
        self.url = url
        evil.bringout(self,self.url)
        evil.otherpagedata(self,self.url)
    def pagedata(self,url):
        r = requests.get(url)
        soup = bs(r.text,'lxml')
        return str(soup)
    def bringout(self,url):
        #print("test:  ",url)
        heart = re.findall(r"[A-Za-z.\-]*\w+\@[A-Za-z_0-9\-]*\.\w+[.a-z]*",evil.pagedata(self,url))
        heart = set(heart)
        cnt = 0
        print(Fore.YELLOW+"[+] CHECKING ON: "+url)
        if len(heart) > 0:
            print(Fore.MAGENTA+"[+]Emails Found.")
            for blood in heart:
                print(Fore.CYAN,cnt+1,blood)
                cnt +=1
        else:
            print(Fore.RED+"[-]nothing found:{")

    def otherpagedata(self,url):
        php = re.findall(r"[\w-]+\.php",evil.pagedata(self,url))
        txt = re.findall(r"[\w-]+\.txt",evil.pagedata(self,url))
        html = re.findall(r"[\w-]+\.html",evil.pagedata(self,url))
        xray = php + txt + html
        if len(set(xray)) > 0:
            if url[-1] == "/":
                for i in set(xray):
                    eurl = url+i
                    evil.bringout(self,eurl)
            else:
                for i in set(xray):
                    eurl = url+'/'+i
                    evil.bringout(self,eurl)


if args.u:
    url = args.u
    print(Fore.YELLOW+"[+] Given :"+url)
else:
    print(Fore.RED+"[*]Error occured!! use -u to insert email.")

data = evil(url)

