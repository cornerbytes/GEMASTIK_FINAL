import requests
import urllib
url = "http://10.100.101.109:10000/art/"
url = "http://10.100.101.117:10000/art/"
payload ="#{7 * 7}"

payload = urllib.parse.quote(payload)
print(payload)
print(requests.get(url+payload).text)

