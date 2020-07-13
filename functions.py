import copy
def find_empty(puzzle):
    """Finds the first empty cell going across and down"""
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if puzzle[i][j] == 0:
                return i, j
    return None

def print_board(puzzle):
    """Prints out the board"""
    for i in range(len(puzzle)):
        if i % 3 == 0:
            print("\n-------------------------")
        else:
            print("")
        for j in range(len(puzzle[i])):
            if j % 3 == 0 or j == 0:
                print("|", end = ' ')
            print(puzzle[i][j], end = ' ')
            if j == 8:
                print("|", end=' ')
    print("\n-------------------------")

def test_validity_row_cols(puzzle, row, col, move):
    """Tests if that is a valid move!"""
    for i in range(len(puzzle[row])):
        if move == puzzle[row][i] and i != col:
            return False
    for j in range(len(puzzle)):
        if move == puzzle[j][col] and j != row:
            return False
    return True

def test_validity_block(puzzle, row, col, move):
    yblock = int(row / 3)
    xblock = int(col / 3)
    yrange = [element + yblock*3 for element in [0, 1, 2]]
    xrange = [element + xblock * 3 for element in [0, 1, 2]]
    for i in yrange:
        for j in xrange:
            if i == row and j == col:
                continue
            elif puzzle[i][j] == move:
                return False
    return True

def find_next_move(puzzle, row, col, currval):
    """Outputs next possible guess for the value"""
    for i in range(currval+1, 10):
        if test_validity_row_cols(puzzle, row, col, i) and test_validity_block(puzzle, row, col, i):
            return i
    return False    # for the case that no possible moves can be found

def generate_empty_list(puzzle):
    """Generates a list of the empty cells"""
    empty_list = []
    temp_puzzle = copy.deepcopy(puzzle)
    while find_empty(temp_puzzle):
        row, col = find_empty(temp_puzzle)
        empty_list.append([row, col])
        temp_puzzle[row][col] = 1
    return empty_list

def test_board(puzzle):
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if puzzle[i][j] != 0:
                if not test_validity_block(puzzle, i, j, puzzle[i][j]):
                    print(i, j)
                    print("Type 1")
                    return False
                if not test_validity_row_cols(puzzle, i, j, puzzle[i][j]):
                    print(i, j)
                    print("Type 2")
                    return False
    return True