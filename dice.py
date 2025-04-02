import random
import tkinter as tk
from tkinter import ttk

def rollDice(self, num):
    random.seed()
    return [random.randint(1,6) for x in range(0,self.cup)]

def stop(self):
    print('You chose to score and pass')

def diceClick(self):
    print('You clicked a dice')

def bust(self):
    pass

def calcScore(self, dice):
    #This should be called anytime a dice from a roll is selected to show what the score would be
    tmpScore = 0
    counter = {
        '1': 0,
        '2': 0,
        '3': 0,
        '4': 0,
        '5': 0,
        '6': 0
    }
    counter2 = {
        '1': 0,
        '2': 0,
        '3': 0,
        '4': 0,
        '5': 0,
        '6': 0
    }
    for x in counter:
        self.counter[str(x)] += 1
    for key,value in counter.items():
        if value >= 3:
            if key == '1':
                tmpScore += 1000
            else:
                tmpScore += (int(key)*100)
            if value > 3:
                tmpScore = tmpScore * 2
        else:
            counter2[key] = int(value)
    
    tmpScore += counter2['1']*100
    tmpScore += counter2['5']*50
    return tmpScore

def scoreAndPass(self, score):
    self.score += score
    return

if __name__ == '__main__':
    #while True:
        #z will be a list of dice roll results
        #z = rollDice(6)
        #print(z)
        #choice = input('Choose dice to keep.')
