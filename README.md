# Adversarial AI Games

AI agents for turn-based board games like **Connect 4** and **Othello**, implemented in Python. This project demonstrates adversarial AI techniques including **Minimax with Alpha-Beta pruning** and **Monte Carlo Tree Search (MCTS)** with **Pygame visualizations**.

## Features

- **Player vs AI** and **AI vs AI** modes  
- **Connect 4** and **Othello** implemented with complete rules  
- Dynamic **AI evaluation functions** (disc difference, mobility, corners)  
- **Valid move hints** for human players  
- Handles **pass turns** automatically in Othello  
- Modular code: easy to add more games or AI agents  

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Naman919/adversarial-ai-games.git
cd adversarial-ai-games
````

2. Create a virtual environment :

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

* **Play Connect 4:**

```bash
python examples/play_connect4.py
```

* **Play Othello:**

```bash
python examples/play_othello.py
```

* **AI vs AI** matches:

```bash
python examples/ai_vs_ai_connect4.py
python examples/ai_vs_ai_othello.py
```

## Folder Structure

```
adversarial-ai-games/
│
├── agents/                             # AI agents
│   ├── __init__.py
|   ├── iterative_deepening_agent.py    # Iterative Deepening Minimax AI
|   ├── random_agent.py                 # Random move AI (for testing/baseline)
│   ├── mcts_agent.py                   # Monte Carlo Tree Search AI
│   └── minimax_agent.py                # Minimax + Alpha-Beta AI
│
├── games/                              # Game logic
│   ├── __init__.py
│   ├── connect4.py                     # Connect 4 game implementation
│   └── othello.py                      # Othello game implementation
│
├── examples/                           # Playable scripts / demos
│   ├── __init__.py
│   ├── play_connect4.py                # Player vs AI Connect 4
│   ├── play_othello.py                 # Player vs AI Othello
│   ├── ai_vs_ai_connect4.py            # AI vs AI Connect 4
│   └── ai_vs_ai_othello.py             # AI vs AI Othello
│
├── core/                 
│   ├── __init__.py
│   ├── timer.py
│   └── transposition_table.py           
│
├── .gitignore            
├── README.md              
└── requirements.txt      
```

## Tech Stack

* Python 3.10+
* NumPy
* Pygame

## Contributing

Contributions are welcome! You can add new games, AI agents, or improve evaluation heuristics.

## License

MIT License

```

