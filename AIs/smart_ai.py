import time
from AIs.random_ai import random_ai
from engine import render, make_move



def finds_winning_moves_ai(board: list[list[int]], curr_player):
    opponent = 'X' if curr_player == 'O' else 'O'

    """MOVE TO WIN"""

    for i in range(3):
        row = board[i]
        if opponent not in row and row.count(curr_player) == 2:
            j = row.index(None)
            return j, i
    

    for i in range(3):
        col = [board[j][i] for j in range(3)]

        if opponent not in col and col.count(curr_player) == 2:
            j = col.index(None)
            return i, j
        

    main_diag = [board[i][i] for i in range(3)]
    if opponent not in main_diag and main_diag.count(curr_player) == 2:
        idx = main_diag.index(None)
        return idx, idx
    

    secondary_diag = [board[i][2-i] for i in range(3)]
    if opponent not in secondary_diag and secondary_diag.count(curr_player) == 2:
        idx = secondary_diag.index(None)
        return 2 - idx, idx
    

    """BLOCK A LOSS"""
    
    for i in range(3):
        row = board[i]
        if curr_player not in row and row.count(opponent) == 2:
            j = row.index(None)
            return j, i
    

    for i in range(3):
        col = [board[j][i] for j in range(3)]

        if curr_player not in col and col.count(opponent) == 2:
            j = col.index(None)
            return i, j
        

    main_diag = [board[i][i] for i in range(3)]
    if curr_player not in main_diag and main_diag.count(opponent) == 2:
        idx = main_diag.index(None)
        return idx, idx
    

    secondary_diag = [board[i][2-i] for i in range(3)]
    if curr_player not in secondary_diag and secondary_diag.count(opponent) == 2:
        idx = secondary_diag.index(None)
        return 2 - idx, idx
    
    
    return random_ai(board, curr_player)


def smart_ai_move(board, curr_player):
    print('---SMART AI ARE THINKING---')
    time.sleep(1)
    move = finds_winning_moves_ai(board, curr_player)
    board = make_move(board, move, curr_player)
    render(board)

    return board