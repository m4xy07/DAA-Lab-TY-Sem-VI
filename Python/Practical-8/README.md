# Practical 8: Travelling Salesman Problem using Branch and Bound - Python

## Overview
This practical implements the Travelling Salesman Problem (TSP) using the Branch and Bound technique with Least Cost (LC) strategy in Python. TSP finds the shortest route visiting all cities exactly once and returning to the start.

---

## Travelling Salesman Problem (TSP)

### Problem Statement
Given:
- **N cities**
- **Cost matrix** where `cost[i][j]` = cost to travel from city i to city j

Find:
- **Minimum cost tour** visiting each city exactly once and returning to start

### Example
```
Cities: 4
Cost Matrix:
     0   1   2   3
0 [  0  10  15  20 ]
1 [ 10   0  35  25 ]
2 [ 15  35   0  30 ]
3 [ 20  25  30   0 ]

One tour: 0 → 1 → 2 → 3 → 0
Cost: 10 + 35 + 30 + 20 = 95

Optimal: 0 → 1 → 3 → 2 → 0
Cost: 10 + 25 + 30 + 15 = 80 ✓
```

---

## Branch and Bound Technique

### Core Concepts

1. **Branch**: Divide problem into subproblems
   - Each branch represents visiting a city
   
2. **Bound**: Calculate lower bound for each subproblem
   - Estimate minimum possible cost from current state
   
3. **Prune**: Discard branches that can't yield better solution
   - If lower bound ≥ best solution found, skip this branch

### Why Use Branch and Bound?
- **Exhaustive Search**: N! possible tours (infeasible for large N)
- **Branch and Bound**: Prunes suboptimal branches intelligently
- **Guaranteed Optimal**: Unlike heuristics

---

## Lower Bound Calculation

### Method
```
Lower Bound = Sum of (two smallest edges from each vertex) / 2
```

### Rationale
- Every tour uses exactly 2 edges per vertex (entering and leaving)
- Using two smallest edges gives optimistic estimate
- Divide by 2 because each edge counted twice

### Python Functions

```python
def first_min(cost, i, n):
    """Find minimum edge cost from vertex i"""
    min_cost = sys.maxsize
    for k in range(n):
        if cost[i][k] < min_cost and i != k:
            min_cost = cost[i][k]
    return min_cost


def second_min(cost, i, n):
    """Find second minimum edge cost from vertex i"""
    first = sys.maxsize
    second = sys.maxsize
    
    for j in range(n):
        if i == j:
            continue
        
        if cost[i][j] <= first:
            second = first
            first = cost[i][j]
        elif cost[i][j] <= second and cost[i][j] != first:
            second = cost[i][j]
    
    return second
```

---

## Python Implementation

```python
import sys

final_path = []
visited = []
final_cost = sys.maxsize


def tsp_recursive(cost, curr_bound, curr_weight, level, curr_path, n):
    """
    Solve TSP using Branch and Bound with LC strategy
    """
    global final_cost, final_path, visited
    
    # Base case: All cities visited
    if level == n:
        # Check if edge exists from last city to first
        if cost[curr_path[level - 1]][curr_path[0]] != 0:
            curr_res = curr_weight + cost[curr_path[level - 1]][curr_path[0]]
            
            # Update final result if better solution found
            if curr_res < final_cost:
                final_path = curr_path.copy()
                final_path.append(curr_path[0])  # Return to start
                final_cost = curr_res
        return
    
    # Try all unvisited cities
    for i in range(n):
        if cost[curr_path[level - 1]][i] != 0 and not visited[i]:
            temp = curr_bound
            curr_weight += cost[curr_path[level - 1]][i]
            
            # Update bound
            if level == 1:
                curr_bound -= (
                    (first_min(cost, curr_path[level - 1], n) + 
                     first_min(cost, i, n)) / 2
                )
            else:
                curr_bound -= (
                    (second_min(cost, curr_path[level - 1], n) + 
                     first_min(cost, i, n)) / 2
                )
            
            # Branch only if bound + current weight is promising
            if curr_bound + curr_weight < final_cost:
                curr_path[level] = i
                visited[i] = True
                
                # Recurse to next level
                tsp_recursive(cost, curr_bound, curr_weight, level + 1, curr_path, n)
            
            # Backtrack
            curr_weight -= cost[curr_path[level - 1]][i]
            curr_bound = temp
            
            # Reset visited array
            visited = [False] * n
            for j in range(level):
                visited[curr_path[j]] = True
```

---

## Python-Specific Features

