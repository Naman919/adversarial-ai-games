import random
from core.timer import Timer

class Node:

    def __init__(self, game, parent=None, move=None):

        self.game = game
        self.parent = parent
        self.move = move
        self.children = []

        self.visits = 0
        self.wins = 0


class MCTSAgent:

    def __init__(self, time_limit=1):
        self.time_limit = time_limit

    def get_move(self, game):

        root = Node(game)

        timer = Timer(self.time_limit)
        timer.begin()

        while not timer.expired():

            node = self.select(root)
            result = self.simulate(node.game)
            self.backpropagate(node, result)
            
        if not root.children:
            return random.choice(game.get_legal_moves())

        best_child = max(root.children, key=lambda c: c.visits)

        return best_child.move

    def select(self, node):

        while node.children:

            node = max(node.children,
                       key=lambda c: c.wins/(c.visits+1e-6))

        if not node.game.is_terminal():
            moves = node.game.get_legal_moves()
            if len(moves) == 0:
                g_pass=node.game.clone()
                g_pass.player *= -1
                child = Node(g_pass, node, move=None)
                node.children.append(child)
            else:
                for move in moves:
                    g = node.game.clone()
                    g.play(move)
                    child = Node(g, node, move)
                    node.children.append(child)

            node = random.choice(node.children)

        return node

    def simulate(self, game):

        g = game.clone()

        while not g.is_terminal():
            moves = g.get_legal_moves()
            if len(moves) == 0:
                g.player *= -1
                continue

            move = random.choice(moves)
            g.play(move)

        return g.evaluate()

    def backpropagate(self, node, result):

        while node:

            node.visits += 1
            node.wins += result
            node = node.parent
