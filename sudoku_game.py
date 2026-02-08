def print_board(puzzle):
    print("\nCurrent Board:")              #board u yazdırıyor.
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
    for r in range(9):       #row ve colomb da orda bir sayı var mı diye bakıyruz.
        for c in range(9):
            if puzzle [r][c] == -1:
                 return r, c
    return None,None       

def is_valid(puzzle,guess,row,col):
    row_vals = puzzle[row]     #verdiğimiz değer puzzle ın rowlarında var mı diye bakıyoruz.
    if guess in row_vals:
        return False
    col_vals = [puzzle[i][col]  for i in range(9)]      #aynısı ama coloumn u kontorl ediyoıruz.
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
    if row is None:     #bütün yerler dolduysa oyun biter
        return True
    
    for guess in range(1, 10):
        if is_valid(puzzle,guess,row,col):
            puzzle[row][col] = guess
            if solve_sudoku(puzzle):
                return True
            #eğer değerimiz ya da tahminimiz problemi çözmüyorsa o zaman, yeni bir numara denemeliyiz.
    
        puzzle[row][col] = -1     #guessi resetliyoruz
    return False     #başka sayı girsekte çözülmüyorsa o zaman sudoku çözülemezdir.

def get_user_move():
    try:                                        #kullanıcıdan sayı alıyoruz
        row = int(input("Row (0-8): "))
        col = int(input("Col (0-8): "))
        value = int(input("Value (1-9): "))
        return row, col, value                      
    except ValueError:
        print("Only Numbers,Please")               #number var mıdiye kontrol ediyor.
        return None, None, None
    
def is_complete(puzzle):               #oyunda herhangi bir kutuda boşluk var mı diye kontrol eder.
    for row in puzzle:
        if -1 in row:
            return False
    return True


def play_sudoku(puzzle):       #oyunu temel yazdıran fonksiyon
    while True:
        print_board(puzzle)

        if is_complete(puzzle):
            print("WELL DONE,YOU COMPLETEDE THE SUDOKU!!.")    #oyun tamamlanmış mı diye her sefrinde kontorl eder,boşluk yoksa devam eder varsa break ile çıkar.
            break

        row, col, value = get_user_move()        #row ve col ini değer yazıdrma fonksiyonunu çağırıyor.

        if row is None:      
            continue

        if not (0 <= row <= 8 and 0 <= col <= 8 and 1 <= value <= 9):     #alınan değer aralıkta mı bakıyoruz.
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

                
            

    


    