# Practical 8: Travelling Salesman Problem using Branch and Bound

## Overview
This practical implements the Travelling Salesman Problem (TSP) using the Branch and Bound technique with Least Cost (LC) strategy. TSP is an NP-hard problem that finds the shortest possible route visiting all cities exactly once and returning to the starting city.

---

## Travelling Salesman Problem

### Problem Statement
Given:
- N cities
- Cost matrix where cost[i][j] = cost to travel from city i to city j

Find:
- Minimum cost tour that visits each city exactly once and returns to starting city

### Example
```
Cities: 0, 1, 2, 3
Cost Matrix:
     0   1   2   3
0 [  0  10  15  20 ]
1 [ 10   0  35  25 ]
2 [ 15  35   0  30 ]
3 [ 20  25  30   0 ]

One tour: 0 → 1 → 2 → 3 → 0
Cost: 10 + 35 + 30 + 20 = 95

Optimal tour: 0 → 1 → 3 → 2 → 0
Cost: 10 + 25 + 30 + 15 = 80
```

---

## Branch and Bound Technique

### What is Branch and Bound?
A systematic method to explore solution space:
1. **Branch**: Divide problem into subproblems (branch)
2. **Bound**: Calculate lower bound for each subproblem
3. **Prune**: Discard subproblems whose bound exceeds best solution found

### Why Use Branch and Bound for TSP?
- **Exhaustive search**: N! possible tours (infeasible for large N)
- **Branch and Bound**: Prunes branches that cannot yield better solution
- **Optimal solution**: Guaranteed to find best tour

---

## Algorithm Explanation

### Lower Bound Calculation

The key to Branch and Bound is computing a **lower bound** for partial tours.

#### Reduced Cost Matrix Method
For each city, the minimum cost to leave must be included in any tour.

```
Lower Bound = Sum of (two smallest edges from each vertex) / 2
```

### First Min and Second Min
```cpp
firstMin(i):  // Smallest edge from vertex i
    return min(cost[i][k]) for all k ≠ i

secondMin(i): // Second smallest edge from vertex i
    return second_min(cost[i][k]) for all k ≠ i
```

### Initial Bound
```
Initial bound = Σ(firstMin(i) + secondMin(i)) / 2 for all vertices i
```

This gives a lower bound for any complete tour.

---

## Algorithm Steps

### Pseudocode
```cpp
TSP():
    1. Calculate initial lower bound
    2. Start with source city (0)
    3. Call TSPRec(bound, weight, level, path)

TSPRec(currBound, currWeight, level, currPath):
    // Base case: all cities visited
    if level == n:
        if edge exists from last city to first:
            totalCost = currWeight + cost[last][first]
            if totalCost < finalCost:
                Update best solution
        return
    
    // Try all unvisited cities
    for each city i:
        if city i not visited and edge exists:
            // Calculate new bound
            newBound = currBound - (edge costs)
            newWeight = currWeight + cost[current][i]
            
            // Prune if this path cannot beat best solution
            if newBound + newWeight < finalCost:
                Mark city i as visited
                currPath[level] = i
                TSPRec(newBound, newWeight, level+1, currPath)
                
                // Backtrack
                Mark city i as unvisited
```

---

## Detailed Example

### Input
```
Cities: 4 (0, 1, 2, 3)
Cost Matrix:
     0   1   2   3
0 [  0  10  15  20 ]
1 [  5   0  9   10 ]
2 [  6  13   0  12 ]
3 [  8   8   9   0 ]
```

### Step 1: Calculate Initial Bound
```
Vertex 0: firstMin = 10, secondMin = 15
Vertex 1: firstMin = 5,  secondMin = 9
Vertex 2: firstMin = 6,  secondMin = 12
Vertex 3: firstMin = 8,  secondMin = 8

Initial Bound = (10+15 + 5+9 + 6+12 + 8+8) / 2
              = 73 / 2 = 36.5 ≈ 36
```

### Step 2: State Space Tree
```
                      Root (City 0)
                      Bound = 36
                    /    |    \
                   1     2     3
                  /
         (0→1, Level 1)
         Weight = 10
         Bound adjustment...
              /    |
             2     3
            /
    (0→1→2, Level 2)
    Weight = 10+9=19
    Bound adjustment...
         /
        3
       /
(0→1→2→3, Level 3)
Weight = 19+12=31
Check return: 31+8=39

Continue exploring other branches...
```

### Step 3: Pruning Example
```
Path: 0 → 1
Current weight: 10
Current bound: 34
Total: 44

Path: 0 → 3
Current weight: 20
Current bound: 35
Total: 55

If best solution so far = 50:
- Path 0→1 continues (44 < 50) ✓
- Path 0→3 pruned (55 > 50) ✗
```

### Step 4: Final Solution
```
After exploring all branches:
Best tour: 0 → 1 → 2 → 3 → 0
Cost: 10 + 9 + 12 + 8 = 39

or

Best tour: 0 → 1 → 3 → 2 → 0
Cost: 10 + 10 + 9 + 6 = 35 ✓ (optimal)
```

