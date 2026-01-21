# Practical 6: Bellman-Ford Algorithm (Dynamic Programming)

## Overview
This practical implements the Bellman-Ford algorithm using Dynamic Programming to find the shortest path from a source vertex to all other vertices in a weighted directed graph. It also handles negative weight edges and detects negative weight cycles.

---

## Bellman-Ford Algorithm (`bellman_ford.cpp`)

### Problem Statement
Given a weighted directed graph with V vertices and E edges, and a source vertex S, find the shortest distance from S to all other vertices. The graph may contain negative weight edges.

---

## Algorithm Explanation

### Dynamic Programming Approach
The algorithm uses the principle of **relaxation** repeatedly to find shortest paths.

### Core Idea
- After i iterations, the shortest paths with at most i edges are computed
- After (V-1) iterations, all shortest paths are found (since any shortest path has at most V-1 edges)
- A Vth iteration checks for negative cycles

### Algorithm Steps
```cpp
bellmanFord(edges[], V, E, src):
    1. Initialize distances:
       dist[src] = 0
       dist[all other vertices] = ∞
    
    2. Relax all edges (V-1) times:
       for i = 1 to V-1:
           for each edge (u, v) with weight w:
               if dist[u] + w < dist[v]:
                   dist[v] = dist[u] + w
    
    3. Check for negative cycles:
       for each edge (u, v) with weight w:
           if dist[u] + w < dist[v]:
               return "Negative cycle detected"
    
    4. Return dist[]
```

---

## Why (V-1) Iterations?

### Path Length Analysis
- A simple path (no cycles) has at most (V-1) edges
- After i iterations, we have shortest paths using at most i edges
- After (V-1) iterations, all shortest simple paths are found

### Example
```
Graph with 4 vertices (V=4):
Longest simple path has 3 edges (V-1)

Iteration 0: Source vertex known
Iteration 1: Paths with ≤1 edge found
Iteration 2: Paths with ≤2 edges found  
Iteration 3: Paths with ≤3 edges found → All shortest paths!
```

---

## Time Complexity Analysis

### Detailed Breakdown
```
1. Initialization: O(V)
   - Set all distances to infinity
   - Set source distance to 0

2. Relaxation Phase: O(V × E)
   - V-1 iterations
   - Each iteration checks E edges
   - Total: (V-1) × E = O(V × E)

3. Negative Cycle Check: O(E)
   - One more pass through all edges

Total Time Complexity: O(V × E)
```

### Verification in Code
```cpp
auto start = high_resolution_clock::now();

// Main algorithm here (V-1 iterations of E edges)
for (int i = 1; i <= V - 1; i++) {
    for (int j = 0; j < E; j++) {
        // Relaxation: O(1) per edge
    }
}

auto stop = high_resolution_clock::now();
auto duration = duration_cast<microseconds>(stop - start);

cout << "Time Complexity: O(V*E) = O(" << V << "*" << E << ")" << endl;
cout << "Execution Time: " << duration.count() << " microseconds" << endl;
```

---

## Space Complexity

O(V) - for storing distances array

---

## Edge Relaxation Concept

### What is Relaxation?
```
For edge (u → v) with weight w:
if dist[u] + w < dist[v]:
    dist[v] = dist[u] + w  // Relax the edge
```

This means: "Can we improve the path to v by going through u?"

### Relaxation Example
```
Initial: dist[u] = 5, dist[v] = 10
Edge: u → v with weight 3

Check: 5 + 3 < 10?
       8 < 10 ✓

Update: dist[v] = 8 (path improved!)
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
```
dist[0] = 0
dist[1] = ∞
dist[2] = ∞
dist[3] = ∞
dist[4] = ∞
```

### Iteration 1 (i=1)
```
Edge 0→1: dist[1] = min(∞, 0 + (-1)) = -1
Edge 0→2: dist[2] = min(∞, 0 + 4) = 4
Edge 1→2: dist[2] = min(4, -1 + 3) = 2
Edge 1→3: dist[3] = min(∞, -1 + 2) = 1
Edge 1→4: dist[4] = min(∞, -1 + 2) = 1
Edge 3→2: No change
Edge 3→1: No change
Edge 4→3: dist[3] = min(1, 1 + (-3)) = -2

