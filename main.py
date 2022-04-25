import requests
from colorama import Fore, init
import shutil
import ctypes
init(convert=True)
columns = shutil.get_terminal_size().columns
ctypes.windll.kernel32.SetConsoleTitleW("IPTracker | By ManiacX0 - discord.gg/yxc3KqNf6e")
foretext = """
                                        ________  ______                __            
                                       /  _/ __ \/_  __/________ ______/ /_____  _____
                                       / // /_/ / / / / ___/ __ `/ ___/ //_/ _ \/ ___/
                                     _/ // ____/ / / / /  / /_/ / /__/ ,< /  __/ /    
                                    /___/_/     /_/ /_/   \__,_/\___/_/|_|\___/_/     
                                                  
                                                IPTracker - By ManiacX0
""".center(columns)

print(Fore.LIGHTBLUE_EX + foretext)
print(Fore.CYAN + "Enter the vicitm's IP")
ip = input("\n> ")

try:
    getip = requests.get(url = f"https://geo.leadboxer.com/GeoIpEngine/{ip}?jsonp")
    data = getip.json()

    req2 = requests.get(url ="https://stevemorse.org/jcal/proxycode.php?&noCacheIE=1650908121322")
    dat = req2.text
    callback = dat[14:][:7]

    print()
    print(Fore.RED + "Country: " + data['countryName'])
    print(Fore.LIGHTRED_EX + "Continent: " + data['continent'])
    print(Fore.LIGHTCYAN_EX + "Postal Code: " + data['postalCode'])
    print(Fore.CYAN + "Latitude: " + data['latitude'])
    print(Fore.BLUE + "Longitude: " + data['longitude'])
    print(Fore.LIGHTGREEN_EX + "City: " + data['city'])

    lat = data['latitude']
    lon = data['longitude']

    req3 = requests.get(url = f"https://stevemorse.org/jcal/latlonlocal.php?cookie=&hidden=&doextra=&code={callback}&protocol=https%3A&time=1650908121321&addr2latlon=0&address=&city=&state=&zip=&country=US&latlon2addr=1&latitude={lat}4&longitude={lon}")
    source = req3.text

    left = "<br><br><i>MapQuest</i><br>"
    right = "<br><br><br><img src"
    print(Fore.GREEN + "Adress: " + source[source.index(left)+len(left):source.index(right)])
    input("\nPress enter to exit...")
except:
    print(Fore.LIGHTRED_EX + "\nFailed... Try again !")
    input("\nPress enter to exit...")