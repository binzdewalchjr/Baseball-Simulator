# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 19:32:23 2021

@author: binzd
"""
import pandas as pd

import csv
df = pd.read_csv(r'Astros Hitters.csv')
dfp = pd.read_csv(r'Astros Pitchers.csv')
print(df)

class Batter:
   def __repr__(self):
       return self.name
#   def __str__(self):
#       return "member of Test"
   def __init__(self, name, POS, HAND, PA, FB, SB, TB, HR, BB, HBP, H):
            self.name = name
            self.POS = POS
            self.HAND = HAND
            self.PA = PA
            self.FB = FB
            self.SB = SB
            self.TB = TB
            self.HR = HR
            self.BB = BB
            self.HBP = HBP
            self.H = H

Batters_list = []
for x in range(len(df)):
    if int(df.iloc[x][9]) != 0 and int(df.iloc[x][6]) != 0 and int(df.iloc[x][5]) != 0:
        player_name = df.iloc[x][2]
        first = (int(df.iloc[x][8]) - (int(df.iloc[x][9]) + int(df.iloc[x][10]) + int(df.iloc[x][11]))) / int(df.iloc[x][8])
        second = (int(df.iloc[x][9])) / int(df.iloc[x][8])
        third = (int(df.iloc[x][10])) / int(df.iloc[x][8])
        HomeRun = (int(df.iloc[x][11])) / int(df.iloc[x][8])
        Walk = (int(df.iloc[x][15])) / int(df.iloc[x][5])
        HitByPitcher = (int(df.iloc[x][24])) / int(df.iloc[x][5])
        Hit = (int(df.iloc[x][15])) / int(df.iloc[x][6])
        p1 = Batter(df.iloc[x][2], df.iloc[x][1], df.iloc[x][28], df.iloc[x][5], first, second, third, HomeRun, Walk, HitByPitcher, Hit)
        Batters_list.append(p1)
print(Batters_list)



class Pitcher:
   def __repr__(self):
       return self.name
   def __str__(self):
       return "member of Test"
   def __init__(self, name, POS, HAND, K, BB, HR, H, NP, TBF, GP, IP, AA, GO_AO):
            self.name = name
            self.POS = POS
            self.HAND = HAND
            self.K = K
            self.BB = BB
            self.HR = HR
            self.H = H
            self.NP = NP
            self.TBF = TBF
            self.GP = GP
            self.IP = IP
            self.AA = AA
            self.GO_AO = GO_AO

Pitchers_list = []
for x in range(len(dfp)):
    if int(dfp.iloc[x][9]) != 0:
        player_name = dfp.iloc[x][2]
        Strikeout = (int(dfp.iloc[x][8]) - (int(dfp.iloc[x][9]) + int(dfp.iloc[x][10]) + int(dfp.iloc[x][11]))) / int(dfp.iloc[x][9])
        PitchCount = (int(dfp.iloc[x][9])) / int(dfp.iloc[x][8])
        BattersFaced = (int(dfp.iloc[x][10])) / int(dfp.iloc[x][8])
        HomeRun = (int(dfp.iloc[x][11])) / int(dfp.iloc[x][8])
        Walk = (int(dfp.iloc[x][15])) / int(dfp.iloc[x][5])
        HitByPitcher = (int(dfp.iloc[x][24])) / int(dfp.iloc[x][5])
        Hit = (int(dfp.iloc[x][15])) / int(dfp.iloc[x][6])
        GamesPitched = dfp.iloc[x][8]
        InningsPitched = dfp.iloc[x][14]
        
        p1 = Batter(dfp.iloc[x][2], dfp.iloc[x][1], dfp.iloc[x][28], dfp.iloc[x][5], first, dfp.iloc[x][9], dfp.iloc[x][10], dfp.iloc[x][11], dfp.iloc[x][15], dfp.iloc[x][24], dfp.iloc[x][8])
        Batters_list.append(p1)
print(Batters_list)


