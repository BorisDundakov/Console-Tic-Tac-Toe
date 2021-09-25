from constraints import coordinates

# 1. Initializing an empty matrix

matrix = [[" " for i in range(3)] for j in range(3)]

print("Player 1, Pick a sign (X or 0): ")
player_1_sign = input()
player_sign_dict = {"Player 1": "?", "Player 2": "?"}


def repr_matrix(board):
    for row in board:
        print(*[ind_el + " |" for ind_el in row if ind_el != 1], end="\n")


# 2. Two functions -> one returns the board_positions for the user and the other checks if the sign is valid

def check_sign_validity(sign):
    while sign.upper() not in ["X", "0"]:
        print("Player 1, Pick a sign (X or 0): ")
        sign = input()

    return_val = sign.upper()
    player_sign_dict["Player 1"] = return_val
    if return_val == "X":
        player_sign_dict["Player 2"] = "0"
    elif return_val == '0':
        player_sign_dict["Player 2"] = "X"
    return return_val


def board_positions():
    print_result = " "
    print_result += "List of board positions:\n"
    print_result += "| 1 | 2 | 3 |\n"
    print_result += "| 4 | 5 | 6 |\n"
    print_result += "| 7 | 8 | 9 |\n"
    return print_result


# 3. Implementing the two functions

# 4. Checking if the position entered is correct and implementing this function below


def check_position_in_range(pos):
    while True:
        try:
            pos = int(pos)
            if pos in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                return pos
            print(f"{next_player}, pick a valid position!")
        except ValueError:
            print(f"{next_player}, pick a valid position!")

        pos = input()


def populate_matrix(board, matrix_row, matrix_column, sign):
    while board[matrix_row][matrix_column] != " ":
        print(f"Element {board[matrix_row][matrix_column]} already added at this position!")
        try:
            print("Please enter an empty position!")
            position = input()
            valid_position = check_position_in_range(position)
            player_coordinates = coordinates[valid_position]
            matrix_row, matrix_column = player_coordinates.split(",")
            matrix_row = int(matrix_row)
            matrix_column = int(matrix_column)

        except ValueError:
            print("Invalid coordinates!")

    board[matrix_row][matrix_column] = sign
    return board


def check_winner(board):
    winner_sign = " "

    # 1. Check diagonals
    if board[0][0] == board[1][1] == board[2][2]:
        winner_sign = board[0][0]
        return winner_sign

    elif board[0][2] == board[1][1] == board[2][0]:
        winner_sign = board[0][2]
        return winner_sign

    # 2. Check rows
    for r in range(3):
        if board[r][0] == board[r][1] == board[r][2]:
            winner_sign = board[r][0]
            return winner_sign

    # 3. Check columns
    for c in range(3):
        if board[0][c] == board[1][c] == board[2][c]:
            winner_sign = board[0][c]
            return winner_sign

    # returns an empty string because there isn't a winner
    return winner_sign


def check_turns(board):
    next_turn = " "
    x_count = sum(x.count("X") for x in board)
    zero_count = sum(o.count("0") for o in board)
    if x_count == zero_count:
        next_turn = "Player 1"
    else:
        next_turn = "Player 2"

    return next_turn


def play(board, first_player_sign):
    if board[0][0] == board[0][1] == board[0][2] == board[1][0] == board[1][1] == board[1][2] == board[2][0] == \
            board[2][1] == board[2][2]:
        first_player = check_sign_validity(first_player_sign)
        player_sign_dict["Player 1"] = first_player

    while check_winner(board) == " ":
        res = any(" " in el for el in board)
        if not res:
            repr_matrix(matrix)
            print()
            print("No winner!")
            exit()

        global next_player
        next_player = check_turns(board)
        print(board_positions())
        repr_matrix(matrix)
        print()
        print(f"{next_player}, pick a position!")
        position = input()
        valid_position = check_position_in_range(position)
        player_coordinates = coordinates[valid_position]
        c_row, c_col = player_coordinates.split(",")
        populate_matrix(matrix, int(c_row), int(c_col), player_sign_dict[next_player])
        end_of_turn = check_winner(matrix)
        if end_of_turn != " ":
            for winner_key, winner_value in player_sign_dict.items():
                if winner_value == end_of_turn:
                    print(f"{winner_key} with sign {winner_value} is the winner!")
                    repr_matrix(matrix)
                    exit()


play(matrix, player_1_sign)
