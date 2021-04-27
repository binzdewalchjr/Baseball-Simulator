#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 13:56:33 2021

@author: javi
"""
import pandas as pd
##File 1
##Scrape data file from the web 

##Types of stats (Hitters)
    ## Plate Apearances, Singles, Doubles, Triples, HR
    ## Walks, Hit By Pitch 
##Types of stats (Pitchers)
    ## Strikeouts, walks, total pitches, batters faced,
    ## GroundOut/AirOut, Games, Innings Pitched, average against, hits
    ## HR
##Format stats to standard format

##Merge relevant stats together

##Save to a CSV file 

##File 2

##Import CSV data and format for being called in game simulaton (format with strings each
    ## team will have own CSV file)
    ## Argument for wheher pulling from entire MLB with the first column of the MLB file
    ## indicating which team a player plays for
SetAwayTeam = False
SetHomeTeam = False
PossibleTeams = ["Astros", "Yankees"]
while SetAwayTeam == False:
    AwayTeam = 'Astros' #input("Enter the name of the Away Team. For a list of possible teams type 'ls', to exit type 'q' \n")
    if AwayTeam == "ls":
        print()
        AwayTeam = input("Choose from one of the listed teams \n")
    elif AwayTeam == "q":
        exit()
    elif AwayTeam in PossibleTeams:
        SetAwayTeam = True
while SetHomeTeam == False:
    HomeTeam = 'Yankees' #input("Enter the name of the Home Team. For a list of possible teams type 'ls', to exit type 'q' \n")
    if HomeTeam == "ls":
        print()
        HomeTeam = input("Choose from one of the listed teams \n")
    elif HomeTeam == "q":
        exit()
    elif HomeTeam in PossibleTeams:
        SetHomeTeam = True
##insert pandas reading in data frame
df = pd.read_csv(r'{0}_Hitters.csv'.format(AwayTeam))
dfp = pd.read_csv(r'{0}_Pitchers.csv'.format(AwayTeam))

df1 = pd.read_csv(r'{0}_Hitters.csv'.format(HomeTeam))
dfp1 = pd.read_csv(r'{0}_Pitchers.csv'.format(HomeTeam))

PlayerDictionary = dict()
PlayerDictionary["Hitting0"] = df
PlayerDictionary["Hitting1"] = df1
PlayerDictionary["Pitching0"] = dfp
PlayerDictionary["Pitching1"] = dfp1
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
Batters_list1 = []
for i in range(0,2):
    PlayersToPass = PlayerDictionary["Hitting{0}".format(i)]
    if i == 0:
        dataframe = df
    else:
        dataframe = df1
    for x in range(len(PlayersToPass)):
        if float(dataframe.iloc[x][8]) != 0 and float(dataframe.iloc[x][6]) != 0 and float(dataframe.iloc[x][5]) != 0:
            player_name = dataframe.iloc[x][2]
            first = (float(dataframe.iloc[x][8]) - (float(dataframe.iloc[x][9]) + float(dataframe.iloc[x][10]) + float(dataframe.iloc[x][11]))) / float(dataframe.iloc[x][8])
            second = (float(dataframe.iloc[x][9])) / float(dataframe.iloc[x][8])
            third = (float(dataframe.iloc[x][10])) / float(dataframe.iloc[x][8])
            HomeRun = (float(dataframe.iloc[x][11])) / float(dataframe.iloc[x][8])
            Walk = (float(dataframe.iloc[x][15])) / float(dataframe.iloc[x][5])
            HitByPitcher = (float(dataframe.iloc[x][24])) / float(dataframe.iloc[x][5])
            Hit = (float(dataframe.iloc[x][8])) / float(dataframe.iloc[x][5])
            p1 = Batter(dataframe.iloc[x][2], dataframe.iloc[x][1], dataframe.iloc[x][28], dataframe.iloc[x][5], first, second, third, HomeRun, Walk, HitByPitcher, Hit)
            if i == 0:
                Batters_list.append(p1)
            if i == 1:
                Batters_list1.append(p1)

#print(Batters_list[0].name)
#print(Batters_list[0].FB)


class Pitcher:
   def __repr__(self):
       return self.name
   def __str__(self):
       return self.name
   def __init__(self, name, POS, HAND, K, BB, HR, H, NP, TBF, GP, IP, AA, GO_AO):
            self.name = name
            self.POS = POS # all listed as pitchers
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
Pitchers_list1 = []
for i in range(0,2):
    PlayersToPass = PlayerDictionary["Pitching{0}".format(i)]
    if i == 0:
        dataframep = dfp
    else:
        dataframep = dfp1
    for x in range(len(PlayersToPass)):
        if int(dataframep.iloc[x][15]) != 0:
            player_name = dataframep.iloc[x][2]
            Strikeout = float(dataframep.iloc[x][21]) / float(dataframep.iloc[x][25])
            PitchCount = float(dataframep.iloc[x][25])/ float(dataframep.iloc[x][8])  # Pitch count has holder values in the current form of the exel file.  Correct values need to be used
            BattersFaced = float(dataframep.iloc[x][25])
            HomeRun = (float(dataframep.iloc[x][18])) / float(dataframep.iloc[x][15])
            Walk = (float(dataframep.iloc[x][17])) / BattersFaced
            HitByPitcher = (float(dataframep.iloc[x][22])) / BattersFaced
            Hit = float(dataframep.iloc[x][15])
            GamesPitched = dataframep.iloc[x][8]
            InningsPitched = round(float(dataframep.iloc[x][14])) + (float(dataframep.iloc[x][14]) % 1)* 3
            AverageAgainst = float(dataframep.iloc[x][15])/ BattersFaced
            GroundOverAir = dataframep.iloc[x][36]
            p1 = Pitcher(dataframep.iloc[x][2], dataframep.iloc[x][1], dataframep.iloc[x][35], Strikeout, Walk, HomeRun, Hit, PitchCount, BattersFaced, GamesPitched, InningsPitched, AverageAgainst, GroundOverAir)
            if i == 0:
                Pitchers_list.append(p1)
            if i == 1:
                Pitchers_list1.append(p1)
   
    
#############################################################################
# #This Part Sets the lineup and starting pitchers for the away team
list_of_batters = []
for x in range(len(Batters_list)):
    list_of_batters.append(Batters_list[x].name)
    
dictionary_of_batters = {}
for x in range(len(Batters_list)):
    BatterName = list_of_batters[x]
    dictionary_of_batters[BatterName] = Batters_list[x]

    
# #Prompting the user to input baters and position
# #Checks to see if it is a batter in the batters list
# #adds that batter to a dictionary
# #batters and pitchers clases stored in AwayLineup
# AwayLineup = []
# for x in range(0,9):
#     flag = True
#     while flag == True:
#         lineupnumber = str(x+1)
#         Player = input("Enter A player for spot " + lineupnumber + " in the lineup: ")
#         if Player in list_of_batters:
#             addtolineup = dictionary_of_batters[Player]
#             flag = False
#         else:
#             print("Please enter a valid player's name: ")
#     AwayLineup.append(addtolineup) #


list_of_pitchers = []
for x in range(len(Pitchers_list)):
    list_of_pitchers.append(Pitchers_list[x].name)
    
dictionary_of_pitchers = {}
for x in range(len(Pitchers_list)):
    PitcherName = list_of_pitchers[x]
    dictionary_of_pitchers[PitcherName] = Pitchers_list[x]

# AwayBullpen = []
# flag = True
# while flag == True:
#      Player = input("Enter starting pitcher:")
#      if Player in list_of_pitchers:
#          addtolineup = dictionary_of_pitchers[Player]
#          flag = False
#      else:
#         print("Please enter a valid player's name: ")
# AwayBullpen.append(addtolineup)

# for x in range(0,8):
#     flag = True
#     while flag == True:
#         lineupnumber = str(x + 1)
#         Player = input("Enter A player for spot " + lineupnumber + " in the Relief Pitcher lineup: ")
#         if Player in list_of_pitchers:
#             addtolineup = dictionary_of_pitchers[Player]
#             flag = False
#         else:
#             print("Please enter a valid pitchers name: ")
#     AwayBullpen.append(addtolineup)



# print("Now Setting the Lineup for the " + HomeTeam)



#This Part Sets the lineup and starting pitchers for the home team
list_of_batters1 = []
for x in range(len(Batters_list1)):
    list_of_batters1.append(Batters_list1[x].name)
    
dictionary_of_batters1 = {}
for x in range(len(Batters_list1)):
    BatterName = list_of_batters1[x]
    dictionary_of_batters1[BatterName] = Batters_list1[x]

    
# #Prompting the user to input baters and position
# #Checks to see if it is a batter in the batters list thus being valid
# #adds that batter to a dictionary
# HomeLineup = []
# for x in range(0,9):
#     flag = True
#     while flag == True:
#         lineupnumber = str(x+1)
#         Player = input("Enter A player for spot " + lineupnumber + " in the lineup: ")
#         if Player in list_of_batters:
#             addtolineup = dictionary_of_batters1[Player]
#             flag = False
#         else:
#             print("Please enter a valid player's name: ")
#     HomeLineup.append(addtolineup) #


list_of_pitchers1 = []
for x in range(len(Pitchers_list1)):
    list_of_pitchers1.append(Pitchers_list1[x].name)
    
dictionary_of_pitchers1 = {}
for x in range(len(Pitchers_list1)):
    PitcherName = list_of_pitchers1[x]
    dictionary_of_pitchers1[PitcherName] = Pitchers_list1[x]
    

# #Prompting the user to input the Starting and Relief Pitchers for the 

# HomeBullpen = []
# flag = True
# while flag == True:
#      Player = input("Enter starting pitcher:")
#      if Player in list_of_pitchers1:
#          addtolineup = dictionary_of_pitchers1[Player]
#          flag = False
#      else:
#         print("Please enter a valid player's name: ")
# HomeBullpen.append(addtolineup)

# for x in range(0,8):
#     flag = True
#     while flag == True:
#         lineupnumber = str(x + 1)
#         Player = input("Enter A player for spot " + lineupnumber + " in the Relief Pitcher lineup: ")
#         if Player in list_of_pitchers:
#             addtolineup = dictionary_of_pitchers1[Player]
#             flag = False
#         else:
#             print("Please enter a valid pitchers name: ")
#     HomeBullpen.append(addtolineup)


#############


HomeLineup = []
for x in range (0,9):
    HomeLineup.append(Batters_list1[x])
HomeLineup.append(Pitchers_list1[0])


HomeBullpen = []
for x in range (0,8):
    HomeBullpen.append(Pitchers_list1[x])

AwayLineup = []
for x in range (0,9):
    AwayLineup.append(Batters_list[x])
AwayLineup.append(Pitchers_list[0])

AwayBullpen = []
for x in range (0,8):
    AwayBullpen.append(Pitchers_list[x])










###Set Up Game Mode
GameMode = 'Inning' #input("Enter game mode from the following options: 100Game, Inning, AtBat: ")
GameModeFlag = False
if GameMode == '100Game' or GameMode == 'Inning' or GameMode == 'AtBat':
    GameModeFlag = True
while GameModeFlag == False:
    print("Please enter a valid game mode. Appropriate options are: 100Game\nInning\nAtBat\nType 'q' to quit")
    GameMode = input()
    if GameMode == '100Game' or GameMode == 'Inning' or GameMode == 'AtBat':
        GameModeFlag = True
    if GameMode == "q":
        exit()
##Pool of available pitchers(dicitonary)

##Pool of available bench players (dictionary)

##Simulation style argument (100 game, per inning , per batter)

##Set line-ups and starting pitchers

##Set bull-pen conditions (optional)

##Having set innings per pitcher (optional)

##Argument for designated hitter
##Main game code
import random
import numpy as np
    ##Actions per at bat
def AtBat(Pitcher,Batter,Bases,Outs,Runners, Score):
    EventPercent = random.random()
    
    # HRPitcher = Pitcher.InningsSinceHR * Pitcher.HRper9 #Adjust formula
    H = Batter.H * (Pitcher.AA)/ 0.248 #Adjust formula
    BB = Batter.BB * Pitcher.BB / 0.090 #Adjust formula
    HBP = Batter.HBP
    K = Pitcher.K #Adjust formula  (Batter.K/Batter.PA) * (Pitcher.K/Pitcher.TBF) / 0.222
    FB = H * (Batter.FB)
    SB = H * (Batter.SB)
    TB = H * (Batter.TB)
    HR = H * (Batter.HR)
    RemainingPercentage = 1-FB-SB-TB-HR-BB-HBP-K
    GO = RemainingPercentage * Pitcher.GO_AO/(1+Pitcher.GO_AO)
    ##Add create wieghted average for each action
    ## Renormalize based on the new total
    ## Add condition for error propagation to rerun the random generator if it
        ##generates a value higher than 1-error
    Runs = 0
    #FlyOut = RemainingPercentage - GroundOut
    if EventPercent < K:
        Result = "K"
    elif EventPercent < K + BB:
        Result = "BB"
    elif EventPercent < K + BB + FB:
        Result = "1B"
    elif EventPercent < K + BB + FB + SB:
        Result = "2B"
    elif EventPercent < K + BB + FB + SB + TB:
        Result = "3B"
    elif EventPercent < K + BB + FB + SB + TB + HR:
        Result = "HR"
    elif EventPercent < K + BB + FB + SB + TB + HR + HBP:
        Result = "HBP"
    elif EventPercent < K + BB + FB + SB + TB + HR + HBP + GO:
        Result = "GO"
    else:
        PopOut_FlyOut = random.random()
        FlyOut = 0.760 #insert fly out stat
        if PopOut_FlyOut < FlyOut:
            Result = "FO"
        else:
            Result = "PO"
            
            
    if Bases == "000":
        if Result == "1B":
            Bases = "001"
            Runners.append(Batter)
        elif Result == "2B":
            Bases = "010"
            Runners.append(Batter)
        elif Result == "3B":
            Bases = "100"
            Runners.append(Batter)
        elif Result == "HR":
            Bases = "000"
            Runs = 1
        elif Result == "BB" or Result == "HBP":
            Bases = "001"
            Runners.append(Batter)
        elif Result == "K" or Result == "FO" or Result == "PO" or Result == "GO":
            Bases == "000"
            Outs += 1
    
    
    elif Bases == "001":
        OddsFirstToThird = 0.276 #insert odds
        if Result == "1B":
            Runners.append(Batter)
            FirstToThird = random.random()
            if Runners[0].POS == "1B" or Runners[0].POS == "C" or Runners[0].POS == "P":
                OddsFirstToThird = 0.85 * OddsFirstToThird #insert odds function
                if Outs == 2:
                    OddsFirstToThird += 0.15
            elif Runners[0].POS == "2B" or Runners[0].POS == "3B" or Runners[0].POS == "DH":
                OddsFirstToThird = OddsFirstToThird
                if Outs == 2:
                    OddsFirstToThird += 0.15
            elif Runners[0].POS == "RF" or Runners[0].POS == "LF":
                OddsFirstToThird = 1.07 * OddsFirstToThird #insert odds function
                if Outs == 2:
                    OddsFirstToThird += 0.15
            elif Runners[0].POS == "SS" or Runners[0].POS == "CF":
                OddsFirstToThird == 1.15 * OddsFirstToThird #insert odds function
                if Outs == 2:
                    OddsFirstToThird += 0.15
            if FirstToThird < OddsFirstToThird:
                Bases = "101"
            else:
                Bases = "011"
        OddsFirstToScore = 0.471  #insert odds
        if Result == "2B":
            Runners.append(Batter)
            FirstToScore = random.random()
            if Runners[0].POS == "1B" or Runners[0].POS == "C" or Runners[0].POS == "P":
                OddsFirstToScore = 0.60 * OddsFirstToScore #insert odds function
                if Outs == 2:
                    OddsFirstToScore += 0.10
            elif Runners[0].POS == "2B" or Runners[0].POS == "3B" or Runners[0].POS == "DH":
                OddsFirstToScore = OddsFirstToScore
                if Outs == 2:
                    OddsFirstToScore += 0.10
            elif Runners[0].POS == "RF" or Runners[0].POS == "LF":
                OddsFirstToScore = 1.15 * OddsFirstToThird #insert odds function
                if Outs == 2:
                    OddsFirstToScore += 0.15
            elif Runners[0].POS == "SS" or Runners[0].POS == "CF":
                OddsFirstToThird == 1.25 * OddsFirstToThird #insert odds function
                if Outs == 2:
                    OddsFirstToScore += 0.15
            if FirstToScore < OddsFirstToScore:
                Bases = "010"
                Runs = 1
                del Runners[0]
            else:
                Bases = "110"
        elif Result == "3B":
            Runners.append(Batter)
            Bases = "100"
            Runs = 1
            del Runners[0]
        elif Result == "HR":
            Bases = "000"
            Runs = 2
            Runners = []
        elif Result == "BB" or Result == "HBP":
            Bases = "011"
        elif Result == "K" or Result == "FO" or Result == "PO":
            Bases = "001"
            Outs += 1
        elif Result == "GO":
            OddsOutAtSecond = 0.7 # insert odds ###estimate
            OutAtSecond = random.random()
            if Runners[0].POS == "1B" or Runners[0].POS == "C" or Runners[0].POS == "P":
                OddsOutAtSecond *= 1.15
            elif Runners[0].POS == "SS" or Runners[0].POS == "CF":
                OddsOutAtSecond *= 0.85
            if OutAtSecond < OddsOutAtSecond:
                Outs += 1
                Bases = "001"
                Runners.append(Batter)
                del Runners[0]
                if Outs <= 2:
                    OddsDoublePlay = 0.25 #insert odds ###estimate
                    DoublePlay = random.random()
                    if Batter.POS == "1B" or Batter.POS == "C" or Batter.POS =="P":
                        OddsDoublePlay *= 1.25
                    elif Batter.POS == "SS" or Batter.POS == "CF":
                        OddsDoublePlay *= 0.85
                    if DoublePlay < OddsDoublePlay:
                        Outs += 1
                        Bases = "000"
                        Runners = []
            else:
                Bases = "010"
                Outs += 1
                    
                
    elif Bases == "010":
        OddsToScore = 0.588 #insert odds
        SecondToScore = random.random()
        if Result == "1B":
            Runners.append(Batter)
            if Runners[0].POS == "1B" or Runners[0].POS == "C" or Runners[0].POS == "P":
                OddsToScore -= 0.15
            if SecondToScore < OddsToScore:
                Bases = "001"
                Runs = 1
                del Runners[0]
            elif SecondToScore < (OddsToScore + 0.03):
                Bases = "001" 
                Outs += 1
                del Runners[0]
            else:
                Bases = "101"
        elif Result == "2B":
            Runners.append(Batter)
            Bases = "010"
            Runs = 1
            del Runners[0]
        elif Result == "3B":
            Runners.append(Batter)
            Bases = "100"
            Runs = 1
            del Runners[0]
        elif Result == "HR":
            Bases = "000"
            Runs = 2
            Runners = []
        elif Result == "BB" or Result == "HBP":
            Bases = "011"
            Runners.append(Batter)
        elif Result == "K" or Result == "FO" or Result == "PO":
            Bases = "010" #Assuming no silly baserunning or tagging up on a flyout
            Outs += 1
        elif Result == "GO":
            #Maybe insert condition based on handedness to determine advancing lead runner
            Bases = "010"
            Outs += 1
            
            
    elif Bases == "100":
        if Result == "1B":
            Bases = "001"
            Runs = 1
            Runners.append(Batter)
            del Runners[0]
        elif Result == "2B":
            Bases = "010"
            Runs = 1
            Runners.append(Batter)
            del Runners[0]
        elif Result == "3B":
            Bases = "100"
            Runs = 1
            Runners.append(Batter)
            del Runners[0]
        elif Result == "HR":
            Bases = "000"
            Runs = 2
            Runners = []
        elif Result == "BB" or Result == "HBP":
            Bases = "101"
            Runners.append(Batter)
        elif Result == "K" or Result == "PO":
            Bases = "100"
            Outs += 1
        elif Result == "FO":
            if Outs < 2:
                OddsTagThird = 0.804 #insert odds
                TagThird = random.random()
                if Runners[0].POS == "1B" or Runners[0].POS == "C" or Runners[0].POS == "P":
                    OddsTagThird *= 0.75
                elif Runners[0].POS == "SS" or Runners[0].POS == "CF":
                    OddsTagThird *= 1.25
                if TagThird < OddsTagThird:
                    Runs = 1
                    Outs += 1
                    Bases = "000"
                elif TagThird < (OddsTagThird + 0.0309):
                    Outs += 2
                    Bases = "000"
                else:
                    Bases = "100"
                    Outs += 1
            else:
                Outs += 1
        elif Result == "GO":
            Outs += 1
            OddsScoreThird = 0.555
            ScoreThird = random.random()
            if ScoreThird < OddsScoreThird:
                Runs += 1
                Bases = "000"
            else:
                Bases = "100"
        
            
    elif Bases == "011":
        if Result == "1B":
            Runners.append(Batter)
            OddsToScore = 0.588 #insert odds
            SecondToScore = random.random()
            if Runners[0].POS == "1B" or Runners[0].POS == "C" or Runners[0].POS == "P":
                OddsToScore -= 0.15
            if SecondToScore < OddsToScore:
                Runs = 1
                del Runners[0]
                FirstToThird = random.random()
                OddsFirstToThird = 0.276
                if Runners[0].POS == "1B" or Runners[0].POS == "C" or Runners[0].POS == "P":
                    OddsFirstToThird = 0.85 * OddsFirstToThird #insert odds function
                    if Outs == 2:
                        OddsFirstToThird += 0.15
                elif Runners[0].POS == "2B" or Runners[0].POS == "3B" or Runners[0].POS == "DH":
                    OddsFirstToThird = OddsFirstToThird
                    if Outs == 2:
                        OddsFirstToThird += 0.15
                elif Runners[0].POS == "RF" or Runners[0].POS == "LF":
                    OddsFirstToThird = 1.07 * OddsFirstToThird #insert odds function
                    if Outs == 2:
                        OddsFirstToThird += 0.15
                elif Runners[0].POS == "SS" or Runners[0].POS == "CF":
                    OddsFirstToThird == 1.15 * OddsFirstToThird #insert odds function
                    if Outs == 2:
                        OddsFirstToThird += 0.15
                if FirstToThird < OddsFirstToThird:
                    Bases = "101"
                else:
                    Bases = "011"
            elif SecondToScore < (OddsToScore + 0.03):
                Outs += 1
                del Runners[0]
                Bases = "001"
            else:
                Bases = "111"
        elif Result == "2B":
            Runners.append(Batter)
            Runs = 1
            del Runners[0]
            ScoreFromFirst = random.random()
            OddsScoreFromFirst = 0.47 #insert odds
            if Runners[0].POS == "1B" or Runners[0].POS == "C" or Runners[0].POS == "P":
                    OddsScoreFromFirst = 0.6 * OddsScoreFromFirst #insert odds function
                    if Outs == 2:
                        OddsScoreFromFirst += 0.10
            elif Runners[0].POS == "2B" or Runners[0].POS == "3B" or Runners[0].POS == "DH":
                OddsScoreFromFirst = OddsScoreFromFirst
                if Outs == 2:
                    OddsScoreFromFirst += 0.10
            elif Runners[0].POS == "RF" or Runners[0].POS == "LF":
                OddsScoreFromFirst = 1.15 * OddsScoreFromFirst #insert odds function
                if Outs == 2:
                    OddsScoreFromFirst += 0.15
            elif Runners[0].POS == "SS" or Runners[0].POS == "CF":
                OddsScoreFromFirst == 1.25 * OddsScoreFromFirst #insert odds function
                if Outs == 2:
                    OddsScoreFromFirst += 0.15
            if ScoreFromFirst < OddsScoreFromFirst:
                Runs += 1
                del Runners[0]
                Bases = "010"
            else:
                Bases = "110"
        elif Result == "3B":
            Runners.append(Batter)
            del Runners[0]
            del Runners[0]
            Runs = 2
            Bases = "100"  
        elif Result == "HR":
            Runs = 3
            Bases = "000"
            Runners = []
        elif Result == "BB" or Result == "HBP":
            Bases = "111"
            Runners.append(Batter)
        elif Result == "K" or Result == "PO" or Result == "FO":
            Outs += 1
            Bases = "011"
        elif Result == "GO": #could add conditional for getting lead runner at third (would be result of
                            # which side of the infield the ball is hit to, as a function of handedness
                            # or more specifically batter data
            OddsOutAtSecond = 0.7 # insert odds ##estimate
            OutAtSecond = random.random()
            if Batter.POS == "1B" or Batter.POS == "C" or Batter.POS == "P":
                OddsOutAtSecond *= 1.15
            elif Batter.POS == "SS" or Batter.POS == "CF":
                OddsOutAtSecond *= 0.85
            if OutAtSecond < OddsOutAtSecond:
                Runners.append(Batter)
                Outs += 1
                Bases = "101"
                del Runners[0]
                if Outs <= 2:
                    OddsDoublePlay = 0.25 #insert odds ##estimate
                    DoublePlay = random.random()
                    if Batter.POS == "1B" or Batter.POS == "C" or Batter.POS =="P":
                        OddsDoublePlay *= 1.25
                    elif Batter.POS == "SS" or Batter.POS == "CF":
                        OddsDoublePlay *= 0.85
                    if DoublePlay < OddsDoublePlay:
                        Outs += 1
                        Bases = "100"
                        Runners = []
            else:
                Bases = "110"
                Outs += 1
                                
    elif Bases == "110":
        if Result == "1B":
            Runners.append(Batter)
            Runs = 1
            del Runners[0]
            OddsToScore = 0.588 #insert odds
            SecondToScore = random.random()
            if Runners[0].POS == "1B" or Runners[0].POS == "C" or Runners[0].POS == "P":
                OddsToScore -= 0.15
            if SecondToScore < OddsToScore:
                Bases = "001"
                Runs += 1
                del Runners[0]
            elif SecondToScore < (OddsToScore + 0.03):
                Outs += 1
                del Runners[0]
                Bases = "001"
            else:
                Bases = "101" 
        elif Result == "2B":
            Runners.append(Batter)
            Runs = 2
            del Runners[0]
            del Runners[0]
            Bases = "010"
        elif Result == "3B":
            Runners.append(Batter)
            Runs = 2
            del Runners[0]
            del Runners[0]
            Bases = "100"
        elif Result == "HR":
            Runs = 3
            Runners = []
        elif Result == "BB"or  Result == "HBP":
            Runners.append(Batter)
            Bases = "111"
        elif Result == "K" or Result == "PO":
            Outs += 1
            Bases = "110"
        elif Result == "FO":
            if Outs < 2:
                OddsTagThird = 0.804 #insert odds
                TagThird = random.random()
                if Runners[0].POS == "1B" or Runners[0].POS == "C" or Runners[0].POS == "P":
                    OddsTagThird *= 0.75
                elif Runners[0].POS == "SS" or Runners[0].POS == "CF":
                    OddsTagThird *= 1.25
                if TagThird < OddsTagThird:
                    Runs = 1
                    Outs += 1
                    Bases = "010"
                elif TagThird < (OddsTagThird + 0.0309):
                    Outs += 2
                    Bases = "010"
                else:
                    Bases = "110"
                    Outs += 1
            else:
                Outs += 1
        elif Result == "GO":
            if Outs < 2:
                OddsScoreGO = 0.555 #insert odds
                ScoreGO = random.random()
                if ScoreGO < OddsScoreGO:
                    Runs = 1
                    del Runners[0]
                    OddsAdvanceThird = 0.5 #adjust later based on handedness
                    AdvanceThird = random.random()
                    if AdvanceThird < OddsAdvanceThird:
                        Bases = "100"
                        Outs += 1
                    else:
                        Bases = "010"
                        Outs += 1
                else:
                    Bases = "110"
                    Outs += 1
            else: 
                Outs += 1
        
    elif Bases == "101":
        if Result == "1B":
            Runners.append(Batter)
            Runs = 1
            del Runners[0]
            OddsFirstToThird = 0.276 #insert odds
            FirstToThird = random.random()
            if Runners[0].POS == "1B" or Runners[0].POS == "C" or Runners[0].POS == "P":
                OddsFirstToThird = 0 * OddsFirstToThird #insert odds function
                if Outs == 2:
                    OddsFirstToThird += 0.25
            elif Runners[0].POS == "2B" or Runners[0].POS == "3B" or Runners[0].POS == "DH":
                OddsFirstToThird = OddsFirstToThird
                if Outs == 2:
                    OddsFirstToThird += 0.20
            elif Runners[0].POS == "RF" or Runners[0].POS == "LF":
                OddsFirstToThird = 0 * OddsFirstToThird #insert odds function
                if Outs == 2:
                    OddsFirstToThird += 0.15
            elif Runners[0].POS == "SS" or Runners[0].POS == "CF":
                OddsFirstToThird == 0 * OddsFirstToThird #insert odds function
                if Outs == 2:
                    OddsFirstToThird += 0.15
            if FirstToThird < OddsFirstToThird:
                Bases = "101"
            else:
                Bases = "011"
        elif Result == "2B":
            Runners.append(Batter)
            Runs = 1
            del Runners[0]
            ScoreFromFirst = random.random()
            OddsScoreFromFirst = 0.471 #insert odds
            if Runners[0].POS == "1B" or Runners[0].POS == "C" or Runners[0].POS == "P":
                    OddsScoreFromFirst = 0.60 * OddsScoreFromFirst #insert odds function
                    if Outs == 2:
                        OddsScoreFromFirst += 0.10
            elif Runners[0].POS == "2B" or Runners[0].POS == "3B" or Runners[0].POS == "DH":
                OddsScoreFromFirst = OddsScoreFromFirst
                if Outs == 2:
                    OddsScoreFromFirst += 0.10
            elif Runners[0].POS == "RF" or Runners[0].POS == "LF":
                OddsScoreFromFirst = 1.15 * OddsScoreFromFirst #insert odds function
                if Outs == 2:
                    OddsScoreFromFirst += 0.15
            elif Runners[0].POS == "SS" or Runners[0].POS == "CF":
                OddsScoreFromFirst == 1.25 * OddsScoreFromFirst #insert odds function
                if Outs == 2:
                    OddsScoreFromFirst += 0.15
            if ScoreFromFirst < OddsScoreFromFirst:
                Runs += 1
                del Runners[0]
                Bases = "010"
            else:
                Bases = "110"
        elif Result == "3B":
            Runners.append(Batter)
            Runs = 2
            del Runners[0]
            del Runners[0]
            Bases = "100"
        elif Result == "HR":
            Runs = 3
            Runners = []
        elif Result == "BB" or Result == "HBP":
            Runners.append(Batter)
            Bases = "111"
        elif Result == "K" or Result == "PO":
            Outs += 1
            Bases = "101"
        elif Result == "FO":
            if Outs < 2:
                OddsTagThird = 0.804 #insert odds
                TagThird = random.random()
                if Runners[0].POS == "1B" or Runners[0].POS == "C" or Runners[0].POS == "P":
                    OddsTagThird *= 0.75
                elif Runners[0].POS == "SS" or Runners[0].POS == "CF":
                    OddsTagThird *= 1.25
                if TagThird < OddsTagThird:
                    Runs = 1
                    Outs += 1
                    Bases = "001"
                elif TagThird < (OddsTagThird + 0.0309):
                    Outs += 2
                    Bases = "001"
                else:
                    Bases = "101"
                    Outs += 1
            else:
                Outs += 1
        elif Result == "GO":
            if Outs == 0 : #default to check runner at third and get one out at first or second
                            #can adjust later to make the decision to trade 2 outs for a run
                if Runners[1].POS == "1B" or Runners[1].POS == "C" or Runners[1].POS == "P":
                    Runners.append(Batter)
                    Outs += 1
                    del Runners[1]
                    Bases = "101"
                else:
                    Outs += 1
                    Bases = "110"
            elif Outs > 0:
                OddsOutAtSecond = 0.7 # insert odds
                OutAtSecond = random.random()
                if Batter.POS == "1B" or Batter.POS == "C" or Batter.POS == "P":
                    OddsOutAtSecond *= 1.15
                elif Batter.POS == "SS" or Batter.POS == "CF":
                    OddsOutAtSecond *= 0.85
                if OutAtSecond < OddsOutAtSecond:
                    Runners.append(Batter)
                    Outs += 1
                    Bases = "101"
                    del Runners[0]
                    if Outs <= 2:
                        OddsDoublePlay = 0.25 #insert odds
                        DoublePlay = random.random()
                        if Batter.POS == "1B" or Batter.POS == "C" or Batter.POS =="P":
                            OddsDoublePlay *= 1.25
                        elif Batter.POS == "SS" or Batter.POS == "CF":
                            OddsDoublePlay *= 0.85
                        if DoublePlay < OddsDoublePlay:
                            Outs += 1
                        else:
                            Runners.append(Batter)
                            Runs += 1
                            del Runners[0]
                            Bases = "001"         
                else:
                    Bases = "010"
                    Runs += 1
                    del Runners[0]
                    Outs += 1
    
    elif Bases == "111":
        if Result == "1B":
            Runners.append(Batter)
            Runs += 1
            del Runners[0]
            OddsToScore = 0.588 #insert odds
            SecondToScore = random.random()
            if Runners[0].POS == "1B" or Runners[0].POS == "C" or Runners[0].POS == "P":
                OddsToScore -= 0.15
            if SecondToScore < OddsToScore:
                Bases = "101"
                Runs += 1
                del Runners[0]
            elif SecondToScore < (OddsToScore + 0.03):
                Outs += 1
                del Runners[0]
                Bases = "101"
            else:
                Bases = "111" 
        elif Result == "2B":
            Runners.append(Batter)
            Runs += 2
            del Runners[0]
            del Runners[0]
            ScoreFromFirst = random.random()
            OddsScoreFromFirst = 0.47 #insert odds
            if Runners[0].POS == "1B" or Runners[0].POS == "C" or Runners[0].POS == "P":
                    OddsScoreFromFirst = 0.60 * OddsScoreFromFirst #insert odds function
                    if Outs == 2:
                        OddsScoreFromFirst += 0.10
            elif Runners[0].POS == "2B" or Runners[0].POS == "3B" or Runners[0].POS == "DH":
                OddsScoreFromFirst = OddsScoreFromFirst
                if Outs == 2:
                    OddsScoreFromFirst += 0.10
            elif Runners[0].POS == "RF" or Runners[0].POS == "LF":
                OddsScoreFromFirst = 1.15 * OddsScoreFromFirst #insert odds function
                if Outs == 2:
                    OddsScoreFromFirst += 0.15
            elif Runners[0].POS == "SS" or Runners[0].POS == "CF":
                OddsScoreFromFirst == 1.25 * OddsScoreFromFirst #insert odds function
                if Outs == 2:
                    OddsScoreFromFirst += 0.15
            if ScoreFromFirst < OddsScoreFromFirst:
                Runs += 1
                del Runners[0]
                Bases = "010"
            else:
                Bases = "110"
        elif Result == "3B":
            Runners.append(Batter)
            Runs += 3
            del Runners[0]
            del Runners[0]
            del Runners[0]
            Bases = "100"
        elif Result == "HR":
            Runs += 4
            Runners = []
            Bases = "000"
        elif Result == "BB" or Result == "HBP":
            Runners.append(Batter)
            Runs += 1
            del Runners[0]
        elif Result == "K" or Result == "PO":
            Outs += 1
            Bases = "111"
        elif Result == "FO":
            if Outs < 2:
                OddsTagThird = 0.804 #insert odds
                TagThird = random.random()
                if Runners[0].POS == "1B" or Runners[0].POS == "C" or Runners[0].POS == "P":
                    OddsTagThird *= 0.75
                elif Runners[0].POS == "SS" or Runners[0].POS == "CF":
                    OddsTagThird *= 1.25
                if TagThird < OddsTagThird:
                    Runs = 1
                    Outs += 1
                    Bases = "011"
                elif TagThird < (OddsTagThird + 0.0309):
                    Outs += 2
                    Bases = "011"
                else:
                    Bases = "111"
                    Outs += 1
            else:
                Outs += 1
        elif Result == "GO":
            if Outs < 2:
                if Runners[0].POS != "SS" and Runners[0].POS != "CF":
                #    ThrowHome = True
                #if ThrowHome == True:
                    Runners.append(Batter)
                    Outs += 1
                    del Runners[0]
                    Bases = "111"
            else:
                OddsOutAtSecond = 0.7 # insert odds
                OutAtSecond = random.random()
                if Runners[1].POS == "1B" or Runners[1].POS == "C" or Runners[1].POS == "P":
                    OddsOutAtSecond *= 1.15
                elif Runners[1].POS == "SS" or Runners[1].POS == "CF":
                    OddsOutAtSecond *= 0.85
                if OutAtSecond < OddsOutAtSecond:
                    Runners.append(Batter)
                    Outs += 1
                    Bases = "101"
                    del Runners[0]
                    if Outs <= 2:
                        OddsDoublePlay = 0.25 #insert odds
                        DoublePlay = random.random()
                        if Batter.POS == "1B" or Batter.POS == "C" or Batter.POS =="P":
                            OddsDoublePlay *= 1.25
                        elif Batter.POS == "SS" or Batter.POS == "CF":
                            OddsDoublePlay *= 0.85
                        if DoublePlay < OddsDoublePlay:
                            Outs += 1
                            Bases = "100"
                        else:
                            Runners.append(Batter)
                            Runs += 1
                            del Runners[0]
                            Bases = "101"         
                else:
                    Bases = "110"
                    Runs += 1
                    del Runners[0]
                    Outs += 1
            
    print("")    
    print("Results of Last at Bat")        
    print(Result)
    print("Status of Bases", Bases)
    print(Batter)
    print("Runs Scored on last at bat", Runs)
    print("Outs ", + Outs)
    
    
    
    return Result, Bases, Outs, Runs, Runners
    ##Use percetages and random function to determine the resulting action
    ##Add the average number of pitches per batter to the pitch count for every batter faced
    ##State of runners on base
    ##Odds of throwing lead runner out
    ##State of outs
    ##Inning by inning report or batter by batter report for slow option
        ## Batter by batter report
            ##Result of the at bat
        ##Inning by inning report
            ##Runs scored
            ##Number of pitches
            ##Pitching change (and state at change)
            ##Left on base
            ##RunnersInScoringPosition average
            ##Options play next inning or finish game with automanager
            ##Option to change pitchers (list pitchers (function to call))
            ##Option to change hitters
##Game initialization
Outs = 0
AwayPitcher = AwayLineup[9]#insert code
HomePitcher = HomeLineup[9]
AwaySpotInLineup = 0
HomeSpotInLineup = 0
AwayScore = 0
HomeScore = 0
AwayHits = 0
HomeHits = 0
SpotInLineup = [AwaySpotInLineup, HomeSpotInLineup]
Score= [AwayScore,HomeScore]
Hits = [AwayHits, HomeHits]
HomePitchCount = 0
AwayPitchCount = 0
PitchCount = [AwayPitchCount, HomePitchCount]
AwayRelieverNumber = 1
HomeRelieverNumber = 1
##Inning Loop
def HalfInning(TeamHitting, LineUp, SpotInLineup, Pitcher, Score, Hits, PitchCount, GameMode):
    if TeamHitting == "Away":
        SpotInLineupINN = SpotInLineup[0]
    if TeamHitting == "Home":
        SpotInLineupINN = SpotInLineup[1]
    AwayScore = Score[0]
    HomeScore = Score[1]
    AwayHits = Hits[0]
    HomeHits = Hits[1]
    Outs = 0
    Bases = "000"
    Runners = []
    while Outs < 3:
        CurrentResult, Bases, CurrentOuts, Runs, CurrentRunners = AtBat(Pitcher, LineUp[SpotInLineupINN], Bases, Outs, Runners, Score)
        print(TeamHitting)
        print(Runs)
        if TeamHitting == "Away":
            AwayScore += Runs
            Score[0] = AwayScore
            PitchCount[0] += (Pitcher.NP*Pitcher.GP/Pitcher.TBF)
            if CurrentResult == "1B" or CurrentResult == "2B" or CurrentResult == "3B" or CurrentResult == "HR":
                AwayHits += 1
            if SpotInLineupINN == 8:
                SpotInLineupINN = 0
            else:
                SpotInLineupINN += 1
            
            TempLineUpSpot = AwaySpotInLineup
            TempLineUp = AwayLineup
            
        if TeamHitting == "Home":
            HomeScore += Runs
            Score[1] = HomeScore
            PitchCount[1] += (Pitcher.NP*Pitcher.GP/Pitcher.TBF)
            if CurrentResult == "1B" or CurrentResult == "2B" or CurrentResult == "3B" or CurrentResult == "HR":
                HomeHits += 1
            if SpotInLineupINN == 8:
                SpotInLineupINN = 0
            else:
                SpotInLineupINN += 1
            TempLineUpSpot = HomeSpotInLineup
            TempLineUp = HomeLineup
             
        if GameMode == "AtBat":
            print("Now Batting: {0} \n Pitching: {1}".format(LineUp[SpotInLineupINN], Pitcher))
            AskUser = input("To continue type 'y' , to change pitcher type 'p' to change hitter type 'h', to simulate to the end of the game type 'e', to quit type 'q'\n")
            if AskUser == "y":
                continue
            if AskUser == "p":
                if TeamHitting == "Away":
                    change_pitcher_list = Pitchers_list1
                else:
                    change_pitcher_list = Pitchers_list
                for player in change_pitcher_list: #Make statement for selecting which pitcher list to go for
                    print(player)
                NewPitcher = input("Enter one of the pitchers above\n")
                if NewPitcher not in change_pitcher_list:
                    while NewPitcher not in change_pitcher_list:
                        NewPitcher = input("Please enter a valid pitcher. To list the pitchers type 'ls'. To exit type 'q' \n")
                        if NewPitcher == "ls":
                            for players in change_pitcher_list:
                                print(player)
                        if NewPitcher == "q":
                            exit()
                        Pitcher = NewPitcher
            if AskUser == "b":
                if TeamHitting == "Away":
                    change_batters_list = Batters_list
                else:
                    change_batters_list = Batters_list1
                for players in change_batters_list:
                    if player not in LineUp:
                        print(player)
                NewBatter = input("Enter one of the batters above\n")
                if NewBatter not in change_batters_list or NewBatter in LineUp:
                    while NewBatter not in change_batters_list:
                        NewBatter = input("Please enter a valid hitter. To list the hitters type 'ls'. To exit type 'q' \n")
                        if NewBatter == "ls":
                           if player not in LineUp:
                               print(player)
                        if NewBatter == "q":
                            exit()
            if AskUser == "e":
                GameMode = "100Game"
                GameNumber = 99
            if AskUser == "q":
                exit()
        Outs = CurrentOuts
   
    return TeamHitting, Score, Hits, Pitcher, PitchCount, SpotInLineupINN

##Main Game Code
CurrentInning = 1
TeamHitting = "Away"
LineUp = AwayLineup
Pitcher = HomePitcher
InningStatus = "Top"
while CurrentInning < 10 or (CurrentInning >= 10 and Score[0] == Score[1]) or (CurrentInning == 9.5 and Score[0]< Score[1]):
    TeamHitting, ScoreINN, HitsINN, CurrentPitcher, PitchCountINN, SpotInLineupINN = HalfInning(TeamHitting, LineUp, SpotInLineup, Pitcher, Score, Hits, PitchCount, GameMode)
    CurrentInning += 0.5
    if TeamHitting == "Away":
        SpotInLineup[0] = SpotInLineupINN
    elif TeamHitting == "Home":
        SpotInLineup[1] = SpotInLineupINN

        
    if TeamHitting == "Away":
        TeamHitting = "Home"
        LineUp = HomeLineup
        Pitcher = AwayLineup[9]
    else:
        TeamHitting = "Away"
        LineUp = AwayLineup
        Pitcher = HomeLineup[9]
        
    if GameMode == "Inning" or GameMode == "AtBat":
        if TeamHitting == 'Away':
            DueUp = LineUp[SpotInLineup[0]]
            if SpotInLineup[0] == 7:
                OnDeck = LineUp[SpotInLineup[0]+1]
                InTheHole = LineUp[0]
            elif SpotInLineup[0] == 8:
                OnDeck = LineUp[0]
                InTheHole = LineUp[1]
            else:
                OnDeck = LineUp[SpotInLineup[0]+1]
                InTheHole = LineUp[SpotInLineup[0]+2]
            
            InningStatus = 'Top'
        if TeamHitting == 'Home':
            DueUp = LineUp[SpotInLineup[1]]
            if SpotInLineup[1] == 7:
                OnDeck = LineUp[SpotInLineup[1]+1]
                InTheHole = LineUp[0]
            elif SpotInLineup[1] == 8:
                OnDeck = LineUp[0]
                InTheHole = LineUp[1]
            else:
                OnDeck = LineUp[SpotInLineup[1]+1]
                InTheHole = LineUp[SpotInLineup[1]+2]
            InningStatus = 'Bottom'
        if CurrentInning >= 10 and InningStatus == "Top" and (Score[0] != Score[1]):
            continue

        print("")
        print("##############################################################")
        print("")
        print("It is the " + InningStatus + " of the " , CurrentInning//1 , "inning")
        print("The Score is ", AwayTeam, Score[0], HomeTeam, Score[1])
        print(Pitcher, "is on the mound")
        print("Due up:{0}\n{1}\n{2}\n".format(DueUp, OnDeck, InTheHole))
        AskUser = input("To continue type 'y' , to change pitcher type 'p' to change hitter type 'b', to simulate to the end of the game type 'e', to quit type 'q'\n")
        if AskUser == "y":
            continue
        if AskUser == "p":
            if TeamHitting == "Away":
                change_pitcher_list = list_of_pitchers1
            else:
                change_pitcher_list = list_of_pitchers
            for player in change_pitcher_list: #Make statement for selecting which pitcher list to go for
                print(player)
            NewPitcher = input("Enter one of the pitchers above\n")
            if NewPitcher not in change_pitcher_list:
                while NewPitcher not in change_pitcher_list:
                    NewPitcher = input("Please enter a valid pitcher. To list the pitchers type 'ls'. To exit type 'q' \n")
                    if NewPitcher == "ls":
                        for players in change_pitcher_list:
                            print(player)
                    if NewPitcher == "q":
                        exit()
            
            if TeamHitting == 'Away':
                FindPitcher = dictionary_of_pitchers1[NewPitcher]
                HomeLineup[9] = FindPitcher
            else:
                FindPitcher = dictionary_of_pitchers[NewPitcher]
                AwayLineup[9] = FindPitcher
        if AskUser == "b":
            if TeamHitting == "Away":
                change_batters_list = list_of_batters
            else:
                change_batters_list = list_of_batters1
            for player in change_batters_list:
                if player not in LineUp:
                    print(player)
            NewBatter = input("Enter one of the batters above\n")
            if NewBatter not in change_batters_list or NewBatter in LineUp:
                while NewBatter not in change_batters_list:
                    NewBatter = input("Please enter a valid hitter. To list the hitters type 'ls'. To exit type 'q' \n")
                    if NewBatter == "ls":
                       if player not in LineUp:
                           print(player)
                    if NewBatter == "q":
                        exit()
            if TeamHitting == "Away":
                FindBatter = dictionary_of_batters[NewBatter]
                AwayLineup[SpotInLineup[0]] = FindBatter
            else:
                FindBatter = dictionary_of_batters1[NewBatter]
                HomeLineup[SpotInLineup[1]] = FindBatter
            
        if AskUser == "e":
            GameMode = "100Games"
            GameNumber = 99
        if AskUser == "q":
            exit()
    else:
        if TeamHitting == 'Away':
            if PitchCount[1] > (HomeLineup[9].NP/HomeLineup[9].TBF):
                HomeLineup[9] = Pitchers_list1[HomeRelieverNumber]
                HomeRelieverNumber += 1
        else:
            if PitchCount[0] > (AwayLineup[9].NP/AwayLineup[9].TBF):
                AwayLineup[9] = Pitchers_list[AwayRelieverNumber]
                AwayRelieverNumber += 1
        

print("The Game is over, The Final Score is", AwayTeam, Score[0], HomeTeam, Score[1])

    ##Managerial style argument
    ##Conditions for how many bases runner on base get per type of hit
    ##3 Battter minimum / end of inning for relief pitchers 
    ##Home team leading after the top of the ninth = game over
    ##Extra innnings conditions (if score tied play additional inning)
    
##Add a spread and total runs for 100 simulated games