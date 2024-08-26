import sys
import urllib.request
import re

def antihtml(url):
        with urllib.request.urlopen(url) as response:
            html_content = response.read().decode('utf-8')
        stripped_content = re.sub(r'<[^>]+>', '', html_content)
        print(stripped_content)

url = sys.argv[1]
antihtml(url)

