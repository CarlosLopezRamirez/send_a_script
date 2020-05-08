import os
import applescript
import requests
from bs4 import BeautifulSoup

print('Type in a phone number, include country code and area code (eg. +1404XXXXXXX)')
pho_num = input()
print("""Type and enter one of the following: 
      - "B" if you want to send the Bee Movie Script,
      - "S" if you want to send the Shrek Script,
      - "SW" if you want to send the Revenge of the Sith Script""")
choice = input()
if choice == 'B':
    print('You chose the Bee Movie! Sending now.')
    bee_url = 'http://www.script-o-rama.com/movie_scripts/a1/bee-movie-script-transcript-seinfeld.html'
    bee_page = requests.get(bee_url)
    bee_soup = BeautifulSoup(bee_page.content, 'html.parser')
    bee_results = bee_soup.find('pre')
    bee_script = bee_results.text.strip()
    bee_script = bee_script.split(' ')
    for word in bee_script:
        apple_script = 'send "%s" to buddy "%s" of service "SMS"' % (word, pho_num)
        r = applescript.tell.app("Messages", apple_script, background=True)
elif choice == 'S':
    print('You chose Shrek! Sending now.')
elif choice == 'SW':
    print('You chose Revenge of the Sith! Sending now.')
else:
    print('You didnt choose a valid option! Ending program...')




          



