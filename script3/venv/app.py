# Group Members: Ivory Steed, Paul Thottappilly, Hassan Chugtai, Tony Le, Shekar Balasubramaniam

import requests

r = requests.get('https://www.charlotte.edu/')

print(r.text)