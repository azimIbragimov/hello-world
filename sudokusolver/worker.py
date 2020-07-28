board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def solve(bo):

    find = find_empty(bo)   # Output: (row, column)
    if not find:
        return True # Found the solution
    else:
        row, col = find

    for i in range(1, 10):
        if valid(bo, i, (row, col)): # Checks if the answer is valid
            bo[row][col] = i    # Enters the answer to the board

            if solve(bo):
                return True

            bo[row][col] = 0

    return False



def valid(bo, num, pos):
    """
    Checks if the sudoku number is correct
    bo --- sudoku table (list)
    number --- guess number (int)
    pos --- position of the guess number (tuple  -- (row, column))
    """
    # Check row
    for i in range(len(bo[0])): # Output: 0,1,2,3,4,5,6,7,8
        if bo[pos[0]][i] == num and pos[1] != i:
            # bo[pos[0][i] == num  -- if there are any numbers with the same value on that row
            # pos[1] != i --- does not include inteself in calculations
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos != i:
        # bo[i][pos[1]] == num  -- if there are any numbers with the same value on that column
        # pos[1] != i --- does not include inteself in calculations
            return False

    # Check Box
    box_x = pos[1]//3   # Determiens x location of the box
    box_y = pos[0]//3   # Determines y location of the box

    for i in range(box_y * 3, box_y*3 + 3): # Checks a certain box
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] ==num and (i, j) != pos:
                return False

    return True



def print_board(bo):

    for i in range(len(bo)):    # Output: 0,1,2,3,4,5,6,7,8
        if i % 3 == 0 and i != 0:   # Output: 3,6
            print("- - - - - - - - - - - - - ") # Prints it on lines 3, 6

        for j in range(len(bo[0])):  # Output: 0,1,2,3,4,5,6,7,8
            if j % 3 == 0:  # Output: 3,6
                print(" | ", end = '') # Prints it on lines 3, 6

            if j == 8:  # Output: 8
                print(bo[i][j]) # Output: bo[range(0,9)][8]
            else:
                print(str(bo[i][j]) + " ", end = '')  # Output: bo[range(0,9)][range(0, 9)]

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j) # Output: (row, column)

    return None



print_board(board)
print()
solve(board)
print()
print_board(board)
