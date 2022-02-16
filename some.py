from datetime import datetime
from logging import error
from tokenize import String
from pythonping import ping
import os

if os.path.exists("ping.txt"):
    os.remove("ping.txt")

print(datetime.now().strftime("%m/%d/%Y, %H:%M:%S"), file=open('ping.txt', 'a'))

while True:
    try:
            fullstring = ping('8.8.8.8', count=1).__str__()
            y = 'Req'
            if y in fullstring:
                print('Packet loss. Gleba:', datetime.now().strftime("%m/%d/%Y, %H:%M:%S"), file=open('gleba.txt', 'a'))
            elif float(fullstring[31:36]) > 99.0:
                print('Ping too high.(', fullstring[31:35], ') Gleba:', datetime.now().strftime("%m/%d/%Y, %H:%M:%S"), file=open('gleba.txt', 'a'))
            else:
                print(fullstring[31:36], file=open('ping.txt', 'a'))
    except Exception as err:
            print('{}'.format(err), file=open('except.txt', 'a'))