#!/usr/bin/env python
# coding: utf-8

# In[7]:


#Nama : Tia Fiendi Aryaningtiyas
#NIM : 1101204055


# In[8]:


import pandas as pd
import numpy as np


# In[9]:


path = "epl-goalScorer(20-21).csv"
df = pd.read_csv(path)


# In[10]:


df.head()


# In[11]:


df


# In[12]:


#10 player terbanyak pencetak gol
top_scorers = df.groupby('player_name').sum().sort_values('goals', ascending=False).head(10)


# In[13]:


print(top_scorers)


# In[15]:


#10 player terlama durasi bermain
longest_players = df.groupby('player_name').sum().sort_values('time', ascending=False).head(10)


# In[16]:


print(longest_players)


# In[17]:


#10 player terbanyak assist
top_assists = df.groupby('player_name').sum().sort_values('assists', ascending=False).head(10)


# In[18]:


print(top_assists)


# In[21]:


#4 player pencetak gol terbanyak dari kesebelasan manchester city
mancity_goals = df[df['team_title'] == 'Manchester City']


# In[22]:


top_4_players = mancity_goals.groupby('player_name').sum().sort_values('goals', ascending=False).head(4)


# In[23]:


print(top_4_players)


# In[25]:


#Pencetak gol terbanyak dari kesebelasan
kesebelasan = df.groupby('team_title')['goals'].nlargest(1).index[0]


# In[26]:


print(kesebelasan)


# In[28]:


#Jumlah kartu kuning dan merah yang diterima pembuat assist  terbanyak 
top_assists_player = df[df['assists']== df['assists'].max()]
yellow_card = top_assists_player.at[top_assists_player.index[0], 'yellow_cards']
red_card = top_assists_player.at[top_assists_player.index[0], 'red_cards']


# In[29]:


print(yellow_card)


# In[30]:


print(red_card)


# In[31]:


#Jumlah assist dan golnya paling banyak dari kesebelasan
top_assist_scorer = df.nlargest(1, ['assists', 'goals'])
kesebelasan_top_assist_scorer = top_assist_scorer['team_title'].iloc[0]


# In[32]:


print(top_assist_scorer)


# In[33]:


print(kesebelasan_top_assist_scorer)


# In[34]:


#5 kesebelasan yang menyumbangkan gol terbanyak
top_5_kesebelasan_gol = df.groupby('team_title')['goals'].sum().nlargest(5)


# In[35]:


print(top_5_kesebelasan_gol)


# In[36]:


#Urutkan pemain berdasarkan jumlah gol terbanyak tanpa mendapatkan kartu sama sekali 
tanpa_kartu = df[(df['yellow_cards'] == 0) & (df['red_cards'] == 0)]
urutan_tanpa_kartu = tanpa_kartu.sort_values(by='goals', ascending=False)


# In[37]:


print(urutan_tanpa_kartu)

