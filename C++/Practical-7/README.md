# Practical 7: N-Queens Problem (Backtracking)

## Overview
This practical implements the classic N-Queens problem using backtracking with recursion. The goal is to place N queens on an N×N chessboard so that no two queens attack each other.

---

## N-Queens Problem (`n_queens.cpp`)

### Problem Statement
Place N queens on an N×N chessboard such that:
1. No two queens share the same row
2. No two queens share the same column
3. No two queens share the same diagonal

---

## Chess Queen Attack Rules

### How Queens Attack
A queen can attack any piece that is:
- In the same **row** (horizontal)
- In the same **column** (vertical)
- In the same **diagonal** (both diagonals)

```
Example (Q = Queen, . = Empty, X = Attacked):

    0 1 2 3 4
  ┌──────────┐
0 │ X X X X X │
1 │ X X . X X │
2 │ X . Q . X │
3 │ X X . X X │
4 │ X X X X X │
  └──────────┘

Queen at (2,2) attacks entire row, column, and both diagonals
```

---

## Backtracking Approach

### What is Backtracking?
Backtracking is a recursive algorithm that tries to build a solution incrementally and abandons (backtracks) when it determines the current path cannot lead to a valid solution.

### Backtracking Steps
1. **Choose**: Place a queen in a column
2. **Explore**: Recursively try to place remaining queens
3. **Un-choose (Backtrack)**: If solution not found, remove queen and try next position

### Algorithm
```cpp
solveNQueens(board, row, n):
    // Base case: All queens placed
    if row == n:
        Print solution
        return true
    
    // Try placing queen in each column of current row
    for col from 0 to n-1:
        if isSafe(board, row, col):
            board[row] = col  // Place queen
            
            if solveNQueens(board, row+1, n):
                found = true
            
            board[row] = -1  // Backtrack (remove queen)
    
    return found
```

### Safety Check
```cpp
isSafe(board, row, col):
    for i from 0 to row-1:
        // Check column attack
        if board[i] == col:
            return false
        
        // Check diagonal attacks
        if board[i] - i == col - row:    // Left diagonal
            return false
        if board[i] + i == col + row:    // Right diagonal
            return false
    
    return true
```

---

## How It Works - Detailed Example

### 4-Queens Problem

#### Board Representation
We use a 1D array where `board[i] = j` means queen in row i is at column j.

```
board[] = [1, 3, 0, 2] represents:

    0 1 2 3
  ┌────────┐
0 │ . Q . . │  board[0] = 1
1 │ . . . Q │  board[1] = 3
2 │ Q . . . │  board[2] = 0
3 │ . . Q . │  board[3] = 2
  └────────┘
```

#### Step-by-Step Execution

**Row 0: Try to place first queen**
```
Try col 0:
  . Q . .    isSafe(0,0) ✓
  . . . .    Place queen at (0,0)
  . . . .    Move to row 1
  . . . .
```

**Row 1: Try to place second queen**
```
Try col 0:
  Q . . .    isSafe(1,0) ✗ (same column as row 0)
  Q . . .    Skip
  . . . .
  . . . .

Try col 1:
  Q . . .    isSafe(1,1) ✗ (diagonal attack)
  . Q . .    Skip
  . . . .
  . . . .

Try col 2:
  Q . . .    isSafe(1,2) ✓
  . . Q .    Place queen at (1,2)
  . . . .    Move to row 2
  . . . .
```

**Row 2: Try to place third queen**
```
Try col 0:
  Q . . .    isSafe(2,0) ✗ (diagonal with row 1)
  . . Q .    Skip
  Q . . .
  . . . .

Try col 1:
  Q . . .    isSafe(2,1) ✗ (diagonal with row 0)
  . . Q .    Skip
  . Q . .
  . . . .

Try col 2:
  Q . . .    isSafe(2,2) ✗ (same column as row 1)
  . . Q .    Skip
  . . Q .
  . . . .

Try col 3:
  Q . . .    isSafe(2,3) ✗ (diagonal with row 1)
  . . Q .    Skip
  . . . Q
  . . . .

All columns tried, no valid position!
BACKTRACK to row 1
```

**Row 1: Continue from where we left (after col 2)**
```
Try col 3:
  Q . . .    isSafe(1,3) ✓
  . . . Q    Place queen at (1,3)
  . . . .    Move to row 2
  . . . .
```

**Row 2: Try again**
```
Try col 0:
  Q . . .    isSafe(2,0) ✗
  . . . Q    
  Q . . .
  . . . .

Try col 1:
  Q . . .    isSafe(2,1) ✓
  . . . Q    Place queen at (2,1)
  . Q . .    Move to row 3
  . . . .
```

**Row 3: Try to place fourth queen**
```
Try col 0:
  Q . . .    isSafe(3,0) ✗
  . . . Q
  . Q . .
  Q . . .

Try col 1:
  Q . . .    isSafe(3,1) ✗
  . . . Q
  . Q . .
  . Q . .

Try col 2:
  Q . . .    isSafe(3,2) ✗
  . . . Q
  . Q . .
  . . Q .

Try col 3:
  Q . . .    isSafe(3,3) ✗
  . . . Q
  . Q . .
  . . . Q

No valid position! BACKTRACK to row 2
```

