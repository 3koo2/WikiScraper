#WikiScraper - Scrape wikipedia
import requests #request thingy
from bs4 import BeautifulSoup #html parser
import re #regex
import json #json

print("WikiScraper")
#First, we need to know which pages to scrape
pagesstring = input("Enter the titles of the pages to scrape (separate with tabs):\n")
pages = pagesstring.split("\t")
#if pagesstring starts with "FROM-FILE:", search the following file for the pages to scrape
if pagesstring[0:10] == "FROM-FILE:":
    f = open(pagesstring[10:], "r")
    pages = f.read().split("\n")#from file is split by newline, not tab

#now, we need details about where to store our results
resultsfname = input("Enter results file name:\n")

validresultsformats = ["json", "tsv"]
#json example
#{"articleName":["linkto","linkto"]} (probably more efficient, more standard)
#tsv example 
#ArticleName    linkto    linkto (probably more foolproof, easier on the eyes)

resultsformat = ""
while resultsformat not in validresultsformats:
    resultsformat = input("Enter a valid format for results (json, tsv):\n")

structuredData = {}
#Next, we loop through the pages array
for page in pages:
    #form the full url
    print(page)
    url = "http://wikipedia.org/wiki/"+page
    request = requests.get(url, {"user-agent":"frgo-admin@frgo.org|github.com:3koo2"})
    #now, find all <a> tags (hyperlinks) that are not absolute urls
    soup = BeautifulSoup(request.content, "html.parser")
    body = soup.find("div", {"id":"bodyContent"})
    atags = body.find_all("a", {"href":re.compile("^(?!https?)^(?!#)^/wiki/(?!Wikipedia:)(?!Category:)(?!Special:)(?!File:)(?!Help:)(?!Template:)(?!Template_talk:)(?!Portal:)")})
    structuredData[page] = []
    for i in atags:
        structuredData[page].append(i.attrs["href"]) 

#format + save data
#first, open file
results = open(resultsfname, "w")
if resultsformat == "json":
    results.write(json.dumps(structuredData))
elif resultsformat == "tsv":
    keys = structuredData.keys()
    for key in keys:
        results.write(key)
        for item in structuredData[key]:
            results.write("\t"+item)
        results.write("\n")

print("Done! Saved to "+resultsfname)
results.close()