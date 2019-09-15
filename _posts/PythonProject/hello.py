import webbrowser
import json
import requests

print("Let's find an old website.")
site = input("Type a website URL: ")
era = input("Type a year, month, and day like 20190101: ")
url = "http://archive.org/wayback/avaliable?url=%s&timestamp=%s" % (site, era)
response = requests.get(url)
data = response.json()
try:
    old_site = data["archived_snapshots"]["closests"]["url"]
    print("Found this copy: ", old_site)
    print("It should appear in your browser now.")
    webbrowser.open(old_site)
except:
    print("Sorry, no luck finding", site)