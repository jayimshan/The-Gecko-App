# from bs4 import BeautifulSoup

# import requests
# import re

# url = 'https://abominabletoys.com/'
# r = requests.get(url)
# soup = BeautifulSoup(r.text, 'lxml')
# for link in soup.find_all('a', href=True):
# 	print(link['href'])

from datetime import datetime
import math

now = datetime.now()
timestamp = datetime.timestamp(now)

print(math.floor(timestamp))