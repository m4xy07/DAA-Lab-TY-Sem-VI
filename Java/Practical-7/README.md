# Practical 7: N-Queens Problem (Backtracking) - Java

## Overview
This practical implements the classic N-Queens problem using backtracking with recursion in Java. The goal is to place N queens on an N×N chessboard so that no two queens attack each other.

---

## N-Queens Problem (`NQueens.java`)

### Problem Statement
Place N queens on an N×N chessboard such that:
1. No two queens share the same row
2. No two queens share the same column
3. No two queens share the same diagonal

---

## Chess Queen Attack Rules

A queen can attack any piece in the same:
- **Row** (horizontal)
- **Column** (vertical)
- **Diagonal** (both diagonals)

```
Example:
    0 1 2 3 4
  ┌──────────┐
0 │ X X X X X │
1 │ X X . X X │
2 │ X . Q . X │
3 │ X X . X X │
4 │ X X X X X │
  └──────────┘

Queen at (2,2) attacks entire row, column, and diagonals
```

---

## Backtracking Approach

### What is Backtracking?
A recursive algorithm that:
1. **Choose**: Make a choice (place queen)
2. **Explore**: Recursively try to complete solution
3. **Un-choose (Backtrack)**: Remove choice if it doesn't work

### Algorithm
```java
public static boolean solveNQueens(int[] board, int row, int n) {
    // Base case: All queens placed
    if (row == n) {
        solutionCount++;
        printSolution(board, n);
        return true;
    }
    
    boolean foundSolution = false;
    
    // Try placing queen in each column of current row
    for (int col = 0; col < n; col++) {
        if (isSafe(board, row, col)) {
            board[row] = col;  // Place queen
            
            if (solveNQueens(board, row + 1, n))
                foundSolution = true;
            
            board[row] = -1;  // Backtrack (remove queen)
        }
    }
    
    return foundSolution;
}
```

---

## Board Representation

### 1D Array Representation
```java
int[] board = new int[n];
```

- `board[i] = j` means queen in row i is at column j
- Saves space: O(n) instead of O(n²)

### Example
```java
board[] = {1, 3, 0, 2} represents:

    0 1 2 3
  ┌────────┐
0 │ . Q . . │  board[0] = 1
1 │ . . . Q │  board[1] = 3
2 │ Q . . . │  board[2] = 0
3 │ . . Q . │  board[3] = 2
  └────────┘
```

---

## Safety Check Implementation

```java
public static boolean isSafe(int[] board, int row, int col) {
    // Check previous rows
    for (int i = 0; i < row; i++) {
        // Check column attack
        if (board[i] == col)
            return false;
        
        // Check left diagonal attack
        if (board[i] - i == col - row)
            return false;
        
        // Check right diagonal attack
        if (board[i] + i == col + row)
            return false;
    }
    return true;
}
```

---

## Diagonal Check Explanation

### Left Diagonal (↘)
All cells on same left diagonal have same `(row - col)`
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
All cells on same right diagonal have same `(row + col)`
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

## Step-by-Step Example (4-Queens)

### Execution Trace

**Row 0: Try column 0**
```
Q . . .    Place queen → Move to row 1
. . . .
. . . .
. . . .
```

**Row 1: Try all columns**
```
Q . . .
Q . . .    Column 0: ✗ (column attack)
. . . .
. . . .

Q . . .
. Q . .    Column 1: ✗ (diagonal attack)
. . . .
. . . .

Q . . .
. . Q .    Column 2: ✓ Place → Move to row 2
. . . .
. . . .
```

**Row 2: Try all columns**
```
No valid position found!
BACKTRACK to row 1
```

**Continue searching...**

**Final Solution Found:**
```
    0 1 2 3
  ┌────────┐
0 │ . Q . . │
1 │ . . . Q │
2 │ Q . . . │
3 │ . . Q . │
  └────────┘

board[] = {1, 3, 0, 2} ✓
```

---

## Java Implementation Details

### Static Variable for Count
```java
static int solutionCount = 0;
```

### Print Solution
```java
public static void printSolution(int[] board, int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (board[i] == j)
                System.out.print("Q ");
            else
                System.out.print(". ");
        }
        System.out.println();
    }
    System.out.println();
}
```

