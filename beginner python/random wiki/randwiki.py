'''
Retrieve random list of articles from wiki
Loop through this list
print title of article
Ask reader if user wants to read it
If they say yes, open the link to the article in a browser
Wait..if user presses N, repeat question and Loop
give an option to exit
'''

'''
need requests to retrieve list
need json to interpret json of wiki and pick article title and link
loop
need webbrowser to open link
'''

import requests, json, sys, webbrowser



url = "https://en.wikipedia.org/w/api.php?action=query&list=random&rnnamespace=0&rnlimit=10&format=json"

articlelist = requests.get(url)

alistjson = json.loads(articlelist.text)

for i in range(0,10):
  x = alistjson["query"]["random"][i]["title"]
  print(f"Do you want to read the article {x}? Press 'Y' to read, 'N' to skip, and 'Q' to quit program")
  proceed = input()
  if proceed == "Y" :
    urlDest = "https://en.wikipedia.org/wiki/" + x
    webbrowser.open(urlDest)
  elif proceed == "N" :
    urlDest = "https://www.google.com"
    webbrowser.open(urlDest)
    continue
  elif proceed == "Q" :
    sys.exit()



