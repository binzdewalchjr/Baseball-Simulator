# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 19:32:23 2021

@author: binzd
"""
import pandas as pd

df = pd.read_csv(r'Astros Hitters.csv')
dfp = pd.read_csv(r'Astros Pitchers.csv')
print(df)

class Batter:
   def __repr__(self):
       return self.name
   def __str__(self):
       return self.name
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
    if float(df.iloc[x][9]) != 0 and float(df.iloc[x][6]) != 0 and float(df.iloc[x][5]) != 0:
        player_name = df.iloc[x][2]
        first = (float(df.iloc[x][8]) - (float(df.iloc[x][9]) + float(df.iloc[x][10]) + float(df.iloc[x][11]))) / float(df.iloc[x][8])
        second = (float(df.iloc[x][9])) / float(df.iloc[x][8])
        third = (float(df.iloc[x][10])) / float(df.iloc[x][8])
        HomeRun = (float(df.iloc[x][11])) / float(df.iloc[x][8])
        Walk = (float(df.iloc[x][15])) / float(df.iloc[x][5])
        HitByPitcher = (float(df.iloc[x][24])) / float(df.iloc[x][5])
        Hit = (float(df.iloc[x][15])) / float(df.iloc[x][6])
        p1 = Batter(df.iloc[x][2], df.iloc[x][1], df.iloc[x][28], df.iloc[x][5], first, second, third, HomeRun, Walk, HitByPitcher, Hit)
        Batters_list.append(p1)
print(Batters_list)



class Pitcher:
   def __repr__(self):
       return self.name
   def __str__(self):
       return self.name
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
    if float(dfp.iloc[x][9]) != 0:
        player_name = dfp.iloc[x][2]
        Strikeout = float(dfp.iloc[x][21]) / float(dfp.iloc[x][25])
        PitchCount = float(dfp.iloc[x][26])  # Pitch count has holder values in the current form of the exel file.  Correct values need to be used
        BattersFaced = float(dfp.iloc[x][35])
        HomeRun = (float(dfp.iloc[x][18])) / BattersFaced
        Walk = (float(dfp.iloc[x][17])) / BattersFaced
        HitByPitcher = (float(dfp.iloc[x][22])) / BattersFaced
        Hit = float(dfp.iloc[x][15])
        GamesPitched = dfp.iloc[x][8]
        InningsPitched = round(float(dfp.iloc[x][14])) + (float(dfp.iloc[x][14]) % 1)* 3
        AverageAgainst = float(dfp.iloc[x][15])/ BattersFaced
        GroundOverAir = dfp.iloc[x][36]
        
        p1 = Pitcher(dfp.iloc[x][2], dfp.iloc[x][1], dfp.iloc[x][35], Strikeout, Walk, HomeRun, Hit, PitchCount, BattersFaced, GamesPitched, InningsPitched, AverageAgainst, GroundOverAir)
        Pitchers_list.append(p1)
print(Pitchers_list)

print(Pitchers_list[0].HR)
