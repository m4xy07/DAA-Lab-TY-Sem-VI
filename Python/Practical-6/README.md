# Practical 6: Bellman-Ford Algorithm (Dynamic Programming) - Python

## Overview
This practical implements the Bellman-Ford algorithm using Dynamic Programming in Python to find shortest paths from a source vertex to all other vertices in a weighted directed graph. It handles **negative weight edges** and **detects negative weight cycles**.

---

## What is Bellman-Ford Algorithm?

### Purpose
Find shortest path from a **single source** to **all other vertices** in a weighted directed graph.

### Key Features
1. **Handles Negative Weights**: Unlike Dijkstra
2. **Detects Negative Cycles**: Can identify if negative cycle exists
3. **Dynamic Programming**: Builds solution iteratively
4. **Time Complexity Verification**: Practical includes timing measurement

---

## Algorithm Overview

### Core Idea
- After **i iterations**, shortest paths with at most **i edges** are computed
- After **(V-1) iterations**, all shortest paths found (any simple path has at most V-1 edges)
- A **Vth iteration** checks for negative weight cycles

### Why V-1 Iterations?
```
In a graph with V vertices:
- Any simple path has at most V-1 edges
- After i iterations: optimal paths using ≤ i edges
- After V-1 iterations: all shortest simple paths found
```

---

## Python Implementation

```python
import time

class Edge:
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight


def bellman_ford(edges, num_vertices, num_edges, source):
    """
    Find shortest paths from source to all vertices using Bellman-Ford
    Returns: (distances, has_negative_cycle)
    """
    # Initialize distances
    dist = [float('inf')] * num_vertices
    dist[source] = 0
    
    # Relax all edges V-1 times
    for i in range(num_vertices - 1):
        for edge in edges:
            if dist[edge.src] != float('inf') and \
               dist[edge.src] + edge.weight < dist[edge.dest]:
                dist[edge.dest] = dist[edge.src] + edge.weight
    
    # Check for negative-weight cycles
    has_negative_cycle = False
    for edge in edges:
        if dist[edge.src] != float('inf') and \
           dist[edge.src] + edge.weight < dist[edge.dest]:
            has_negative_cycle = True
            break
    
    return dist, has_negative_cycle
```

---

## Python-Specific Features

### 1. Class for Edge
```python
class Edge:
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight
```

### 2. float('inf') for Infinity
```python
dist = [float('inf')] * num_vertices
```
Represents infinity, can be compared with numbers.

### 3. List Multiplication
```python
dist = [float('inf')] * num_vertices
# Creates list with num_vertices copies of inf
```

### 4. Backslash for Line Continuation
```python
if dist[edge.src] != float('inf') and \
   dist[edge.src] + edge.weight < dist[edge.dest]:
```

### 5. time Module
```python
import time
start_time = time.perf_counter()
# ... algorithm ...
end_time = time.perf_counter()
duration_us = (end_time - start_time) * 1_000_000  # microseconds
```

### 6. Underscore in Numbers (Python 3.6+)
```python
duration_us = (end_time - start_time) * 1_000_000
# Underscore for readability: 1_000_000 = 1000000
```

---

## Edge Relaxation Explained

### What is Relaxation?
```python
# For edge (u → v) with weight w:
if dist[u] + w < dist[v]:
    dist[v] = dist[u] + w  # Relax the edge
```

**Question**: Can we improve the path to v by going through u?

### Example
```
Current distances:
dist[u] = 5
dist[v] = 10

Edge: u → v with weight 3

Check: 5 + 3 < 10?
       8 < 10 ✓

Update: dist[v] = 8
(Found better path to v through u!)
```

---

## Step-by-Step Example

### Graph
```
Vertices: 5 (0, 1, 2, 3, 4)
Edges:
0 → 1 (weight: -1)
0 → 2 (weight: 4)
1 → 2 (weight: 3)
1 → 3 (weight: 2)
1 → 4 (weight: 2)
3 → 2 (weight: 5)
3 → 1 (weight: 1)
4 → 3 (weight: -3)

Source: 0
```

### Initialization
```python
dist = [0, inf, inf, inf, inf]
       ↑
    source
```

