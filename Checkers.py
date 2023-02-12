# Define the board as a 2D array of integers
board = [[0, 1, 0, 1, 0, 1, 0, 1],
         [1, 0, 1, 0, 1, 0, 1, 0],
         [0, 1, 0, 1, 0, 1, 0, 1],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [-1, 0, -1, 0, -1, 0, -1, 0],
         [0, -1, 0, -1, 0, -1, 0, -1],
         [-1, 0, -1, 0, -1, 0, -1, 0]]

# Define a function to print the board
def print_board(board):
    for row in board:
        print(row)

# Define a function to get the legal moves for a piece at a given location
def get_legal_moves(board, row, col):
    legal_moves = []
    if board[row][col] == 1:
        if row > 1 and col > 1 and board[row-1][col-1] == -1:
            legal_moves.append((row-2, col-2))
        if row > 1 and col < 6 and board[row-1][col+1] == -1:
            legal_moves.append((row-2, col+2))
    elif board[row][col] == -1:
        if row < 6 and col > 1 and board[row+1][col-1] == 1:
            legal_moves.append((row+2, col-2))
        if row < 6 and col < 6 and board[row+1][col+1] == 1:
            legal_moves.append((row+2, col+2))
    return legal_moves

# Define a function to move a piece on the board
def make_move(board, start_row, start_col, end_row, end_col):
    board[end_row][end_col] = board[start_row][start_col]
    board[start_row][start_col] = 0
    if abs(end_row - start_row) == 2:
        board[(end_row + start_row) // 2][(end_col + start_col) // 2] = 0

# Define a function to check if a player has any legal moves left
def has_legal_moves(board, player):
    for row in range(8):
        for col in range(8):
            if board[row][col] == player:
                if get_legal_moves(board, row, col):
                    return True
    return False

# Define a function to play the game
def play_game():
    current_player = 1
    while has_legal_moves(board, current_player):
        print_board(board)
        print("Player", current_player, "to move")
        start_row, start_col = map(int, input("Enter starting row and column: ").split())
        end
