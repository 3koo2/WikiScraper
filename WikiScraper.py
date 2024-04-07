#WikiScraper - Scrape wikipedia
import requests #request thingy
from bs4 import BeautifulSoup #html parser

#First, we need to know which pages to scrape
pagesstring = input("Enter the titles of the pages to scrape (separate with tabs):\n")
pages = pagesstring.split("\t")

#Next, we loop through the pages array
for page in pages:
    #form the full url
    url = "http://wikipedia.org/wiki/"+page
    request = requests.get(url, {"user-agent":"frgo-admin@frgo.org|github.com/3koo2"})
    print(request.content)