**Eventually finds solution:**
```
board[] = [1, 3, 0, 2]

    0 1 2 3
  ┌────────┐
0 │ . Q . . │
1 │ . . . Q │
2 │ Q . . . │
3 │ . . Q . │
  └────────┘

This is a valid solution! ✓
```

---

## Diagonal Check Explanation

### Left Diagonal (↘)
All cells on same left diagonal have same value of (row - col)
```
    0 1 2 3
  ┌────────┐
0 │ 0 -1 -2 -3│
1 │ 1  0 -1 -2│
2 │ 2  1  0 -1│
3 │ 3  2  1  0│
  └────────┘

Check: if board[i] - i == col - row
```

### Right Diagonal (↙)
All cells on same right diagonal have same value of (row + col)
```
    0 1 2 3
  ┌────────┐
0 │ 0 1 2 3 │
1 │ 1 2 3 4 │
2 │ 2 3 4 5 │
3 │ 3 4 5 6 │
  └────────┘

Check: if board[i] + i == col + row
```

---

## Time and Space Complexity

### Time Complexity
O(N!) in worst case
- Each row has N choices
- First row: N choices
- Second row: ~(N-2) choices (after eliminating attacked positions)
- Third row: ~(N-4) choices
- Total: N × (N-2) × (N-4) × ... ≈ N!

### Space Complexity
- **Recursion Stack**: O(N) - maximum depth is N
- **Board Storage**: O(N)
- **Total**: O(N)

---

## Number of Solutions for Different N

| N | Solutions | Notes |
|---|-----------|-------|
| 1 | 1 | Trivial |
| 2 | 0 | Impossible |
| 3 | 0 | Impossible |
| 4 | 2 | First non-trivial case |
| 5 | 10 | |
| 6 | 4 | |
| 7 | 40 | |
| 8 | 92 | Classic 8-queens |
| 9 | 352 | |
| 10 | 724 | |

---

## Finding All Solutions vs One Solution

### Find All Solutions
```cpp
bool solveNQueens(board, row, n):
    if row == n:
        solutionCount++
        printSolution(board, n)
        return true  // Continue searching
    
    foundSolution = false
    for col in 0 to n-1:
        if isSafe(board, row, col):
            board[row] = col
            if solveNQueens(board, row+1, n):
                foundSolution = true
            board[row] = -1  // Always backtrack
    
    return foundSolution
```

### Find First Solution Only
```cpp
bool solveNQueens(board, row, n):
    if row == n:
        printSolution(board, n)
        return true  // Stop immediately
    
    for col in 0 to n-1:
        if isSafe(board, row, col):
            board[row] = col
            if solveNQueens(board, row+1, n):
                return true  // Propagate success
            board[row] = -1
    
    return false
```

---

## Optimization Techniques

### 1. Symmetry Elimination
- For N-queens, many solutions are rotations/reflections of each other
- Can reduce search space by 8x

### 2. Bit Manipulation
- Use bit arrays instead of checking each position
- Faster than array-based checking

### 3. Heuristic Ordering
- Try columns with fewer conflicts first
- Can reduce backtracking

---

## How to Compile and Run

```bash
# Compile
g++ n_queens.cpp -o n_queens

# Run
./n_queens
```

### Sample Input
```
Enter number of queens (N): 4
```

### Sample Output
```
Solving 4-Queens Problem using Backtracking...

Solution 1:
. Q . .
. . . Q
Q . . .
. . Q .

Solution 2:
. . Q .
Q . . .
. . . Q
. Q . .

Total solutions found: 2
```

### Sample Input (No Solution)
```
Enter number of queens (N): 3
```

### Sample Output
```
No solution exists for N = 3
```

---

## Key Backtracking Concepts

### 1. State Space Tree
```
                    Root (empty board)
                   /  |  |  \
           Col0  Col1 Col2 Col3  (Row 0)
           /       |
        Col0-3   Col0-3  (Row 1)
         /         |
       ...       ...
```

### 2. Pruning
When `isSafe()` returns false, entire subtree is pruned (not explored).

### 3. Backtracking Template
```
backtrack(state):
    if is_solution(state):
        output(state)
        return
    
    for choice in get_choices(state):
        if is_valid(choice):
            make_choice(choice)
            backtrack(new_state)
            undo_choice(choice)  # BACKTRACK
```

---

## Applications of Backtracking

1. **Constraint Satisfaction**: Sudoku, Graph Coloring
2. **Combinatorial**: Subset Sum, Permutations
3. **Puzzles**: Maze solving, Crosswords
4. **Games**: Chess, Go (with alpha-beta pruning)

---

## Key Takeaways

1. **Backtracking**: Try → Check → Fail → Undo → Try next
2. **Recursion**: Natural fit for exploring state space
3. **Pruning**: Essential for performance (skip invalid branches)
4. **N-Queens**: Classic problem demonstrating backtracking
5. **Time Complexity**: Exponential (O(N!)) but pruning helps significantly

---

## Common Mistakes to Avoid

1. **Not backtracking**: Forgetting to remove queen after recursive call
2. **Wrong safety check**: Incorrect diagonal calculation
3. **Premature exit**: Stopping after first solution when all solutions needed
4. **Index errors**: Off-by-one errors in row/column checks
