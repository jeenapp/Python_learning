import sys
import urllib.request

def download_url(url):
    if url.endswith('/'):
        filename = 'index.html'
        print(filename)
    else:
        filename = url.split('/')[-1] or 'index.html'
    with urllib.request.urlopen(url) as response:
        content = response.read()
    with open(filename, 'wb') as file:
        file.write(content)   
    print(f"File saved as {filename}")
    
url = sys.argv[1]
download_url(url)


