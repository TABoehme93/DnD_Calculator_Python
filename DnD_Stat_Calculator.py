#Thomas Boehme
#started: 2017/3/14
#last edited: 2019/8/11
#finished: --
#Quick stat calculator for D&D, starting with 4e stat calculations
#Next goals:
    #add level input, this includes modifiers + half level
    #calculate skills
    #utilize a database to add racial modifiers
    #allow the option to select editions between 2e, 3.5, 4e, and 5e

#from tkinter import *
import tkinter
import tkinter.messagebox

def main():
    dnd = DnD_Calculator()
#end main function

class DnD_Calculator:
    def __init__(self):
        self.mainWindow = tkinter.Tk()
        self.mainWindow.title("D&D Stat Calculator") #sets the title for window

        #stats and scores frames and to hold the two columns
        self.levelRow = tkinter.Frame(self.mainWindow)#holds level information
        self.columns = tkinter.Frame(self.mainWindow) #holds the columns
        self.statsFrame = tkinter.Frame(self.columns) #holds stat labels
        self.scoreFrame = tkinter.Frame(self.columns) #holds score inputs
        self.modsFrame = tkinter.Frame(self.columns) #holds modifiers
        self.modHalfFrame = tkinter.Frame(self.columns) #holds modifiers + half level

        #level label and input
        self.level = tkinter.Label(self.levelRow, text="LEVEL")
        self.lvlEntry = tkinter.Entry(self.levelRow, width=10)
        self.lvlError = tkinter.Label(self.levelRow, text="")
        #self.lvlValid = False   #used to see if the current level input is valid

        #labels for stats column
        self.stats = tkinter.Label(self.statsFrame, text="STATS")
        self.strLabel = tkinter.Label(self.statsFrame, text="Strength")
        self.conLabel = tkinter.Label(self.statsFrame, text="Constitution")
        self.dexLabel = tkinter.Label(self.statsFrame, text="Dexterity")
        self.intLabel = tkinter.Label(self.statsFrame, text="Intellegence")
        self.wisLabel = tkinter.Label(self.statsFrame, text="Wisdom")
        self.chaLabel = tkinter.Label(self.statsFrame, text="Charisma")

        #label and entries for scores column
        self.score = tkinter.Label(self.scoreFrame, text="SCORE")
        self.strEntry = tkinter.Entry(self.scoreFrame, width=10)
        self.conEntry = tkinter.Entry(self.scoreFrame, width=10)
        self.dexEntry = tkinter.Entry(self.scoreFrame, width=10)
        self.intEntry = tkinter.Entry(self.scoreFrame, width=10)
        self.wisEntry = tkinter.Entry(self.scoreFrame, width=10)
        self.chaEntry = tkinter.Entry(self.scoreFrame, width=10)

        #label and modifiers for the modifier column
        self.mods = tkinter.Label(self.modsFrame, text="MODIFIERS")
        self.strMod = tkinter.Label(self.modsFrame, text="-")
        self.conMod = tkinter.Label(self.modsFrame, text="-")
        self.dexMod = tkinter.Label(self.modsFrame, text="-")
        self.intMod = tkinter.Label(self.modsFrame, text="-")
        self.wisMod = tkinter.Label(self.modsFrame, text="-")
        self.chaMod = tkinter.Label(self.modsFrame, text="-")

        #label and modifiers for the modifier column
        self.modHalf = tkinter.Label(self.modHalfFrame, text="MOD+HalfLVL")
        self.strModHalf = tkinter.Label(self.modHalfFrame, text="-")
        self.conModHalf = tkinter.Label(self.modHalfFrame, text="-")
        self.dexModHalf = tkinter.Label(self.modHalfFrame, text="-")
        self.intModHalf = tkinter.Label(self.modHalfFrame, text="-")
        self.wisModHalf = tkinter.Label(self.modHalfFrame, text="-")
        self.chaModHalf = tkinter.Label(self.modHalfFrame, text="-")

        #calculate button
        self.calculate = tkinter.Button(self.mainWindow, text="Calculate",\
                                        command=self.display_Stats)
        self.pack_Columns() #packs the window
        
        tkinter.mainloop()
    #end __init__ method
    
    def pack_Columns(self):
        self.level.pack(side="left")   #packs the level row
        self.lvlEntry.pack(side="left")
        self.lvlError.pack(side="left")

        self.stats.pack()   #packs stats column
        self.strLabel.pack()
        self.conLabel.pack()
        self.dexLabel.pack()
        self.intLabel.pack()
        self.wisLabel.pack()
        self.chaLabel.pack()

        self.score.pack()   #packs score column
        self.strEntry.pack()
        self.conEntry.pack()
        self.dexEntry.pack()
        self.intEntry.pack()
        self.wisEntry.pack()
        self.chaEntry.pack()

        self.mods.pack()   #packs modifier column
        self.strMod.pack()
        self.conMod.pack()
        self.dexMod.pack()
        self.intMod.pack()
        self.wisMod.pack()
        self.chaMod.pack()

        self.modHalf.pack()   #packs modifier column
        self.strModHalf.pack()
        self.conModHalf.pack()
        self.dexModHalf.pack()
        self.intModHalf.pack()
        self.wisModHalf.pack()
        self.chaModHalf.pack()
        
        #packs the columns
        self.levelRow.pack(side="top")
        self.statsFrame.pack(side="left")
        self.scoreFrame.pack(side="left")
        self.modsFrame.pack(side="left")
        self.modHalfFrame.pack(side="left")
        self.columns.pack()
        self.calculate.pack()
    #end pack_Columns method

    def display_Stats(self):
        #level check
        self.level_Check()

        #modifier column text change
        self.strMod.config(text=self.get_Stat(self.strEntry.get())+"")
        self.conMod.config(text=self.get_Stat(self.conEntry.get())+"")
        self.dexMod.config(text=self.get_Stat(self.dexEntry.get())+"")
        self.intMod.config(text=self.get_Stat(self.intEntry.get())+"")
        self.wisMod.config(text=self.get_Stat(self.wisEntry.get())+"")
        self.chaMod.config(text=self.get_Stat(self.chaEntry.get())+"")

        #modifiers + half level column text change
        #
    #end display_Stats method

    def level_Check(self):  #checks if the level is valid
        try:
            lvlNum = int(self.lvlEntry.get()+"")
            self.lvlError.config(text="")
            self.lvlValid = True
        except ValueError:
            self.lvlError.config(text="not a valid input")
            self.lvlValid = False
    #end level_Check method

    def get_Stat(self, givenStat): 
        try:    #checks if the input is a number
            number = int(givenStat)
            modifier = (number - 10) // 2
            if (modifier > 0):
                return ("+" + str(modifier))
            else:
                return str(modifier)
        except ValueError:
            return "not a valid input"
    #end get_Stat method
main()  #start program

