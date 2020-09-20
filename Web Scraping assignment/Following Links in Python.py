import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

input_link = input('enter URL - ')
open_url = urllib.request.urlopen(input_link).read()

soup = BeautifulSoup(open_url, 'html.parser')
tags = soup('a')


count = 7
for i in range (count):
    position =18
    for tag in tags:
        position -= 1
        if position == 0:
            print(tag.get('href', None))
            print(tag.contents[0])
            new_url = tag.get('href', None)
            open_url = urllib.request.urlopen(new_url).read()
            soup = BeautifulSoup(open_url, 'html.parser')
            tags = soup('a')