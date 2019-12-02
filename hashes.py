import hashlib
import urllib.request

with open('hashes.txt', 'r', encoding='utf-8') as fp:
    mylist = fp.read().splitlines() 

i = 0
for line in mylist:
    print ("Checking hash "+str(i+1))
    m = hashlib.sha1()
    m.update(line.encode('utf-8'))
    hexdigest = m.hexdigest()
    firstfive=hexdigest[:5]
    lastfive=hexdigest[35:]
    response = urllib.request.urlopen('https://api.pwnedpasswords.com/range/'+firstfive)
    html = response.read()
    if lastfive.encode('utf-8') in html:
        print ("Match found")
    
    i=i+1