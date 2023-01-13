from pprint import pprint

board = [[0, 0, 7, 0, 6, 0, 0, 9, 0],
         [0, 0, 5, 0, 4, 2, 0, 6, 0],
         [6, 0, 0, 1, 0, 7, 0, 0, 0],
         [0, 7, 0, 0, 2, 0, 4, 0, 5],
         [0, 0, 9, 8, 5, 1, 0, 7, 0],
         [2, 0, 6, 0, 7, 3, 9, 0, 1],
         [0, 6, 0, 2, 1, 0, 0, 0, 8],
         [5, 9, 0, 7, 0, 0, 6, 0, 2],
         [1, 0, 0, 6, 8, 0, 0, 0, 9]]

# get_subboard: returns the 3x3 subboard that a specific cell,
# denoted by the row n and column m, is within as a 2d list. 
def get_subboard(board: list, n: int, m: int):
    subboard = []
    
    # Finding coordinates of top-left cell of the subgroup
    row, col = 0, 0
    if (m <= 2): col = 0
    elif (m <= 5): col = 3
    else: col = 6

    if (n <= 2): row = 0
    elif (n <= 5): row = 3
    else: row = 6
 
    # Adding parts of each applicable row into the subboard array
    for r in range(row, row + 3):
        subboard.append(board[r][col : col + 3])
    
    return subboard

# Flattens a 2d array
# takes in a subboard and returns all the elements in a 1d list.
def one_d_subboard(board, n, m):
    subboard = get_subboard(board, n, m)
    one_d = []
    for array in subboard:
        one_d += array
    return one_d

# Takes in the coordinates to a cell on a board and returns a
# list of numbers that are valid possible choices for the cell,
# based on the rules of Sudoku. Returns an empty list is the cell
# is already filled.
def valid_choices(board, n, m):
    if board[n][m] != 0: return []
    possible = [i for i in range(1, 10)]
    valid = []
    
    for elm in possible:
        if (elm not in [board[n][j] for j in range(0, 9)]) and (elm not in [board[i][m] for i in range(0, 9)]):
            if elm not in one_d_subboard(board, n, m):

                valid.append(elm)
    
    return valid

# My own implementation of the backtracking algorithm:
# Goes through each empty cell and tries one of the possible
# choices, then recurses on that choice. If that choice leads to
# a deadend, then the algorithm backtracks and chooses another
# possible choice for the initial cell.
def solve(board, n = 0, m = 0):
    if m > 8:
        if n > 8:
            return board
        else:
            return solve(board, n + 1, 0)
    if n > 8:
        return board

    elif board[n][m] == 0:
        possible = valid_choices(board, n, m)
        if possible == []: return False
        
        for choice in possible:
            board[n][m] = choice
            temp = solve(board, n, m + 1)
            if temp != False:
                return temp
        
        board[n][m] = 0
        return False
    else:
        return solve(board, n, m + 1)



pprint(solve(board))





