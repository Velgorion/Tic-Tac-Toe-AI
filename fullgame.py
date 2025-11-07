from AIs.random_ai import random_ai_move
from AIs.smart_ai import smart_ai_move
from AIs.minimax_ai import minimax_ai_move
from engine import is_valid_move, render, make_move, get_winner, is_draw


def new_board() -> list[list[str | None]]:
    board = []

    for _ in range(3):
        row = []
        for _ in range(3):
            row.append(None)

        board.append(row)

    return board


def get_move() -> tuple[int, int]:
    """Getting user move with using recursion call"""

    try:
        x = int(input("=> What is your move's X co-ordinate?: "))
        y = int(input("=> What is your move's Y co-ordinate?: "))
        
        if not (0 <= x <= 2 and 0 <= y <= 2):
            raise ValueError('Coordinates out of range')
        return x, y
    except ValueError as e:
        print(f'Invalid input: {e}')
        return get_move()


def first_move() -> str:
    while True:
        curr_player = input("Who's moving first? [X | O]: ").upper()

        if curr_player in ('X', 'O'):
            return curr_player
        else:
            print('Please, choose "X" or "O"')


def human_move(board, player):

    while True:
        move_coords = get_move()
        if is_valid_move(board, move_coords):
            break
        else:
            print('\n' + f"Can't make move {move_coords} square already taken!" + '\n')

    board = make_move(board, move_coords, player)
    render(board)

    return board


def select_players():

    PLAYER_TYPES = {
    1: 'random_ai',
    2: 'smart_ai',
    3: 'minimax_ai',
    4: 'human'
}
    
    player_x = int(input('=> Choose the X-player:\n1) Random_AI\n2) Smart_AI\n3) Minimax_AI\n4) Human\n'))
    player_y = int(input('=> Choose the O-player:\n1) Random_AI\n2) Smart_AI\n3) Minimax_AI\n4) Human\n'))

    return {
        'X': PLAYER_TYPES[player_x],
        'O': PLAYER_TYPES[player_y]
    }

def main_game():

    board = new_board()
    render(board)

    ai_config = select_players()
    ai_functions = {
        'random_ai': random_ai_move,
        'smart_ai': smart_ai_move,
        'human': human_move,
        'minimax_ai': minimax_ai_move
    }

    curr_player = first_move()

    game_active = True
    while game_active:

        ai_function = ai_functions[ai_config[curr_player]]
        board = ai_function(board, curr_player)
        
        if winner := get_winner(board):
            print(f'The Winner is {ai_config[winner].capitalize()}!')
            game_active = False
        elif is_draw(board):
            print('DRAW...')
            game_active = False

        curr_player = 'O' if curr_player == 'X' else 'X'
            


if __name__ == '__main__':
    main_game()