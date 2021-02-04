from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from os import system, name
from colorama import Fore, Back, Style
from tqdm import tqdm 
import requests
for i in tqdm (range (101),  
               desc=Fore.RED + "",  
               ascii=False, ncols=100): 
    time.sleep(0.01) 
def clear():
        _ = system('cls')
clear()
print(Fore.RED + '''
            Made by Jammy#4613

 ▄· ▄▌      ▄• ▄▌▄▄▄▄▄▄• ▄▌▄▄▄▄· ▄▄▄ .     ▌ ▐·▪  ▄▄▄ .▄▄▌ ▐ ▄▌    ▄▄▄▄·       ▄▄▄▄▄
▐█▪██▌▪     █▪██▌•██  █▪██▌▐█ ▀█▪▀▄.▀·    ▪█·█▌██ ▀▄.▀·██· █▌▐█    ▐█ ▀█▪▪     •██  
▐█▌▐█▪ ▄█▀▄ █▌▐█▌ ▐█.▪█▌▐█▌▐█▀▀█▄▐▀▀▪▄    ▐█▐█•▐█·▐▀▀▪▄██▪▐█▐▐▌    ▐█▀▀█▄ ▄█▀▄  ▐█.▪
 ▐█▀·.▐█▌.▐▌▐█▄█▌ ▐█▌·▐█▄█▌██▄▪▐█▐█▄▄▌     ███ ▐█▌▐█▄▄▌▐█▌██▐█▌    ██▄▪▐█▐█▌.▐▌ ▐█▌·
  ▀ •  ▀█▄▀▪ ▀▀▀  ▀▀▀  ▀▀▀ ·▀▀▀▀  ▀▀▀     . ▀  ▀▀▀ ▀▀▀  ▀▀▀▀ ▀▪    ·▀▀▀▀  ▀█▄▀▪ ▀▀▀ 

       [!] Modules [!]
       [1] Selenium bot without proxies
       [2] Selenium bot with proxies [Only 2 drivers]
       [3] Request bot without proxies [Test]
''')
optionfirst = input("Eneter option: ")
if optionfirst == '1':
    URL = input("Eneter youtube link: ")
    print("Views automatically set to infinite!")
    time.sleep(1)
    WATCHTIME = input("Enter watch time: ")
    WATCHTIME = float(WATCHTIME)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--mute-audio")
    browser1 = webdriver.Chrome(chrome_options=chrome_options)
    browser2 = webdriver.Chrome(chrome_options=chrome_options)
    browser3 = webdriver.Chrome(chrome_options=chrome_options)
    browser4 = webdriver.Chrome(chrome_options=chrome_options)
    browser5 = webdriver.Chrome(chrome_options=chrome_options)
    browser1.get(URL)
    browser2.get(URL)
    browser3.get(URL)
    browser4.get(URL)
    browser5.get(URL)
    browser1.refresh()
    browser2.refresh()
    browser3.refresh()
    browser4.refresh()
    browser5.refresh()
    clear()
    print(Fore.RED + '''
            Jammy#4613

 ▄· ▄▌      ▄• ▄▌▄▄▄▄▄▄• ▄▌▄▄▄▄· ▄▄▄ .     ▌ ▐·▪  ▄▄▄ .▄▄▌ ▐ ▄▌    ▄▄▄▄·       ▄▄▄▄▄
▐█▪██▌▪     █▪██▌•██  █▪██▌▐█ ▀█▪▀▄.▀·    ▪█·█▌██ ▀▄.▀·██· █▌▐█    ▐█ ▀█▪▪     •██  
▐█▌▐█▪ ▄█▀▄ █▌▐█▌ ▐█.▪█▌▐█▌▐█▀▀█▄▐▀▀▪▄    ▐█▐█•▐█·▐▀▀▪▄██▪▐█▐▐▌    ▐█▀▀█▄ ▄█▀▄  ▐█.▪
 ▐█▀·.▐█▌.▐▌▐█▄█▌ ▐█▌·▐█▄█▌██▄▪▐█▐█▄▄▌     ███ ▐█▌▐█▄▄▌▐█▌██▐█▌    ██▄▪▐█▐█▌.▐▌ ▐█▌·
  ▀ •  ▀█▄▀▪ ▀▀▀  ▀▀▀  ▀▀▀ ·▀▀▀▀  ▀▀▀     . ▀  ▀▀▀ ▀▀▀  ▀▀▀▀ ▀▪    ·▀▀▀▀  ▀█▄▀▪ ▀▀▀ 

    ''')
    number = int(1)
    while True:
     time.sleep(WATCHTIME)
     browser1.refresh()
     browser2.refresh()
     browser3.refresh()
     browser4.refresh()
     browser5.refresh()
     print ("[", end = '')
     print (number, end = '')
     print ("] View/s sent", end = '')
     print(" ")
     number = number + 1

