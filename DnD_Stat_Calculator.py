#Thomas Boehme
#started: 3/14/2017
#last edited: 3/14/2017
#finished: 3/14/2017
#Quick stat calculator for D&D

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
        self.columns = tkinter.Frame(self.mainWindow) #holds the columns
        self.statsFrame = tkinter.Frame(self.columns)
        self.scoreFrame = tkinter.Frame(self.columns)

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

        #calculate button
        self.calculate = tkinter.Button(self.mainWindow, text="Calculate",\
                                        command= self.display_Stats)
        self.pack_Columns() #packs the window
        
        tkinter.mainloop()
    #end __init__ method
    
    def pack_Columns(self):
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
        
        self.statsFrame.pack(side="left")
        self.scoreFrame.pack(side="right")
        self.columns.pack()
        self.calculate.pack()
    #end pack_Columns method

    def display_Stats(self):
        statsString = "Stats\t\tScore\t\tModifier\n"\
                      "Stength\t\t"+self.strEntry.get()+"\t\t"+\
                      self.get_Stat(self.strEntry.get()) + "\n" +\
                      "Constitution\t"+self.conEntry.get()+"\t\t"+\
                      self.get_Stat(self.conEntry.get()) + "\n" + \
                      "Dexterity\t\t"+self.dexEntry.get()+"\t\t"+\
                      self.get_Stat(self.dexEntry.get()) + "\n" + \
                      "Intelligence\t"+self.intEntry.get()+"\t\t"+\
                      self.get_Stat(self.intEntry.get()) + "\n" + \
                      "Wisdom\t\t"+self.wisEntry.get()+"\t\t"+\
                      self.get_Stat(self.wisEntry.get()) + "\n" + \
                      "Charisma\t\t"+self.chaEntry.get()+"\t\t"+\
                      self.get_Stat(self.chaEntry.get())
                      

        tkinter.messagebox.showinfo("Response", statsString)
    #end display_Stats method

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
