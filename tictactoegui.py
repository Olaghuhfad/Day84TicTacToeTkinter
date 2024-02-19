import tkinter as tk
from tkinter import *
import random
from tictactoe import TicTacToe

class TicTacToeGUI:

    def __init__(self, window):
        self.window = window

        self.ttt_engine = TicTacToe()

        self.load_images()
        self.make_buttons()
        self.make_button_list()
        self.make_end_buttons()

    def on_click(self, button_pressed):

        check = self.ttt_engine.check_position_free(button_pressed)
        if check:
            self.ttt_engine.playPiece(pos=button_pressed, user="player")
            self.buttonlist[button_pressed - 1].config(image=self.button_X)
            self.buttonlist[button_pressed - 1].config(command=0)


        if self.ttt_engine.check_win() == "player":
            self.end_game("player")
            return

        curmoves = self.ttt_engine.get_number_of_moves()
        if curmoves == 9:
            self.end_game_tie()
            return

        new_cpu_move = random.randint(1,9)
        while not self.ttt_engine.check_position_free(new_cpu_move):
            new_cpu_move = random.randint(1,9)
        self.ttt_engine.playPiece(pos=new_cpu_move, user="cpu")
        self.buttonlist[new_cpu_move - 1].config(image=self.button_O)
        self.buttonlist[new_cpu_move - 1].config(command=0)

        if self.ttt_engine.check_win() == "cpu":
            self.end_game("cpu")
            return

    def end_game(self, winner):
        if winner == "player":
            self.win_button.grid(column=1, row=1)
        elif winner == "cpu":
            self.lose_button.grid(column=1, row=1)
        else:
            print("error")

    def end_game_tie(self):
        self.tie_button.grid(column=1, row=1)

    def restart_game(self):
        self.clear_end_buttons()
        self.refresh_buttons()
        self.ttt_engine.clear_positions()


    def load_images(self):
        self.black_button = PhotoImage(file="./images/BlackButtonPNG.png")
        self.button_X = PhotoImage(file="./images/ButtonXPNG.png")
        self.button_O = PhotoImage(file="./images/ButtonOPNG.png")

        self.win_img = PhotoImage(file="./images/GreenWinPNG.png")
        self.lose_img = PhotoImage(file="./images/RedLosePNG.png")
        self.tie_img = PhotoImage(file="./images/OrangeTiePNG.png")

    def make_buttons(self):
        self.button_one = Button(image=self.black_button, borderwidth=0, command=lambda: self.on_click(1))
        self.button_one.grid(column=0, row=2)

        self.button_two = Button(image=self.black_button, borderwidth=0, command=lambda: self.on_click(2))
        self.button_two.grid(column=1, row=2)

        self.button_three = Button(image=self.black_button, borderwidth=0, command=lambda: self.on_click(3))
        self.button_three.grid(column=2, row=2)

        self.button_four = Button(image=self.black_button, borderwidth=0, command=lambda: self.on_click(4))
        self.button_four.grid(column=0, row=1)

        self.button_five = Button(image=self.black_button, borderwidth=0, command=lambda: self.on_click(5))
        self.button_five.grid(column=1, row=1)

        self.button_six = Button(image=self.black_button, borderwidth=0, command=lambda: self.on_click(6))
        self.button_six.grid(column=2, row=1)

        self.button_seven = Button(image=self.black_button, borderwidth=0, command=lambda: self.on_click(7))
        self.button_seven.grid(column=0, row=0)

        self.button_eight = Button(image=self.black_button, borderwidth=0, command=lambda: self.on_click(8))
        self.button_eight.grid(column=1, row=0)

        self.button_nine = Button(image=self.black_button, borderwidth=0, command=lambda: self.on_click(9))
        self.button_nine.grid(column=2, row=0)

    def make_button_list(self):
        self.buttonlist = []
        self.buttonlist.append(self.button_one)
        self.buttonlist.append(self.button_two)
        self.buttonlist.append(self.button_three)
        self.buttonlist.append(self.button_four)
        self.buttonlist.append(self.button_five)
        self.buttonlist.append(self.button_six)
        self.buttonlist.append(self.button_seven)
        self.buttonlist.append(self.button_eight)
        self.buttonlist.append(self.button_nine)

    def make_end_buttons(self):
        self.win_button = Button(image=self.win_img, borderwidth=0, command=self.restart_game)
        self.lose_button = Button(image=self.lose_img, borderwidth=0, command=self.restart_game)
        self.tie_button = Button(image=self.tie_img, borderwidth=0, command=self.restart_game)

    def clear_end_buttons(self):
        self.win_button.grid_forget()
        self.lose_button.grid_forget()
        self.tie_button.grid_forget()

    def refresh_buttons(self):
        self.button_one.config(image=self.black_button, command=lambda: self.on_click(1))
        self.button_one.grid(column=0, row=2)
        self.button_two.config(image=self.black_button, command=lambda: self.on_click(2))
        self.button_two.grid(column=1, row=2)
        self.button_three.config(image=self.black_button, command=lambda: self.on_click(3))
        self.button_three.grid(column=2, row=2)
        self.button_four.config(image=self.black_button, command=lambda: self.on_click(4))
        self.button_four.grid(column=0, row=1)
        self.button_five.config(image=self.black_button, command=lambda: self.on_click(5))
        self.button_five.grid(column=1, row=1)
        self.button_six.config(image=self.black_button, command=lambda: self.on_click(6))
        self.button_six.grid(column=2, row=1)
        self.button_seven.config(image=self.black_button, command=lambda: self.on_click(7))
        self.button_seven.grid(column=0, row=0)
        self.button_eight.config(image=self.black_button, command=lambda: self.on_click(8))
        self.button_eight.grid(column=1, row=0)
        self.button_nine.config(image=self.black_button, command=lambda: self.on_click(9))
        self.button_nine.grid(column=2, row=0)
