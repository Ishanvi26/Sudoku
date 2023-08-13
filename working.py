# 0 represents the cells to be filled i.e, cells that are empty
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
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False

def valid(bo, num, pos):
    # checks if the value we want to enter already exists in given row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i: 
            # pos[0][i] means we are checking every cell in a row
            # pos[1] != i is necessary to ensure we are not checking the existing cell for validity
            return False

    # checks if the value we want to enter already exists in given column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            # pos[0][i] means we are checking every cell in a column
            # pos[0] != i is necessary to ensure we are not checking the existing cell for validity
            return False

    # checks if the value we want to enter already exists in given box
    box_x = pos[1] // 3 # finds the column coordinates
    box_y = pos[0] // 3 # finds the row coordinates

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True

def print_board(bo): # bo is short for board
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("--------------------------") # separating after every three rows

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="") # separating after every three columns

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="") # end="" is to ensure that we stay on the same line

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # returns row and column that is empty

    return None

print("Sudoko board before solving")
print_board(board)
solve(board)
print("\nSudoko board after solving")
print_board(board)