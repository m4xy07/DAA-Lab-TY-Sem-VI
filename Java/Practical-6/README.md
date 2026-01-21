# Practical 6: Bellman-Ford Algorithm (Dynamic Programming) - Java

## Overview
This practical implements the Bellman-Ford algorithm using Dynamic Programming in Java to find the shortest path from a source vertex to all other vertices in a weighted directed graph. It handles negative weight edges and detects negative weight cycles.

---

## Bellman-Ford Algorithm (`BellmanFord.java`)

### Problem Statement
Given a weighted directed graph with V vertices and E edges, and a source vertex S, find the shortest distance from S to all other vertices. The graph may contain negative weight edges.

---

## Edge Class

```java
class Edge {
    int src, dest, weight;
    
    Edge(int src, int dest, int weight) {
        this.src = src;
        this.dest = dest;
        this.weight = weight;
    }
}
```

---

## Algorithm Implementation

```java
public static void bellmanFord(Edge[] edges, int V, int E, int src) {
    int[] dist = new int[V];
    
    // Initialize distances
    for (int i = 0; i < V; i++)
        dist[i] = Integer.MAX_VALUE;
    dist[src] = 0;
    
    long startTime = System.nanoTime();
    
    // Relax all edges V-1 times
    for (int i = 1; i <= V - 1; i++) {
        for (int j = 0; j < E; j++) {
            int u = edges[j].src;
            int v = edges[j].dest;
            int weight = edges[j].weight;
            
            if (dist[u] != Integer.MAX_VALUE && 
                dist[u] + weight < dist[v]) {
                dist[v] = dist[u] + weight;
            }
        }
    }
    
    long endTime = System.nanoTime();
    long duration = (endTime - startTime) / 1000; // microseconds
    
    // Check for negative-weight cycles
    boolean hasNegativeCycle = false;
    for (int i = 0; i < E; i++) {
        int u = edges[i].src;
        int v = edges[i].dest;
        int weight = edges[i].weight;
        
        if (dist[u] != Integer.MAX_VALUE && 
            dist[u] + weight < dist[v]) {
            hasNegativeCycle = true;
            break;
        }
    }
    
    // Print results
    if (hasNegativeCycle) {
        System.out.println("Graph contains negative weight cycle");
    } else {
        printDistances(dist, V, src);
    }
    
    System.out.println("\nTime Complexity: O(V*E) = O(" + V + "*" + E + ")");
    System.out.println("Execution Time: " + duration + " microseconds");
}
```

---

## Dynamic Programming Approach

### Core Idea
- After i iterations, shortest paths with **at most i edges** are computed
- After (V-1) iterations, all shortest paths are found
- A Vth iteration checks for negative cycles

### Why (V-1) Iterations?
- Any simple path (no cycles) has at most (V-1) edges
- After i iterations: paths using ≤i edges are optimal
- After (V-1) iterations: all shortest simple paths are found

---

## Edge Relaxation

### Concept
```java
// For edge (u → v) with weight w:
if (dist[u] + weight < dist[v]) {
    dist[v] = dist[u] + weight;  // Relax the edge
}
```

This means: "Can we improve the path to v by going through u?"

### Example
```
dist[u] = 5, dist[v] = 10
Edge: u → v with weight 3

Check: 5 + 3 < 10?
       8 < 10 ✓

Update: dist[v] = 8 (path improved!)
```

---

## Time Complexity

### Detailed Breakdown
```
1. Initialization: O(V)
2. Relaxation Phase: O(V × E)
   - V-1 iterations
   - Each checks E edges
3. Negative Cycle Check: O(E)

Total: O(V × E)
```

### Verification in Code
```java
long startTime = System.nanoTime();
// Main algorithm
long endTime = System.nanoTime();
long duration = (endTime - startTime) / 1000; // microseconds

System.out.println("Time Complexity: O(V*E) = O(" + V + "*" + E + ")");
System.out.println("Execution Time: " + duration + " microseconds");
```

---

## Space Complexity

O(V) - for storing distances array

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
```java
dist[0] = 0
dist[1] = ∞ (Integer.MAX_VALUE)
dist[2] = ∞
dist[3] = ∞
dist[4] = ∞
```

