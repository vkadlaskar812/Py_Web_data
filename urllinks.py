import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


flag = 0
count = 7
i = 0
j = 0

while i<count:
    if flag == 0:
        url = input('Enter- ')
        flag = 1
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup('a')
        for tag in tags:
            S = str(tag.get('href', None))
            
            j+=1
            if j == 18:
            # print("-------------") // just to know where loop ends
             break
            
        url = S
        
    else :
       
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup('a')
        k=0
        for tag in tags:
            S = str(tag.get('href', None))
           
            k+=1
            if k == 18:
            #  print("-------------") //just to know where loop ends
             break
        url = S
    i+=1    
x = re.findall("_\S(Y[a-z]+)\S",url)
print(x[0])

