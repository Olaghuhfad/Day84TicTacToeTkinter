import tkinter as tk
from tkinter import *
from tictactoe import TicTacToe
from tictactoegui import TicTacToeGUI


FONT = ("Arial", 24, "normal")

root = Tk()
root.title("TicTacToe")
root.minsize(width=600, height=800)

GUI = TicTacToeGUI(root)

root.mainloop()