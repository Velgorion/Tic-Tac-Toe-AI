import time
from engine import get_legal_moves, make_move, render, get_winner, is_draw, \
evaluate_position_heuristic, _board_to_key

def minimax_ai_move(board, curr_player):
    best_score = None
    best_move = None

    legal_moves = get_legal_moves(board)

    print('---MINIMAX AI WILL DESTROY YOU---')
    time.sleep(1)

    for move in legal_moves:
        new_board = make_move(board, move, curr_player)

        opp = 'O' if curr_player == 'X' else 'X'
        score = _minimax_score(new_board, opp, curr_player, float('-inf'), float('inf'))

        if score == 10:
            best_move = move
            break

        if best_score is None or score > best_score:
            best_score = score
            best_move = move
    
    board = make_move(board, best_move, curr_player)
    render(board)

    return board


cache = {}

def _minimax_score(board, player_to_move, player_to_optimize,
                   alpha = float('-inf'),
                   beta = float('inf')):

    cur_key = (_board_to_key(board), player_to_move, player_to_optimize)
    if cur_key in cache:
        return cache[cur_key]
    
    winner = get_winner(board)
    if winner is not None:
        if winner == player_to_optimize:
            value = 10
            cache[cur_key] = value
            return value
        else:
            value = -10
            cache[cur_key] = value
            return value
    
    if is_draw(board):
        value = evaluate_position_heuristic(board, player_to_optimize)
        cache[cur_key] = value
        return value
    
    
    if player_to_move == player_to_optimize:
        best_score = float('-inf')
        
        for move in get_legal_moves(board):
            new_board = make_move(board, move, player_to_move)
            opp = 'O' if player_to_move == 'X' else 'X'

            child_key = (_board_to_key(new_board), opp, player_to_optimize)

            if child_key in cache:
                score = cache[child_key]
            else:
                score = _minimax_score(new_board, opp, player_to_optimize, alpha, beta)
                cache[child_key] = score

            if score > best_score:
                best_score = score
            if best_score > alpha:
                alpha = best_score
            
            if alpha >= beta:
                break
        
        cache[cur_key] = best_score
        return best_score
    
    else:
        best_score = float('inf')
        
        for move in get_legal_moves(board):
            new_board = make_move(board, move, player_to_move)
            opp = 'O' if player_to_move == 'X' else 'X'

            child_key = (_board_to_key(new_board), opp, player_to_optimize)

            if child_key in cache:
                score = cache[child_key]
            else:
                score = _minimax_score(new_board, opp, player_to_optimize, alpha, beta)
                cache[child_key] = score

            if score < best_score:
                best_score = score
            if best_score < beta:
                beta = best_score
            
            if beta <= alpha:
                break
        
        cache[cur_key] = best_score
        return best_score
