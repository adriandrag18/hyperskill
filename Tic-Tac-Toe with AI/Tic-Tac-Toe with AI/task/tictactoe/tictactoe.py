import random

opposite_side = {
    'X': 'O',
    'O': 'X'
}

modes = {'user': 0, 'easy': 1, 'medium': 2, 'hard': 3}


def print_board(board):
    print('-' * 10)
    for j in range(3):
        print('|', board[j][0], board[j][1], board[j][2], '|')
    print('-' * 10)


def read_board():
    s = ''.join(input('Enter cells: ').replace('>', '').split())

    num_X = s.count('X')
    num_O = s.count('O')
    side = 'X'
    if num_X == num_O + 1:
        side = 'O'
    elif num_X == num_O:
        side = 'X'
    elif num_X < num_O:
        print("To many '0'")
        exit()
    else:
        print("To many 'X'")
        exit()

    board = []
    if len(s) != 9:
        print("Length must be 9!")
        exit()
    else:
        k = -1
        for i, char in enumerate(s):
            if char not in '_XO':
                print(f"problem at character {i} in {s}")
                exit()
            if i % 3 == 0:
                k += 1
                board.append([])
            board[k].append(' ' if char == '_' else char)
    return board, side


def parse_coordinates(s, board):
    s = ''.join(s.replace('> ', '').split())

    if s == 'exit':
        exit()

    if not (s[0].isdigit() and s[1].isdigit()):
        print("You should enter numbers!")
        return -1, -1

    x, y = int(s[0]), int(s[1])

    if not (1 <= x <= 3 and 1 <= y <= 3):
        print('Coordinates should be from 1 to 3!')
        return -1, -1

    x, y = 3 - y, x - 1

    if board[x][y] != ' ':
        print('This cell is occupied! Choose another one!')
        return -1, -1

    return x, y


def parse_input(s):
    if s == 'exit':
        exit()

    commands = s.split()
    if len(commands) == 3 and commands[0] == 'start' \
            and commands[1] in modes.keys() and commands[2] in modes.keys():
        engines = {'X': modes[commands[1]], 'O': modes[commands[2]]}
    else:
        print('Bad parameters!')
        return None

    return engines


def game_over(board):
    winner = ''
    for j in range(3):
        if board[j][0] == board[j][1] == board[j][2] != ' ':
            winner = board[j][0]
        if board[0][j] == board[1][j] == board[2][j] != ' ':
            winner = board[0][j]

    if board[0][0] == board[1][1] == board[2][2] != ' ':
        winner = board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != ' ':
        winner = board[0][2]

    if winner == '' or winner == ' ':
        if board[0].count(' ') + board[1].count(' ') + board[2].count(' ') == 0:
            return 'Draw'
        else:
            return 'Game not finished'
    else:
        return winner + ' wins'


def generate_all_moves(board):
    empty = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                empty.append((i, j))
    return empty


def go_easy(board, side=''):
    moves = generate_all_moves(board)
    return random.choice(moves)


def go_medium(board, side):
    moves = generate_all_moves(board)
    for i, j in moves:
        board[i][j] = side
        state = game_over(board)
        if side == state[0]:
            board[i][j] = ' '
            return i, j
        board[i][j] = ' '

    for i, j in moves:
        board[i][j] = opposite_side[side]
        state = game_over(board)
        if opposite_side[side] == state[0]:
            board[i][j] = ' '
            return i, j
        board[i][j] = ' '
    return random.choice(moves)


def go_hard(board, side):
    state, move = minimax(board, side)
    return move


def minimax(board, side):
    state = game_over(board)
    if state != 'Game not finished':
        return state, None

    moves = generate_all_moves(board)
    best_move = moves[0]
    best_state = opposite_side[side] + ' wins'
    for i, j in moves:
        board[i][j] = side
        side = opposite_side[side]
        state = minimax(board, side)
        board[i][j] = ' '
        side = opposite_side[side]
        if side == state[0]:
            best_move = i, j
            best_state = state

        if best_state == opposite_side[side] + ' wins' and state == 'Draw':
            best_move = i, j
            best_state = state

    return best_state, best_move


def main():
    engines_modes = [None, go_easy, go_medium, go_hard]
    levels = ['user', 'easy', 'medium', 'hard']
    while True:
        engines = None
        while engines is None:
            s = input('Input command: ')
            engines = parse_input(s)

        print(engines)

        board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        side = 'X'
        print_board(board)

        state = 'Game not finished'
        while state == 'Game not finished':

            if engines[side]:
                print(f'Making move level "{levels[engines[side]]}"')
                i, j = engines_modes[engines[side]](board, side)
            else:
                i, j = -1, -1
                while i == -1:
                    s = input('Enter the coordinates: ')
                    i, j = parse_coordinates(s, board)

            board[i][j] = side
            print_board(board)
            side = opposite_side[side]
            state = game_over(board)

        print(state)


if __name__ == '__main__':
    main()
