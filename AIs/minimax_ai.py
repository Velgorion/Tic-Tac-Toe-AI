import time
from engine import get_legal_moves, make_move, render, get_winner, is_draw, evaluate_position_heuristic



def minimax_ai_move(board, player):
    best_score = None
    best_move = None

    print('---MINIMAX AI WILL DESTROY YOU---')
    time.sleep(1)
    legal_moves = get_legal_moves(board)

    for move in legal_moves:
        new_board = make_move(board, move, player)

        opp = 'X' if player == 'O' else 'O'

        score = _minimax_score(new_board, opp, player)

        if score == 10:
            best_move = move
            break
        
        if best_score is None or score > best_score:
            best_score = score
            best_move = move

    
    board = make_move(board, best_move, player)
    render(board)

    return board



cache = {}

def _minimax_score(board, player_to_move, player_to_optimize):

    winner = get_winner(board)
    if winner is not None:
        if winner == player_to_optimize:
            return 10
        else:
            return -10
    
    if is_draw(board):
        return evaluate_position_heuristic(board, player_to_optimize)
    
    legal_moves = get_legal_moves(board)
    scores = []
    
    for move in legal_moves:
        new_board = make_move(board, move, player_to_move)
        
        cache_key = (
            tuple(tuple(row) for row in new_board),
            player_to_move,                
            player_to_optimize                     
        )
        
        if cache_key in cache:
            score = cache[cache_key]
        else:

            opp = 'X' if player_to_move == 'O' else 'O'
            score = _minimax_score(new_board, opp, player_to_optimize)
            cache[cache_key] = score
        
        scores.append(score)
    

    if player_to_move == player_to_optimize:
        return max(scores)
    else:
        return min(scores)