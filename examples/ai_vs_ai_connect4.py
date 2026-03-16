from games.connect4 import Connect4
from agents.mcts_agent import MCTSAgent
from agents.minimax_agent import MinimaxAgent
from experiments.benchmark import run_benchmark

agentA = MCTSAgent(time_limit=0.5)
agentB = MinimaxAgent(depth=5)

run_benchmark(agentA, agentB, Connect4, num_games=500)
