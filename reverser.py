import re , urllib2  , sys , os, requests
from platform import system
from time import sleep
from threading import Thread
import time
import webbrowser
W  = '\033[0m'  # white (default)
R  = '\033[31m' # red
G  = '\033[1;32m' # green bold
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[38m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush() # defeat buffering
        time.sleep(8./90)
def timer():
    now = time.localtime(time.time())
    return time.asctime(now)
slowprint (G+"\n\t                       Reverse IP Lookup") 
slowprint (R+"\n\t        Coded By "+O+"./Rooted Hunter" +R+"From" +O+"BANGLADESH CYBER GHO5T"+O)
slowprint (W+"                  www.facebook.com/rooted.h.hunter")
if system() == 'Linux':
    os.system('clear')
if system() == 'Windows':
    os.system('cls')
url = 'http://api.hackertarget.com/reverseiplookup/?q='
lista = raw_input(" Enter List : ")
lista = open(lista,'r')
read = lista.readlines()
for ip in read:
 ip = ip.rstrip("\n")
 print("Scanning -> "+ip)
 curl = url+ip 
 openurl = urllib2.urlopen(curl)
 read = openurl.read()
 file = open('site.txt','a')
 file.write(read)
 file.close()
 file = open('site.txt','r')
 read = file.readlines()
 file.close()
 os.system('rm site.txt')
 for i in read:
  i = i.rstrip("\n")
  file = open('sites.txt','a')
  i = 'http://'+i
  file.write(i+"\n")
  file.close()
  print(B + " [ + ] Found -> "+O+i)
hacker = 'http://www.hacker-ar.com'
tools = 'http://www.tools-hack.com'
webbrowser.open_new_tab(hacker)
webbrowser.open_new_tab(tools)
