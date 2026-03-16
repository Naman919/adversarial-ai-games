import pygame
from games.connect4 import Connect4
from agents.mcts_agent import MCTSAgent

# Constants
CELL_SIZE = 100
COLS = 7
ROWS = 6
RADIUS = CELL_SIZE // 2 - 5
WIDTH = COLS * CELL_SIZE
HEIGHT = ROWS * CELL_SIZE
SIZE = (WIDTH, HEIGHT)

# Colors
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

# Initialize game and AI
game = Connect4()
ai = MCTSAgent(time_limit=3)

pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Connect4: Player vs AI")

font = pygame.font.SysFont("monospace", 40)

def draw_board(board):
    for r in range(ROWS):
        for c in range(COLS):
            pygame.draw.rect(screen, BLUE, (c*CELL_SIZE, r*CELL_SIZE, CELL_SIZE, CELL_SIZE))
            color = BLACK
            if board[r][c] == 1:
                color = RED
            elif board[r][c] == -1:
                color = YELLOW
            pygame.draw.circle(screen, color, (c*CELL_SIZE+RADIUS+5, r*CELL_SIZE+RADIUS+5), RADIUS)
    pygame.display.update()

def show_message(text, color=WHITE):
    pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, 50))
    label = font.render(text, True, color)
    screen.blit(label, (10, 5))
    pygame.display.update()

draw_board(game.board)
game_over = False
while not game_over:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if game.player == 1 and event.type == pygame.MOUSEBUTTONDOWN:

            x = event.pos[0]
            col = x // CELL_SIZE

            if col not in game.get_legal_moves():
                print("Invalid move! Choose another column.")
                continue

            game.play(col)
            draw_board(game.board)

        elif game.player == -1:
            # AI move
            move = ai.get_move(game)
            game.play(move)
            draw_board(game.board)
        winner = game.check_winner()
        if winner == 1:
            show_message("Player 1 (Red) wins!",RED)
            game_over = True
        elif winner == -1:
            show_message("AI (Yellow) wins!",YELLOW)
            game_over = True
        elif game.is_terminal():
            show_message("Draw!",WHITE)
            game_over = True


pygame.time.wait(4000)
