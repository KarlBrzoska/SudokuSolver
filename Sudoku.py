import random


#functino to display the puzzle
def print_puzzle(puzzle):
    print('\n')
    for i in range(len(puzzle)):
        line = ""
        if i == 3 or i == 6:
            print("---------------------")
        for j in range(len(puzzle)):
            if j == 3 or j == 6:
                line += "| "
            line += str(puzzle[i][j])+" "   #print x y z unless j - 3 or 6, than x y z | x
        print(line)


# function to find all the spots where that is not filled in
def find_empty_spaces(puzzle):
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if puzzle[i][j] == 0:
                return i, j
    return None, None


#function to transpose the matrix so we can iterate through the columns
def transpose(l1, l2):
    # iterate over list l1 to the length of an item
    for i in range(len(l1[0])):
        # print(i)
        row = []
        for item in l1:
            # appending to new list with values and index positions
            # i contains index position and item contains values
            row.append(item[i])
        l2.append(row)
    return l2

def valid_num(puzzle, guess, row, col):
    #iterate through each row and if the guess is equal to an element in a row, than invalid
    #iterate through each column and do same. I did this sby tranposing grid and then iteratign through each row
    is_valid_row = True
    is_valid_col = True
    is_valid_matrix = True

    for i in puzzle[row]:
        if guess == i:
            is_valid_row = False

    puzzle_transpose = []
    #transpose matrix to check columns
    transpose(puzzle, puzzle_transpose)
    for j in puzzle_transpose[col]:
        if guess == j:
            is_valid_col = False

    matrix_x = row // 3
    matrix_y = col // 3

    for i in range(matrix_x * 3, (matrix_x * 3) + 3):
        for j in range(matrix_y * 3, (matrix_y * 3) + 3):
            if guess == puzzle[i][j]:
                is_valid_matrix = False


    return is_valid_col and is_valid_row and is_valid_matrix



#function to solve puzzle
def solve_sudoku(puzzle):
    row, col = find_empty_spaces(puzzle)

    if col == None:
        return True #return True if solved


    for guess in range(1, 10):
        if valid_num(puzzle, guess, row, col):
            puzzle[row][col] = guess
            if solve_sudoku(puzzle):
                return True

        puzzle[row][col] = 0

    return False


puzzle =   [[8, 1, 0, 0, 3, 0, 0, 2, 7],
            [0, 6, 2, 0, 5, 0, 0, 9, 0],
            [0, 7, 0, 0, 0, 0, 0, 0, 0],
            [0, 9, 0, 6, 0, 0, 1, 0, 0],
            [1, 0, 0, 0, 2, 0, 0, 0, 4],
            [0, 0, 8, 0, 0, 5, 0, 7, 0],
            [0, 0, 0, 0, 0, 0, 0, 8, 0],
            [0, 2, 0, 0, 1, 0, 7, 5, 0],
            [3, 8, 0, 0, 7, 0, 0, 4, 2]]
print_puzzle(puzzle)
print(find_empty_spaces(puzzle))
print(solve_sudoku(puzzle))
print_puzzle(puzzle)
print_puzzle(puzzle)
