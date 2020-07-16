### Simple script to download a couple of pages for examination
import requests
import bs4

base_url = 'https://forums.sufficientvelocity.com/threads/warhammer-fantasy-divided-loyalties-an-advisors-quest.44838/'
threadmarks_url = base_url + 'threadmarks'
page_1_url = base_url + 'page-1'

def download_page(url, filename):
    request = requests.get(url)
    if (request.ok):
        soup = bs4.BeautifulSoup(request.text,features="html.parser")
        f = open(filename, 'w')
        f.write(soup.prettify())
        f.close()
    else:
        print (f"oops, something went wrong. Here's the error code: {request.status_code}")

download_page(threadmarks_url, 'test_data/dl_threadmarks.html')
download_page(page_1_url, 'test_data/dl_page_1.html')

