# Practical 8: Travelling Salesman Problem using Branch and Bound (Java)

## Overview
This practical implements the Travelling Salesman Problem (TSP) using the Branch and Bound technique with Least Cost (LC) strategy in Java. TSP finds the shortest route visiting all cities exactly once and returning to the start.

---

## Travelling Salesman Problem

### Problem Statement
Given:
- N cities
- Cost matrix where `cost[i][j]` = cost to travel from city i to city j

Find:
- Minimum cost tour visiting each city exactly once and returning to start

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

Optimal: 0 → 1 → 3 → 2 → 0
Cost: 10 + 25 + 30 + 15 = 80 ✓
```

---

## Branch and Bound Technique

### Core Concepts
1. **Branch**: Divide problem into subproblems
2. **Bound**: Calculate lower bound for each subproblem
3. **Prune**: Discard branches that can't yield better solution

### Why Use for TSP?
- Exhaustive search: N! possible tours (infeasible)
- Branch and Bound: Prunes suboptimal branches
- Guaranteed: Finds optimal solution

---

## Lower Bound Calculation

### Method
```
Lower Bound = Sum of (two smallest edges from each vertex) / 2
```

### First and Second Min
```java
public static int firstMin(int i) {
    int min = Integer.MAX_VALUE;
    for (int k = 0; k < n; k++)
        if (cost[i][k] < min && i != k)
            min = cost[i][k];
    return min;
}

public static int secondMin(int i) {
    int first = Integer.MAX_VALUE, second = Integer.MAX_VALUE;
    for (int j = 0; j < n; j++) {
        if (i == j) continue;
        
        if (cost[i][j] <= first) {
            second = first;
            first = cost[i][j];
        } else if (cost[i][j] <= second && cost[i][j] != first) {
            second = cost[i][j];
        }
    }
    return second;
}
```

### Initial Bound
```java
int currBound = 0;
for (int i = 0; i < n; i++)
    currBound += (firstMin(i) + secondMin(i));
currBound = (currBound == 1) ? currBound / 2 + 1 : currBound / 2;
```

---

## Algorithm Implementation

```java
public static void TSPRec(int currBound, int currWeight, 
                          int level, int[] currPath) {
    // Base case: all cities visited
    if (level == n) {
        // Check if edge exists from last to first city
        if (cost[currPath[level - 1]][currPath[0]] != 0) {
            int currRes = currWeight + 
                         cost[currPath[level - 1]][currPath[0]];
            
            if (currRes < finalCost) {
                copyToFinal(currPath);
                finalCost = currRes;
            }
        }
        return;
    }
    
    // Try all unvisited cities
    for (int i = 0; i < n; i++) {
        if (cost[currPath[level - 1]][i] != 0 && !visited[i]) {
            int temp = currBound;
            currWeight += cost[currPath[level - 1]][i];
            
            // Update bound
            if (level == 1)
                currBound -= ((firstMin(currPath[level - 1]) + 
                              firstMin(i)) / 2);
            else
                currBound -= ((secondMin(currPath[level - 1]) + 
                              firstMin(i)) / 2);
            
            // Prune or explore
            if (currBound + currWeight < finalCost) {
                currPath[level] = i;
                visited[i] = true;
                
                TSPRec(currBound, currWeight, level + 1, currPath);
            }
            
            // Backtrack
            currWeight -= cost[currPath[level - 1]][i];
            currBound = temp;
            
            Arrays.fill(visited, false);
            for (int j = 0; j <= level - 1; j++)
                visited[currPath[j]] = true;
        }
    }
}
```

---

## Java-Specific Features

### Static Variables
```java
static int n;
static int[][] cost;
static int[] finalPath;
static boolean[] visited;
static int finalCost = Integer.MAX_VALUE;
```

### Arrays Class
```java
import java.util.*;

// Fill array with value
Arrays.fill(visited, false);

// Copy array
for (int i = 0; i < n; i++)
    finalPath[i] = currPath[i];
```

### 2D Array
```java
int[][] cost = new int[n][n];
```

---

## Step-by-Step Example

### Input
```
Cities: 4
Cost Matrix:
     0   1   2   3
0 [  0  10  15  20 ]
1 [  5   0   9  10 ]
2 [  6  13   0  12 ]
3 [  8   8   9   0 ]
```

### Initial Bound Calculation
```
Vertex 0: firstMin=10, secondMin=15
Vertex 1: firstMin=5,  secondMin=9
Vertex 2: firstMin=6,  secondMin=12
Vertex 3: firstMin=8,  secondMin=8

Initial Bound = (10+15 + 5+9 + 6+12 + 8+8) / 2
              = 73 / 2 = 36
