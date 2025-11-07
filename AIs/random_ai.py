import time
import random
from engine import render, make_move



def random_ai(board, curr_player: str) -> tuple[int, int]:
    legal_moves = []

    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                legal_moves.append((j, i))

    return random.choice(legal_moves)


def random_ai_move(board, curr_player):
    print('---RANDOM AI ARE CHOOSING---')
    time.sleep(1)
    move = random_ai(board, curr_player)

    board = make_move(board, move, curr_player)
    render(board)

    return board
