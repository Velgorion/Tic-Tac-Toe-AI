from copy import deepcopy

def get_legal_moves(board):
    legal_moves = []

    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                legal_moves.append((j, i))
    
    return legal_moves


def get_winner(board):
    all_lines = [[], [], [], [], []] + board

    for i in range(3):
        for j in range(3):
            cell = board[i][j]
            if j == 0:
                all_lines[0].append(cell)
            if j == 1:
                all_lines[1].append(cell)
            if j == 2:
                all_lines[2].append(cell)
            if j == i:
                all_lines[3].append(cell)
            if i + j == 2:
                all_lines[4].append(cell)
        
    for line in all_lines:
        if len(set(line)) == 1 and not line[0] is None:
            return line[0]
        
    return None


def is_draw(board):
    for row in board:
        for cell in row:
            if cell is None:
                return False

    return True


def is_valid_move(board, move_coords) -> bool:
    x, y = move_coords

    if board[y][x] in ('X', 'O'):
        return False
    
    return True


def render(board: list[list[str | None]]):
    ordinate_row = ['', '', '0', '1', '2']
    barrier_row = ['', '', '-', '-', '-']

    
    print(' '.join(char.rjust(1) for char in ordinate_row))
    print(' '.join(char.rjust(1) for char in barrier_row))
    
    for i, row in enumerate(board):
        formatted = [str(i), '|'] + row + ['|']
        print(' '.join(char.rjust(1) if char is not None else ' ' for char in formatted))
    
    print(' '.join(char.rjust(1) for char in barrier_row))


def make_move(board, move_coords, curr_player = 'X'):

    board = deepcopy(board)
    x, y = move_coords

    board[y][x] = curr_player

    return board


def evaluate_position_heuristic(board, player_to_optimize):

    score = 0

    if board[1][1] == player_to_optimize:
        score += 2
    
    corners = [(0,0), (0,2), (2,0), (2,2)]
    for x, y in corners:
        if board[y][x] == player_to_optimize:
            score += 1
    
    win_lines = _get_winning_lines(board, player_to_optimize)

    score += win_lines * 0.5

    return score


def _get_winning_lines(board, player):

    opponent = 'X' if player == 'O' else 'O'
    lines = 0
    

    win_lines = [

        [(0,0), (0,1), (0,2)],
        [(1,0), (1,1), (1,2)],
        [(2,0), (2,1), (2,2)],

        [(0,0), (1,0), (2,0)],
        [(0,1), (1,1), (2,1)],
        [(0,2), (1,2), (2,2)],

        [(0,0), (1,1), (2,2)],
        [(0,2), (1,1), (2,0)]
    ]
    
    for line in win_lines:
        line_cells = [board[y][x] for x, y in line]

        if opponent not in line_cells:
            lines += 1
    
    return lines