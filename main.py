import tkinter as tk
from tictactoegui import TicTacToeGUI


FONT = ("Arial", 24, "normal")

root = tk.Tk()
root.title("TicTacToe")
root.minsize(width=600, height=800)


def on_closing():
    '''call save streak on close'''
    GUI.save_streak()
    root.destroy()


GUI = TicTacToeGUI(root)

# how to bind a function to closing the program window
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()