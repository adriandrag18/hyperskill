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
    state = None
    if num_X == num_O + 1:
        side = 'O'
    elif num_X == num_O:
        side = 'X'
    elif num_X < num_O:
        # print("To many '0'")
        if num_X != num_O - 1:
            state = 'Impossible'
        # exit()
    else:
        # print("To many 'X'")
        state = 'Impossible'
        # exit()

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

    if state is None:
        state = game_over(board)

    return board, side, state


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


def game_over(board):
    winner = []
    win_on_line = 0
    win_on_col = 0
    for j in range(3):
        if board[j][0] == board[j][1] == board[j][2] != ' ':
            winner.append(board[j][0])
            win_on_line += 1
        if board[0][j] == board[1][j] == board[2][j] != ' ':
            winner.append(board[0][j])
            win_on_col += 1

    if board[0][0] == board[1][1] == board[2][2] != ' ':
        winner.append(board[0][0])

    if board[0][2] == board[1][1] == board[2][0] != ' ':
        winner = board[0][2]

    if len(winner) >= 3 or win_on_col >= 2 or win_on_col >= 2 or \
            (winner.count('X') and winner.count('O')):
        return 'Impossible'

    if not winner:
        if board[0].count(' ') + board[1].count(' ') + board[2].count(' ') == 0:
            return 'Draw'
        else:
            return 'Game not finished'
    else:
        return winner[0] + ' wins'


def main():
    opposite_side = {'X': 'O', 'O': 'X'}
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    side = 'X'
    state = 'Game not finished'
    while state == 'Game not finished':
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