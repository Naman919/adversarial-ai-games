import math

class MinimaxAgent:

    def __init__(self, depth=5):
        self.depth = depth

    def get_move(self, game):
        legal_moves = self._order_moves(game)
        if not legal_moves:
            return None

        best_score = -math.inf
        best_move = None

        alpha = -math.inf
        beta = math.inf
        legal_moves = self._order_moves(game)
        if not legal_moves:
            return None

        for move in legal_moves:
            new_game = game.clone()
            new_game.play(move)
            score = self.minimax(new_game, self.depth-1,alpha, beta, False)
            if score > best_score:
                best_score = score
                best_move = move
            alpha = max(alpha, best_score)
        return best_move

    def minimax(self, game, depth, alpha, beta, maximizing):
        if depth == 0 or game.is_terminal():
            return game.evaluate()
        if maximizing:
            best = -math.inf
            for move in self._order_moves(game):
                new_game = game.clone()
                new_game.play(move)
                best = max(best,
                           self.minimax(new_game, depth-1, alpha, beta, False))
                alpha = max(alpha, best)
                if beta <= alpha:
                    break
            return best

        else:
            best = math.inf
            for move in self._order_moves(game):
                new_game = game.clone()
                new_game.play(move)
                best = min(best,
                           self.minimax(new_game, depth-1, alpha, beta, True))
                beta=min(beta,best)
                if beta <= alpha:
                    break
            return best

    def _order_moves(self, game):
        moves = game.get_legal_moves()
        if not moves:
            return []
        if isinstance(moves[0], int):
            center = 3
            return sorted(moves, key=lambda m: abs(m - center))
        else:
            def othello_priority(move):
                r, c = move
                if r in [0, 7] and c in [0, 7]: return 0
                if r in [0, 7] or c in [0, 7]: return 1
                return 2     
            
            return sorted(moves, key=othello_priority)

            
