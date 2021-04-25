#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 13:56:33 2021

@author: javi
"""
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
PossibleTeams = [""]
AwayTeam = input("Enter the name of the Away Team. For a list of possible teams type 'ls', to exit type 'q' \n")
if AwayTeam == "ls":
    print()
    AwayTeam = input("Choose from one of the listed teams \n")
elif AwayTeam == "q":
    exit()
elif AwayTeam in PossibleTeams:
    SetAwayTeam = True
    
AwayLineup = input("Enter away team line up in the form 'Player[Postition],[Player[Postition]...' "+ \
                   "The first 9 spots in the line up are the hitters and the 10th is the pitcher. "+\
                   "If the pitcher is hitting for himself in the National League list the name twice"+ \
                     " once for his hitting spot in the line up and againg at the end as a pitcher.")
    
HomeLineup = input("Enter home team line up in the form 'Player[Postition],[Player[Postition]...' "+ \
                   "The first 9 spots in the line up are the hitters and the 10th is the pitcher. "+\
                   "If the pitcher is hitting for himself in the National League list the name twice"+ \
                     " once for his hitting spot in the line up and againg at the end as a pitcher.")
    
GameMode = input("Enter game mode: 100Game, Inning, AtBat\n")

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
    HR = Batter.HR  #Adjust formula
    BBPitcher = Pitcher.BB
    BB = Batter.BB + BBPitcher #Adjust formula
    HBP = np.mean(Batter.HBP + Pitcher.HBP)
    K = Batter.K + Pitcher.K #Adjust formula
    FB = Batter.FB
    SB = Batter.SB
    TB = Batter.TB
    RemainingPercentage = 1-FB-SB-TB-HR-BB-HBP-K
    GO = RemainingPercentage / (1+Pitcher.GO_AO) * Pitcher.GO_AO
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
        FlyOut = 0 #insert fly out stat
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
            if Runners[0].position == "1B" or Runners.position[0] == "C" or Runners[0].position == "P":
                OddsFirstToThird = 0.85 * OddsFirstToThird #insert odds function
                if Outs == 2:
                    OddsFirstToThird += 0.15
            elif Runners[0].position == "2B" or Runners.position[0] == "3B" or Runners.position[0] == "DH":
                OddsFirstToThird = OddsFirstToThird
                if Outs == 2:
                    OddsFirstToThird += 0.15
            elif Runners[0].position == "RF" or Runners.position[0] == "LF":
                OddsFirstToThird = 1.07 * OddsFirstToThird #insert odds function
                if Outs == 2:
                    OddsFirstToThird += 0.15
            elif Runners[0].position == "SS" or Runners.position[0] == "CF":
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
            if Runners[0].position == "1B" or Runners.position[0] == "C" or Runners[0].position == "P":
                OddsFirstToScore = 0.60 * OddsFirstToScore #insert odds function
                if Outs == 2:
                    OddsFirstToScore += 0.10
            elif Runners[0].position == "2B" or Runners.position[0] == "3B" or Runners.position[0] == "DH":
                OddsFirstToScore = OddsFirstToScore
                if Outs == 2:
                    OddsFirstToScore += 0.10
            elif Runners[0].position == "RF" or Runners.position[0] == "LF":
                OddsFirstToScore = 1.15 * OddsFirstToThird #insert odds function
                if Outs == 2:
                    OddsFirstToScore += 0.15
            elif Runners[0].position == "SS" or Runners.position[0] == "CF":
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
            if Runners[0].position == "1B" or Runners.position[0] == "C" or Runners[0].position == "P":
                OddsOutAtSecond *= 1.15
            elif Runners[0].position == "SS" or Runners.position[0] == "CF":
                OddsOutAtSecond *= 0.85
            if OutAtSecond < OddsOutAtSecond:
                Outs += 1
                Bases = "001"
                Runners.append(Batter)
                del Runners[0]
                if Outs <= 2:
                    OddsDoublePlay = 0.25 #insert odds ###estimate
                    DoublePlay = random.random()
                    if Batter.position == "1B" or Batter.position == "C" or Batter.position =="P":
                        OddsDoublePlay *= 1.25
                    elif Batter.position == "SS" or Batter.position == "CF":
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
            if Runners[0].position == "1B" or Runners.position[0] == "C" or Runners[0].position == "P":
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
                OddsTagThird = 0 #insert odds
                TagThird = random.random()
                if Runners[0].position == "1B" or Runners.position[0] == "C" or Runners[0].position == "P":
                    OddsTagThird *= 0.75
                elif Runners[0].position == "SS" or Runners.position[0] == "CF":
                    OddsTagThird *= 1.25
                if TagThird < OddsTagThird:
                    Runs = 1
                    Outs += 1
                    Bases = "000"
                elif TagThird < (OddsTagThird + 0.05):
                    Outs += 2
                    Bases = "000"
                else:
                    Bases = "100"
                    Outs += 1
            else:
                Outs += 1
        elif Result == "GO":
            Outs += 1
            Bases = "100"
        
            
    elif Bases == "011":
        if Result == "1B":
            Runners.append(Batter)
            OddsToScore = 0.588 #insert odds
            SecondToScore = random.random()
            if Runners[0].position == "1B" or Runners.position[0] == "C" or Runners[0].position == "P":
                OddsToScore -= 0.15
            if SecondToScore < OddsToScore:
                Runs = 1
                del Runners[0]
                FirstToThird = random.random()
                OddsFirstToThird = 0.276
                if Runners[0].position == "1B" or Runners.position[0] == "C" or Runners[0].position == "P":
                    OddsFirstToThird = 0.85 * OddsFirstToThird #insert odds function
                    if Outs == 2:
                        OddsFirstToThird += 0.15
                elif Runners[0].position == "2B" or Runners.position[0] == "3B" or Runners.position[0] == "DH":
                    OddsFirstToThird = OddsFirstToThird
                    if Outs == 2:
                        OddsFirstToThird += 0.15
                elif Runners[0].position == "RF" or Runners.position[0] == "LF":
                    OddsFirstToThird = 1.07 * OddsFirstToThird #insert odds function
                    if Outs == 2:
                        OddsFirstToThird += 0.15
                elif Runners[0].position == "SS" or Runners.position[0] == "CF":
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
            if Runners[0].position == "1B" or Runners.position[0] == "C" or Runners[0].position == "P":
                    OddsScoreFromFirst = 0.6 * OddsScoreFromFirst #insert odds function
                    if Outs == 2:
                        OddsScoreFromFirst += 0.10
            elif Runners[0].position == "2B" or Runners.position[0] == "3B" or Runners.position[0] == "DH":
                OddsScoreFromFirst = OddsScoreFromFirst
                if Outs == 2:
                    OddsScoreFromFirst += 0.10
            elif Runners[0].position == "RF" or Runners.position[0] == "LF":
                OddsScoreFromFirst = 1.15 * OddsScoreFromFirst #insert odds function
                if Outs == 2:
                    OddsScoreFromFirst += 0.15
            elif Runners[0].position == "SS" or Runners.position[0] == "CF":
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
            if Runners[1].position == "1B" or Runners.position[1] == "C" or Runners[1].position == "P":
                OddsOutAtSecond *= 1.15
            elif Runners[1].position == "SS" or Runners.position[1] == "CF":
                OddsOutAtSecond *= 0.85
            if OutAtSecond < OddsOutAtSecond:
                Runners.append(Batter)
                Outs += 1
                Bases = "101"
                del Runners[0]
                if Outs <= 2:
                    OddsDoublePlay = 0.25 #insert odds ##estimate
                    DoublePlay = random.random()
                    if Batter.position == "1B" or Batter.position == "C" or Batter.position =="P":
                        OddsDoublePlay *= 1.25
                    elif Batter.position == "SS" or Batter.position == "CF":
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
            if Runners[0].position == "1B" or Runners.position[0] == "C" or Runners[0].position == "P":
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
                OddsTagThird = 0 #insert odds
                TagThird = random.random()
                if Runners[0].position == "1B" or Runners.position[0] == "C" or Runners[0].position == "P":
                    OddsTagThird *= 0.75
                elif Runners[0].position == "SS" or Runners.position[0] == "CF":
                    OddsTagThird *= 1.25
                if TagThird < OddsTagThird:
                    Runs = 1
                    Outs += 1
                    Bases = "010"
                elif TagThird < (OddsTagThird + 0.05):
                    Outs += 2
                    Bases = "010"
                else:
                    Bases = "110"
                    Outs += 1
            else:
                Outs += 1
        elif Result == "GO":
            if Outs < 2:
                OddsScoreGO = 0 #insert odds
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
            OddsFirstToThird = 0 #insert odds
            FirstToThird = random.random()
            if Runners[0].position == "1B" or Runners.position[0] == "C" or Runners[0].position == "P":
                OddsFirstToThird = 0 * OddsFirstToThird #insert odds function
                if Outs == 2:
                    OddsFirstToThird += 0.25
            elif Runners[0].position == "2B" or Runners.position[0] == "3B" or Runners.position[0] == "DH":
                OddsFirstToThird = OddsFirstToThird
                if Outs == 2:
                    OddsFirstToThird += 0.20
            elif Runners[0].position == "RF" or Runners.position[0] == "LF":
                OddsFirstToThird = 0 * OddsFirstToThird #insert odds function
                if Outs == 2:
                    OddsFirstToThird += 0.15
            elif Runners[0].position == "SS" or Runners.position[0] == "CF":
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
            OddsScoreFromFirst = 0.47 #insert odds
            if Runners[0].position == "1B" or Runners.position[0] == "C" or Runners[0].position == "P":
                    OddsScoreFromFirst = 0.60 * OddsScoreFromFirst #insert odds function
                    if Outs == 2:
                        OddsScoreFromFirst += 0.10
            elif Runners[0].position == "2B" or Runners.position[0] == "3B" or Runners.position[0] == "DH":
                OddsScoreFromFirst = OddsScoreFromFirst
                if Outs == 2:
                    OddsScoreFromFirst += 0.10
            elif Runners[0].position == "RF" or Runners.position[0] == "LF":
                OddsScoreFromFirst = 1.15 * OddsScoreFromFirst #insert odds function
                if Outs == 2:
                    OddsScoreFromFirst += 0.15
            elif Runners[0].position == "SS" or Runners.position[0] == "CF":
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
                OddsTagThird = 0 #insert odds
                TagThird = random.random()
                if Runners[0].position == "1B" or Runners.position[0] == "C" or Runners[0].position == "P":
                    OddsTagThird *= 0.75
                elif Runners[0].position == "SS" or Runners.position[0] == "CF":
                    OddsTagThird *= 1.25
                if TagThird < OddsTagThird:
                    Runs = 1
                    Outs += 1
                    Bases = "001"
                elif TagThird < (OddsTagThird + 0.05):
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
                if Runners[1].position == "1B" or Runners.position[1] == "C" or Runners[1].position == "P":
                    Runners.append(Batter)
                    Outs += 1
                    del Runners[1]
                    Bases = "101"
                else:
                    Outs += 1
                    Bases = "110"
            elif Outs > 0:
                OddsOutAtSecond = 0 # insert odds
                OutAtSecond = random.random()
                if Runners[1].position == "1B" or Runners.position[1] == "C" or Runners[1].position == "P":
                    OddsOutAtSecond *= 1.15
                elif Runners[1].position == "SS" or Runners.position[1] == "CF":
                    OddsOutAtSecond *= 0.85
                if OutAtSecond < OddsOutAtSecond:
                    Runners.append(Batter)
                    Outs += 1
                    Bases = "101"
                    del Runners[0]
                    if Outs <= 2:
                        OddsDoublePlay = 0 #insert odds
                        DoublePlay = random.random()
                        if Batter.position == "1B" or Batter.position == "C" or Batter.position =="P":
                            OddsDoublePlay *= 1.25
                        elif Batter.position == "SS" or Batter.position == "CF":
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
            OddsToScore = 0 #insert odds
            SecondToScore = random.random()
            if Runners[0].position == "1B" or Runners.position[0] == "C" or Runners[0].position == "P":
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
            if Runners[0].position == "1B" or Runners.position[0] == "C" or Runners[0].position == "P":
                    OddsScoreFromFirst = 0.60 * OddsScoreFromFirst #insert odds function
                    if Outs == 2:
                        OddsScoreFromFirst += 0.10
            elif Runners[0].position == "2B" or Runners.position[0] == "3B" or Runners.position[0] == "DH":
                OddsScoreFromFirst = OddsScoreFromFirst
                if Outs == 2:
                    OddsScoreFromFirst += 0.10
            elif Runners[0].position == "RF" or Runners.position[0] == "LF":
                OddsScoreFromFirst = 1.15 * OddsScoreFromFirst #insert odds function
                if Outs == 2:
                    OddsScoreFromFirst += 0.15
            elif Runners[0].position == "SS" or Runners.position[0] == "CF":
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
                OddsTagThird = 0 #insert odds
                TagThird = random.random()
                if Runners[0].position == "1B" or Runners.position[0] == "C" or Runners[0].position == "P":
                    OddsTagThird *= 0.75
                elif Runners[0].position == "SS" or Runners.position[0] == "CF":
                    OddsTagThird *= 1.25
                if TagThird < OddsTagThird:
                    Runs = 1
                    Outs += 1
                    Bases = "011"
                elif TagThird < (OddsTagThird + 0.05):
                    Outs += 2
                    Bases = "011"
                else:
                    Bases = "111"
                    Outs += 1
            else:
                Outs += 1
        elif Result == "GO":
            if Outs < 2:
                if Runners[0].position != "SS" and Runners.position[0] != "CF":
                    ThrowHome = True
                if ThrowHome == True:
                    Runners.append(Batter)
                    Outs += 1
                    del Runners[0]
                    Bases = "111"
            else:
                OddsOutAtSecond = 0 # insert odds
                OutAtSecond = random.random()
                if Runners[1].position == "1B" or Runners.position[1] == "C" or Runners[1].position == "P":
                    OddsOutAtSecond *= 1.15
                elif Runners[1].position == "SS" or Runners.position[1] == "CF":
                    OddsOutAtSecond *= 0.85
                if OutAtSecond < OddsOutAtSecond:
                    Runners.append(Batter)
                    Outs += 1
                    Bases = "101"
                    del Runners[0]
                    if Outs <= 2:
                        OddsDoublePlay = 0 #insert odds
                        DoublePlay = random.random()
                        if Batter.position == "1B" or Batter.position == "C" or Batter.position =="P":
                            OddsDoublePlay *= 1.25
                        elif Batter.position == "SS" or Batter.position == "CF":
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
AwayPitcher = #insert code
HomePitcher = 
AwaySpotInLineup = 0
HomeSpotInLineup = 0
AwayScore = 0
HomeScore = 0
AwayHits = 0
HomeHits = 0
Score= [AwayScore,HomeScore]
Hits = [AwayHit, HomeHits]
##Inning Loop
def HalfInning(TeamHitting, LineUp, Pitcher, Score, Hits, Pitchcount)
    Outs = 0
    while Outs < 3:
        CurrentResult, Bases, CurrentOuts, Runs, CurrentRunners = AtBat(Pitcher, Lineup[SpotInLineup], Bases, Outs, Runners, Score)
        PitchCount += Pitcher.PitchesPerBatter
        if TeamHitting == "Away":
            AwayScore += Runs
            if Result == "1B" or Result == "2B" or Result == "3B" or Result == "HR":
                AwayHits += 1
            if AwaySpotInLineup == 8:
                AwaySpotInLineup = 0
            else:
            AwaySpotInLineup += 1
            
            TempLineUpSpot = AwaySpotInLineup
            TempLineUp = AwayLineup
            TempPitcher = HomePitcher
            
        if TeamHitting == "Home":
            HomeScore += Runs
            if Result == "1B" or Result == "2B" or Result == "3B" or Result == "HR":
                HomeHits += 1
            if HomeSpotInLineup == 8:
                HomeSpotInLineup = 0
            else:
                HomeSpotInLineup += 1
             TempLineUpSpot = HomeSpotInLineup
             TempLineUp = HomeLineup
             TempPitcher = AwayPitcher
             
        if GameMode == "AtBat":
            print("Now Batting: {0} \n Pitching: {1}".format(TempLineUp[TempLineUpSpot], TempPitcher))
            AskUser = input("To continue type 'y' , to change pitcher type 'p' to change hitter type 'h', to simulate to the end of the game type 'e', to quit type 'q'\n")
            if AskUser == "y":
                continue
            if AskUser == "p":
                for players in pitcher_list:
                    print(player)
                NewPitcher = input("Enter one of the pitchers above\n")
                if NewPitcher not in pitcher_list:
                    while NewPitcher not in pitcher_list:
                        NewPitcher = input("Please enter a valid pitcher. To list the pitchers type 'ls'. To exit type 'q' \n")
                        if NewPitcher = "ls":
                            for players in pitcher_list:
                                print(player)
                        if NewPitcher == "q":
                            exit()
                if TeamHitting == "Away":
                    HomePitcher = NewPitcher
                if TeamHitting == "Home":
                    AwayPitcher = NewPitcher
            if AskUser == "b":
                for players in Batters_list:
                    if player not in TempLineUp:
                        print(player)
                NewBatter = input("Enter one of the batters above\n")
                if NewBatter not in Batters_list:
                    while NewBatter not in Batters_list:
                        NewBatter = input("Please enter a valid hitter. To list the hitters type 'ls'. To exit type 'q' \n")
                        if NewBatter = "ls":
                           if player not in TempLineUp:
                               print(player)
                        if NewBatter == "q":
                            exit()
            if AskUser == "e":
                GameMode = "Sim2End"
            if AskUser == "q":
                exit()
    if TeamHitting == "Away":
        TeamHitting = "Home"
    if TeamHitting == "Home":
        TeamHitting = "Away"
    return TeamHitting, Score, Hits, PitchCount, LineUpSpot

##Main Game Code
CurrentInning = 1
while CurrentInning < 10 or (CurrentInning >= 10 and Score[0] = Score[1]):
    HalfInning()
    CurrentInning += 1
    if GameMode == "Inning":
        DueUp = LineUp[LineUpSpot]
        OnDeck = LineUp[LineUpSpot+1]
        InTheHole = LineUp[LineUpSpot+2]
        print("Due up:{0}\n{1}\n{2}\n".format(DueUp, OnDeck, InTheHole))
        AskUser = input("To continue type 'y' , to change pitcher type 'p' to change hitter type 'h', to simulate to the end of the game type 'e', to quit type 'q'\n")
            if AskUser == "y":
                continue
            if AskUser == "p":
                for players in pitcher_list:
                    print(player)
                NewPitcher = input("Enter one of the pitchers above\n")
                if NewPitcher not in pitcher_list:
                    while NewPitcher not in pitcher_list:
                        NewPitcher = input("Please enter a valid pitcher. To list the pitchers type 'ls'. To exit type 'q' \n")
                        if NewPitcher = "ls":
                            for players in pitcher_list:
                                print(player)
                        if NewPitcher == "q":
                            exit()
                if TeamHitting == "Away":
                    HomePitcher = NewPitcher
                if TeamHitting == "Home":
                    AwayPitcher = NewPitcher
            if AskUser == "b":
                for players in Batters_list:
                    if player not in TempLineUp:
                        print(player)
                NewBatter = input("Enter one of the batters above\n")
                if NewBatter not in Batters_list:
                    while NewBatter not in Batters_list:
                        NewBatter = input("Please enter a valid hitter. To list the hitters type 'ls'. To exit type 'q' \n")
                        if NewBatter = "ls":
                           if player not in TempLineUp:
                               print(player)
                        if NewBatter == "q":
                            exit()
            if AskUser == "e":
                GameMode = "Sim2End"
            if AskUser == "q":
                exit()

    ##Managerial style argument
    ##Conditions for how many bases runner on base get per type of hit
    ##3 Battter minimum / end of inning for relief pitchers 
    ##Home team leading after the top of the ninth = game over
    ##Extra innnings conditions (if score tied play additional inning)
    
##Add a spread and total runs for 100 simulated games