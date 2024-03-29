import tkinter as tk
from tkinter import *
import random
from tictactoe import TicTacToe
from functools import partial

FONT = ("Courier", 24, "normal")

class TicTacToeGUI:

    def __init__(self, window):
        self.window = window

        self.ttt_engine = TicTacToe()

        self.player_score = 0
        self.cpu_score = 0
        self.button_list = []
        self.old_streak = self.load_streak()
        self.current_streak = 0
        self.previous_result = "win"

        self.load_images()
        self.load_gif()
        self.make_buttons()
        self.make_end_buttons()

    def on_click(self, button_pressed):
        '''when button pressed it makes the player move and cpu move after
            takes in which button pressed and uses a list to find that button'''

        # this check may not be needed because buttons turn off when unavailable as moves
        check = self.ttt_engine.check_position_free(button_pressed)
        if check:
            self.ttt_engine.playPiece(pos=button_pressed, user="player")
            self.wiggle_button(button_pressed, 0, user="player")
            # disabling a button made it change colour, so remove command instead
            self.button_list[button_pressed - 1].config(command=0)

        # need to check if the move made the player win, so then cpu does not make a move
        if self.ttt_engine.check_win() == "player":
            # self.end_game("player")
            # after gif was added the game was ending too fast, so added a delay
            self.window.after(800, self.end_game, "player")
            return

        # checks if the player move created a tie, so the cpu does not make a move
        curmoves = self.ttt_engine.get_number_of_moves()
        if curmoves == 9:
            # self.end_game_tie()
            # after gif was added the game was ending too fast, so added a delay
            self.window.after(800, self.end_game_tie)
            return



        # cpu currently only able to make random moves
        new_cpu_move = random.randint(1,9)
        # because cpu is random it may pick a move that is already taken
        while not self.ttt_engine.check_position_free(new_cpu_move):
            new_cpu_move = random.randint(1,9)
        self.ttt_engine.playPiece(pos=new_cpu_move, user="cpu")
        self.wiggle_button(new_cpu_move, 0, user="cpu")

        self.button_list[new_cpu_move - 1].config(command=0)

        # check if cpu has won from the new move, so game can end
        if self.ttt_engine.check_win() == "cpu":
            # self.end_game("cpu")
            self.window.after(800, self.end_game, "cpu")
            return



    def end_game(self, winner):
        '''ends game when someone wins, adds to score, brings up restart button and changes top display colour'''
        # buttons were still clickable by player
        self.disable_buttons()
        if winner == "player":
            self.player_score += 1
            # grid the win button so it can be seen and clicked
            self.win_button.grid(column=1, row=2)
            # change colour of top display to be same colour as win button
            self.display.itemconfig(self.display_img, image=self.top_display_win_img)
            self.streak_check("win")
        elif winner == "cpu":
            self.cpu_score += 1
            self.lose_button.grid(column=1, row=2)
            self.display.itemconfig(self.display_img, image=self.top_display_lose_img)
            self.streak_check("lose")
        else:
            print("error")

    def end_game_tie(self):
        '''if the game ends in a tie, bring up restart button and change top display colour'''
        self.disable_buttons()
        self.tie_button.grid(column=1, row=2)
        self.display.itemconfig(self.display_img, image=self.top_display_tie_img)
        self.streak_check("tie")

    def restart_game(self):
        '''how to restart the game'''
        self.clear_end_buttons()
        self.refresh_buttons()
        self.ttt_engine.restart()


    def streak_check(self, result):
        '''called after a game is over, adds to streak if player wins, breaks if player loses'''
        if result == "win":
            self.current_streak += 1
        elif result == "lose" or result == "tie":
            self.current_streak = 0
        # result is now previous result
        self.previous_result = result
        if self.current_streak > self.old_streak:
            self.old_streak = self.current_streak


    def make_end_buttons(self):
        '''makes the buttons for when the game ends, that restart the game when pressed'''
        self.win_button = Button(image=self.win_img, borderwidth=0, command=self.restart_game)
        self.lose_button = Button(image=self.lose_img, borderwidth=0, command=self.restart_game)
        self.tie_button = Button(image=self.tie_img, borderwidth=0, command=self.restart_game)

    def clear_end_buttons(self):
        '''removes any restart buttons used when game is restarted'''
        self.win_button.grid_forget()
        self.lose_button.grid_forget()
        self.tie_button.grid_forget()

    def disable_buttons(self):
        '''make it so player can no longer make moves'''
        # the buttons are still clickable but don't do anything
        for button in self.button_list:
            button.config(command=0)

    def make_buttons(self):
        '''creates all the buttons and the top display'''
        # num keeps track of which number is passed from the button being pressed
        num = 0
        # double loop like this to create grid locations
        for row in range(1, 4):
            for col in range(3):
                num += 1
                temp_button = Button(image=self.black_button, borderwidth=0, command=partial(self.on_click, num))
                temp_button.grid(column=col, row=row)
                self.button_list.append(temp_button)

        self.display = Canvas(width=600, height=200, highlightthickness=0)
        self.display_img = self.display.create_image((300,100), image=self.top_display_img)
        self.display_player_score = self.display.create_text(110, 50, text=f"Player: {self.player_score}", fill="white", font=FONT)
        self.display_cpu_score = self.display.create_text(510, 50, text=f"CPU: {self.cpu_score}", fill="white", font=FONT)
        self.display_current_streak = self.display.create_text(110, 140, text=f"Current\nstreak: {self.current_streak}", font=FONT, fill="white")
        self.display_longest_streak = self.display.create_text(500, 140, text=f"Best\nstreak: {self.old_streak}", fill="white", font=FONT)
        self.display.grid(column=0, columnspan=3, row=0)

    def refresh_buttons(self):
        ''' for game restart brings back all the buttons with commands restored and restores the top display'''
        num = 0
        for row in range(1, 4):
            for col in range(3):
                num += 1
                self.button_list[num - 1].configure(image=self.black_button)
                self.button_list[num - 1].configure(command=partial(self.on_click, num))
                self.button_list[num - 1].grid(column=col, row=row)

        self.display.itemconfig(self.display_img, image=self.top_display_img)
        self.display.itemconfig(self.display_player_score, text=f"Player: {self.player_score}")
        self.display.itemconfig(self.display_cpu_score, text=f"CPU: {self.cpu_score}")
        self.display.itemconfig(self.display_current_streak, text=f"Current\nstreak: {self.current_streak}")
        if self.current_streak > self.old_streak:
            self.display.itemconfig(self.display_longest_streak, text=f"Best\nstreak: {self.current_streak}")
        else:
            self.display.itemconfig(self.display_longest_streak, text=f"Best\nstreak: {self.old_streak}")
        self.display.grid(column=0, columnspan=3, row=0)

    def load_images(self):
        '''loads images all in one place'''
        self.black_button = PhotoImage(file="./images/BlackButtonPNG.png")
        self.button_X = PhotoImage(file="./images/ButtonXPNG.png")
        self.button_O = PhotoImage(file="./images/ButtonOPNG.png")

        self.win_img = PhotoImage(file="./images/GreenWinPNG.png")
        self.lose_img = PhotoImage(file="./images/RedLosePNG.png")
        self.tie_img = PhotoImage(file="./images/OrangeTiePNG.png")

        self.top_display_img = PhotoImage(file="./images/TopDisplayPNG.png")
        self.top_display_win_img = PhotoImage(file="./images/TopDisplayWinPNG.png")
        self.top_display_lose_img = PhotoImage(file="./images/TopDisplayLosePNG.png")
        self.top_display_tie_img = PhotoImage(file="./images/TopDisplayTiePNG.png")


    def load_streak(self):
        '''load in previous longest streak from file'''
        with open(mode="r", file="./data/streakdata.txt") as file:
            streak = int(file.readline())
        return streak

    def save_streak(self):
        '''called when window closed, saves the new top streak if player beats old streak'''
        saved_streak = self.load_streak()
        if self.old_streak > saved_streak:

            with open(mode="w", file="./data/streakdata.txt") as file:
                file.write(str(self.current_streak))

    def load_gif(self):
        '''loads the gif'''
        # the gif needs to be loaded into a list of images
        self.frame_count = 13
        self.frames = [PhotoImage(file="./images/gif/shrunkwigglegif.gif", format="gif -index %i" %(i)) for i in range(self.frame_count)]

    def wiggle_button(self, button_pressed, ind, user):
        '''a function for running the gif'''
        # was having issues with the wrong image being displayed at the end of the gif
        # so split it like this
        if user == "player":
            self.wiggle_x(self.button_list[button_pressed - 1], 0)
        else:
            self.window.after(500, self.wiggle_o, self.button_list[button_pressed - 1], 0)

    def wiggle_x(self, widget, ind):
        '''displays the gif then changes the button to player X'''
        frame = self.frames[ind]
        ind += 1
        widget.configure(image=frame)
        if ind == self.frame_count:
            widget.configure(image=self.button_X)
            return
        self.window.after(30, self.wiggle_x, widget, ind)

    def wiggle_o(self, widget, ind):
        '''displays the gif then changes the button to cpu O'''
        frame = self.frames[ind]
        ind += 1
        widget.configure(image=frame)
        if ind == self.frame_count:
            widget.configure(image=self.button_O)
            return
        self.window.after(30, self.wiggle_o, widget, ind)