### Iteration 1 (Relax all edges once)
```
Process 0→1: dist[1] = min(inf, 0 + (-1)) = -1
Process 0→2: dist[2] = min(inf, 0 + 4) = 4
Process 1→2: dist[2] = min(4, -1 + 3) = 2
Process 1→3: dist[3] = min(inf, -1 + 2) = 1
Process 1→4: dist[4] = min(inf, -1 + 2) = 1
Process 3→2: dist[2] = min(2, 1 + 5) = 2 (no change)
Process 3→1: dist[1] = min(-1, 1 + 1) = -1 (no change)
Process 4→3: dist[3] = min(1, 1 + (-3)) = -2

After Iteration 1:
dist = [0, -1, 2, -2, 1]
```

### Iteration 2
```
Process 0→1: No change (0 + (-1) = -1)
Process 0→2: No change
Process 1→2: No change
Process 1→3: No change
Process 1→4: No change
Process 3→2: dist[2] = min(2, -2 + 5) = 2 (no change)
Process 3→1: dist[1] = min(-1, -2 + 1) = -1 (no change)
Process 4→3: No change

After Iteration 2:
dist = [0, -1, 2, -2, 1]
```

### Iterations 3 and 4
No changes occur (already optimal).

### Final Distances
```
Vertex    Distance from Source 0
  0              0
  1             -1
  2              2
  3             -2
  4              1
```

---

## Negative Cycle Detection

### What is a Negative Cycle?
A cycle whose sum of edge weights is **negative**.

```
Example:
Cycle: 1 → 2 → 3 → 1
Weights: 5 + (-10) + 3 = -2 (negative!)

Problem: Can keep going around to reduce distance indefinitely
```

### Detection Method
```python
# After V-1 iterations, check if any edge can still be relaxed
for edge in edges:
    if dist[edge.src] != float('inf') and \
       dist[edge.src] + edge.weight < dist[edge.dest]:
        # If we can still improve, negative cycle exists!
        has_negative_cycle = True
        break
```

