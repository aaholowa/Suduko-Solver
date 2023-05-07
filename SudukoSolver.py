# Suduko Solver with backtracking algorithm


board = []

# prompt user to input board values


def user_input():
    while True:
        row = list(input('Enter Row: '))
        convert = []  # list to convert to int

        for i in row:
            convert.append(int(i))

        board.append(convert)

        if len(board) == 9:
            break

        print(f"Row: {str(len(board))} Complete")
    print("Row: 9 Complete\n")
    return True

# display board to user


def display(board):  # display unsolved board
    for i in range(len(board)):  # rows
        if i % 3 == 0 and i != 0:  # split into rows of 3
            print('------------------------')

        for j in range(len(board[0])):  # columns
            if j % 3 == 0 and j != 0:  # split into columns of 3
                print(' | ', end='')

            if j == 8:
                print(board[i][j])  # print row a column of the board

            else:
                print(str(board[i][j]) + ' ', end='')


# locate empty box and return postion within board

def empty(board):  # loop through board to find empty space '0'
    for i in range(len(board)):  # loop through rows
        for j in range(len(board[0])):  # loop through columns
            if board[i][j] == 0:
                return (i, j)  # return the row and then column
    return False

# determine valid solutions for current board


def valid(board, number, position):

    # check to see if number is not valid
    # check row
    for i in range(len(board[0])):  # loop though every column in row
        if board[position[0]][i] == number and position[1] != i:  # check each element in the row
            return False

    # check columns
    for i in range(len(board)):
        if board[i][position[1]] == number and position[0] != i:  # check each element in the row
            return False

    # check boxes
    # integer division (columns 1-3 = 0 , columns 4-6 = 1, columns 7-9 = 2)
    xpos = position[1] // 3
    # integer division (rows 1-3 = 0 , rows 4-6 = 1, rows 7-9 = 2)
    ypos = position[0] // 3

    for i in range(ypos*3, (ypos*3) + 3):
        for j in range(xpos * 3, (xpos*3) + 3):
            # checks if any other element in box equals the one we just added
            if board[i][j] == number and (i, j) != position:
                return False

    return True  # valid solution

# recursively solve board using backtracking algorithm


def solve(board):

    value = empty(board)

    if not empty(board):  # solved if no empties found
        return True

    else:
        row, col = value

    for i in range(1, 10):
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):  # now check the updated board  # solve recursively
                return True

            board[row][col] = 0  # reset the value just placed


# call functions/display
print("Welcome to Suduko Solver!\n")
user_input()
print("Unsolved Board:")
display(board)
print()
solve(board)
print()
print("Solved Board:")
display(board)
