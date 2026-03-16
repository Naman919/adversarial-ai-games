import numpy as np

class Connect4:

    ROWS = 6
    COLS = 7

    def __init__(self):

        self.board = np.zeros((self.ROWS, self.COLS))
        self.player = 1

    def clone(self):

        g = Connect4()
        g.board = self.board.copy()
        g.player = self.player
        return g

    def get_legal_moves(self):

        return [c for c in range(self.COLS)
                if self.board[0][c] == 0]

    def play(self, col):

        for r in reversed(range(self.ROWS)):

            if self.board[r][col] == 0:
                self.board[r][col] = self.player
                break

        self.player *= -1

    def is_terminal(self):

        return self.check_winner() != 0 or len(self.get_legal_moves()) == 0
    
    def check_winner(self):
        for r in range(self.ROWS):
            for c in range(self.COLS - 3):
                line = self.board[r, c:c+4]
                if np.all(line == 1):
                    return 1 
                elif np.all(line == -1):
                    return -1
                
        for c in range(self.COLS):
            for r in range(self.ROWS - 3):
                line = self.board[r:r+4, c]
                if np.all(line == 1):
                    return 1
                elif np.all(line == -1):
                    return -1
                
        for r in range(self.ROWS):
            for c in range(self.COLS-3):
                line =  [self.board[r-i][c+i] for i in range(4)]
                if all(x == 1 for x in line):
                    return 1 
                elif all(x == -1 for x in line):
                    return -1
                    

        for r in range(self.ROWS - 3):
            for c in range(self.COLS - 3):
                line = [self.board[r+i][c+i] for i in range(4)]
                if all(x == 1 for x in line):
                    return 1
                elif all(x == -1 for x in line):
                    return -1
        return 0  



    def evaluate(self, player=None):
        if player is None:
            player=self.player * -1
        def score_line(line, player):
            opponent = -player
            if np.count_nonzero(line == player) == 3 and np.count_nonzero(line == 0) == 1:
                return 100 
            elif np.count_nonzero(line == opponent) == 3 and np.count_nonzero(line == 0) == 1:
                return -150 
            else:
                return 0
        total_score = 0
        
        for r in range(self.ROWS):
            for c in range(self.COLS - 3):
                line = self.board[r, c:c+4]
                total_score += score_line(line, player)
                
        for c in range(self.COLS):
            for r in range(self.ROWS - 3):
                line = self.board[r:r+4, c]
                total_score += score_line(line, player)

        for r in range(self.ROWS - 3):
            for c in range(self.COLS - 3):
                line = [self.board[r+i][c+i] for i in range(4)]
                total_score += score_line(line, player)

        for r in range(3, self.ROWS):
            for c in range(self.COLS - 3):
                line = [self.board[r-i][c+i] for i in range(4)]
                total_score += score_line(line, player)

        return total_score



