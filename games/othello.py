import numpy as np

class Othello:
    SIZE = 8

    def __init__(self):
        self.board = np.zeros((8,8))
        self.board[3][3] = -1
        self.board[3][4] = 1
        self.board[4][3] = 1
        self.board[4][4] = -1
        self.player = 1  # 1 = Black (Player), -1 = White (AI)

    def clone(self):
        g = Othello()
        g.board = self.board.copy()
        g.player = self.player
        return g

    def get_legal_moves(self):
        moves = set()
        directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        for r in range(8):
            for c in range(8):
                if self.board[r][c] != 0:
                    continue
                for dr,dc in directions:
                    rr, cc = r+dr, c+dc
                    found_opponent = False
                    while 0 <= rr < 8 and 0 <= cc < 8:
                        if self.board[rr][cc] == -self.player:
                            found_opponent = True
                        elif self.board[rr][cc] == self.player and found_opponent:
                            moves.add((r,c))
                            break
                        else:
                            break
                        rr += dr
                        cc += dc
        return list(moves)

    def get_legal_moves_opponent(self):
        self.player *= -1
        moves = self.get_legal_moves()
        self.player *= -1
        return moves

    def count_corners(self, player):
        corners = [(0,0),(0,7),(7,0),(7,7)]
        return sum(1 for r,c in corners if self.board[r,c] == player)

    def play(self, move):
        r,c = move
        self.board[r][c] = self.player
        directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        for dr,dc in directions:
            rr, cc = r+dr, c+dc
            captured = []
            while 0 <= rr < 8 and 0 <= cc < 8:
                if self.board[rr][cc] == -self.player:
                    captured.append((rr,cc))
                elif self.board[rr][cc] == self.player:
                    for cr,ccr in captured:
                        self.board[cr][ccr] = self.player
                    break
                else:
                    break
                rr += dr
                cc += dc
        self.player *= -1

    def is_terminal(self):
        if len(self.get_legal_moves()) > 0:
            return False
        self.player *= -1
        opponent_moves = len(self.get_legal_moves())
        self.player *= -1
        return opponent_moves == 0

    def count_pieces(self):
        black_count = (self.board == 1).sum()
        white_count = (self.board == -1).sum()
        return black_count, white_count

    def evaluate(self, player=None):
        if player is None:
            player = self.player * -1  
        black_count, white_count = self.count_pieces()
        disc_diff = (black_count - white_count) if player == 1 else (white_count - black_count)
        mobility = len(self.get_legal_moves()) - len(self.get_legal_moves_opponent())
        corners = self.count_corners(player) - self.count_corners(-player)
        return (disc_diff * 1) + (mobility * 10) + (corners * 100)
