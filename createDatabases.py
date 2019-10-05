#!/usr/bin/env python
# coding: utf-8

# In[11]:


import sqlite3

# In[12]:


conn = sqlite3.connect('Hello.db')
c = conn.cursor()

# In[13]:


c.execute('''CREATE TABLE Tests
             ([generated_id] INTEGER PRIMARY KEY,[Player_ID] integer, [Mat] integer, [Inns] integer, [NO] integer, [Runs] integer,

             [HS] integer, [Ave] integer, [BF] integer, [SR] integer, [100] integer, [50] integer, [4s] integer,
             [6s] integer, [Ct] integer, [St] integer)''')

# In[14]:


c.execute('''CREATE TABLE ODIs
             ([generated_id] INTEGER PRIMARY KEY,[Player_ID] integer,[Mat] integer, [Inns] integer, [NO] integer, [Runs] integer,

             [HS] integer, [Ave] integer, [BF] integer, [SR] integer, [100] integer, [50] integer, [4s] integer,
             [6s] integer, [Ct] integer, [St] integer)''')

# In[15]:


c.execute('''CREATE TABLE T20Is
             ([generated_id] INTEGER PRIMARY KEY,[Player_ID] integer,[Mat] integer, [Inns] integer, [NO] integer, [Runs] integer,

             [HS] integer, [Ave] integer, [BF] integer, [SR] integer, [100] integer, [50] integer, [4s] integer,
             [6s] integer, [Ct] integer, [St] integer)''')

# In[16]:


c.execute('''CREATE TABLE 'First-class'
             ([generated_id] INTEGER PRIMARY KEY,[Player_ID] integer,[Mat] integer, [Inns] integer, [NO] integer, [Runs] integer,

             [HS] integer, [Ave] integer, [BF] integer, [SR] integer, [100] integer, [50] integer, [4s] integer,
             [6s] integer, [Ct] integer, [St] integer)''')

# In[17]:


c.execute('''CREATE TABLE 'List A'
             ([generated_id] INTEGER PRIMARY KEY,[Player_ID] integer,[Mat] integer, [Inns] integer, [NO] integer, [Runs] integer,

             [HS] integer, [Ave] integer, [BF] integer, [SR] integer, [100] integer, [50] integer, [4s] integer,
             [6s] integer, [Ct] integer, [St] integer)''')

# In[18]:


c.execute('''CREATE TABLE T20s
             ([generated_id] INTEGER PRIMARY KEY,[Player_ID] integer,[Mat] integer, [Inns] integer, [NO] integer, [Runs] integer,

             [HS] integer, [Ave] integer, [BF] integer, [SR] integer, [100] integer, [50] integer, [4s] integer,
             [6s] integer, [Ct] integer, [St] integer)''')

# In[19]:


c.execute('''CREATE TABLE Players
             ([player_id] INTEGER PRIMARY KEY,[Player_Name] text)''')

# In[20]:


conn.close()

# In[ ]:




