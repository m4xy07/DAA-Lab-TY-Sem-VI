# Practical 7: N-Queens Problem (Backtracking) - Python

## Overview
This practical implements the classic N-Queens problem using backtracking with recursion in Python. The goal is to place N queens on an N×N chessboard so that no two queens attack each other.

---

## N-Queens Problem

### Problem Statement
Place **N queens** on an **N×N chessboard** such that:
1. No two queens share the same **row**
2. No two queens share the same **column**  
3. No two queens share the same **diagonal**

### Chess Queen Attack Rules
A queen can attack any piece in the same:
- **Row** (horizontal line)
- **Column** (vertical line)
- **Diagonal** (both diagonals: ↘ and ↙)

```
Example: Queen at (2,2)
    0 1 2 3 4
  ┌──────────┐
0 │ X . X . X │
1 │ . X X X . │
2 │ X X Q X X │
3 │ . X X X . │
4 │ X . X . X │
  └──────────┘
```

---

## Backtracking Approach

### What is Backtracking?
A systematic way to try all possibilities:
1. **Choose**: Make a choice (place queen)
2. **Explore**: Recursively try to complete solution
3. **Unchoose (Backtrack)**: If doesn't work, undo choice and try next

### Backtracking Template
```python
def backtrack(state):
    if is_solution(state):
        output(state)
        return
    
    for choice in get_choices(state):
        if is_valid(choice):
            make_choice(choice)
            backtrack(new_state)
            undo_choice(choice)  # BACKTRACK!
```

---

## Python Implementation

```python
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
```

---

## Board Representation

### 1D Array (Space Efficient)
```python
board = [-1] * n
```
- `board[i] = j` means queen in row i is at column j
- **Space**: O(n) instead of O(n²)

### Example
```python
board = [1, 3, 0, 2]  # 4-Queens solution

Represents:
    0 1 2 3
  ┌────────┐
0 │ . Q . . │  board[0] = 1
1 │ . . . Q │  board[1] = 3
2 │ Q . . . │  board[2] = 0
3 │ . . Q . │  board[3] = 2
  └────────┘
```

---

## Safety Check Explained

### Column Check
```python
if board[i] == col:
    return False
```
Queens in different rows can't be in same column.

### Diagonal Check
```python
if abs(board[i] - col) == abs(i - row):
    return False
```

#### Why This Works?

**Left Diagonal (↘)**: All cells on same diagonal have same `(row - col)`
```
    0 1 2 3
  ┌────────┐
0 │ 0 -1 -2 -3│  row - col
1 │ 1  0 -1 -2│
2 │ 2  1  0 -1│
3 │ 3  2  1  0│
  └────────┘
```

**Right Diagonal (↙)**: All cells on same diagonal have same `(row + col)`
```
    0 1 2 3
  ┌────────┐
0 │ 0 1 2 3 │  row + col
1 │ 1 2 3 4 │
2 │ 2 3 4 5 │
3 │ 3 4 5 6 │
  └────────┘
```

**Combined Check**:
```python
# If difference in rows equals difference in columns, they're diagonal
abs(board[i] - col) == abs(i - row)
```

---

## Python-Specific Features

### 1. Global Variable
```python
solution_count = 0

def solve_n_queens(board, row, n):
    global solution_count
    solution_count += 1
```

### 2. List Initialization
```python
board = [-1] * n  # Creates list of n elements, all -1
```

### 3. F-String Formatting
```python
print(f"\nSolution {sol_num}:")
print("-" * (n * 2 + 1))  # String repetition
```

### 4. Range Function
```python
for col in range(n):  # 0 to n-1
for i in range(row):  # 0 to row-1
```

### 5. Boolean Logic
```python
if not solve_n_queens(board, 0, n):
    print("No solution exists")
```

---

## Step-by-Step Example (4-Queens)

### Execution Trace

```
Initial: board = [-1, -1, -1, -1]

ROW 0: Try columns 0, 1, 2, 3

Place Q at (0, 0):
Q . . .
. . . .
. . . .
. . . .

  ROW 1: Try columns 0, 1, 2, 3
  
  (0,0) attacks (1,0) and (1,1) → Try (1,2)
  Q . . .
  . . Q .
  . . . .
  . . . .
  
    ROW 2: Try columns 0, 1, 2, 3
    All columns attacked! DEAD END
  
  BACKTRACK to ROW 1, try (1,3)
  Q . . .
  . . . Q
  . . . .
  . . . .
  
    ROW 2: Try columns 0, 1, 2, 3
    All columns attacked! DEAD END
  
  BACKTRACK to ROW 1, no more options
  
BACKTRACK to ROW 0, try (0,1)
. Q . .
. . . .
. . . .
. . . .

  ROW 1: Try columns 0, 1, 2, 3
  
  (0,1) attacks (1,0), (1,1), (1,2) → Try (1,3)
  . Q . .
  . . . Q
  . . . .
  . . . .
  
    ROW 2: Try columns 0, 1, 2, 3
    
    Try (2,0): Safe!
    . Q . .
    . . . Q
    Q . . .
    . . . .
    
      ROW 3: Try columns 0, 1, 2, 3
      
      Try (3,2): Safe!
      . Q . .
      . . . Q
      Q . . .
      . . Q .
      
      ✓ SOLUTION 1 FOUND!
    
    BACKTRACK to find more solutions...
    
Continue searching...

SOLUTION 2:
. . Q .
Q . . .
. . . Q
. Q . .
```