if optionfirst == '2':
    URL = input("Eneter youtube link: ")
    WATCHTIME = input("Enter watch time: ")
    WATCHTIME = float(WATCHTIME)
    proxie1 = input("Eneter proxie: ")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server=%s' % proxie1)
    chrome_options.add_argument("--mute-audio")
    chrome_options.add_argument("--headless")
    browser1 = webdriver.Chrome(chrome_options=chrome_options)
    browser2 = webdriver.Chrome(chrome_options=chrome_options)
    browser1.get(URL)
    browser2.get(URL)
    time.sleep(5)
    browser1.refresh()
    browser2.refresh()
    clear()
    print(Fore.RED + '''
            Jammy#4613

 ▄· ▄▌      ▄• ▄▌▄▄▄▄▄▄• ▄▌▄▄▄▄· ▄▄▄ .     ▌ ▐·▪  ▄▄▄ .▄▄▌ ▐ ▄▌    ▄▄▄▄·       ▄▄▄▄▄
▐█▪██▌▪     █▪██▌•██  █▪██▌▐█ ▀█▪▀▄.▀·    ▪█·█▌██ ▀▄.▀·██· █▌▐█    ▐█ ▀█▪▪     •██  
▐█▌▐█▪ ▄█▀▄ █▌▐█▌ ▐█.▪█▌▐█▌▐█▀▀█▄▐▀▀▪▄    ▐█▐█•▐█·▐▀▀▪▄██▪▐█▐▐▌    ▐█▀▀█▄ ▄█▀▄  ▐█.▪
 ▐█▀·.▐█▌.▐▌▐█▄█▌ ▐█▌·▐█▄█▌██▄▪▐█▐█▄▄▌     ███ ▐█▌▐█▄▄▌▐█▌██▐█▌    ██▄▪▐█▐█▌.▐▌ ▐█▌·
  ▀ •  ▀█▄▀▪ ▀▀▀  ▀▀▀  ▀▀▀ ·▀▀▀▀  ▀▀▀     . ▀  ▀▀▀ ▀▀▀  ▀▀▀▀ ▀▪    ·▀▀▀▀  ▀█▄▀▪ ▀▀▀ 

    ''')
    number = int(1)
    while True:
     time.sleep(WATCHTIME)
     browser1.refresh()
     browser2.refresh()
     print ("[", end = '')
     print (number, end = '')
     print ("] View/s sent", end = '')
     print(" ")
     number = number + 1

if optionfirst == '3':
    URL = input("Eneter youtube link: ")
    clear()
    print(Fore.RED + '''
            Jammy#4613

 ▄· ▄▌      ▄• ▄▌▄▄▄▄▄▄• ▄▌▄▄▄▄· ▄▄▄ .     ▌ ▐·▪  ▄▄▄ .▄▄▌ ▐ ▄▌    ▄▄▄▄·       ▄▄▄▄▄
▐█▪██▌▪     █▪██▌•██  █▪██▌▐█ ▀█▪▀▄.▀·    ▪█·█▌██ ▀▄.▀·██· █▌▐█    ▐█ ▀█▪▪     •██  
▐█▌▐█▪ ▄█▀▄ █▌▐█▌ ▐█.▪█▌▐█▌▐█▀▀█▄▐▀▀▪▄    ▐█▐█•▐█·▐▀▀▪▄██▪▐█▐▐▌    ▐█▀▀█▄ ▄█▀▄  ▐█.▪
 ▐█▀·.▐█▌.▐▌▐█▄█▌ ▐█▌·▐█▄█▌██▄▪▐█▐█▄▄▌     ███ ▐█▌▐█▄▄▌▐█▌██▐█▌    ██▄▪▐█▐█▌.▐▌ ▐█▌·
  ▀ •  ▀█▄▀▪ ▀▀▀  ▀▀▀  ▀▀▀ ·▀▀▀▀  ▀▀▀     . ▀  ▀▀▀ ▀▀▀  ▀▀▀▀ ▀▪    ·▀▀▀▀  ▀█▄▀▪ ▀▀▀ 

    ''')
    number = int(1)
    while True:
     r = requests.get(URL)
     print ("[", end = '')
     print (number, end = '')
     print ("] Requests/s sent", end = '')
     print(" ")
     number = number + 1
