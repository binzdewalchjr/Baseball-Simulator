# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 15:29:22 2021

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

players = soup.find_all('tr', attrs={'class':re.compile('row prlayer-10-')})
for player in players:
    
    stats = [stat.get_text() for stat in player.find_all('td')]
    
    temp_df = pd.DataFrame(stats).transpose()
    temp_df.columns = columns
    
    final_df = pd.concat([final_df,temp_df], ignore_index=True)
    
final_df