### 1. sys.maxsize for Large Number
```python
import sys
final_cost = sys.maxsize  # Maximum integer value
```

### 2. Global Variables
```python
final_path = []
visited = []
final_cost = sys.maxsize

def tsp_recursive(...):
    global final_cost, final_path, visited
```

### 3. List Copy
```python
final_path = curr_path.copy()  # Create copy, not reference
```

### 4. List Methods
```python
final_path.append(curr_path[0])  # Add element
visited = [False] * n            # Initialize list
```

### 5. Floor Division
```python
curr_bound = curr_bound // 2  # Integer division
```

### 6. Conditional Assignment
```python
curr_bound = (sum // 2) if sum % 2 == 0 else (sum // 2) + 1
```

---

## Step-by-Step Example

### Input
```
Cities: 4
Cost Matrix:
     0   1   2   3
0 [  0  10  15  20 ]
1 [ 10   0  35  25 ]
2 [ 15  35   0  30 ]
3 [ 20  25  30   0 ]
```

### Initial Bound Calculation
```
Vertex 0: first_min=10, second_min=15
Vertex 1: first_min=10, second_min=25
Vertex 2: first_min=15, second_min=30
Vertex 3: first_min=20, second_min=25

Initial Bound = (10+15 + 10+25 + 15+30 + 20+25) / 2
              = 150 / 2 = 75
```

### State Space Tree (Partial)
```
                Root (City 0, Bound=75)
              /       |       \
         City1      City2    City3
      (W=10, B=65)  (W=15)   (W=20)
        /    |    \
      City2 City3 ...
         ...
```

### Pruning Example
```
Path: 0 → 1 → 2
Weight: 10 + 35 = 45
Bound: 50
Total: 95

If best_so_far = 80:
  95 > 80 → PRUNE this branch! ✗
  (No need to explore further)

Path: 0 → 1 → 3
Weight: 10 + 25 = 35
Bound: 40
Total: 75

  75 < 80 → CONTINUE exploring ✓
```

---

## Algorithm Flow

### Main Function
```python
def solve_tsp(cost, n):
    """Main function to solve TSP"""
    global final_cost, final_path, visited
    
    # Initialize
    curr_path = [-1] * (n + 1)
    visited = [False] * n
    
    # Calculate initial lower bound
    curr_bound = 0
    for i in range(n):
        curr_bound += first_min(cost, i, n) + second_min(cost, i, n)
    
    # Round up if odd
    curr_bound = (curr_bound // 2) if curr_bound % 2 == 0 else (curr_bound // 2) + 1
    
    # Start from vertex 0
    visited[0] = True
    curr_path[0] = 0
    
    # Solve recursively
    tsp_recursive(cost, curr_bound, 0, 1, curr_path, n)
```

---

## Complexity Analysis

### Time Complexity
- **Best Case**: O(n²) with heavy pruning
- **Average Case**: O(n² × 2ⁿ)
- **Worst Case**: O(n!) without pruning

### Space Complexity
- **Recursion Stack**: O(n)
- **Cost Matrix**: O(n²)
- **Total**: O(n²)

### Why Better Than Brute Force?
```
For n=10 cities:
Brute Force: 10! = 3,628,800 tours
Branch & Bound: ~10,000-100,000 nodes (with good pruning)

Reduction: ~97-99%!
```

---

## How to Run

```bash
python travelling_salesman.py
```

### Sample Input
```
Enter number of cities: 4
Enter cost matrix (use 0 for no direct path):
Cost[0][0]: 0
Cost[0][1]: 10
Cost[0][2]: 15
Cost[0][3]: 20
Cost[1][0]: 10
Cost[1][1]: 0
Cost[1][2]: 35
Cost[1][3]: 25
Cost[2][0]: 15
Cost[2][1]: 35
Cost[2][2]: 0
Cost[2][3]: 30
Cost[3][0]: 20
Cost[3][1]: 25
Cost[3][2]: 30
Cost[3][3]: 0
```

### Sample Output
```
============================================================
TRAVELLING SALESMAN PROBLEM - Branch and Bound (LC)
============================================================

Cost Matrix:
       0   1   2   3
  0:   0  10  15  20
  1:  10   0  35  25
  2:  15  35   0  30
  3:  20  25  30   0

============================================================
SOLVING TSP...
============================================================

============================================================
SOLUTION:
============================================================
Minimum cost: 80

Path taken:
0 -> 1 -> 3 -> 2 -> 0

============================================================
COMPLEXITY ANALYSIS:
============================================================
Number of cities: 4
Time Complexity: O(n^2 * 2^n)
Space Complexity: O(n^2)
============================================================
```

