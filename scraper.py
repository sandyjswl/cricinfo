import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import pandas as pd
from collections import OrderedDict
import sqlite3
import sys


def playerName():
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    # In[39]:

    # html = urllib.request.urlopen(url, context=ctx).read()
    text_file = open("links.txt", "r")

    lines = text_file.read().split('\n')

    # print(lines)

    for url in lines:
        html = urllib.request.urlopen(url, context=ctx).read()
        bs = BeautifulSoup(html, "lxml")
        names = bs.find_all("h1");
        print(names[1].text)

def getFullLink(link):
    return "http://www.espncricinfo.com"+link


def listOfPlayers():
    res = {}
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    url = "http://www.espncricinfo.com/india/content/player/country.html?country=6"
    html = urllib.request.urlopen(url, context=ctx).read()
    bs = BeautifulSoup(html, "lxml")
    headings = bs.findAll('table', {"class", "playersTable"})
    # print(headings)
    for h in headings:
        r = h.findAll("td",{"class":"divider"})
        # print(r)
        for i in r:
            link = (i.find("a").get("href"))
            name = (i.text)
            res[name] =getFullLink(link)
    # print(res)
    return res

if __name__ == '__main__':
    listOfPlayers()