# Tic Tac Toe Game

board = [' ' for _ in range(9)]

def print_board():
    print()
    print(board[0], '|', board[1], '|', board[2])
    print('--+---+--')
    print(board[3], '|', board[4], '|', board[5])
    print('--+---+--')
    print(board[6], '|', board[7], '|', board[8])
    print()

def check_winner(player):
    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],   # Rows
        [0,3,6], [1,4,7], [2,5,8],   # Columns
        [0,4,8], [2,4,6]             # Diagonals
    ]

    for pos in win_positions:
        if all(board[i] == player for i in pos):
            return True
    return False

def is_draw():
    return ' ' not in board

current_player = 'X'

while True:
    print_board()

    try:
        move = int(input(f"Player {current_player}, enter position (1-9): ")) - 1
    except ValueError:
        print("Invalid input! Enter a number between 1 and 9.")
        continue

    if move < 0 or move > 8:
        print("Invalid position!")
        continue

    if board[move] != ' ':
        print("Position already occupied!")
        continue

    board[move] = current_player

    if check_winner(current_player):
        print_board()
        print(f"Player {current_player} Wins!")
        break

    if is_draw():
        print_board()
        print("Game Draw!")
        break

    current_player = 'O' if current_player == 'X' else 'X'