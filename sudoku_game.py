def print_board(puzzle):
    print("\nCurrent Board:")              #output the board.
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            value = puzzle[i][j]
            print("." if value == -1 else value, end=" ")
        print()
    print()


def find_empty(puzzle):
    for r in range(9):       #checking the row and columns.
        for c in range(9):
            if puzzle [r][c] == -1:
                 return r, c
    return None,None       

def is_valid(puzzle,guess,row,col):
    row_vals = puzzle[row]     #checking if the value we provided is in the row.
    if guess in row_vals:
        return False
    col_vals = [puzzle[i][col]  for i in range(9)]      #checking if the value we provided is in the column.
    if guess in col_vals:
        return False 
    row_start= (row//3) * 3
    col_start = (col // 3) * 3
    for r in range(row_start, row_start+3):
        for c in range (col_start, col_start+3):
            if puzzle [r][c] == guess:
                return False
    return True

def solve_sudoku(puzzle):
    row,col = find_empty(puzzle)
    if row is None:     #no empty space left, puzzle solved
        return True
    
    for guess in range(1, 10):
        if is_valid(puzzle,guess,row,col):
            puzzle[row][col] = guess
            if solve_sudoku(puzzle):
                return True
            #if our guess didn't solve the puzzle, we need to try a new number.
    
        puzzle[row][col] = -1     #resetting the guess because it didn't work out.
    return False     #even if we try all numbers, if it doesn't solve, then the sudoku is unsolvable.

def get_user_move():
    try:                                        #getting user input
        row = int(input("Row (0-8): "))
        col = int(input("Col (0-8): "))
        value = int(input("Value (1-9): "))
        return row, col, value                      
    except ValueError:
        print("Only Numbers,Please")               #checking if the user input is valid or not.
        return None, None, None
    
def is_complete(puzzle):               #checking if there are any empty spaces left in the puzzle.
    for row in puzzle:
        if -1 in row:
            return False
    return True


def play_sudoku(puzzle):       #the main function to play the sudoku game
    while True:
        print_board(puzzle)

        if is_complete(puzzle):
            print("WELL DONE,YOU COMPLETEDE THE SUDOKU!!.")    #checking if the game is completed, if so, break the loop.
            break

        row, col, value = get_user_move()        #calling the function to get user input.

        if row is None:      
            continue

        if not (0 <= row <= 8 and 0 <= col <= 8 and 1 <= value <= 9):     #checking if the value is within the valid range.
            print("Value out of range .")
            continue

        if puzzle[row][col] != -1:          
            print("This cell is already full.")
            continue
        if is_valid(puzzle, value, row, col):
            puzzle[row][col] = value
        else:
            print("Your move is not fitting the rules.")

if __name__== "__main__":
    board = [[5,3,-1,-1,7,-1,-1,-1,-1],
             [6,-1,-1,1,9,5,-1,-1,-1],
             [-1,9,8,-1,-1,-1,-1,6,-1],
             
             [8,-1,-1,-1,-1,6,-1,-1,3],
             [4,-1,-1,8,-1,3,-1,-1,1],
             [7,-1,-1,-1,2,-1,-1,-1,6],
             
             [-1,6,-1,-1,-1,-1,2,8,-1],
             [-1,-1,-1,4,1,9,-1,-1,5],
             [-1,-1,-1,-1,8,-1,-1,7,9],
             ]
    play_sudoku(board)

                
            

    


    