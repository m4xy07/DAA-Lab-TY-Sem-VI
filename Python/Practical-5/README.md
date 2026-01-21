# Practical 5: Greedy vs Dynamic Programming - Knapsack Comparison - Python

## Overview
This practical demonstrates why **Greedy approach fails** for 0/1 Knapsack problem while **Dynamic Programming gives the optimal solution**. It also shows that Greedy works perfectly for Fractional Knapsack.

---

## The Knapsack Problem: Two Variants

### 1. Fractional Knapsack
- **Can take fractions** of items
- **Greedy works optimally** ✓
- **Example**: Filling knapsack with gold dust (can take any amount)

### 2. 0/1 Knapsack
- **Must take entire item or leave it** (no fractions)
- **Greedy does NOT guarantee optimal** ✗
- **Needs Dynamic Programming** for optimal solution
- **Example**: Stealing items from a store (can't take half a TV)

---

## Why This Comparison Matters

**Question**: If greedy works for fractional knapsack, why not for 0/1?

**Answer**: Because we can't take fractions!
- Greedy picks highest ratio first
- But in 0/1, sometimes better to skip high-ratio item for combination of others
- Greedy makes irrevocable choice, DP considers all possibilities

---

## Implementation Overview

### Three Approaches Implemented

```python
# 1. Fractional Knapsack (Greedy - OPTIMAL)
def fractional_knapsack_greedy(items, capacity):
    items_copy = items.copy()
    items_copy.sort(key=lambda x: x.ratio, reverse=True)
    
    max_value = 0
    for item in items_copy:
        if capacity >= item.weight:
            capacity -= item.weight
            max_value += item.value
        else:
            max_value += item.value * (capacity / item.weight)
            break
    
    return max_value


# 2. 0/1 Knapsack (Greedy - NOT ALWAYS OPTIMAL)
def knapsack_01_greedy(items, capacity):
    items_copy = items.copy()
    items_copy.sort(key=lambda x: x.ratio, reverse=True)
    
    max_value = 0
    selected = []
    
    for item in items_copy:
        if capacity >= item.weight:
            capacity -= item.weight
            max_value += item.value
            selected.append(item)
    
    return max_value, selected


# 3. 0/1 Knapsack (Dynamic Programming - OPTIMAL)
def knapsack_01_dp(items, capacity):
    n = len(items)
    
    # Create DP table
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # Build table bottom-up
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if items[i - 1].weight <= w:
                # Max of including or excluding current item
                dp[i][w] = max(
                    items[i - 1].value + dp[i - 1][w - items[i - 1].weight],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]
    
    # Backtrack to find selected items
    selected = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.append(items[i - 1])
            w -= items[i - 1].weight
    
    return dp[n][capacity], selected, dp
```

---

## Dynamic Programming Approach Explained

### DP Table Structure

```
dp[i][w] = Maximum value using first i items with capacity w

Base Cases:
dp[0][w] = 0  (no items, value = 0)
dp[i][0] = 0  (no capacity, value = 0)

Recurrence:
For each item i and capacity w:
  If item fits (weight[i] ≤ w):
    dp[i][w] = max(
        value[i] + dp[i-1][w-weight[i]],  // Include item
        dp[i-1][w]                         // Exclude item
    )
  Else:
    dp[i][w] = dp[i-1][w]  // Can't include
```

### Step-by-Step DP Example

```
Items:
Item 1: Value=60,  Weight=10
Item 2: Value=100, Weight=20
Item 3: Value=120, Weight=30

Capacity: 50

DP Table (rows = items, columns = capacity):

      0   10  20  30  40  50
  0 [ 0   0   0   0   0   0 ]
I 1 [ 0  60  60  60  60  60 ]
I 2 [ 0  60 100 160 160 160 ]
I 3 [ 0  60 100 160 180 220 ]

Filling process:

dp[1][10]: Can take Item1(W:10)
  Include: 60 + dp[0][0] = 60
  Exclude: dp[0][10] = 0
  Max: 60 ✓

dp[2][20]: Can take Item2(W:20)
  Include: 100 + dp[1][0] = 100
  Exclude: dp[1][20] = 60
  Max: 100 ✓

dp[2][30]: Can take Item2(W:20)
  Include: 100 + dp[1][10] = 100 + 60 = 160
  Exclude: dp[1][30] = 60
  Max: 160 ✓ (Take both Item1 and Item2!)

dp[3][50]: Can take Item3(W:30)
  Include: 120 + dp[2][20] = 120 + 100 = 220
  Exclude: dp[2][50] = 160
  Max: 220 ✓
```

### Backtracking to Find Items

```
Start at dp[3][50] = 220
w = 50

i=3: dp[3][50]=220 ≠ dp[2][50]=160
  → Item 3 included
  → w = 50 - 30 = 20

i=2: dp[2][20]=100 ≠ dp[1][20]=60
  → Item 2 included
  → w = 20 - 20 = 0

i=1: w=0, stop

Selected: [Item3, Item2]
```

---

## Python-Specific Features

### 1. List Comprehension for 2D Array
```python
# Create 2D DP table
dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
```

### 2. Lambda with max()
```python
# Find maximum value
items_copy.sort(key=lambda x: x.ratio, reverse=True)
```

### 3. Conditional Expression
```python
# Ternary operator
dp[i][w] = max(include_value, exclude_value) if fits else exclude_value
```

### 4. Backtracking Loop
```python
for i in range(n, 0, -1):  # Count down from n to 1
```

---

## Classic Counter-Example

### Why Greedy Fails for 0/1 Knapsack

```python
Items:
Item 1: Value=60,  Weight=10  → Ratio = 6.0
Item 2: Value=100, Weight=20  → Ratio = 5.0
Item 3: Value=120, Weight=30  → Ratio = 4.0

Capacity: 50

GREEDY SOLUTION (Sort by ratio):
1. Take Item1 (W:10): Value=60,  Remaining=40
2. Take Item2 (W:20): Value=100, Remaining=20
3. Item3 (W:30) doesn't fit, skip

Total Value: 60 + 100 = 160

DP SOLUTION (Consider all combinations):
Option 1: Item1 + Item2 = 60 + 100 = 160 (W:30)
Option 2: Item1 + Item3 = 60 + 120 = 180 (W:40)
Option 3: Item2 + Item3 = 100 + 120 = 220 (W:50) ✓ BEST!

Total Value: 220

DIFFERENCE: 220 - 160 = 60
Greedy gave suboptimal solution by 60 units!
```

### Why It Happened
- Greedy committed to Item1 because of high ratio
- Once taken, couldn't reconsider
- Optimal was to skip Item1 and take Item2 + Item3
- DP considered all possibilities!

---

## Program Flow

```python
def main():
    # 1. Get input
    items = [Item(value, weight), ...]
    capacity = 50
    
    # 2. Run Fractional Knapsack (Greedy)
    frac_value = fractional_knapsack_greedy(items, capacity)
    
    # 3. Run 0/1 Knapsack (Greedy)
    greedy_value, greedy_items = knapsack_01_greedy(items, capacity)
    
    # 4. Run 0/1 Knapsack (DP)
    dp_value, dp_items, dp_table = knapsack_01_dp(items, capacity)
    
    # 5. Compare results
    if greedy_value < dp_value:
        print("⚠ GREEDY FAILED!")
        print(f"Difference: {dp_value - greedy_value}")
    else:
        print("✓ Greedy happened to give optimal")
```

---

## Complexity Analysis

| Approach | Time | Space | Optimal? |
|----------|------|-------|----------|
| **Fractional (Greedy)** | O(n log n) | O(1) | Yes ✓ |
| **0/1 (Greedy)** | O(n log n) | O(n) | No ✗ |
| **0/1 (DP)** | O(nW) | O(nW) | Yes ✓ |

Where:
- n = number of items
- W = knapsack capacity

---

## How to Run

```bash
python knapsack_comparison.py
```

### Option 1: Custom Input
```
Run with your own input (1) or see counter-example (2)? 1

Enter number of items: 3
Enter items (value weight):
Item 1 - Value: 60
Item 1 - Weight: 10
Item 2 - Value: 100
Item 2 - Weight: 20
Item 3 - Value: 120
Item 3 - Weight: 30

Enter knapsack capacity: 50
```

### Option 2: Counter-Example
```
Run with your own input (1) or see counter-example (2)? 2

============================================================
CLASSIC COUNTER-EXAMPLE:
============================================================
Items:
  Item 1: Value=60, Weight=10, Ratio=6.00
  Item 2: Value=100, Weight=20, Ratio=5.00
  Item 3: Value=120, Weight=30, Ratio=4.00
Capacity: 50

Greedy Result: 160
  (Selects Item 1 + Item 2 based on ratio)

DP Result: 220
  (Selects Item 2 + Item 3 for maximum value)

Difference: 60
```

---

## Sample Output

```
============================================================
KNAPSACK COMPARISON: Greedy vs Dynamic Programming
============================================================

ITEMS:
============================================================
Item 1: Value=60, Weight=10, Ratio=6.00
Item 2: Value=100, Weight=20, Ratio=5.00
Item 3: Value=120, Weight=30, Ratio=4.00

============================================================
1. FRACTIONAL KNAPSACK (Greedy - OPTIMAL)
============================================================
Maximum value (fractional allowed): 220.00
Note: Greedy approach is OPTIMAL for fractional knapsack

============================================================
2. 0/1 KNAPSACK - GREEDY APPROACH (NOT ALWAYS OPTIMAL)
============================================================
Maximum value (greedy): 160
Selected items (greedy):
  Value=60, Weight=10
  Value=100, Weight=20

============================================================
3. 0/1 KNAPSACK - DYNAMIC PROGRAMMING (OPTIMAL)
============================================================
Maximum value (DP): 220
Selected items (DP):
  Value=120, Weight=30
  Value=100, Weight=20

DP Table:
      0  10  20  30  40  50
  0:  0   0   0   0   0   0
I 1:  0  60  60  60  60  60
I 2:  0  60 100 160 160 160
I 3:  0  60 100 160 180 220

============================================================
COMPARISON RESULTS:
============================================================
Fractional Knapsack (Greedy): 220.00
0/1 Knapsack (Greedy):        160
0/1 Knapsack (DP):            220

⚠ GREEDY FAILED! Greedy gave suboptimal solution for 0/1 Knapsack
Difference: 60

============================================================
KEY TAKEAWAY:
============================================================
• Greedy works OPTIMALLY for FRACTIONAL Knapsack
• Greedy does NOT guarantee optimal solution for 0/1 Knapsack
• Dynamic Programming is needed for 0/1 Knapsack
============================================================
```

---

## Common Mistakes

### 1. Using Greedy for 0/1 Knapsack
```python
# ✗ Wrong - assumes greedy always works
def solve_01_knapsack(items, capacity):
    items.sort(key=lambda x: x.ratio, reverse=True)
    # Take items greedily...
    # This is NOT optimal!

# ✓ Correct - use DP for 0/1
def solve_01_knapsack(items, capacity):
    # Use DP table approach
```

### 2. Incorrect DP Recurrence
```python
# ✗ Wrong - doesn't consider excluding item
dp[i][w] = items[i-1].value + dp[i-1][w - items[i-1].weight]

# ✓ Correct - max of including or excluding
dp[i][w] = max(
    items[i-1].value + dp[i-1][w - items[i-1].weight],  # Include
    dp[i-1][w]                                           # Exclude
)
```

### 3. Not Checking Weight Constraint
```python
# ✗ Wrong - may cause negative index
dp[i][w] = max(
    items[i-1].value + dp[i-1][w - items[i-1].weight],
    dp[i-1][w]
)

# ✓ Correct - check if item fits first
if items[i-1].weight <= w:
    dp[i][w] = max(...)
else:
    dp[i][w] = dp[i-1][w]
```

---

## When to Use Which?

| Scenario | Algorithm | Reason |
|----------|-----------|--------|
| Can take fractions | Greedy | Optimal & Fast |
| Must take whole items | DP | Greedy fails |
| Small capacity & items | DP | Feasible time/space |
| Very large capacity | Approximation | DP too slow |

---

## Key Takeaways

1. **Greedy Choice Property**: Fractional has it, 0/1 doesn't
2. **Fractional Knapsack**: Greedy is OPTIMAL (sort by ratio)
3. **0/1 Knapsack**: Greedy FAILS, need DP
4. **DP Table**: Considers all item combinations
5. **Time Complexity**: Greedy O(n log n) vs DP O(nW)
6. **Counter-Example**: Shows greedy failure clearly
7. **Python Features**: List comprehension, lambda, 2D arrays

---

## Real-World Applications

### Fractional Knapsack
- **Investment**: Divisible assets (stocks)
- **Resource Allocation**: Bandwidth, budget
- **Cutting Stock**: Materials that can be cut

### 0/1 Knapsack
- **Project Selection**: Complete projects or not
- **Loading Cargo**: Indivisible packages
- **Portfolio Selection**: Discrete investments

---

## Next Steps
- **Practical 6**: Bellman-Ford Algorithm (DP for shortest paths)
- **Practice**: More DP problems (Coin change, LCS, Edit distance)
- **Understand**: Optimal substructure and overlapping subproblems
