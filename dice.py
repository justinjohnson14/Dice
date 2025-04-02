import random
import tkinter as tk
from tkinter import ttk

class GameState:
    def __init__(self, cup=6, roll=None, kd=None, score=0):
        self.cup = cup
        self.roll = roll
        self.keptDice = kd
        self.score = score

    def rollDice(self):
        self.roll = [random.randint(1,6) for x in range(0,self.cup)]

    def bust(self):
        pass

    def calcScore(self):
        #This should be called anytime a dice from a roll is selected to show what the score would be
        pass


class App(tk.Frame):
    def __init__(self, master, gs):
        super().__init__(master)
        self.pack()

        self.btn_roll = tk.Button(text='Roll',command=self.roll)
        self.btn_stop = tk.Button(text='Score and stop',command=self.stop)

        self.btn_roll.pack()
        self.btn_stop.pack()

        #self.contents = tk.StringVar()

        #self.contents.set('this is a variable')

        #self.entrythingy["textvariable"] = self.contents

    def print_contents(self, event):
        print("Hi. The current entry content is:",self.contents.get())

    def roll(self):
        print('You chose to roll again')

    def stop(self):
        print('You chose to score and pass')

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
