#Practical 4

def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False
    return True

def solve_n_queens(board, row, n):
    if row == n:
        return True  

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1  
            if solve_n_queens(board, row + 1, n):
                return True  
            board[row][col] = 0  

    return False  

def print_solution(board):
    for row in board:
        print(" ".join(["Q" if cell == 1 else "." for cell in row]))

def n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    
    board[0][0] = 1
    
    if solve_n_queens(board, 1, n):
        print_solution(board)
    else:
        print("No solution exists")

n = int(input("Enter number of queens :"))  
n_queens(n)