### Why This Works?
- After V-1 iterations, all shortest paths should be found
- If we can still improve a distance, it means we're going through a cycle
- And that cycle must be negative (otherwise wouldn't improve)

---

## Time Complexity Analysis

### Detailed Breakdown
```python
# 1. Initialization: O(V)
dist = [float('inf')] * num_vertices
dist[source] = 0

# 2. Relaxation Phase: O(V × E)
for i in range(num_vertices - 1):     # V-1 iterations
    for edge in edges:                 # E edges
        # Constant time relaxation

# 3. Negative Cycle Check: O(E)
for edge in edges:
    # Check each edge once

Total: O(V) + O(V × E) + O(E) = O(V × E)
```

### Verification in Code
```python
print(f"Time Complexity: O(V × E) = O({num_vertices} × {num_edges})")
print(f"Execution Time: {duration_us:.2f} microseconds")
```

---

## Space Complexity
**O(V)** - Only stores distances array

---

## How to Run

```bash
python bellman_ford.py
```

### Sample Input
```
Enter number of vertices: 5
Enter number of edges: 8
Enter 8 edges (source destination weight):
Edge 1 - Source: 0
Edge 1 - Destination: 1
Edge 1 - Weight: -1
Edge 2 - Source: 0
Edge 2 - Destination: 2
Edge 2 - Weight: 4
Edge 3 - Source: 1
Edge 3 - Destination: 2
Edge 3 - Weight: 3
Edge 4 - Source: 1
Edge 4 - Destination: 3
Edge 4 - Weight: 2
Edge 5 - Source: 1
Edge 5 - Destination: 4
Edge 5 - Weight: 2
Edge 6 - Source: 3
Edge 6 - Destination: 2
Edge 6 - Weight: 5
Edge 7 - Source: 3
Edge 7 - Destination: 1
Edge 7 - Weight: 1
Edge 8 - Source: 4
Edge 8 - Destination: 3
Edge 8 - Weight: -3

Enter source vertex: 0
```

### Sample Output
```
============================================================
BELLMAN-FORD ALGORITHM (Dynamic Programming)
============================================================

============================================================
RUNNING BELLMAN-FORD ALGORITHM...
============================================================

Shortest distances from source vertex 0
------------------------------
Vertex     Distance  
------------------------------
0          0         
1          -1        
2          2         
3          -2        
4          1         

============================================================
TIME COMPLEXITY ANALYSIS:
============================================================
Vertices (V): 5
Edges (E): 8
Time Complexity: O(V × E) = O(5 × 8)
Execution Time: 12.50 microseconds
============================================================
```

### Sample with Negative Cycle
```
Graph with cycle:
1 → 2 (weight: 1)
2 → 3 (weight: -3)
3 → 1 (weight: 1)

Output:
⚠ Graph contains negative weight cycle!
Shortest paths are not defined.
```

---

## Comparison with Other Algorithms

| Algorithm | Negative Weights | Time Complexity | Space | Use Case |
|-----------|------------------|-----------------|-------|----------|
| **Bellman-Ford** | ✓ Yes | O(V × E) | O(V) | Negative weights |
| **Dijkstra** | ✗ No | O((V+E) log V) | O(V) | All positive |
| **Floyd-Warshall** | ✓ Yes | O(V³) | O(V²) | All-pairs shortest path |

---

## Common Mistakes

### 1. Not Checking for Infinity
```python
# ✗ Wrong - may cause issues if dist[u] is inf
if dist[edge.src] + edge.weight < dist[edge.dest]:
    dist[edge.dest] = dist[edge.src] + edge.weight

# ✓ Correct - check for infinity first
if dist[edge.src] != float('inf') and \
   dist[edge.src] + edge.weight < dist[edge.dest]:
    dist[edge.dest] = dist[edge.src] + edge.weight
```

### 2. Wrong Number of Iterations
```python
# ✗ Wrong - should be V-1
for i in range(num_vertices):

# ✓ Correct - exactly V-1 times
for i in range(num_vertices - 1):
```

### 3. Forgetting Negative Cycle Check
```python
# ✗ Wrong - doesn't detect negative cycles
def bellman_ford(edges, num_vertices, source):
    # ... only does V-1 iterations ...
    return dist

# ✓ Correct - includes Vth iteration check
def bellman_ford(edges, num_vertices, source):
    # ... V-1 iterations ...
    # Check for negative cycle
    for edge in edges:
        if dist[edge.src] + edge.weight < dist[edge.dest]:
            return dist, True  # Has negative cycle
```

---

## Applications

1. **Network Routing**: Distance-vector routing protocols (RIP)
2. **Currency Arbitrage**: Detect profitable exchange rate cycles
3. **Resource Allocation**: Negative costs represent gains
4. **Social Networks**: Influence propagation with negative effects
5. **Game Theory**: Payoff maximization

---

## Why Dynamic Programming?

### DP Characteristics in Bellman-Ford

1. **Optimal Substructure**:
   - Shortest path to v through u uses shortest path to u
   
2. **Overlapping Subproblems**:
   - Same vertices processed multiple times
   - Each iteration refines previous results

3. **Bottom-Up Approach**:
   - Start with source (distance 0)
   - Build up distances iteratively

---

## Optimization: Early Termination

```python
def bellman_ford_optimized(edges, num_vertices, source):
    dist = [float('inf')] * num_vertices
    dist[source] = 0
    
    for i in range(num_vertices - 1):
        changed = False
        
        for edge in edges:
            if dist[edge.src] != float('inf') and \
               dist[edge.src] + edge.weight < dist[edge.dest]:
                dist[edge.dest] = dist[edge.src] + edge.weight
                changed = True
        
        # If no changes, we're done!
        if not changed:
            break
    
    return dist
```

---

## Key Takeaways

1. **Dynamic Programming**: Builds solution iteratively over V-1 iterations
2. **Handles Negative Weights**: Unlike Dijkstra's algorithm
3. **Negative Cycle Detection**: Extra iteration after V-1
4. **Time Complexity**: O(V × E), verified with timing
5. **Edge Relaxation**: Core operation, checks if path can be improved
6. **Python Features**: `float('inf')`, classes, time measurement
7. **Simple Implementation**: Straightforward nested loops

---

## Practice Problems

1. Implement with adjacency list instead of edge list
2. Print the actual shortest path, not just distances
3. Handle disconnected graphs
4. Modify to find longest path (hint: negate weights)

---

## Next Steps
- **Practical 7**: N-Queens Problem (Backtracking)
- **Compare**: Bellman-Ford vs Dijkstra performance
- **Study**: More DP algorithms (Floyd-Warshall, Matrix Chain Multiplication)
