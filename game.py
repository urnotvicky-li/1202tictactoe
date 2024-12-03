#tictactoe game using numpy
# Initialize the board with rows A, B, C and columns 0, 1, 2
board = {
    'A': [' ', ' ', ' '],  # Row A
    'B': [' ', ' ', ' '],  # Row B
    'C': [' ', ' ', ' ']   # Row C
}

def check_win(board):
    # Total 8 chances
    # Check rows (A, B, C) (A0, A1, A2 and B0, B1, B2 and C0, C1, C2)
    for row in ['A', 'B', 'C']:
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] != ' ':
            winner = board[row][0]
            loser = 'O' if winner == 'X' else 'X'
            return f"{winner} wins, and {loser} loses."

    # Check columns (0, 1, 2) (A0, B0, C0 and A1, B1, C1 and A2, B2, C2)
    for col in range(3):
        if board['A'][col] == board['B'][col] == board['C'][col] and board['A'][col] != ' ':
            winner = board['A'][col]
            loser = 'O' if winner == 'X' else 'X'
            return f"{winner} wins, and {loser} loses."

    # Check diagonals (A0, B1, C2 and A2, B1, C0)
    if board['A'][0] == board['B'][1] == board['C'][2] and board['A'][0] != ' ':
        winner = board['A'][0]
        loser = 'O' if winner == 'X' else 'X'
        return f"{winner} wins, and {loser} loses."
    if board['A'][2] == board['B'][1] == board['C'][0] and board['A'][2] != ' ':
        winner = board['A'][2]
        loser = 'O' if winner == 'X' else 'X'
        return f"{winner} wins, and {loser} loses."

    # Check for draw (if the board is full and no one has won)
    if all(board[row][col] != ' ' for row in ['A', 'B', 'C'] for col in range(3)):
        return "It's a draw!"

    return "Draw."

# Example board configuration (assuming X and O are players)
board = {
    'A': ['X', 'O', 'X'],
    'B': ['O', 'X', 'O'],
    'C': ['O', ' ', 'X']
}

# Check for a win or draw
result = check_win(board)
print(result)  # Output: Player X wins, and Player O loses!

