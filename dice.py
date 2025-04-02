import random
import tkinter as tk
from tkinter import ttk



#class GameState:
#    def __init__(self, cup=6, roll=None, kd=None, score=0):
#        self.cup = cup
#        self.roll = roll
#        self.keptDice = kd
#        self.score = score

class App(tk.Frame):
    def __init__(self, master, gs):
        super().__init__(master)
        self.pack()

        self.btn_roll = tk.Button(text='Roll',command=self.roll)
        self.btn_stop = tk.Button(text='Score and stop',command=self.stop)
        self.dice1 = tk.Radiobutton(text='dice1',command=self.diceClick)
        self.dice2 = tk.Radiobutton(text='dice2',command=self.diceClick)
        self.dice3 = tk.Radiobutton(text='dice3',command=self.diceClick)
        self.dice4 = tk.Radiobutton(text='dice4',command=self.diceClick)
        self.dice5 = tk.Radiobutton(text='dice5',command=self.diceClick)
        self.dice6 = tk.Radiobutton(text='dice6',command=self.diceClick)
        #Add dice gui elements here. Everytime a dice is selected or unselected you must call the calcScore func in GameState

        self.btn_roll.pack()
        self.btn_stop.pack()
        self.dice1.pack()
        self.dice2.pack()
        self.dice3.pack()
        self.dice4.pack()
        self.dice5.pack()
        self.dice6.pack()

        #self.contents = tk.StringVar()

        #self.contents.set('this is a variable')

        #self.entrythingy["textvariable"] = self.contents

    def print_contents(self, event):
        print("Hi. The current entry content is:",self.contents.get())

    def roll(self):
        print('You chose to roll again')

    def stop(self):
        print('You chose to score and pass')

    def diceClick(self):
        print('You clicked a dice')

    def rollDice(self):
        self.roll = [random.randint(1,6) for x in range(0,self.cup)]

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
    root = tk.Tk()
    root.geometry('600x400')
    gameState = GameState()
    myapp = App(root, gs)
    myapp.mainloop()

    random.seed()
    #while True:
        #z will be a list of dice roll results
        #z = rollDice(6)
        #print(z)
        #choice = input('Choose dice to keep.')