### Main Method
```java
public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    
    System.out.print("Enter number of queens (N): ");
    int n = sc.nextInt();
    
    if (n < 4 && n != 1) {
        System.out.println("No solution exists for N = " + n);
        sc.close();
        return;
    }
    
    int[] board = new int[n];
    for (int i = 0; i < n; i++)
        board[i] = -1;
    
    solutionCount = 0;
    
    if (!solveNQueens(board, 0, n)) {
        System.out.println("No solution exists");
    } else {
        System.out.println("Total solutions found: " + solutionCount);
    }
    
    sc.close();
}
```

---

## Time and Space Complexity

### Time Complexity
O(N!) in worst case
- Each row has N choices initially
- Choices reduce as queens are placed
- Total: N × (N-2) × (N-4) × ... ≈ N!

### Space Complexity
- **Recursion Stack**: O(N)
- **Board Storage**: O(N)
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

---

## Finding All vs First Solution

### Find All Solutions (Current)
```java
if (solveNQueens(board, row + 1, n))
    foundSolution = true;  // Continue searching
board[row] = -1;  // Always backtrack
```

### Find First Solution Only
```java
if (solveNQueens(board, row + 1, n))
    return true;  // Stop immediately
board[row] = -1;
```

---

## How to Compile and Run

```bash
# Compile
javac NQueens.java

# Run
java NQueens
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

## Common Mistakes

### 1. Incorrect Diagonal Check
```java
// ✗ Wrong
if (Math.abs(board[i] - col) == Math.abs(i - row))

// ✓ Correct (more efficient)
if (board[i] - i == col - row || board[i] + i == col + row)
```

### 2. Not Backtracking
```java
// ✗ Wrong - doesn't reset
board[row] = col;
solveNQueens(board, row + 1, n);
// Missing: board[row] = -1;

// ✓ Correct
board[row] = col;
solveNQueens(board, row + 1, n);
board[row] = -1;  // Backtrack!
```

### 3. Array Initialization
```java
// ✗ Wrong - default is 0, not -1
int[] board = new int[n];

// ✓ Correct - initialize to -1
int[] board = new int[n];
for (int i = 0; i < n; i++)
    board[i] = -1;
```

---

## Optimization Techniques

### 1. Bit Manipulation
Use bit arrays for faster checking:
```java
boolean[] cols = new boolean[n];
boolean[] diag1 = new boolean[2*n - 1];
boolean[] diag2 = new boolean[2*n - 1];
```

### 2. Symmetry Elimination
Reduce search by 8x using rotations/reflections

### 3. Heuristic Ordering
Try columns with fewer conflicts first

---

## Key Backtracking Concepts

### State Space Tree
```
              Root (empty)
            /  |  |  \
       Col0 Col1 Col2 Col3  (Row 0)
       /      |
   Col0-3  Col0-3  (Row 1)
     /       |
   ...     ...
```

### Pruning
When `isSafe()` returns false, entire subtree is pruned.

### Backtracking Template
```java
backtrack(state):
    if is_solution(state):
        output(state)
    
    for choice in get_choices(state):
        if is_valid(choice):
            make_choice(choice)
            backtrack(new_state)
            undo_choice(choice)  // BACKTRACK
```

---

## Applications of Backtracking

1. **Puzzles**: Sudoku, Crosswords, Maze solving
2. **Games**: Chess, Go
3. **Constraint Satisfaction**: Graph Coloring, Scheduling
4. **Combinatorial**: Permutations, Subsets

---

## Key Takeaways

1. **Backtracking**: Try → Check → Fail → Undo → Try next
2. **Recursion**: Natural fit for state space exploration
3. **Pruning**: Skip invalid branches for efficiency
4. **N-Queens**: Classic backtracking demonstration
5. **Time Complexity**: O(N!) but pruning helps significantly
6. **Java**: Use static for solution count, -1 for empty cell

---

## Next Steps

- **Practical 8**: Travelling Salesman (Branch and Bound)
- **Practice**: Sudoku Solver, Rat in a Maze
- **Optimization**: Bit manipulation, heuristics
