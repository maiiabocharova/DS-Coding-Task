import requests
from lxml import html
import time

hpilosophy_link = "https://en.wikipedia.org/wiki/Philosophy"
visited_urls = set()
start_url = input()

while url != hpilosophy_link or url not in visited_urls:
    visited_urls.add(url)
    page = requests.get(url=url).text
    root = html.fromstring(page)
    href = root.xpath("//div/p/a[not(@class)]/@href")[0]
    url = "https://en.wikipedia.org" + href
    print(url)
    time.sleep(0.5)