import requests
import re
import sys
import time

time.sleep(2)

url = sys.argv[1]
r = requests.get(url)
html = r.text.encode('utf8')
search = re.findall(r'<a href=[\'"?](https[://\w\-._]+)', html.decode('utf8'))

for link in search:
    print(link)
