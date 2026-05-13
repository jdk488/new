def solve_n_queens(n):
    board = [-1] * n

    col_used = [False]*n
    diag1 = [False]*(2*n)
    diag2 = [False]*(2*n)

    def solve(row):
        if row == n:
            return True

        for col in range(n):
            if not col_used[col] and not diag1[row+col] and not diag2[row-col+n]:
                
                board[row] = col
                col_used[col] = diag1[row+col] = diag2[row-col+n] = True

                if solve(row+1):
                    return True

                col_used[col] = diag1[row+col] = diag2[row-col+n] = False

        return False

    solve(0)

    for i in range(n):
        for j in range(n):
            print("Q" if board[i]==j else ".", end=" ")
        print()

solve_n_queens(4)