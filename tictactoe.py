
class TicTacToe:

    def __init__(self):

        self.board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

        self.playerPositions = []
        self.cpuPositions = []


    def playPiece(self, pos, user):
        if user == "player":
            self.playerPositions.append(pos)
            self.board[pos-1] = "X"
        elif user == "cpu":
            self.cpuPositions.append(pos)
            self.board[pos-1] = "O"
        else:
            print("Error in play piece, not valid user.")

    def check_position_free(self, pos):
        if pos in self.playerPositions or pos in self.cpuPositions:
            return False
        else:
            return True

    def check_win(self):
        winning_combos = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
        for sublist in winning_combos:
            result = all(item in self.playerPositions for item in sublist)
            if result:
                return "player"
            cpu_result = all(item in self.cpuPositions for item in sublist)
            if cpu_result:
                return "cpu"
        return "false"

    def get_player_positions(self):
        return self.playerPositions

    def get_number_of_moves(self):
        return len(self.playerPositions) + len(self.cpuPositions)

    def check_tie(self):
        moves = self.get_number_of_moves()
        if moves == 9:
            return True
        else:
            return False

    def clear_positions(self):
        del self.playerPositions[:]
        del self.cpuPositions[:]