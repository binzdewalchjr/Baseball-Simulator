# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 14:34:50 2021

@author: binzd
"""

# Adding Packages
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import requests

url = 'https://www.espn.com/mlb/history/leaders/_/breakdown/season/year/2018/start/1'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

attrs = {'attribute1_name': 'attribute1_value', 'attribute2_name': 'attribute2_value'}
header = soup.find('tr', attrs={'class':'colhead'})
row = soup.find('tr', attrs = {'class': 'oddrow player-10-33039'})
columns = [col.get_text() for col in header.find_all('td')]
final_df = pd.DataFrame(columns=columns)
final_df
players = soup.find_all('tr', attrs={'class':re.compile('row prlayer-10-')})

players = soup.find_all('tr', attrs={'class':re.compile('row prlayer-10-')})
for i in range(1,331,50):

    url = 'https://www.espn.com/mlb/history/leaders/_/breakdown/season/year/2018/start/1'.format(i)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    players = soup.find_all('tr', attrs={'class':re.compile('row player-10-')})
    for player in players:
        
        stats = [stat.get_text() for stat in player.find_all('td')]
        
        temp_df = pd.DataFrame(stats).transpose()
        temp_df.columns = columns
        
        final_df = pd.concat([final_df,temp_df], ignore_index=True)

player1 = []
for data in row.find_all('td'):
    player1.append(data.get_text())
    print(data.get_text())
    
final_df.to_csv(r"mlb_stats.csv", index = False, sep= ',', encoding = 'utf-8')

