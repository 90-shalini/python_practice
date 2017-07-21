import urllib

url = input('Enter url: ')
html = urllib.urlopen(url).read()

tags = {}
for tag in tags:
    print(tag.get('href', None))