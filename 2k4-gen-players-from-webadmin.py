#!/usr/bin/env python3

import requests
import lxml.html as lh
from requests.auth import HTTPBasicAuth

# Version:  0.0.9
# Date:  20200307
# Author:  serverlinkdev@gmail.com
# License:   BSD
# Requires:  python 3
# Validation:  Ubuntu 18.04 LTS Python 3, Windows 10 Home Python 3
#
# Changelog:
# 20200307 0900hrs: init rel. 0.0.9
################################################################################

url = "http://localhost:3177/ServerAdmin/current_players"
page = requests.get(url, auth=HTTPBasicAuth("adminName", "mypassword"))
data = lh.fromstring(page.content)

# Parse data tween <tr>..</tr> of HTML only
tr_elements = data.xpath('//tr')

listLen = str(len(tr_elements))
numPlayers = str(int(listLen) - 7)
print("There are : " + numPlayers + " playing right now")
# we start from number 6 and then thru the list to avoid headers, checkboxes
# in the html, -1 is so we don't get empty line at end of printout
i = 1
for t in tr_elements[6:(int(listLen)-1)]:
    playerName = t[2].text_content().strip()
    print(str(i) + " : " + playerName)
    i += 1

# Installation:
# Windows 10 msys2:
# pacman -S mingw-w64-x86_64-python3-requests mingw-w64-x86_64-python3-pandas \
#   mingw-w64-x86_64-python3-numexpr mingw-w64-x86_64-python3-lxml 
#   optional: but really recommended if we expand this app: mingw-w64-x86_64-python3-cssselect
#
# Compilation:
# Windows python 3 official release native:
# 
# Install python 3 from python.org
# Install pip:
#   curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
#   or download it w/web browser
# pip install requests numexpr lxml pyinstaller
#
# pip and pyinstaller are installed into python/scripts dir.
#
# pyinstaller -F 2k4-gen-players-from-webadmin.py #(builds standalone exe)
#
# Output will be in subdirectory called "dist" with 2k4-gen-players-from-webadmin.exe
#
# INFO: use -w to if you want to remove console display for GUI's.
#   not applicable to this project, but good to know.
