from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from os import system, name
from colorama import Fore, Back, Style
def clear():
        _ = system('cls')
print(Fore.RED + '''
            Youtube view bot made by jame
             ________________________________________________
            /                                                \
           |    _________________________________________     |
           |   |                                         |    |
           |   |  C:\jam\> python main.py                |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |_________________________________________|    |
           |                                                  |
            \_________________________________________________/
                   \___________________________________/
                ___________________________________________
             _-'    .-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.  --- `-_
          _-'.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.--.  .-.-.`-_
       _-'.-.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-`__`. .-.-.-.`-_
    _-'.-.-.-.-. .-----.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-----. .-.-.-.-.`-_
 _-'.-.-.-.-.-. .---.-. .-------------------------. .-.---. .---.-.-.-.`-_
:-------------------------------------------------------------------------:
`---._.-------------------------------------------------------------._.---'
       Type help for help
       [1]View bot without proxies
       [2]View bot with proxies
''')
optionfirst = input("Eneter option: ")
if optionfirst == '1':
    URL = input("Eneter youtube link: ")
    print("Views automatically set to infinite!")
    time.sleep(1)
    WATCHTIME = input("Enter watch time: ")
    WATCHTIME = float(WATCHTIME)
    VIEWDELAY = input("Enter delay between each watch: ")
    VIEWDELAY = float(VIEWDELAY)
    time.sleep(1)
    print("Settup up varibles")
    browser1 = webdriver.Chrome()
    browser2 = webdriver.Chrome()
    browser3 = webdriver.Chrome()
    browser4 = webdriver.Chrome()
    browser5 = webdriver.Chrome()
    time.sleep(1)
    print("Drivers getting link...")
    browser1.get(URL)
    browser2.get(URL)
    browser3.get(URL)
    browser4.get(URL)
    browser5.get(URL)
    time.sleep(10)
    print("Drivers successfully opened link..")
    print("Refreshing drivers...")
    browser1.refresh()
    browser2.refresh()
    browser3.refresh()
    browser4.refresh()
    browser5.refresh()
    time.sleep(1.5)
    print("Setting up loop...")
    time.sleep(1)
    clear()
    print(Fore.RED + '''
            Youtube view bot made by jame


             ________________________________________________
            /                                                \
           |    _________________________________________     |
           |   |                                         |    |
           |   |  C:\jam\> python main.py                |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |_________________________________________|    |
           |                                                  |
            \_________________________________________________/
                   \___________________________________/
                ___________________________________________
             _-'    .-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.  --- `-_
          _-'.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.--.  .-.-.`-_
       _-'.-.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-`__`. .-.-.-.`-_
    _-'.-.-.-.-. .-----.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-----. .-.-.-.-.`-_
 _-'.-.-.-.-.-. .---.-. .-------------------------. .-.---. .---.-.-.-.`-_
:-------------------------------------------------------------------------:
`---._.-------------------------------------------------------------._.---'
    ''')
    while True:
     time.sleep(WATCHTIME)
     browser1.refresh()
     browser2.refresh()
     browser3.refresh()
     browser4.refresh()
     browser5.refresh()
     print("All browsers finished")
     time.sleep(VIEWDELAY)
     print("View delay finished")

if optionfirst == '2':
    URL = input("Eneter youtube link: ")
    print("Views automatically set to infinite!")
    time.sleep(1)
    WATCHTIME = input("Enter watch time: ")
    WATCHTIME = float(WATCHTIME)
    VIEWDELAY = input("Enter delay between each watch: ")
    VIEWDELAY = float(VIEWDELAY)
    print("Proxie should look like (11.456.448.110:8080) and should be a http/https proxie")
    proxie1 = input("Eneter proxie 1: ")
    proxie2 = input("Eneter proxie 2: ")
    proxie3 = input("Eneter proxie 3: ")
    proxie4 = input("Eneter proxie 4: ")
    proxie5 = input("Eneter proxie 5: ")
    time.sleep(1)
    print("Settup up varibles")
    #browser 1
    chrome_options = WebDriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server=%s' % proxie1)
    browser1 = webdriver.Chrome(chrome_options=chrome_options)
    #browser 2
    chrome_options2 = WebDriver.ChromeOptions()
    chrome_options2.add_argument('--proxy-server=%s' % proxie2)
    browser2 = webdriver.Chrome(chrome_options2=chrome_options2)
    #browser 3
    chrome_options3 = WebDriver.ChromeOptions()
    chrome_options3.add_argument('--proxy-server=%s' % proxie3)
    browser3 = webdriver.Chrome(chrome_options3=chrome_options3)
    #browser 4
    chrome_options4 = WebDriver.ChromeOptions()
    chrome_options4.add_argument('--proxy-server=%s' % proxie4)
    browser4 = webdriver.Chrome(chrome_options4=chrome_options4)
    #browser 5
    chrome_options5 = WebDriver.ChromeOptions()
    chrome_options5.add_argument('--proxy-server=%s' % proxie5)
    browser5 = webdriver.Chrome(chrome_options5=chrome_options5)
    time.sleep(1)
    print("Drivers getting link...")
    browser1.get(URL)
    browser2.get(URL)
    browser3.get(URL)
    browser4.get(URL)
    browser5.get(URL)
    time.sleep(10)
    print("Drivers successfully opened link..")
    print("Refreshing drivers...")
    browser1.refresh()
    browser2.refresh()
    browser3.refresh()
    browser4.refresh()
    browser5.refresh()
    time.sleep(1.5)
    print("Setting up loop...")
    time.sleep(1)
    clear()
    print(Fore.RED + '''
            Youtube view bot made by jame


             ________________________________________________
            /                                                \
           |    _________________________________________     |
           |   |                                         |    |
           |   |  C:\jam\> python main.py                |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |_________________________________________|    |
           |                                                  |
            \_________________________________________________/
                   \___________________________________/
                ___________________________________________
             _-'    .-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.  --- `-_
          _-'.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.--.  .-.-.`-_
       _-'.-.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-`__`. .-.-.-.`-_
    _-'.-.-.-.-. .-----.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-----. .-.-.-.-.`-_
 _-'.-.-.-.-.-. .---.-. .-------------------------. .-.---. .---.-.-.-.`-_
:-------------------------------------------------------------------------:
`---._.-------------------------------------------------------------._.---'
    ''')
    while True:
     time.sleep(WATCHTIME)
     browser1.refresh()
     browser2.refresh()
     browser3.refresh()
     browser4.refresh()
     browser5.refresh()
     print("All browsers finished")
     time.sleep(VIEWDELAY)
     print("View delay finished")