### Iteration 1
```
Process edges:
0→1: dist[1] = min(∞, 0 + (-1)) = -1
0→2: dist[2] = min(∞, 0 + 4) = 4
1→2: dist[2] = min(4, -1 + 3) = 2
1→3: dist[3] = min(∞, -1 + 2) = 1
1→4: dist[4] = min(∞, -1 + 2) = 1
4→3: dist[3] = min(1, 1 + (-3)) = -2

After: [0, -1, 2, -2, 1]
```

### Final Result
```
Vertex    Distance from Source
  0              0
  1             -1
  2              2
  3             -2
  4              1
```

---

## Negative Cycle Detection

### What is a Negative Cycle?
A cycle whose sum of edge weights is negative.

```
Example:
Cycle: 1 → 2 → 3 → 1
Weights: 1 + (-3) + 1 = -1 (negative!)

Problem: Can keep going around to reduce distance indefinitely
```

### Detection Method
```java
// After V-1 iterations, check if any edge can still be relaxed
for (int i = 0; i < E; i++) {
    if (dist[u] != Integer.MAX_VALUE && 
        dist[u] + weight < dist[v]) {
        return "Negative cycle detected";
    }
}
```

---

## Java-Specific Features

### Integer.MAX_VALUE
```java
// Represents infinity
int[] dist = new int[V];
for (int i = 0; i < V; i++)
    dist[i] = Integer.MAX_VALUE;

// Check before using (avoid overflow)
if (dist[u] != Integer.MAX_VALUE)
```

### System.nanoTime()
```java
// High-resolution time measurement
long startTime = System.nanoTime();
// ... algorithm ...
long endTime = System.nanoTime();
long duration = (endTime - startTime) / 1000; // microseconds
```

### Edge Array
```java
Edge[] edges = new Edge[E];
edges[i] = new Edge(src, dest, weight);
```

---

## Comparison with Other Algorithms

| Algorithm | Negative Weights | Time Complexity | Space |
|-----------|------------------|-----------------|-------|
| Bellman-Ford | ✓ Yes | O(V × E) | O(V) |
| Dijkstra | ✗ No | O((V+E) log V) | O(V) |
| Floyd-Warshall | ✓ Yes | O(V³) | O(V²) |

---

## How to Compile and Run

```bash
# Compile
javac BellmanFord.java

# Run
java BellmanFord
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

---

## Common Mistakes

### 1. Overflow Check
```java
// ✗ Wrong - can cause overflow
if (dist[u] + weight < dist[v])

// ✓ Correct - check for infinity first
if (dist[u] != Integer.MAX_VALUE && dist[u] + weight < dist[v])
```

### 2. Loop Bounds
```java
// ✗ Wrong - should be V-1
for (int i = 1; i < V; i++)

// ✓ Correct - exactly V-1 times
for (int i = 1; i <= V - 1; i++)
```

### 3. Edge Direction
```java
// Make sure to use correct source and destination
int u = edges[j].src;   // From vertex
int v = edges[j].dest;  // To vertex
```

---

## Applications

1. **Network Routing**: Distance-vector routing (RIP)
2. **Currency Arbitrage**: Detect profitable exchange cycles
3. **Social Networks**: Influence propagation
4. **Resource Allocation**: Costs can be negative (gains)

---

## Key Takeaways

1. **Dynamic Programming**: Builds solution iteratively
2. **Time Complexity**: O(V × E) - verified with timing
3. **Handles Negative Weights**: Unlike Dijkstra
4. **Detects Negative Cycles**: Extra iteration after V-1
5. **Simple Implementation**: Straightforward to code
6. **Java Features**: Integer.MAX_VALUE, System.nanoTime()

---

## When to Use

### Use Bellman-Ford When:
- Graph has negative weight edges
- Need to detect negative cycles
- Working with distributed systems
- Graph is sparse (E ≈ V)

### Don't Use When:
- All weights are positive (use Dijkstra)
- Graph is dense and large (too slow)
- Need all-pairs shortest paths (use Floyd-Warshall)

---

## Next Steps

- **Practical 7**: N-Queens Problem (Backtracking)
- **Understand**: DP principles and relaxation
- **Compare**: With Dijkstra and Floyd-Warshall
