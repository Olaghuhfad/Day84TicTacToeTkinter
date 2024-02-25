import tkinter as tk
from tictactoegui import TicTacToeGUI


FONT = ("Arial", 24, "normal")

root = tk.Tk()
root.title("TicTacToe")
root.minsize(width=600, height=800)

def on_closing():
    GUI.save_streak()
    root.destroy()


GUI = TicTacToeGUI(root)

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()