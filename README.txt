WikiScraper
WikiScraper is a project intended to scrape wikipedia and record hyperlinks

It is written in python

WikiScraper is very simple to use
Download WikiScraper.py, and run
Requires requests, Beautiful Soup 4 (bs4), Regex (re), and json

You will be prompted for a list of articles you want to scrape the links from
There are two ways to tell the program what articles to scrape:
    1. A direct list
    2. A list file
Direct List:
When prompted for you article list, type in the names of the articles you want to scrape, separated by tabs
eg.
Python_(Programming_language)   Web_scraping    Frog

List File:
Before running the program, create a plaintext file
In this file, write each article you want to visit on its own line
eg.
Python_(Programming_language)
Web_scraping
Frog

Save this file as any name you would like
Now, when you execute the program and it prompts you to enter your article list, type
"FROM-FILE:" and then (with no space) the name of your file
If you saved your file in a different directory, you will need to put a complete path

Note that wikipedia may redirect names that are spelled incorrectly

The program will now ask you for a name for your output file - enter any file name you would like
The next, and final step is to enter the format you would like your data back in
You can type either "json" or "tsv"

Now, wait for the program to scan each page, and it will record the internal wikipedia links in the specified file.