# Adding Packages
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import requests

# Setting the website to Scrbu the data from
url = 'https://www.baseball-reference.com/teams/HOU/2019.shtml'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')


attrs = {'attribute1_name': 'attribute1_value', 'attribute2_name': 'attribute2_value'}
soup.find_all('tr', attrs = {'class': 'data-row'})
dt = soup.find('tbody')
header = soup.find('tr')
columns = [col.get_text() for col in header.find_all('th')]
final_df = pd.DataFrame(columns=columns)
final_df
players = soup.find_all('tr', attrs={'class':re.compile('data-row')})

players = soup.find_all('tr', attrs={'class':re.compile('data-row')})

url = 'https://www.baseball-reference.com/teams/HOU/2019.shtml'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

players = soup.find_all('tr')
print(players)
for player in players:
    
    stats = [stat.get_text() for stat in player.find_all('td')]
    
    temp_df = pd.DataFrame(stats).transpose()
    temp_df.columns = columns
    
    final_df = pd.concat([final_df,temp_df], ignore_index=True)


row = soup.find('tr')
player1 = []
for data in row.find_all('th'):
    player1.append(data.get_text())
    print(data.get_text())

player1 = []
dt = soup.find('tbody')
for data in dt.find_all('tr'):
    for data in row.find_all('td'):
        player1.append(data.get_text())
        print(data.get_text())


final_df.to_csv(r"mlb_stats.csv", index = False, sep= ',', encoding = 'utf-8')