---

## Comparison with Other Approaches

| Approach | Time | Optimal? | Space | Notes |
|----------|------|----------|-------|-------|
| **Brute Force** | O(n!) | Yes | O(n) | Too slow |
| **Branch & Bound** | O(n²×2ⁿ) | Yes | O(n²) | Pruning helps |
| **Dynamic Programming** | O(n²×2ⁿ) | Yes | O(n×2ⁿ) | Held-Karp |
| **Greedy (Nearest Neighbor)** | O(n²) | No | O(n) | Fast approximation |
| **Genetic Algorithm** | Varies | No | Varies | Good approximate |

---

## Common Mistakes

### 1. Not Resetting Visited Array
```python
# ✗ Wrong - doesn't maintain state properly
visited[i] = False

# ✓ Correct - restore previous visited state
visited = [False] * n
for j in range(level):
    visited[curr_path[j]] = True
```

### 2. Incorrect Bound Calculation
```python
# ✗ Wrong - integer division issues
curr_bound = (first_min(i) + second_min(i)) / 2

# ✓ Correct - handle odd sum
sum_val = first_min(i) + second_min(i)
curr_bound = sum_val // 2 if sum_val % 2 == 0 else sum_val // 2 + 1
```

### 3. Not Copying List
```python
# ✗ Wrong - reference copy
final_path = curr_path

# ✓ Correct - deep copy
final_path = curr_path.copy()
```

### 4. Forgetting to Return to Start
```python
# ✗ Wrong - doesn't complete tour
final_path = curr_path.copy()

# ✓ Correct - add return edge
final_path = curr_path.copy()
final_path.append(curr_path[0])
```

---

## Advantages and Limitations

### Advantages
1. **Optimal Solution**: Guaranteed
2. **Pruning**: Avoids many suboptimal branches
3. **Flexible**: Can stop early for approximate solution
4. **Better than Brute Force**: Significantly fewer nodes explored

### Limitations
1. **Still Exponential**: O(n²×2ⁿ) in worst case
2. **Memory**: Stores state information
3. **Not Scalable**: Practical only for n ≤ 20-25
4. **Bound Quality**: Effectiveness depends on lower bound calculation

---

## Real-World Applications

1. **Logistics**: Delivery route optimization (Amazon, UPS)
2. **Manufacturing**: PCB drilling, robot arm movement
3. **DNA Sequencing**: Fragment assembly
4. **Telescope Scheduling**: Observation planning
5. **Tourism**: Tour planning, GPS navigation
6. **Circuit Design**: Wire routing

---

## Key Takeaways

1. **Branch and Bound**: Systematic exploration with intelligent pruning
2. **Lower Bound**: Enables pruning of unpromising branches
3. **Optimal Guarantee**: Finds best solution (unlike heuristics)
4. **Pruning Power**: Effectiveness depends on bound quality
5. **Python Features**: `sys.maxsize`, global variables, list operations
6. **Practical Limit**: Works for n ≤ 20-25 cities
7. **Time vs Optimality**: Slower than heuristics but guarantees optimal

---

## Optimization Tips

### 1. Better Initial Bound
```python
# Use nearest neighbor heuristic for initial upper bound
initial_bound = nearest_neighbor_heuristic(cost, n)
final_cost = initial_bound  # Better starting point
```

### 2. Priority Queue
```python
# Use priority queue for best-first search
import heapq
# Explore nodes with lowest bounds first
```

### 3. Symmetry Breaking
```python
# Fix first city to reduce search space
# If path 0→1→2→0 optimal, 1→2→0→1 also optimal
```

---

## Practice Problems

1. Implement TSP with time windows (cities have time constraints)
2. TSP with multiple salesman
3. Compare with Held-Karp DP algorithm
4. Implement nearest neighbor heuristic
5. Visualize search tree and pruning

---

## Summary

This practical demonstrates:
- **Branch and Bound**: Optimal solution with pruning
- **Lower Bound Calculation**: Key to effective pruning
- **Recursive Exploration**: Systematic search with backtracking
- **Optimal for Small Instances**: n ≤ 25 cities
- **Significantly Better**: Than brute force O(n!)
- **Python Implementation**: Clean and readable code

---

## Next Steps
- **Mini Project**: Apply DAA concepts to real-world problems
- **Study**: Approximation algorithms for large TSP instances
- **Compare**: Branch & Bound vs DP (Held-Karp) vs Heuristics
- **Practice**: More optimization problems with B&B
