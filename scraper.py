import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import pandas as pd
from collections import OrderedDict
import sqlite3
import sys


def playerName(url):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    # In[39]:
    # url = "http://www.espncricinfo.com/india/content/player/34102.html"

    # html = urllib.request.urlopen(url, context=ctx).read()
    # text_file = open("links.txt", "r")
    #
    # lines = text_file.read().split('\n')
    #
    # # print(lines)

    # for url in lines:
    html = urllib.request.urlopen(url, context=ctx).read()
    bs = BeautifulSoup(html, "lxml")
    names = bs.find_all("p",{"class":"ciPlayerinformationtxt"});
    return names[0].text.split("\n")[1]

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
            name = playerName(getFullLink(link))
            res[name] =getFullLink(link)
    # print(res)
    return res

if __name__ == '__main__':
    print(listOfPlayers())