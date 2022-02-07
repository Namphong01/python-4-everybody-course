import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import collections
collections.Callable = collections.abc.Callable
import ssl

ctx= ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

n = input('Enter URL: ')
count = input('Enter count ')
position = input('Enter position ')

for i in range(int(count) + 1):
    html = urllib.request.urlopen(n, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    print ('Retrieving:',n)

    n = tags[int(position) - 1].get('href', None)