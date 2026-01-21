# Practical 5: Greedy vs Dynamic Programming - Knapsack Problem

## Overview
This practical compares Greedy and Dynamic Programming approaches by implementing both Fractional Knapsack (Greedy) and 0/1 Knapsack (Dynamic Programming). It demonstrates why greedy doesn't always work optimally.

---

## Problem Comparison

### Fractional Knapsack
- **Items can be broken** into fractions
- **Greedy approach is optimal**
- Solved using Greedy Algorithm

### 0/1 Knapsack  
- **Items cannot be broken** (all or nothing)
- **Greedy approach is NOT optimal**
- Requires Dynamic Programming for optimal solution

---

## 1. Fractional Knapsack (Greedy Approach)

### Algorithm
```cpp
fractionalKnapsack(items[], capacity):
    1. Calculate ratio = value/weight for each item
    2. Sort items by ratio in descending order
    3. totalValue = 0
    
    4. For each item:
        if capacity >= item.weight:
            Take whole item
            capacity -= item.weight
            totalValue += item.value
        else:
            Take fraction = capacity/item.weight
            totalValue += item.value * fraction
            break
    
    5. Return totalValue
```

### Time Complexity
O(n log n) - dominated by sorting

### Space Complexity
O(n) - for storing sorted items

### Example
```
Items: 
Item 1: V=60, W=10, Ratio=6.0
Item 2: V=100, W=20, Ratio=5.0
Item 3: V=120, W=30, Ratio=4.0
Capacity = 50

Greedy Solution:
- Take Item 1 (full): 60
- Take Item 2 (full): 100
- Take Item 3 (2/3): 80
Total = 240 ✓ OPTIMAL
```

---

## 2. 0/1 Knapsack (Dynamic Programming)

### Why Greedy Fails for 0/1

**Counter Example:**
```
Items:
Item 1: Value=60, Weight=10
Item 2: Value=100, Weight=50
Item 3: Value=120, Weight=50
Capacity = 100

Greedy (by value/weight ratio):
Ratio1 = 6.0, Ratio2 = 2.0, Ratio3 = 2.4
Takes: Item1(60) + Item3(120) = 180

Optimal (DP):
Takes: Item2(100) + Item3(120) = 220 ✓

Greedy is SUBOPTIMAL!
```

### Dynamic Programming Approach

### Algorithm
```cpp
knapsack01(items[], n, capacity):
    Create dp[n+1][capacity+1]
    
    // Base case: 0 items or 0 capacity = 0 value
    for i from 0 to n:
        dp[i][0] = 0
    for w from 0 to capacity:
        dp[0][w] = 0
    
    // Fill the DP table
    for i from 1 to n:
        for w from 1 to capacity:
            if items[i-1].weight <= w:
                // Choice: include or exclude item
                include = items[i-1].value + dp[i-1][w - items[i-1].weight]
                exclude = dp[i-1][w]
                dp[i][w] = max(include, exclude)
            else:
                // Can't include (too heavy)
                dp[i][w] = dp[i-1][w]
    
    return dp[n][capacity]
```

### DP Table Explanation
- **dp[i][w]** = maximum value achievable with first i items and capacity w
- **Choice**: For each item, decide to include or exclude
- **Optimal Substructure**: Solution uses solutions to smaller subproblems

### Time Complexity
O(n × W) where W = capacity

### Space Complexity
O(n × W) for the DP table

### Example with DP Table
```
Items:
Item 1: V=60, W=10
Item 2: V=100, W=20
Item 3: V=120, W=30
Capacity = 50

DP Table (dp[i][w]):
        w=0  10   20   30   40   50
i=0      0   0    0    0    0    0
i=1      0   60   60   60   60   60
i=2      0   60  100  160  160  160
i=3      0   60  100  160  180  220

Step-by-step for dp[3][50]:
- Without Item3: dp[2][50] = 160
- With Item3: 120 + dp[2][20] = 120 + 100 = 220
- dp[3][50] = max(160, 220) = 220 ✓

Solution: Take Items 2 and 3
Total Value = 220
```

---

## Why Greedy Fails for 0/1 Knapsack

### Key Difference
```
Fractional Knapsack:
- Can take partial items
- Highest ratio always contributes maximum per unit weight
- Local optimum = Global optimum

0/1 Knapsack:
- All-or-nothing decision
- Highest ratio might not fit well with other items
- Local optimum ≠ Global optimum
- Need to consider all combinations
```

