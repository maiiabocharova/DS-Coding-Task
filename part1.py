import requests
from lxml import html
import time
from bs4 import BeautifulSoup
hpilosophy_link = "https://en.wikipedia.org/wiki/Philosophy"
visited_urls = set()
url = input()

while url != hpilosophy_link and url not in visited_urls:
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    print(r.url)  # Print current url

    # getting rid of unnecessary stuff
    content = soup.find(id='mw-content-text')
    for t in content.find_all(class_=['navbox', 'vertical-navbox', 'toc']):
        t.replace_with("")

    for s in content.find_all(
            ['span', 'small', 'sup,', 'i', 'table']):  # remove spans and smalls with language, pronounciation
        s.replace_with("")

    root = html.fromstring(str(content))
    href = root.xpath("//div/p/a/@href")[0]

    url = "https://en.wikipedia.org" + href
    print(href)
    time.sleep(0.5)