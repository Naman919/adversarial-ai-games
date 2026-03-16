from core.timer import Timer
from agents.minimax_agent import MinimaxAgent

class IterativeDeepeningAgent:

    def __init__(self, time_limit=1):
        self.time_limit = time_limit

    def get_move(self, game):

        timer = Timer(self.time_limit)
        timer.begin()

        depth = 1
        best_move = None

        while not timer.expired():

            agent = MinimaxAgent(depth)
            move = agent.get_move(game)

            if move is not None:
                best_move = move

            depth += 1

        return best_move