### Counter-Example Explained
```
Items: V1=10,W1=5  V2=40,W2=20  V3=50,W3=25
Capacity = 35

Ratios: R1=2.0, R2=2.0, R3=2.0 (all equal!)

Greedy tries:
- Item1 (V=10, W=5): Take it → Remaining capacity=30
- Item2 (V=40, W=20): Take it → Remaining capacity=10
- Item3 (V=50, W=25): Can't take (too heavy)
Total = 50

Optimal (DP):
- Item2 (V=40, W=20) + Item1 (V=10, W=5) = 50
  OR
- Item2 (V=40, W=20) + partial of Item3... wait, this is 0/1!
- Actually: Item2 + Item3 won't fit (45 > 35)
- So: Item1 + Item2 = 50 OR just Item3 = 50

Better optimal: Item2(40) + Item1(10) = 50
(Both give same here, but DP explores all)
```

---

## Comparison Implementation

### The Code Structure
```cpp
1. Input items and capacity
2. Run Fractional Knapsack (Greedy)
   - Sort by ratio
   - Take items greedily
3. Run 0/1 Knapsack (DP)
   - Build DP table
   - Find optimal value
4. Compare results
   - Show both values
   - Explain why they differ (if they do)
```

---

## When Each Approach Works

| Problem Type | Greedy | Dynamic Programming |
|-------------|--------|---------------------|
| Fractional Knapsack | ✓ Optimal | ✓ Optimal (but overkill) |
| 0/1 Knapsack | ✗ Suboptimal | ✓ Optimal |
| Activity Selection | ✓ Optimal | ✓ Optimal (but overkill) |
| Shortest Path (Dijkstra) | ✓ Optimal | - |
| Longest Common Subsequence | ✗ Fails | ✓ Optimal |

---

## Performance Comparison

### Time Complexity
- **Greedy**: O(n log n) - fast
- **DP**: O(n × W) - slower for large capacity

### Space Complexity
- **Greedy**: O(1) - minimal
- **DP**: O(n × W) - can be significant

### Accuracy
- **Greedy (Fractional)**: Always optimal
- **Greedy (0/1)**: Often suboptimal
- **DP (0/1)**: Always optimal

---

## How to Compile and Run

```bash
# Compile
g++ knapsack_comparison.cpp -o knapsack_comparison

# Run
./knapsack_comparison
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
Maximum value: 240

--- 0/1 Knapsack (Dynamic Programming) ---
Maximum value: 220

--- Comparison ---
Greedy approach gives better result for fractional knapsack.
However, for 0/1 knapsack, DP is optimal as items cannot be broken.
```

### Example Showing Greedy Failure
```
Input:
Item 1: Value=60, Weight=10
Item 2: Value=100, Weight=50
Item 3: Value=120, Weight=50
Capacity: 100

Output:
Fractional Knapsack (Greedy): 240 (takes 1 full, 2 and 3 partial)
0/1 Knapsack (DP): 220 (takes items 2 and 3)

For pure 0/1 with greedy by ratio:
Would take item 1 + either 2 or 3 = 180
DP correctly finds: items 2 + 3 = 220 ✓
```

---

## Key Insights

### Greedy Choice Property
**Fractional Knapsack has it**: Taking highest ratio item is always part of optimal solution

**0/1 Knapsack lacks it**: Taking highest ratio item might block better combinations

### Optimal Substructure
**Both have it**: Optimal solution contains optimal solutions to subproblems

### The Critical Difference
```
Fractional: Decisions are independent
            (taking part of item doesn't affect others)

0/1:        Decisions are interdependent
            (taking whole item affects remaining capacity)
```

---

## Learning Outcomes

1. **Greedy works when**: Greedy choice property + Optimal substructure
2. **DP needed when**: No greedy choice property, but optimal substructure exists
3. **Trade-offs**: Greedy is faster, DP is more general
4. **Problem recognition**: Knowing when to use which approach

---

## Conclusion

- **Fractional Knapsack**: Greedy is perfect (and faster)
- **0/1 Knapsack**: Dynamic Programming is necessary for optimal solution
- **General Rule**: Use greedy when proven optimal, otherwise consider DP
- This practical clearly demonstrates why **greedy strategy does not necessarily yield an optimal solution** compared to dynamic programming for problems where greedy choice property doesn't hold.
