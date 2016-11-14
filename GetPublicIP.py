import urllib.request
import praw
import sys
import configparser
import os

def reddit_message(myIP, config):
    r = praw.Reddit("My Assistant")
    r.login(config["main"]["fromaccount"], config["main"]["fromaccountpassword"])
    r.send_message(config["main"]["toaccount"], "new ip", myIP)

config = configparser.ConfigParser()
config.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), "currentip.cfg"))
oldIP = config["main"]["address"]

try:
    myIP = (urllib.request.urlopen('http://ip.42.pl/raw').read()).decode()
except (urllib.error.HTTPError, urllib.error.URLError) as err:
    print(err)
    sys.exit()
else:
    if (myIP != oldIP):
        with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "currentip.cfg"), "w") as configfile:
            config.set("main", "address", myIP)
            config.write(configfile)
            configfile.close()
        reddit_message(myIP, config)
        print("Detected IP change. Sending message ", myIP, oldIP)