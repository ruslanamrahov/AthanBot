import requests


api_key = '58b05ba71037e485f296f17e222f4449'
requests.packages.urllib3.disable_warnings()
r = requests.get("http://muslimsalat.com/krakow/4.json?key="+api_key)
reply = r.json()
print(reply["items"][0]["fajr"])