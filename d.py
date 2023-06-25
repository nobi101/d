from bs4 import BeautifulSoup
from datetime import datetime
import re,requests,os,sys
from time import sleep 
from datetime import date
import requests, random
import requests
import base64, json,os
from datetime import date
from datetime import datetime
from time import sleep,strftime
from bs4 import BeautifulSoup
from datetime import datetime
import re,requests,os,sys
from time import sleep 
from datetime import date
import requests, random
import uuid, re
from pystyle import Write,Colors
os.system('title TOOL GỘP TRAODOISUB')

time=datetime.now().strftime("%H:%M:%S")
from pystyle import *
data_machine = []
today = date.today()
now = datetime.now()
thu = now.strftime("%A")
ngay_hom_nay = now.strftime("%d")
thang_nay = now.strftime("%m")
nam_ = now.strftime("%Y")
print('             ███████╗██████╗ ██╗██╗   ██╗███████╗')
print('             ██╔════╝██╔══██╗██║██║   ██║██╔════╝')
print('             █████╗  ██████╔╝██║██║   ██║█████╗  ')
print('             ██╔══╝  ██╔══██╗██║╚██╗ ██╔╝██╔══╝  ')
print('             ██║     ██║  ██║██║ ╚████╔╝ ███████╗')
print('             ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝  ╚══════╝')
print('           Copyright © FRIVE-Tool 2023 | Version 1.1')
print(f"                Ngày: {ngay_hom_nay} Tháng: {thang_nay} Năm: {nam_}\n")
print("┌─────┬────────────────────────────────────┬─────────┬─────────┐")
print("│ STT │             MENU TOOL              │ STATUS  │ VERSION │")
print("├─────┼────────────────────────────────────┼─────────┼─────────┤")
print("│  1  │ TDS FACEBOOK                       │ ONLINE  │  [1.0]  │")
print("├─────┼────────────────────────────────────┼─────────┼─────────┤")
print("│  2  │ TDS FACEBOOK                       │ ONLINE  │  [2.0]  │")
print("├─────┼────────────────────────────────────┼─────────┼─────────┤")
print("│  3  │ TDS FACEBOOK PRO5                  │ ONLINE  │  [1.0]  │")
print("├─────┼────────────────────────────────────┼─────────┼─────────┤")
print("│  4  │ TDS INSTAGRAM                      │ ONLINE  │  [1.0]  │")
print("├─────┼────────────────────────────────────┼─────────┼─────────┤")
print("│  5  │ TDS TIKTOK                         │ ONLINE  │  [1.0]  │")
print("├─────┼────────────────────────────────────┼─────────┼─────────┤")
print("│  6  │ TDS TIKTOK MAX SPEED               │ ONLINE  │  [1.0]  │")
print("├─────┼────────────────────────────────────┼─────────┼─────────┤")
print("│  7  │ QUAY LẠI                           │   =.=   │   NEXT  │")
print("└─────┴────────────────────────────────────┴─────────┴─────────┘\n")
chon = input("Nhập Lựa Chọn: ")
os.system("cls" if os.name == "nt" else "clear")
try:
        if chon == '1':
                run = requests.get('https://raw.githubusercontent.com/nobi101/facebooki/main/facebook.py').text
        elif chon == '2':
                run = requests.get('https://raw.githubusercontent.com/nobi101/tdspr5/main/tdspr5.py').text
        elif chon == '3':
                run = requests.get('https://raw.githubusercontent.com/nobi101/ins/main/ins.py').text
        elif chon == '4':
                run = requests.get('https://raw.githubusercontent.com/nobi101/tiktok/main/tiktok.py').text
        elif chon == '5':
                run = requests.get('https://raw.githubusercontent.com/nobi101/tiktokspeed/main/tiktokspeed.py').text
        elif chon == '6':
                run = requests.get('https://raw.githubusercontent.com/nobi101/gop/main/gop.py').text
        else:
                run = print('Lựa Chọn Không Xác Định')
except:
        if not is_connected():
                print('Hãy Kiểm Tra Kết Nối Mạng !!! ')
        else:
                print('Sever Gặp Lỗi Hãy Liên Hệ Admin !!! ')
        exit()
exec(run)
