import tkinter as tk
from tkinter import *
from tictactoe import TicTacToe
from tictactoegui import TicTacToeGUI


FONT = ("Arial", 24, "normal")

root = Tk()
root.title("TicTacToe")
root.minsize(width=600, height=800)

def on_closing():
    GUI.save_streak()


GUI = TicTacToeGUI(root)

# root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()