#WikiScraper - Scrape wikipedia
import requests #request thingy
from bs4 import BeautifulSoup #html parser
import re #regex

print("WikiScraper")
#First, we need to know which pages to scrape
pagesstring = input("Enter the titles of the pages to scrape (separate with tabs):\n")
pages = pagesstring.split("\t")
#if pagesstring starts with "FROM-FILE:", search the following file for the pages to scrape
if pagesstring[0:9] == "FROM-FILE:":
    f = open(pagesstring[10:], "r")
    pages = f.read().split("\n")#from file is split by newline, not tab

#now, we need details about where to store our results
resultsfname = input("Enter results file name:\n")

validresultsformats = ["json", "tsv"]
#json example
#{"articleName":["linkto","linkto"]} (probably more efficient)
#tsv example 
#ArticleName    linkto    linkto (probably more foolproof)

resultsformat = ""
while resultsformat not in validresultsformats:
    resultsformat = input("Enter a valid format for results (json, tsv):\n")

structuredData = {}
#Next, we loop through the pages array
for page in pages:
    #form the full url
    url = "http://wikipedia.org/wiki/"+page
    request = requests.get(url, {"user-agent":"frgo-admin@frgo.org|github.com:3koo2"})
    #now, find all <a> tags (hyperlinks) that are not absolute urls
    soup = BeautifulSoup(request.content, "html.parser")
    atags = soup.find_all("a", {"href":re.compile("^(?!https?)^(?!#)")})
    structuredData[page] = []
    for i in atags:
        structuredData[page].append(i.attrs["href"]) 

print(structuredData) 