import json
import requests
#import time

headers = {"User-Agent": "Assetto Corsa Launcher", ".": "DAB7072BFE38B33F658E7E376CDFAB0F", "Host": "93.57.10.21", "Accept-Encoding": "gzip, deflate", "Connection": "Keep-Alive"}
content = {"guid": "76561197985541827"}
listurl = "http://93.57.10.21/lobby.ashx/list"
server = "http://176.9.76.209:9826/"

r = requests.post(server, headers=headers, data=content)
#r.encoding = 'utf-8'
print r.content
