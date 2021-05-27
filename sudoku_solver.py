# Sudoku Solver

def print_board(board):
    for i in range(0, 9):
        if i != 0 and i % 3 == 0:
            print("---------------------")
        for j in range(0, 9):
            if j % 3 == 0 and j != 0:
                print("| " + str(board[i][j]) + " ", end="")
            elif j == 8:
                print(str(board[i][j]))
            else:
                print(str(board[i][j]) + " ", end="")
        
def get_free_pos(board):
    for i in range(0, 9):
        for j in range(0, 9):
            if board[i][j] == 0:
                return (i, j)
    return False

def check_value(board, num, row, col):
    # check row
    for i in range(0, 9):
        if board[row][i] == num:
            return False

    # check col
    for i in range(0, 9):
        if board[i][col] == num:
            return False

    # check square
    round_row = row % 3
    round_col = col % 3
    start_sq_row = row - round_row
    start_sq_col = col - round_col

    for i in range(start_sq_row, start_sq_row + 3):
        for j in range(start_sq_col, start_sq_col + 3):
            if board[i][j] == num:
                return False

    return True

def solve_board(board):
    pos = get_free_pos(board)
    if pos == False:
        return True
    row = pos[0]
    col = pos[1]
    for i in range(1, 10):
        valid = check_value(board, i, row, col)
        if valid == True:
            board[row][col] = i
            result = solve_board(board)
            if result == True:
                return True
            else:
                board[row][col] = 0;
                #return False
            
    return False

def get_board():
    board = []
    file = open("board.txt", "r")
    for line in file:       
        row = line.strip()
        row = [int(i) for i in str(row)]
        board.append(row)

    return board

def main():
    board = get_board()
    print_board(board)
    result = solve_board(board)
    if result == False:
        print("Unable to complete board")
    else:
        print("Success!")
        print_board(board)



main()