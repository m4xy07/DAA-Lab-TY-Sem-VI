# N-Queens Problem using Backtracking
# Time Complexity: O(N!)
# Space Complexity: O(N)

solution_count = 0


def is_safe(board, row, col):
    """
    Check if placing queen at (row, col) is safe
    board[i] = j means queen in row i is at column j
    """
    # Check previous rows
    for i in range(row):
        # Check column attack
        if board[i] == col:
            return False
        
        # Check diagonal attacks
        if abs(board[i] - col) == abs(i - row):
            return False
    
    return True


def solve_n_queens(board, row, n):
    """
    Solve N-Queens using backtracking
    Returns True if solution exists
    """
    global solution_count
    
    # Base case: All queens placed
    if row == n:
        solution_count += 1
        print_solution(board, n, solution_count)
        return True
    
    found_solution = False
    
    # Try placing queen in each column of current row
    for col in range(n):
        if is_safe(board, row, col):
            # Place queen
            board[row] = col
            
            # Recurse to next row
            if solve_n_queens(board, row + 1, n):
                found_solution = True
            
            # Backtrack (remove queen)
            board[row] = -1
    
    return found_solution


def print_solution(board, n, sol_num):
    """Print the board configuration"""
    print(f"\nSolution {sol_num}:")
    print("-" * (n * 2 + 1))
    for i in range(n):
        for j in range(n):
            if board[i] == j:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
    print("-" * (n * 2 + 1))


def main():
    global solution_count
    
    print("="*60)
    print("N-QUEENS PROBLEM (Backtracking)")
    print("="*60)
    
    # Input
    n = int(input("\nEnter number of queens (N): "))
    
    # Check for impossible cases
    if n < 4 and n != 1:
        print(f"\nNo solution exists for N = {n}")
        print("Solutions exist for N = 1 or N >= 4")
        return
    
    # Initialize board
    board = [-1] * n
    solution_count = 0
    
    print(f"\nSolving {n}-Queens Problem using Backtracking...\n")
    
    # Solve
    if not solve_n_queens(board, 0, n):
        print("\nNo solution exists")
    else:
        print("\n" + "="*60)
        print(f"Total solutions found: {solution_count}")
        print("="*60)
    
    # Information
    print("\nTime Complexity: O(N!)")
    print("Space Complexity: O(N)")


if __name__ == "__main__":
    main()
