# Scraping Numbers from HTML using BeautifulSoup 

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
sum =0
count = 0
for span in tags:
    # Look at the parts of a tag
    cont = int(span.contents[0])
    sum = sum + cont
    count += 1

# Prints the content count and sum      
print('Count ' + str(count))
print('Sum ' + str(sum))    