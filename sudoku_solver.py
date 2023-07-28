import pyautogui as pag
# cmd > pip install pyautogui
import os
# Currently test works, but now working on reading screens to solve puzzles automatically from websudoku

def get_path():
    folderpath = r'/Users/Dan/Python_projects/Sudoku/'
    filenamelist = []
    for filename in os.listdir('/Users/Dan/Python_projects/Sudoku/'):
        print(filename)
        if filename.endswith('.png'):
            f = open(os.path.join(folderpath,filename), 'r')
            filenamelist.append(f.read())
    print(filenamelist)
    return filenamelist

# Test Puzzle
sudoku =   [[3, 9, 0,   0, 5, 0,    0, 0, 0], 
            [0, 0, 0,   2, 0, 0,    0, 0, 5], 
            [0, 0, 0,   7, 1, 9,    0, 8, 0],

            [0, 5, 0,   0, 6, 8,    0, 0, 0], 
            [2, 0, 6,   0, 0, 3,    0, 0, 0], 
            [0, 0, 0,   0, 0, 0,    0, 0, 4],

            [5, 0, 0,   0, 0, 0,    0, 0, 0], 
            [6, 7, 0,   1, 0, 5,    0, 4, 0], 
            [1, 0, 9,   0, 0, 0,    2, 0, 0]]



def find_next_empty(puzzle):
    # finds the next empty index(row, col) on the puzzle to make a guess -> rep with -1
    # return row, col tuple (or (None, None) if there is none)
    # Note index is 0 - 8
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == 0:
                return r, c
    
    return None, None #if there is no empty space (0)

def is_valid(puzzle, guess, row, col):
    # identifies if guess is valid
    # Return True if valid, else False
    # check Row
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    # check Columns
    col_vals = [puzzle[i][cols] for i in range(9)]
    if guess in col_vals:
        return False
    # Check the 3x3 square for number
    # Possibly use iterator for square
    row_start = (row // 3) #remainder not needed
    col_start = (col // 3) #remainder not needed
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
    return True

def number_locator():
    for pos in pag.locateOnScreen("1.png"):
        print(pos)
def solve_sud(puzzle):
    # solve the puzzle using backtracking
    #Puzzle should be a list of lists, where each inner list is a row in the puzzle
    # return whether a solution exists
    # mutate puzzle to the solution

    # 1. choose an index on the puzzle to make a guess
    row, col = find_next_empty(puzzle)

    # if no empty space exists, puzzle should be solved.
    if row is None:
        return True
    
    # 2. If space is 0, then make guess between 1 and 9
    for guess in range(1,10):
        # check if valid guess
        if is_valid(puzzle, guess, row, col):
            #true will place guess
            puzzle[row][col] = guess

            if solve_sud(puzzle):
                return True
            #recursion
        puzzle[row][col] = 0
    #if every guess is complete and no solution found, unsolvable
    return False


# png_list = get_path()
# number_locator()
print(solve_sud(sudoku))
print(sudoku)