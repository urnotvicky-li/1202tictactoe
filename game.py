import numpy as np

# create a 3x3 game board
board = np.zeros((3, 3)).astype(int)

# check if there is a winner
def check_win():
    # check if any row or column sums to 3 
    if any(np.sum(board, 1)==3) or any(np.sum(board, 0)==3) or sum(np.diag(board))==3 or sum(np.diag(board[::-1]))==3:
        return True   # IF any row or coloumn or diagonal sums to 3, player 1 wins 
    # Check if any row or coloumn or diagonal sums to -3 or -3 for diagonals
    if any(np.sum(board, 1)==-3) or any(np.sum(board, 0)==-3) or sum(np.diag(board))==-3 or sum(np.diag(board[::-1]))==-3:
        return True # IF any row or coloumn or diagonal sums to -3, Player -1 wins
    return False # no winner

# To handle player's turn
def play_turn():
    # clarify the x and y position when each player play
    x = int(input(f"What is player {turn}'s x position?"))
    y = int(input(f"What is player {turn}'s y position?"))
    try:
        #check if the selection position is empty
        if board[y, x]==0:   
            board[y, x]=turn  # place current player's mark on the board
        else:
            play_turn()  # if the place is occupided, ask again
    except IndexError:
        play_turn() # if the coordinates are out of bounds, ask again

# assume player 1 starts
turn = 1
# the max number of move in the tictactoe game
move = 9

# continue if there are no moves left or a player wins
while move >0:
    print (board)  #print the current result
    play_turn()   
    # check if there is a winner after the turn
    if check_win():
        print (f"Player {turn} has won!") # print winner result
        break
    turn = turn*-1  # switch turns 
    move = move -1  # decrease the remaining number of moves










# #tictactoe game using numpy
# # Initialize the board with rows A, B, C and columns 0, 1, 2
# board = {
#     'A': [' ', ' ', ' '],  # Row A
#     'B': [' ', ' ', ' '],  # Row B
#     'C': [' ', ' ', ' ']   # Row C
# }

# def check_win(board):
#     # Total 8 chances
#     # Check rows (A, B, C) (A0, A1, A2 and B0, B1, B2 and C0, C1, C2)
#     for row in ['A', 'B', 'C']:
#         if board[row][0] == board[row][1] == board[row][2] and board[row][0] != ' ':
#             winner = board[row][0]
#             loser = 'O' if winner == 'X' else 'X'
#             return f"{winner} wins, and {loser} loses."

#     # Check columns (0, 1, 2) (A0, B0, C0 and A1, B1, C1 and A2, B2, C2)
#     for col in range(3):
#         if board['A'][col] == board['B'][col] == board['C'][col] and board['A'][col] != ' ':
#             winner = board['A'][col]
#             loser = 'O' if winner == 'X' else 'X'
#             return f"{winner} wins, and {loser} loses."

#     # Check diagonals (A0, B1, C2 and A2, B1, C0)
#     if board['A'][0] == board['B'][1] == board['C'][2] and board['A'][0] != ' ':
#         winner = board['A'][0]
#         loser = 'O' if winner == 'X' else 'X'
#         return f"{winner} wins, and {loser} loses."
#     if board['A'][2] == board['B'][1] == board['C'][0] and board['A'][2] != ' ':
#         winner = board['A'][2]
#         loser = 'O' if winner == 'X' else 'X'
#         return f"{winner} wins, and {loser} loses."

#     # Check for draw (if the board is full and no one has won)
#     if all(board[row][col] != ' ' for row in ['A', 'B', 'C'] for col in range(3)):
#         return "It's a draw!"

#     return "Draw."

# # Example board configuration (assuming X and O are players)
# board = {
#     'A': ['X', 'O', 'X'],
#     'B': ['O', 'X', 'O'],
#     'C': ['O', ' ', 'X']
# }

# # Check for a win or draw
# result = check_win(board)
# print(result)  # Output: Player X wins, and Player O loses!