After Iteration 1: [0, -1, 2, -2, 1]
```

### Iteration 2 (i=2)
```
Edge 4→3: dist[3] = min(-2, 1 + (-3)) = -2
Edge 3→1: dist[1] = min(-1, -2 + 1) = -1
Edge 1→2: dist[2] = min(2, -1 + 3) = 2

After Iteration 2: [0, -1, 2, -2, 1]
```

### Iteration 3 (i=3)
```
No changes occur

After Iteration 3: [0, -1, 2, -2, 1]
```

### Iteration 4 (i=4)
```
No changes occur

After Iteration 4: [0, -1, 2, -2, 1]
```

### Negative Cycle Check
```
Check all edges again:
No edge can be relaxed further
→ No negative cycle detected
```

### Final Result
```
Vertex    Distance from Source(0)
  0              0
  1             -1
  2              2
  3             -2
  4              1
```

---

## Negative Weight Cycle Detection

### What is a Negative Cycle?
A cycle whose sum of edge weights is negative.

```
Example:
Cycle: 1 → 2 → 3 → 1
Weights: 1 + (-3) + 1 = -1 (negative!)

Problem: Can keep going around cycle to reduce path length indefinitely
         → No shortest path exists!
```

### Detection Method
```
After V-1 iterations:
- All shortest paths should be finalized
- If we can still relax an edge → negative cycle exists

for each edge (u, v):
    if dist[u] + weight < dist[v]:
        return "Negative cycle detected"
```

### Example with Negative Cycle
```
Graph:
0 → 1 (weight: 1)
1 → 2 (weight: -3)
2 → 1 (weight: 1)

Cycle: 1 → 2 → 1 with total weight = -2

After V-1 iterations:
dist[1] can still be reduced
→ Negative cycle detected!
```

---

## Comparison with Other Algorithms

| Algorithm | Negative Weights | Time Complexity | Space |
|-----------|------------------|-----------------|-------|
| Bellman-Ford | ✓ Yes | O(V × E) | O(V) |
| Dijkstra | ✗ No | O((V+E) log V) | O(V) |
| Floyd-Warshall | ✓ Yes | O(V³) | O(V²) |

### When to Use Bellman-Ford
1. Graph has negative weight edges
2. Need to detect negative cycles
3. Distributed systems (can be parallelized)
4. Small to medium graphs

### When NOT to Use
1. Large dense graphs (too slow)
2. All weights are positive (use Dijkstra instead)
3. Need all-pairs shortest paths (use Floyd-Warshall)

---

## Dynamic Programming Properties

### Optimal Substructure
Shortest path from s to v through u consists of:
1. Shortest path from s to u
2. Edge from u to v

### Overlapping Subproblems
- Same subproblems (shortest paths) computed multiple times
- DP table (dist array) stores results
- Avoids recomputation

---

## How to Compile and Run

```bash
# Compile
g++ bellman_ford.cpp -o bellman_ford

# Run
./bellman_ford
```

### Sample Input
```
Enter number of vertices: 5
Enter number of edges: 8
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
Shortest distances from source vertex 0:
Vertex          Distance
0               0
1               -1
2               2
3               -2
4               1

Time Complexity: O(V*E) = O(5*8)
Execution Time: 15 microseconds
```

### Sample Input (Negative Cycle)
```
Enter number of vertices: 3
Enter number of edges: 3
Edge 1 - Source: 0
Edge 1 - Destination: 1
Edge 1 - Weight: 1
Edge 2 - Source: 1
Edge 2 - Destination: 2
Edge 2 - Weight: -3
Edge 3 - Source: 2
Edge 3 - Destination: 1
Edge 3 - Weight: 1
Enter source vertex: 0
```

### Sample Output (Negative Cycle)
```
Graph contains negative weight cycle
```

---

## Key Takeaways

1. **Dynamic Programming**: Builds solution iteratively using relaxation
2. **Time Complexity**: O(V × E) - verified in code with timing
3. **Handles Negative Weights**: Unlike Dijkstra
4. **Detects Negative Cycles**: Extra iteration after V-1 iterations
5. **Simple Implementation**: Easy to code and understand
6. **Optimal Substructure**: Uses DP principle effectively

---

## Applications

1. **Network Routing**: Distance-vector routing protocols (RIP)
2. **Currency Arbitrage**: Detect profitable exchange rate cycles
3. **Social Networks**: Influence propagation with costs
4. **Resource Allocation**: Negative costs represent gains
