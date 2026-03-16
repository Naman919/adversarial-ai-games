from games.othello import Othello
from agents.mcts_agent import MCTSAgent
from agents.minimax_agent import MinimaxAgent
from experiments.benchmark import run_benchmark

game = Othello()

ai1 = MCTSAgent(1)
ai2 = MinimaxAgent(3)

agents = {1: ai1, -1: ai2}

while not game.is_terminal():
    moves = game.get_legal_moves()
    
    if not moves:
        game.player *= -1
        continue

    agent = agents[game.player]
    move = agent.get_move(game)
    game.play(move)

run_benchmark(ai1, ai2, Othello, num_games=2)


