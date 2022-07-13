import urllib.request, urllib.parse, urllib.error
import re
from bs4 import BeautifulSoup

url = input('Enter- ') #http://www.dr-chuck.com/page1.htm
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

sum =0
tags = soup('span')
for tag in tags:
    y = str(tag)
    
    x= re.findall("[0-9]+",y)
    for i in x:
        i = int(i)
        sum+=i
print(sum)
    
 