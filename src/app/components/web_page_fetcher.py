import sys
import urllib.request
from urllib.parse import urlparse
from lxml import html
from pprint import pprint


prog_name, full_url = sys.argv

if full_url:
    hrefs = []
    
    scheme = urlparse(full_url).scheme
    baseurl = urlparse(full_url).netloc
    
    root = html.fromstring(urllib.request.urlopen(full_url).read())        
    links = root.xpath('//a/@href')
    html = html.tostring(root, pretty_print=True, method="html").decode('utf-8')

    for link in links:
        if (urlparse(link).scheme and urlparse(link).netloc):
            hrefs.append(link)
        else:
            o = urlparse(link)
            link = o._replace(scheme=f'{scheme}', netloc=f'{baseurl}').geturl()
            hrefs.append(link)
            
    print(html)
    print("Link: ")
    pprint(hrefs)
    
