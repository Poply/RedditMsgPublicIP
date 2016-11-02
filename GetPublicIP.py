import urllib.request
import praw
import sys
import configparser

def reddit_message(myIP, config):
    r = praw.Reddit("My Assistant")
    r.login(config["main"]["fromaccount"], config["main"]["fromaccountpassword"])                  #Custom setting
    r.send_message(config["main"]["toaccount"], "new ip", myIP)      #Custom setting

config = configparser.ConfigParser()
config.read("currentip.cfg")                            #MIGHT NEED TO PUT IN ABSOLUTE PATH
oldIP = config["main"]["address"]

try:
    myIP = (urllib.request.urlopen('http://ip.42.pl/raw').read()).decode()
except (urllib.error.HTTPError, urllib.error.URLError) as err:
    print(err)
    sys.exit()
else:
    if (myIP != oldIP):
        with open("currentip.cfg", "w") as configfile:
            config.set("main", "address", myIP)
            config.write(configfile)
            configfile.close()
        reddit_message(myIP, config)
        print("Detected IP change. Sending message ", myIP, oldIP)