---

## How It Works: Recursion Tree

```
                    Root (Row 0)
            /      |      |      \
        Col0    Col1   Col2   Col3
         /       /       \       \
     Row1    Row1      Row1    Row1
    /  |  \   ...       ...     ...
  C0 C1 C2 C3
  |
Row2
 |
C0 (Solution!)
```

Each path from root to leaf represents trying a complete board configuration.

---

## Complexity Analysis

### Time Complexity
**O(N!)** in worst case
- Row 0: N choices
- Row 1: ~N-2 valid choices
- Row 2: ~N-4 valid choices
- Total: N × (N-2) × (N-4) × ... ≈ N!

But pruning significantly reduces actual work!

### Space Complexity
- **Board**: O(N)
- **Recursion Stack**: O(N) - maximum depth is N
- **Total**: O(N)

---

## Number of Solutions

| N | Solutions | Notes |
|---|-----------|-------|
| 1 | 1 | Trivial |
| 2 | 0 | Impossible |
| 3 | 0 | Impossible |
| 4 | 2 | First non-trivial |
| 5 | 10 | |
| 6 | 4 | |
| 7 | 40 | |
| 8 | 92 | Classic 8-queens |
| 9 | 352 | |
| 10 | 724 | |

---

## How to Run

```bash
python n_queens.py
```

### Sample Input
```
Enter number of queens (N): 4
```

### Sample Output
```
============================================================
N-QUEENS PROBLEM (Backtracking)
============================================================

Solving 4-Queens Problem using Backtracking...


Solution 1:
---------
. Q . .
. . . Q
Q . . .
. . Q .
---------

Solution 2:
---------
. . Q .
Q . . .
. . . Q
. Q . .
---------

============================================================
Total solutions found: 2
============================================================

Time Complexity: O(N!)
Space Complexity: O(N)
```

### Invalid Input
```
Enter number of queens (N): 3

No solution exists for N = 3
Solutions exist for N = 1 or N >= 4
```

---

## Finding All vs First Solution

### Current Implementation (Find All)
```python
if solve_n_queens(board, row + 1, n):
    found_solution = True  # Continue searching
board[row] = -1  # Always backtrack
```

### Modify to Find First Only
```python
if solve_n_queens(board, row + 1, n):
    return True  # Stop immediately
board[row] = -1
```

---

## Common Mistakes

### 1. Incorrect Diagonal Check
```python
# ✗ Wrong - checks all diagonals unnecessarily
for i in range(n):
    if abs(board[i] - col) == abs(i - row):
        return False

# ✓ Correct - only check previous rows
for i in range(row):
    if abs(board[i] - col) == abs(i - row):
        return False
```

### 2. Not Backtracking
```python
# ✗ Wrong - doesn't reset board
board[row] = col
solve_n_queens(board, row + 1, n)
# Missing: board[row] = -1

# ✓ Correct
board[row] = col
solve_n_queens(board, row + 1, n)
board[row] = -1  # Backtrack!
```

### 3. Wrong Initialization
```python
# ✗ Wrong - default is 0, not -1
board = [0] * n

# ✓ Correct - use -1 for empty
board = [-1] * n
```

---

## Optimization: Bit Manipulation

```python
def solve_n_queens_fast(n):
    """Faster version using bit manipulation"""
    solutions = []
    
    def backtrack(row, cols, diag1, diag2, board):
        if row == n:
            solutions.append(board[:])
            return
        
        available = ~(cols | diag1 | diag2) & ((1 << n) - 1)
        
        while available:
            col = available & -available  # Get rightmost bit
            available ^= col  # Remove this bit
            
            board[row] = (col - 1).bit_length() - 1
            backtrack(
                row + 1,
                cols | col,
                (diag1 | col) << 1,
                (diag2 | col) >> 1,
                board
            )
    
    backtrack(0, 0, 0, 0, [-1] * n)
    return solutions
```

Much faster but less readable!

---

## Applications of Backtracking

1. **Puzzles**: Sudoku, Crosswords, Maze solving
2. **Games**: Chess, Go
3. **Constraint Satisfaction**: Graph coloring, Scheduling
4. **Combinatorial**: Permutations, Subsets, Partitions
5. **Optimization**: Traveling Salesman (small instances)

---

## Key Takeaways

1. **Backtracking**: Try → Check → Fail → Undo → Try next
2. **Recursion**: Natural fit for state space exploration
3. **Pruning**: Skip invalid branches early (is_safe)
4. **1D Array**: Efficient board representation
5. **Diagonal Check**: Using absolute difference
6. **Time Complexity**: O(N!) but pruning helps significantly
7. **Python Features**: Global variables, list initialization, f-strings

---

## Practice Problems

1. Print only first solution (stop early)
2. Count solutions without printing
3. N-Queens with obstacles (some squares blocked)
4. Find all unique solutions (remove symmetries)
5. Sudoku Solver using backtracking

---

## Next Steps
- **Practical 8**: Traveling Salesman (Branch and Bound)
- **Practice**: More backtracking (Sudoku, Maze, Subset Sum)
- **Optimize**: Implement bit manipulation version
- **Compare**: Backtracking vs other approaches
