import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import pandas as pd
from collections import OrderedDict
import sqlite3
import sys


class StatsDownloader:
    def __init__(self, playerProfileLink,playerName):
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        self.playerProfileLink = playerProfileLink
        self.html = urllib.request.urlopen(self.playerProfileLink, context=ctx).read()
        self.playerName = playerName


    def downloadBattingStats(self):
        print("Downloading batting stats for "+self.playerName)
        list_of_dict = []
        bs = BeautifulSoup(self.html, "lxml")
        table_body = bs.find_all('tbody')
        rows = table_body[0].find_all('tr')
        headings = bs.findAll('tr', {"class", "head"})

        heads = headings[:2]
        vatting = heads[0]
        bowling = heads[1]

        batText = vatting.find_all("th")
        bowlText = bowling.find_all("th")
        bat = []
        for i in batText:
            bat.append(i.text)

        bowl = []
        for i in bowlText:
            bowl.append(i.text)

        # print(len(bat))

        for row in rows:
            cols = row.find_all('td')
            cols = [x.text.strip() for x in cols]
            temp_data = OrderedDict()
            # {el: 0 for el in bat}
            #     print(len(cols))
            #     print(cols)
            #     print(bat)
            for col in range(len(cols)):
                temp_data[bat[col]] = cols[col]

            list_of_dict.append(temp_data)

        # In[41]:

        batDf = pd.DataFrame(list_of_dict)
        batDf.set_index('', inplace=True)
        print("Download successfull")
        return batDf


    def downloadBowlingStats(self):
        temp_data = OrderedDict()
        list_of_dict = []
        bs = BeautifulSoup(self.html, "lxml")
        table_body = bs.find_all('tbody')
        rows = table_body[1].find_all('tr')
        headings = bs.findAll('tr', {"class", "head"})

        heads = headings[:2]
        vatting = heads[0]
        bowling = heads[1]

        batText = vatting.find_all("th")
        bowlText = bowling.find_all("th")
        bat = []
        for i in batText:
            bat.append(i.text)

        bowl = []
        for i in bowlText:
            bowl.append(i.text)

        # print(bat[1:])
        # print(bowl[1:])

        # bat = bat[1:]
        # bowl = bowl[1:]
        print(len(bat))

        for row in rows:
            cols = row.find_all('td')
            cols = [x.text.strip() for x in cols]
            temp_data = OrderedDict()
            #     print(len(cols))
            #     print(cols)
            #     print(bat)
            for col in range(len(cols)):
                temp_data[bowl[col]] = cols[col]

            list_of_dict.append(temp_data)


        bowl_df = pd.DataFrame(list_of_dict)
        bowl_df.set_index('', inplace=True)
        return bowl_df


