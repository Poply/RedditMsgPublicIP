import urllib.request
import praw
import sys
import os

def reddit_message(myIP):
    r = praw.Reddit("My Assistant")
    r.login("MYACCOUNT", "MYPASSWORD")                  #Custom setting
    r.send_message("OTHERACCOUNT", "new ip", myIP)      #Custom setting

fileLocation = os.getcwd() + str("/" if "/" in os.getcwd() else "\\") + "currentip.txt"     #Will look at current directory to determine whether to use / or \
f = open(fileLocation, 'r+')
oldIP = f.read()[:-1] #TODO currently cutting off last character because it is picking up a garbage char and ruining the if...then check when comparing IPs

try:
    myIP = (urllib.request.urlopen('http://ip.42.pl/raw').read()).decode()
except (urllib.error.HTTPError, urllib.error.URLError) as err:
    print(err)
    sys.exit()
else:
    if (myIP != oldIP):
        f.seek(0)
        f.write(myIP)
        reddit_message(myIP)
        print("Detected IP change. Sending message ", len(myIP), len(oldIP), (myIP == oldIP))
finally:
    f.close()