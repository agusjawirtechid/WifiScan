import json
import subprocess
import shutil
from colorama import Fore
import time
import os

cmd = "termux-wifi-scaninfo"
if shutil.which(cmd) is None:
  print("Wifi tidak ditemukan")
wifi_hasil = subprocess.run([cmd],
capture_output=True, text=True)
data = json.loads(wifi_hasil.stdout)


print(Fore.RED + r"""
 __          ___  __  _____            
 \ \        / (_)/ _|/ ____|           
  \ \  /\  / / _| |_| |     __ _ _ __  
   \ \/  \/ / | |  _| |    / _` | '_ \ 
    \  /\  /  | | | | |___| (_| | | | |
     \/  \/   |_|_|  \_____\__,_|_| |_|
                                       
                          by: AgusJawir""")
print(" ")

for i in range(3):
  os.system("termux-torch on")
  time.sleep(0.5)
  os.system("termux-torch off")

for w in data:
  rssi = w["rssi"]
  ssid = w["ssid"]
  keamanan = w["capabilities"]
  
  if rssi <= -90:
    sinyal = "[|     ] 1"
  elif rssi <= -80:
    sinyal = "[||    ] 2"
  elif rssi <= -70:
    sinyal = "[|||   ] 3"
  elif rssi <= -60:
    sinyal = "[||||  ] 4"
  elif rssi <= -50:
    sinyal = "[||||| ] 5"
  elif rssi <= -40:
    sinyal = "[||||||] 6"
  elif rssi <= -30:
    sinyal = "[###########] 5"
  
  print(Fore.LIGHTGREEN_EX + f"nama wiffi: {ssid}")
  print(Fore.LIGHTBLUE_EX + f"PING SINYAL {sinyal}")
  print(Fore.LIGHTYELLOW_EX + f"Keamanan wifi {keamanan}")
  print(Fore.LIGHTRED_EX + """password : ********"""
  )
  time.sleep(2)
  print(" ")
pilih = input("masukan nama wifi untuk di hack: ")
print(Fore.LIGHTYELLOW_EX + "Mana bisa tolol😂😂")