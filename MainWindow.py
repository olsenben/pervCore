import tkinter as tk
from tkinter import ttk
from tkinterdnd2 import TkinterDnD, DND_FILES #make sure to pip install tkinterdnd2-universal
import pygame
import os
from pads import Pad


class mainWindow(TkinterDnD.Tk): 
    #Let MainWindow be the child class of TkinterDnD.Tk allows us to copy functionality of TkinterDnD.Tk and define our own additonal stuff - kj
    def __init__(self, title="Pervcore", window_size="800x600"): #allows us to recall this function and but set these as parameters for now - kj
        super().__init__() #initialize parent class - kj

        # Set window title and size dynamically
        self.title(title)
        self.geometry(window_size)

        
        # Mframe for waveform editors
        self.display_frame = ttk.Frame(self, height=200)
        self.display_frame.pack(fill=tk.X)

        #frame for pads
        self.pads_frame = ttk.Frame(self)
        self.pads_frame.pack()

        # create 4x4 grid for pads
        self.pads = []
        for i in range(4):
            for j in range(4):
                pad_id = i * 4 + j + 1
                pad = Pad(self.pads_frame, self, pad_id)
                pad.grid(row=i, column=j,padx=10, pady=10)
                self.pads.append(pad)


        
   


    

if __name__ == "__main__":
    pervcore = mainWindow()
    pervcore.mainloop()
