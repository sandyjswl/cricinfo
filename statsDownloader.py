#!/usr/bin/env python
# coding: utf-8

# In[34]:


import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import pandas as pd
from collections import OrderedDict
import sqlite3
import sys

# In[35]:


conn = sqlite3.connect('Hello.db')
curr = conn.cursor()
playerName = "Rohit Sharma"

# In[36]:


curr.execute("SELECT * FROM Players WHERE Player_Name=?", ("Rohit Sharma",))
rows = curr.fetchall()
if (len(rows) != 0):
    print("Player already exists")
    sys.exit(0)

# In[37]:


curr.execute('INSERT INTO Players (Player_Name) VALUES (?)',
             (playerName,))
player_Id = curr.lastrowid

print(player_Id)
conn.commit()
conn.close()

# In[38]:


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# In[39]:


url = "http://www.espncricinfo.com/india/content/player/34102.html"
html = urllib.request.urlopen(url, context=ctx).read()

# In[40]:


temp_data = OrderedDict()
list_of_dict = []
bs = BeautifulSoup(html, "lxml")
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

print(len(bat))

for row in rows:
    cols = row.find_all('td')
    cols = [x.text.strip() for x in cols]
    temp_data = OrderedDict()
    {el: 0 for el in bat}
    #     print(len(cols))
    #     print(cols)
    #     print(bat)
    for col in range(len(cols)):
        temp_data[bat[col]] = cols[col]

    list_of_dict.append(temp_data)

# In[41]:


batDf = pd.DataFrame(list_of_dict)
batDf
batDf.set_index('', inplace=True)
batDf

# In[ ]:


# In[42]:


temp_data = OrderedDict()
list_of_dict = []
bs = BeautifulSoup(html, "lxml")
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
    {el: 0 for el in bat}
    #     print(len(cols))
    #     print(cols)
    #     print(bat)
    for col in range(len(cols)):
        temp_data[bowl[col]] = cols[col]

    list_of_dict.append(temp_data)

# In[43]:


bowl_df = pd.DataFrame(list_of_dict)
bowl_df
bowl_df.set_index('', inplace=True)
bowl_df

# In[44]:


conn = sqlite3.connect('Hello.db')
c = conn.cursor()

# In[45]:


for index, row in batDf.iterrows():
    query = """INSERT INTO `{}`
                          ('Player_ID','Mat', 'Inns', 'NO', 'Runs', 'HS', 'Ave', 'BF', 'SR', '100', '50', '4s', '6s', 'Ct', 'St') 
                          VALUES (?, ?, ?, ?,?,?, ?, ?,?,?, ?, ?,?,?,?);""".format(index)
    values = list(row)
    values.insert(0, player_Id)
    print((values))
    c.execute(query, values)

conn.commit()
conn.close()

