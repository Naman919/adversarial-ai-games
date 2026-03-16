def play_game(agentA, agentB, GameClass):
    game = GameClass()
    agents = {1: agentA, -1: agentB}
    
    while not game.is_terminal():
        moves = game.get_legal_moves()
        if not moves:
            game.player *= -1
            continue
        agent = agents[game.player]
        move = agent.get_move(game)
        if move is not None:
            game.play(move)
        else:
            game.player *= -1
    if hasattr(game, 'check_winner'):
        winner = game.check_winner()
        return winner

    score = game.evaluate()

    if score > 0:
        return 1
    elif score < 0:
        return -1
    else:
        return 0


def run_benchmark(agentA, agentB, GameClass, num_games=10):
    results = {"A_wins": 0, "B_wins": 0, "draws": 0}

    for i in range(num_games):
        winner = play_game(agentA, agentB, GameClass)
        if winner == 1:
            results["A_wins"] += 1
        elif winner == -1:
            results["B_wins"] += 1
        else:
            results["draws"] += 1

    print(f"Benchmark Results ({num_games} games):")
    print(f"Agent A wins: {results['A_wins']}")
    print(f"Agent B wins: {results['B_wins']}")
    print(f"Draws: {results['draws']}")
    return results