---

## Bound Calculation in Detail

### Why Divide by 2?
Each edge is counted twice in the sum (once for each endpoint).

### Bound Update
When moving from city u to city v:
```
New Bound = Old Bound - (secondMin(u) + firstMin(v)) / 2

Why?
- We're committing to edge u→v
- Remove the "potential" of other edges from u and to v
```

### Example Bound Update
```
At city 0 (firstMin=10, secondMin=15)
Moving to city 1 (firstMin=5, secondMin=9)

Bound reduction = (15 + 5) / 2 = 10

If current bound = 36:
New bound = 36 - 10 = 26
```

---

## Time and Space Complexity

### Time Complexity
- **Best Case**: O(n²) - with heavy pruning
- **Average Case**: O(n² × 2ⁿ)
- **Worst Case**: O(n!) - no pruning, explores all tours

**In practice**: Much better than O(n!) due to pruning

### Space Complexity
- **Recursion Stack**: O(n)
- **Data Structures**: O(n²) for cost matrix
- **Total**: O(n²)

---

## Comparison with Other TSP Approaches

| Approach | Time Complexity | Optimal? | Notes |
|----------|----------------|----------|-------|
| Brute Force | O(n!) | Yes | Infeasible for n>12 |
| Branch & Bound | O(n² × 2ⁿ) | Yes | Pruning helps significantly |
| Dynamic Programming | O(n² × 2ⁿ) | Yes | Held-Karp algorithm |
| Greedy (Nearest Neighbor) | O(n²) | No | Fast but suboptimal |
| Genetic Algorithm | Varies | No | Good approximation |
| Simulated Annealing | Varies | No | Probabilistic |

---

## Advantages of Branch and Bound

1. **Optimal Solution**: Guaranteed to find best tour
2. **Pruning**: Avoids exploring suboptimal branches
3. **Bounding**: Guides search toward promising solutions
4. **Flexible**: Can be stopped early for approximate solution

---

## Limitations

1. **Still Exponential**: Worst case is O(n!)
2. **Memory**: Requires storing state information
3. **Not Scalable**: Practical only for small to medium n (up to ~20-25 cities)
4. **Heuristic Dependent**: Quality of bound affects performance

---

## Implementation Details

### State Representation
```cpp
currPath[level] = city     // Current tour path
visited[city] = true/false // City visit status
currWeight = accumulated   // Total cost so far
currBound = lower_bound    // Estimated remaining cost
```

### Backtracking
```cpp
visited[i] = true;           // Mark visited
currPath[level] = i;         // Add to path
TSPRec(...);                 // Recurse
visited[i] = false;          // Backtrack
```

### Pruning Condition
```cpp
if (currBound + currWeight < finalCost):
    explore this branch
else:
    prune (don't explore)
```

---

## How to Compile and Run

```bash
# Compile
g++ tsp_branch_bound.cpp -o tsp

# Run
./tsp
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
Minimum cost: 80
Path taken: 0 -> 1 -> 3 -> 2 -> 0
```

---

## Visualization of Branch and Bound

### State Space Tree
```
                    Start (City 0)
                    /    |    \
                   /     |     \
              City1   City2   City3
             /  |  \    ...     ...
            /   |   \
        City2 City3 City4
         ...   ...   ...
         
Legend:
✓ = Explored (bound < best)
✗ = Pruned (bound ≥ best)
⭐ = Best solution found
```

---

## Optimization Techniques

### 1. Better Bound Calculation
- Use Minimum Spanning Tree cost as bound
- More accurate bound → more pruning

### 2. Best-First Search
- Explore nodes with lowest bound first
- May find optimal solution faster

### 3. Dynamic Programming Integration
- Store subproblem results
- Avoid redundant calculations

---

## Real-World Applications

1. **Logistics**: Delivery route optimization
2. **Manufacturing**: Drilling circuit boards
3. **Genetics**: DNA sequencing
4. **Astronomy**: Telescope observation scheduling
5. **Tourism**: Tour planning

---

## Key Takeaways

1. **Branch and Bound**: Systematic exploration with pruning
2. **Bounding**: Lower bound guides search and enables pruning
3. **Optimal Solution**: Guaranteed but computationally expensive
4. **Pruning Power**: Effectiveness depends on bound quality
5. **Practical Limit**: Works for small to medium instances (n ≤ 25)

---

## Extensions and Variations

### Asymmetric TSP
Cost[i][j] ≠ Cost[j][i] (different costs for each direction)

### Multiple Salesmen
Multiple tours starting from same city

### Time Windows
Visit cities within specific time constraints

### TSP with Profits
Select subset of cities to maximize profit while minimizing cost

---

## Comparison with Backtracking

| Aspect | Branch & Bound | Backtracking |
|--------|----------------|--------------|
| Pruning | Based on bound | Based on constraints |
| Optimality | Finds optimal | Finds any solution |
| Efficiency | Uses bound to prune | Explores more states |
| Application | Optimization | Feasibility |

Branch and Bound is more sophisticated than pure backtracking because it uses bounds to intelligently prune the search space.
