# RedditMsgPublicIP
Put getpublicip.py and currentip.cfg in the same directory for this to work.

I made this script with the purpose of notifying me when the public IP on my internet service is changed due to the residential IPs being assigned dynamically by the ISP. I personally keep this running on a cronjob on my raspberry pi at home and send std and err output to a log.txt file.

It works by sending an http request to a site made for the explcit purpose of telling you your IP, ip.42.pl. It will then check that IP with the IP in your currentip.cfg file. If it is the same, the program ends. If it is different it will login to your reddit account specified in the config file and send a message to the specified user. You may use the same user account for both the sender and receiver.
