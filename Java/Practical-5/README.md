# Practical 5: Greedy vs Dynamic Programming - Knapsack Comparison (Java)

## Overview
This practical compares Greedy and Dynamic Programming approaches by implementing both Fractional Knapsack (Greedy) and 0/1 Knapsack (Dynamic Programming) in Java. It demonstrates why greedy doesn't always work optimally.

---

## Problem Comparison

### Fractional Knapsack
- **Items can be broken** into fractions
- **Greedy approach is optimal**
- Can take partial items to fill knapsack

### 0/1 Knapsack  
- **Items cannot be broken** (all or nothing)
- **Greedy approach is NOT optimal**
- Must take entire item or leave it
- Requires Dynamic Programming for optimal solution

---

## Implementation

### Item Class
```java
class Item {
    int value;
    int weight;
    double ratio;
    
    Item(int value, int weight) {
        this.value = value;
        this.weight = weight;
        this.ratio = (double) value / weight;
    }
}
```

---

## 1. Fractional Knapsack (Greedy)

### Algorithm
```java
public static double fractionalKnapsack(Item[] items, int capacity) {
    // Create copy to avoid modifying original
    Item[] temp = new Item[items.length];
    for (int i = 0; i < items.length; i++) {
        temp[i] = items[i];
    }
    
    // Sort by ratio (descending)
    Arrays.sort(temp, (a, b) -> Double.compare(b.ratio, a.ratio));
    
    double totalValue = 0.0;
    
    for (int i = 0; i < temp.length; i++) {
        if (capacity >= temp[i].weight) {
            capacity -= temp[i].weight;
            totalValue += temp[i].value;
        } else {
            totalValue += temp[i].value * ((double) capacity / temp[i].weight);
            break;
        }
    }
    
    return totalValue;
}
```

### Time Complexity
O(n log n) - sorting dominates

---

## 2. 0/1 Knapsack (Dynamic Programming)

### Algorithm
```java
public static int knapsack01(Item[] items, int capacity) {
    int n = items.length;
    int[][] dp = new int[n + 1][capacity + 1];
    
    // Build DP table bottom-up
    for (int i = 0; i <= n; i++) {
        for (int w = 0; w <= capacity; w++) {
            if (i == 0 || w == 0) {
                dp[i][w] = 0;
            } else if (items[i - 1].weight <= w) {
                // Max of: include item or exclude item
                int include = items[i - 1].value + 
                             dp[i - 1][w - items[i - 1].weight];
                int exclude = dp[i - 1][w];
                dp[i][w] = Math.max(include, exclude);
            } else {
                // Can't include (too heavy)
                dp[i][w] = dp[i - 1][w];
            }
        }
    }
    
    return dp[n][capacity];
}
```

### Time Complexity
O(n × W) where W = capacity

### Space Complexity
O(n × W) for DP table

---

## Why Greedy Fails for 0/1 Knapsack

### Counter Example
```java
Items:
Item 1: Value=60, Weight=10, Ratio=6.0
Item 2: Value=100, Weight=50, Ratio=2.0
Item 3: Value=120, Weight=50, Ratio=2.4
Capacity = 100

Greedy (by ratio):
- Takes Item 1 (value=60, weight=10)
- Remaining capacity = 90
- Takes Item 3 (value=120, weight=50)
- Remaining capacity = 40
- Can't take Item 2 (weight=50 > 40)
Total = 180

Optimal (DP):
- Takes Item 2 (value=100, weight=50)
- Takes Item 3 (value=120, weight=50)
Total = 220 ✓ BETTER!

Greedy is SUBOPTIMAL for 0/1 Knapsack!
```

---

## DP Table Explanation

### DP[i][w] Meaning
Maximum value achievable with:
- First i items
- Maximum weight capacity w

### Recurrence Relation
```
dp[i][w] = max(
    dp[i-1][w],                           // Don't include item i
    value[i] + dp[i-1][w - weight[i]]    // Include item i
)
```

### Example DP Table
```
Items:
Item 1: V=60, W=10
Item 2: V=100, W=20
Item 3: V=120, W=30
Capacity = 50

DP Table:
        w=0  10   20   30   40   50
i=0      0   0    0    0    0    0
i=1      0   60   60   60   60   60
i=2      0   60  100  160  160  160
i=3      0   60  100  160  180  220

Explanation for dp[3][50]:
- Without Item3: dp[2][50] = 160
- With Item3: 120 + dp[2][20] = 120 + 100 = 220
- dp[3][50] = max(160, 220) = 220 ✓
```

---

## Comparison Code Structure

```java
public static void main(String[] args) {
    // Input items and capacity
    
    System.out.println("\n--- Fractional Knapsack (Greedy) ---");
    double greedyResult = fractionalKnapsack(items, capacity);
    System.out.println("Maximum value: " + greedyResult);
    
    System.out.println("\n--- 0/1 Knapsack (Dynamic Programming) ---");
    int dpResult = knapsack01(items, capacity);
    System.out.println("Maximum value: " + dpResult);
    
    System.out.println("\n--- Comparison ---");
    if (greedyResult > dpResult) {
        System.out.println("Greedy approach gives better result for fractional knapsack.");
        System.out.println("However, for 0/1 knapsack, DP is optimal as items cannot be broken.");
    } else if (dpResult > greedyResult) {
        System.out.println("Dynamic Programming gives optimal solution for 0/1 knapsack.");
        System.out.println("Greedy strategy does not work for 0/1 knapsack.");
    } else {
        System.out.println("Both approaches give same result in this case.");
    }
}
```

