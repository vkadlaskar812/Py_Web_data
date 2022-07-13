import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('file:///C:/Users/Vikrant/Desktop/bunny.html')
for line in fhand:
    print(line.decode().strip())