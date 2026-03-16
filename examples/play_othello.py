import pygame
from games.othello import Othello
from agents.mcts_agent import MCTSAgent

# Constants
CELL_SIZE = 60
ROWS = COLS = 8
WIDTH = COLS * CELL_SIZE
HEIGHT = ROWS * CELL_SIZE + 50  
SIZE = (WIDTH, HEIGHT)

# Colors
GREEN = (0, 128, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)

# Initialize game and AI
game = Othello()
ai = MCTSAgent(time_limit=3)  

pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Othello: Player vs AI")
font = pygame.font.SysFont("monospace", 30)

def draw_board(board, valid_moves=None):
    screen.fill(GREEN)
    valid_moves = valid_moves or []
    for r in range(ROWS):
        for c in range(COLS):
            rect = pygame.Rect(c*CELL_SIZE, r*CELL_SIZE+50, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, GREEN, rect)
            pygame.draw.rect(screen, BLACK, rect, 1)
            if board[r][c] == 1:
                pygame.draw.circle(screen, BLACK, rect.center, CELL_SIZE//2 - 5)
            elif board[r][c] == -1:
                pygame.draw.circle(screen, WHITE, rect.center, CELL_SIZE//2 - 5)
            elif (r, c) in valid_moves:
                pygame.draw.circle(screen, GRAY, rect.center, 5)  # hint for valid moves for human
    pygame.display.update()

def show_message(text, color=WHITE):
    pygame.draw.rect(screen, GREEN, (0, 0, WIDTH, 50))
    label = font.render(text, True, color)
    screen.blit(label, (10, 10))
    pygame.display.update()
valid_moves=game.get_legal_moves() if game.player == 1 else []
draw_board(game.board,valid_moves)
show_message("Player (Black) turn")

game_over = False
while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if game.player == 1 and event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            row = (y - 50) // CELL_SIZE
            col = x // CELL_SIZE

            valid_moves = game.get_legal_moves()
            if (row, col) not in valid_moves:
                show_message("Invalid move!", WHITE)
                continue

            game.play((row, col))
            draw_board(game.board, [])#game.get_legal_moves())

    if not game_over and game.player == -1:
        show_message("AI is thinking...")
        valid_moves = game.get_legal_moves()
        if len(valid_moves) == 0:
            game.player *= -1
            show_message("AI has no moves! Turn passed.", WHITE)
            pygame.time.delay(1000)
        else:
            move = ai.get_move(game)
            game.play(move)
        draw_board(game.board,game.get_legal_moves())
            #pygame.time.delay(500)

        # Check for terminal
        if game.is_terminal():
            black_count, white_count = game.count_pieces()
            if black_count > white_count:
                show_message(f"Player (Black) wins! {black_count} : {white_count}", BLACK)
            elif white_count > black_count:
                show_message(f"AI (White) wins! {white_count} : {black_count}", WHITE)
            else:
                show_message(f"Draw! {black_count} : {white_count}", (128, 128, 128))
            game_over = True

pygame.time.wait(4000)
