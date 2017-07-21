import urllib.parse
import urllib.request
import json
import requests

service_url = "https://maps.googleapis.com/maps/api/geocode/json?&address="
address = "omaxe city, rohtak, haryana, india"

url = service_url + urllib.parse.urlencode({'sensor': 'false', 'address':address})
print('Retrieving:', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print(data)
headers = uh.info()
print(dict(headers))
print("Attribute from header: ", headers["Vary"])
js = json.loads(data.decode('UTF-8'))

if js is None or js["status"] != "OK":
    print("Failure")

print("STATUS: ", js["status"])

print("Printing json dumps: ",json.dumps(js, indent=4))

