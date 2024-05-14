# 9x9 bir tablonunun oluşturulması
board = [
    [0, 7, 0, 0, 0, 0, 0, 3, 0],
    [0, 1, 0, 9, 5, 0, 0, 6, 0],
    [8, 0, 0, 0, 0, 0, 2, 0, 0],
    [6, 0, 0, 0, 2, 3, 0, 0, 4],
    [9, 4, 1, 0, 8, 0, 0, 7, 0],
    [0, 0, 0, 0, 0, 1, 5, 8, 0],
    [2, 0, 0, 0, 0, 8, 7, 1, 9],
    [0, 0, 0, 0, 0, 4, 0, 0, 3],
    [7, 0, 6, 5, 0, 0, 0, 0, 0]
]


# Matrisi alt matrislere ayırır.
def printMatrixSubgrid(board):
    for i in range(0, 9, 3):  # 0,3,6
        for k in range(3):  # satırlar
            for j in range(0, 9, 3):#0,3,6
                for l in range(3):#sütunlar
                    print(board[i + k][j + l], end=" ")
                print("", end="|")
            print()
        print("------------------------")


# boş hücre(0) kontrolü yapar
def isValidUnit(unit):
    unit = [i for i in unit if i != 0]
    return len(unit) == len(set(unit))


# Sudokunun uygunluğunu kontrol eder
def isValid(board, row, col, num):
    # Satır kontrolü
    if num in board[row]:
        return False

    # Sütun kontrolü
    if num in [board[i][col] for i in range(9)]:
        return False

    # 3x3 alt matris kontrolü
    start_row = 3 * (row // 3)
    start_col = 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True


def solveSudoku(board):
    empty = findEmptyLocation(board)
    if not empty:
        return True
    row, col = empty

    for num in range(1, 10):
        if isValid(board, row, col, num):
            board[row][col] = num

            if solveSudoku(board):
                return True

            board[row][col] = 0

    return False


def findEmptyLocation(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None


print("SUDOKU BOARD")
printMatrixSubgrid(board)
print()
if solveSudoku(board):
    print("Çözülmüş Sudoku Tahtası:")
    printMatrixSubgrid(board)
else:
    print("Çözüm Bulunamadı")
