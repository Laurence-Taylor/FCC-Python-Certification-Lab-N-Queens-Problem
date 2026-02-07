def is_valid(row, col, queens):
    for r in range(row):
        # Check Queens column
        if col == queens[r]: return False
        # Check Queens Diagonal
        elif abs(col-queens[r]) == abs(row - r): return False
    return True

def place_queens(row, queens, n):
    if row == n:
        # Return the Queens valid Solution (When this happend then we found a valid solution)
        return queens
    else:
        # Initializate total solution
        total_solns = []
        # Find in the other colums
        for col in range(n):
            # check if the new position is valid
            if is_valid(row, col, queens):
                # Add column to the queens valid list
                queens[row] = col
                # add element to total solution
                total_solns += place_queens(row + 1, queens, n)
        return total_solns         

def dfs_n_queens(n):
    if n < 1: return []
    # initialize queens list
    queens = ['']*n
    row = 0
    # Find all posible places solutions
    solutions = place_queens(row,queens,n)
    # Return right format solution.
    return [solutions[i:i+n] for i in range(0, len(solutions),n)]


if __name__ == '__main__':
    print(dfs_n_queens(5))