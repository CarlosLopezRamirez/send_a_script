import os
import applescript
import requests
import time
import sys
from bs4 import BeautifulSoup

# Function that sends script #
def send_script(str):
    if str == 'B':
        url = 'http://www.script-o-rama.com/movie_scripts/a1/bee-movie-script-transcript-seinfeld.html'
    elif str == 'S':
        url = 'http://www.script-o-rama.com/movie_scripts/s/shrek-script-transcript-mike-myers.html'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find('pre')
    script = results.text.strip()
    script = script.split(' ')
    for word in script:
        apple_script = 'send "%s" to buddy "%s" of service "SMS"' % (word, pho_num)
        applescript.tell.app("Messages", apple_script, background=True)
        time.sleep(2)

# Gathers phone number #
print('Type in a phone number, include country code and area code (eg. +1404XXXXXXX)')
pho_num = input()

# Gathers choice of script #
print("""Type and enter one of the following: 
      - "B" if you want to send the Bee Movie Script,
      - "S" if you want to send the Shrek Script,
      """)
choice = input()

# Calls function based on choice of script #
if choice == 'B':
    print('You chose the Bee Movie! Sending now.')
    send_script('B')
elif choice == 'S':
    print('You chose Shrek! Sending now.')
    send_script('S')
else:
    print('You didnt choose a valid option! Ending program...')
    sys.exit(0)