```

### State Space Tree
```
                Root (City 0, Bound=36)
              /       |       \
         City1      City2    City3
      (W=10, B=34)  ...      ...
        /    |    \
      City2 City3 ...
         ...
```

### Pruning Example
```
Path: 0 → 1
Weight: 10, Bound: 34
Total: 44

Path: 0 → 3
Weight: 20, Bound: 35
Total: 55

If best so far = 50:
- 0→1 continues (44 < 50) ✓
- 0→3 pruned (55 > 50) ✗
```

---

## Time and Space Complexity

### Time Complexity
- **Best Case**: O(n²) with heavy pruning
- **Average Case**: O(n² × 2ⁿ)
- **Worst Case**: O(n!) without pruning

### Space Complexity
- **Recursion Stack**: O(n)
- **Cost Matrix**: O(n²)
- **Total**: O(n²)

---

## How to Compile and Run

```bash
# Compile
javac TravellingSalesman.java

# Run
java TravellingSalesman
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

## Comparison with Other Approaches

| Approach | Time | Optimal? | Notes |
|----------|------|----------|-------|
| Brute Force | O(n!) | Yes | Infeasible for n>12 |
| Branch & Bound | O(n²×2ⁿ) | Yes | Pruning helps |
| Dynamic Programming | O(n²×2ⁿ) | Yes | Held-Karp |
| Greedy | O(n²) | No | Fast approximation |
| Genetic Algorithm | Varies | No | Good approximate |

---

## Common Mistakes

### 1. Initial Bound Calculation
```java
// ✗ Wrong - integer division issues
currBound = (firstMin(i) + secondMin(i)) / 2;

// ✓ Correct - handle odd sum
currBound = (sum == 1) ? sum / 2 + 1 : sum / 2;
```

### 2. Visited Array Reset
```java
// ✗ Wrong - doesn't maintain state
Arrays.fill(visited, false);

// ✓ Correct - restore previous state
Arrays.fill(visited, false);
for (int j = 0; j <= level - 1; j++)
    visited[currPath[j]] = true;
```

### 3. Final Path Copy
```java
// ✗ Wrong - reference copy
finalPath = currPath;

// ✓ Correct - deep copy
for (int i = 0; i < n; i++)
    finalPath[i] = currPath[i];
finalPath[n] = currPath[0];  // Return to start
```

---

## Advantages and Limitations

### Advantages
1. **Optimal Solution**: Guaranteed
2. **Pruning**: Avoids suboptimal branches
3. **Flexible**: Can stop early for approximation

### Limitations
1. **Exponential**: Still O(n²×2ⁿ) in worst case
2. **Memory**: Stores state information
3. **Not Scalable**: Practical only for n ≤ 25

---

## Optimization Techniques

### 1. Better Bound
```java
// Use Minimum Spanning Tree cost as bound
// More accurate bound → more pruning
```

### 2. Best-First Search
```java
// Use priority queue to explore lowest bound first
// May find optimal faster
```

### 3. Symmetry Breaking
```java
// Reduce search space by fixing first city
// Divide by symmetry factor
```

---

## Real-World Applications

1. **Logistics**: Delivery route optimization
2. **Manufacturing**: PCB drilling, robot arm movement
3. **DNA Sequencing**: Fragment assembly
4. **Telescope Scheduling**: Observation planning
5. **Tourism**: Tour planning systems

---

## Key Takeaways

1. **Branch and Bound**: Systematic exploration with pruning
2. **Bounding**: Lower bound enables intelligent pruning
3. **Optimal**: Guaranteed but computationally expensive
4. **Pruning Power**: Effectiveness depends on bound quality
5. **Java Features**: Static variables, Arrays class
6. **Practical Limit**: Works for n ≤ 20-25 cities

---

## Comparison with Backtracking

| Aspect | Branch & Bound | Backtracking |
|--------|----------------|--------------|
| Pruning | Based on bound | Based on constraints |
| Goal | Optimization | Feasibility |
| Efficiency | Uses bound | Explores more |
| Use Case | Find optimal | Find any solution |

---

## Summary

This practical demonstrates:
- **Branch and Bound technique** for optimization
- **Lower bound calculation** for pruning
- **Recursive exploration** with intelligent pruning
- **Optimal solution** for small to medium instances
- Significantly better than brute force O(n!)

---

## Next Steps

- **Mini Project**: Apply DAA concepts to real problems
- **Study**: Approximation algorithms for large TSP
- **Practice**: More optimization problems
- **Compare**: DP (Held-Karp) vs Branch & Bound for TSP
