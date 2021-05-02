
# Adding Packages
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import requests

# Setting the website to Scrbu the data from
# Change the team city abbreviation to match the desired team
#change the year to change the year
url = 'https://www.baseball-reference.com/teams/BOS/2019.shtml'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')


attrs = {'attribute1_name': 'attribute1_value', 'attribute2_name': 'attribute2_value'}
soup.find_all('tr', attrs = {'class': 'data-row'})
header = soup.find('tr')
columns = [col.get_text() for col in header.find_all('th')]
columns.append('Hand')
final_df = pd.DataFrame(columns=columns)
final_df
players = soup.find_all('tr', attrs={'class':re.compile('data-row')})

players = soup.find_all('tr')
count = 0
flag = 'Batters'
flag1 = True
while flag1 == True:
    for player in players:
        if flag == 'Batters':
            stats = [stat.get_text() for stat in player.find_all('th')]
            stats = stats + ([stat.get_text() for stat in player.find_all('td')])
            if '*' in stats[2]:
                stats.append('L')
                stats[2] = stats[2].replace ('*', '')
            elif '#' in stats[2]:
                stats.append('L')
                stats[2] = stats[2].replace ('#', '')
            else:
                stats.append('R')
            if stats[0] != 'Rk' and stats[0].isdigit() == True:
                temp_df = pd.DataFrame(stats).transpose()
                temp_df.columns = columns
        
                final_df = pd.concat([final_df,temp_df], ignore_index=True)
            if stats[0].isdigit() == False and stats[0] != 'Rk':
                flag = 'Pitchers'
        if flag == 'Pitchers':
            count = count + 1
            stats = [stat.get_text() for stat in player.find_all('th')]
            stats = stats + ([stat.get_text() for stat in player.find_all('td')])
            if count > 4:
                if '*' in stats[2]:
                   stats.append('L')
                   stats[2] = stats[2].replace ('*', '')
                elif '#' in stats[2]:
                   stats.append('L')
                   stats[2] = stats[2].replace ('#', '')
                else:
                   stats.append('R')
                if stats[0] == 'Rk' and count == 6:
                    columnsp = [stat.get_text() for stat in player.find_all('th')]
                    columnsp = stats + ([stat.get_text() for stat in player.find_all('td')])
                    columnsp[34] = 'Hand'
                    final_dfp = pd.DataFrame(columns=columnsp)
                if stats[0].isdigit() == True and stats[0] != 'Rk':
                    stats[1] = 'P'
                    temp_df = pd.DataFrame(stats).transpose()
                    temp_df.columns = columnsp
                    final_dfp = pd.concat([final_dfp,temp_df], ignore_index=True)
                if stats[0].isdigit() == False and stats[0] != 'Rk':
                    flag1 = False



url2 = 'https://www.mlb.com/astros/stats/pitching/2019'
page = requests.get(url2)
soup = BeautifulSoup(page.text, 'html.parser')

header = ['Name', 'NP', 'GO/AO']
final_dfp2 = pd.DataFrame(columns=header)
final_dfp2
flag = True
players = soup.find_all('tr')
count = 0 
index_add = 0
for player in players:
    count = count + 1
    if count > 1:
        if count >11:
            index_add = 1
        stats = [stat.get_text() for stat in player.find_all('th')]
        string1 = stats[0]
        index1 = string1.find(' ')
        index2 = len(string1)
        length = int(((index2 - 3 - index_add) - index1)/2)
        string2 = string1[1 + index_add:index1-1]
        string3 = string1[index1+1:(index1 + length)]
        finalstring = string2 + " " + string3
        stats[0] = finalstring
        stats = stats + ([stat.get_text() for stat in player.find_all('td', attrs = {'class':re.compile('number-aY5arzrB align-right-3nN_D3xs is-table-pinned-1WfPW2jT')})])
        stats = stats + ([stat.get_text() for stat in player.find_all('td', attrs = {'class':re.compile('col-group-end-2UJpJVwW number-aY5arzrB align-right-3nN_D3xs is-table-pinned-1WfPW2jT')})])
        stats = stats[0:3]
        temp_df = pd.DataFrame(stats).transpose()
        temp_df.columns = header
        
        final_dfp2 = pd.concat([final_dfp2,temp_df], ignore_index=True)

    players = soup.find_all('tr', attrs={'class':re.compile('row player-10-')})
    
sorted_dfp = final_dfp.sort_values(by=['Name'])    
sorted_dfp2 = final_dfp2.sort_values(by=['Name']) 
dfp2tail = sorted_dfp2[["NP","GO/AO"]]

finaldfp = pd.concat([sorted_dfp, dfp2tail], axis = 1)
finaldfp = finaldfp.sort_index()

# Change the name of the team to match the team name in the .csv file
final_df.to_csv(r"Red_Sox_Hitters.csv", index = False, sep= ',', encoding = 'utf-8')
finaldfp.to_csv(r"Red_Sox_Pitchers.csv", index = False, sep= ',', encoding = 'utf-8')