---

## Java-Specific Features

### 2D Array Creation
```java
int[][] dp = new int[n + 1][capacity + 1];
```

### Math.max()
```java
dp[i][w] = Math.max(include, exclude);
```

### Array Copying
```java
// Deep copy of Item array
Item[] temp = new Item[items.length];
for (int i = 0; i < items.length; i++) {
    temp[i] = items[i];
}
```

### Type Casting
```java
double fraction = (double) capacity / temp[i].weight;
```

---

## How to Compile and Run

```bash
# Compile
javac KnapsackComparison.java

# Run
java KnapsackComparison
```

### Sample Input
```
Enter number of items: 3
Item 1 - Value: 60
Item 1 - Weight: 10
Item 2 - Value: 100
Item 2 - Weight: 20
Item 3 - Value: 120
Item 3 - Weight: 30
Enter knapsack capacity: 50
```

### Sample Output
```
--- Fractional Knapsack (Greedy) ---
Maximum value: 240.0

--- 0/1 Knapsack (Dynamic Programming) ---
Maximum value: 220

--- Comparison ---
Greedy approach gives better result for fractional knapsack.
However, for 0/1 knapsack, DP is optimal as items cannot be broken.
```

---

## Key Differences

### Fractional vs 0/1

| Aspect | Fractional | 0/1 |
|--------|-----------|-----|
| Items | Can break | All or nothing |
| Greedy | Optimal | Suboptimal |
| Best Approach | Greedy | Dynamic Programming |
| Time | O(n log n) | O(n × W) |
| Space | O(1) | O(n × W) |

---

## When Each Approach Works

| Problem | Greedy | Dynamic Programming |
|---------|--------|---------------------|
| Fractional Knapsack | ✓ Optimal | ✓ Optimal (overkill) |
| 0/1 Knapsack | ✗ Suboptimal | ✓ Optimal |
| Activity Selection | ✓ Optimal | ✓ Optimal (overkill) |
| Longest Common Subsequence | ✗ Fails | ✓ Optimal |
| Shortest Path (Dijkstra) | ✓ Optimal | - |

---

## Greedy Choice Property

### Why Greedy Works for Fractional
- Taking highest ratio item is always part of optimal solution
- Can adjust by taking fraction to fill remaining capacity
- Local optimum = Global optimum

### Why Greedy Fails for 0/1
- Can't take partial items
- Highest ratio might not combine well with other items
- Local optimum ≠ Global optimum
- Need to explore all combinations

---

## Space Optimization for DP

### Current: O(n × W)
```java
int[][] dp = new int[n + 1][capacity + 1];
```

### Optimized: O(W)
```java
// Only need previous row
int[] dp = new int[capacity + 1];

for (int i = 1; i <= n; i++) {
    for (int w = capacity; w >= items[i-1].weight; w--) {
        dp[w] = Math.max(dp[w], 
                        items[i-1].value + dp[w - items[i-1].weight]);
    }
}
```

---

## Performance Comparison

### Time Complexity
- **Greedy**: O(n log n) - fast
- **DP**: O(n × W) - slower for large capacity

### Example
For n=100 items, W=1000:
- Greedy: ~664 operations (100 × log 100)
- DP: 100,000 operations (100 × 1000)

### When to Use What
- **Greedy**: Fractional knapsack, fast approximate solutions
- **DP**: 0/1 knapsack, exact optimal solutions

---

## Common Mistakes

### 1. Confusing Problem Types
```java
// ✗ Using greedy for 0/1 knapsack
// ✓ Use DP for 0/1 knapsack
```

### 2. DP Array Indexing
```java
// ✗ Wrong - off by one
dp[i][w] = items[i].value + dp[i-1][w - items[i].weight];

// ✓ Correct - items[i-1] for i-th item
dp[i][w] = items[i-1].value + dp[i-1][w - items[i-1].weight];
```

### 3. Capacity Check
```java
// ✗ Wrong - doesn't check capacity
if (items[i-1].weight <= w)

// ✓ Correct - checks before accessing
if (i > 0 && items[i-1].weight <= w)
```

---

## Key Takeaways

1. **Fractional Knapsack**: Greedy is optimal (O(n log n))
2. **0/1 Knapsack**: DP is necessary for optimal (O(n × W))
3. **Greedy fails** when items can't be broken
4. **DP** explores all combinations for optimal solution
5. **Trade-off**: Speed (Greedy) vs Accuracy (DP)
6. This practical clearly demonstrates **greedy strategy does not necessarily yield an optimal solution** over dynamic programming

---

## Next Steps

- **Practical 6**: Bellman-Ford Algorithm (Another DP application)
- **Understanding**: Greedy choice property and optimal substructure
- **Practice**: More knapsack variations (Bounded, Unbounded)
