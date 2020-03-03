import json
import requests
import sys
import time

with open("json.json", "r") as j :
    ldata = j.read()

w = open("new.txt", "a")

ldata = json.loads(ldata)
#url = "/json.json"
#ldata = requests.get(url, headers = {'customazzusername345754': 'yourbot4356747'})
#ldata = requests.get(url)
'''
try :
    ldata.raise_for_status()
except Exception :
    print("There was a problem. Maybe reddit json has been called too many times or the username is no good.")
    sys.exit()'''


for i in range(0,25) :
    ld = ldata["data"]["children"][i]["data"]["title"]
    ld = ld.strip()
    if ld.startswith("TIL that") :
        ld = ld.lstrip("TIL that ")
    elif ld.startswith("TIL") :
        ld = ld.lstrip("TIL")
    ld = ld.strip()
    print(ld.capitalize())
    w.write(ld)
    print("#"*20)
    time.sleep(0)

print(w)
