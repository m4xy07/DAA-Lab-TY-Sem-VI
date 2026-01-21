# Practical 4: Greedy Algorithms - Python

## Overview
This practical implements two classic greedy algorithm problems in Python: Fractional Knapsack and Job Sequencing with Deadlines. Greedy algorithms make locally optimal choices at each step to find a global optimum.

---

## What is a Greedy Algorithm?

### Strategy
1. **Make Choice**: Pick the best option at current step
2. **No Backtracking**: Never reconsider previous choices
3. **Local Optimum → Global Optimum**: Hope local choices lead to global solution

### When Greedy Works
- Problem has **greedy choice property**
- Problem has **optimal substructure**

### Key Difference from Other Approaches
- **Greedy**: Makes choice now, never looks back
- **Dynamic Programming**: Considers all possibilities
- **Backtracking**: Tries possibilities, backtracks if wrong

---

## 1. Fractional Knapsack (`fractional_knapsack.py`)

### Problem Statement
Given:
- N items, each with value and weight
- Knapsack with capacity W
- Can take **fractions** of items

Find: Maximum value that can be obtained

### Greedy Strategy
Sort items by **value-to-weight ratio** (value per unit weight) in descending order, then greedily pick items.

### Python Implementation

```python
class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight
    
    def __repr__(self):
        return f"(V:{self.value}, W:{self.weight}, R:{self.ratio:.2f})"


def fractional_knapsack(items, capacity):
    """
    Solve fractional knapsack using greedy approach
    Returns: (max_value, selected_items)
    """
    # Sort items by value-to-weight ratio in descending order
    items.sort(key=lambda x: x.ratio, reverse=True)
    
    max_value = 0
    selected = []
    
    for item in items:
        if capacity >= item.weight:
            # Take entire item
            capacity -= item.weight
            max_value += item.value
            selected.append((item, 1.0))  # 1.0 = 100%
        else:
            # Take fraction of item
            fraction = capacity / item.weight
            max_value += item.value * fraction
            selected.append((item, fraction))
            break  # Knapsack is full
    
    return max_value, selected
```

### Python-Specific Features

#### 1. Class Definition
```python
class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight
```

#### 2. Lambda Function for Sorting
```python
# Sort by ratio in descending order
items.sort(key=lambda x: x.ratio, reverse=True)
```

#### 3. __repr__ Method
```python
def __repr__(self):
    return f"(V:{self.value}, W:{self.weight}, R:{self.ratio:.2f})"
```
Defines string representation when printing object.

#### 4. Tuple in List
```python
selected.append((item, fraction))
```

### Step-by-Step Example

```
Items:
Item 1: Value=60,  Weight=10  → Ratio = 60/10 = 6.0
Item 2: Value=100, Weight=20  → Ratio = 100/20 = 5.0
Item 3: Value=120, Weight=30  → Ratio = 120/30 = 4.0

Capacity: 50

STEP 1: Sort by ratio
Sorted: [Item1(R:6.0), Item2(R:5.0), Item3(R:4.0)]

STEP 2: Greedy Selection
Take Item 1: 
  Weight: 10 ≤ 50 ✓
  Take 100% (10 kg)
  Value: 60
  Remaining capacity: 50 - 10 = 40

Take Item 2:
  Weight: 20 ≤ 40 ✓
  Take 100% (20 kg)
  Value: 100
  Remaining capacity: 40 - 20 = 20

Take Item 3:
  Weight: 30 > 20 ✗
  Take fraction: 20/30 = 0.667 (66.7%)
  Value: 120 × 0.667 = 80
  Remaining capacity: 0

RESULT:
Maximum Value = 60 + 100 + 80 = 240
Items: Item1(100%), Item2(100%), Item3(66.7%)
```

### Why Greedy Works Here
Taking highest ratio first always gives maximum value for fractional knapsack!

**Proof Intuition**: If we swap a higher ratio fraction with lower ratio, total value decreases.

### Complexity
- **Time**: O(n log n) - dominated by sorting
- **Space**: O(n) - for selected items list

---

## 2. Job Sequencing with Deadlines (`job_sequencing.py`)

### Problem Statement
Given:
- N jobs
- Each job has: deadline and profit
- Each job takes 1 unit of time

Find: Maximum profit by scheduling jobs before their deadlines

### Greedy Strategy
1. Sort jobs by **profit** (descending)
2. For each job, assign it to the **latest available slot** before its deadline

### Python Implementation

```python
class Job:
    def __init__(self, job_id, deadline, profit):
        self.id = job_id
        self.deadline = deadline
        self.profit = profit
    
    def __repr__(self):
        return f"(J{self.id}, D:{self.deadline}, P:{self.profit})"


def job_sequencing(jobs):
    """
    Solve job sequencing with deadlines using greedy approach
    Returns: (max_profit, sequence)
    """
    # Sort jobs by profit in descending order
    jobs.sort(key=lambda x: x.profit, reverse=True)
    
    # Find maximum deadline
    max_deadline = max(job.deadline for job in jobs)
    
    # Create time slots
    slots = [-1] * max_deadline
    sequence = []
    max_profit = 0
    
    # Schedule jobs
    for job in jobs:
        # Find a free slot for this job (starting from last possible slot)
        for slot in range(min(max_deadline, job.deadline) - 1, -1, -1):
            if slots[slot] == -1:
                slots[slot] = job.id
                sequence.append(job)
                max_profit += job.profit
                break
    
    return max_profit, sequence
```

### Python Features

#### 1. Generator Expression with max()
```python
max_deadline = max(job.deadline for job in jobs)
```

#### 2. List Initialization
```python
slots = [-1] * max_deadline  # Creates list of -1s
```

#### 3. min() Function
```python
# Don't exceed max_deadline or job's deadline
for slot in range(min(max_deadline, job.deadline) - 1, -1, -1):
```

### Step-by-Step Example

```
Jobs:
Job 1: Deadline=4, Profit=20
Job 2: Deadline=1, Profit=10
Job 3: Deadline=1, Profit=40
Job 4: Deadline=1, Profit=30

STEP 1: Sort by profit (descending)
Sorted: [Job3(D:1, P:40), Job4(D:1, P:30), Job1(D:4, P:20), Job2(D:1, P:10)]

STEP 2: Create time slots
Max deadline = 4
Slots: [_, _, _, _]  (4 slots: 0, 1, 2, 3)

STEP 3: Schedule jobs (greedy)

Job 3 (D:1, P:40):
  Try slot 0 (last before deadline 1): Free ✓
  Slots: [J3, _, _, _]
  Profit: 40

Job 4 (D:1, P:30):
  Try slot 0: Occupied ✗
  No available slot before deadline 1
  Skip this job

Job 1 (D:4, P:20):
  Try slot 3: Free ✓
  Slots: [J3, _, _, J1]
  Profit: 40 + 20 = 60

Job 2 (D:1, P:10):
  Try slot 0: Occupied ✗
  No available slot
  Skip this job

RESULT:
Sequence: [Job3 at slot 0, Job1 at slot 3]
Schedule: J3 → (any) → (any) → J1
Maximum Profit: 60
```

### Why Assign to Latest Slot?
Assigning to the latest possible slot leaves earlier slots available for jobs with earlier deadlines.

**Example:**
```
Job A: Deadline=3, Profit=50
Job B: Deadline=1, Profit=40

If we assign A to slot 0:
Slots: [A, _, _]
B must go to slot 0 → Conflict! Lost B.

If we assign A to slot 2 (latest):
Slots: [_, _, A]
B can go to slot 0 → No conflict! Both scheduled ✓
```

### Complexity
- **Time**: O(n²) - for each job, scan slots
- **Space**: O(n) - slots array

### Optimization
Can use Union-Find (Disjoint Set) to reduce time to O(n log n).

---

## Comparison: Fractional vs 0/1 Knapsack

| Aspect | Fractional Knapsack | 0/1 Knapsack |
|--------|---------------------|--------------|
| **Can take fraction?** | Yes | No |
| **Greedy works?** | Yes (Optimal) ✓ | No (Not optimal) ✗ |
| **Algorithm** | Greedy | Dynamic Programming |
| **Time** | O(n log n) | O(nW) |

**Key Point**: Greedy is OPTIMAL for Fractional but NOT for 0/1!

---

## Python-Specific Features Summary

### 1. Classes
```python
class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
```

### 2. Lambda Functions
```python
items.sort(key=lambda x: x.ratio, reverse=True)
```

### 3. List Comprehension & Generators
```python
max_deadline = max(job.deadline for job in jobs)
```

### 4. Multiple Assignment
```python
max_value, selected = fractional_knapsack(items, capacity)
```

### 5. Enumerate
```python
for i, item in enumerate(items):
    print(f"Item {i + 1}: {item}")
```

---

## How to Run

```bash
# Run Fractional Knapsack
python fractional_knapsack.py

# Run Job Sequencing
python job_sequencing.py
```

### Sample Input (Fractional Knapsack)
```
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

### Sample Output
```
=== Fractional Knapsack Problem (Greedy) ===

==================================================
SOLUTION:
==================================================

Items sorted by value/weight ratio:
  Value: 60, Weight: 10, Ratio: 6.00
  Value: 100, Weight: 20, Ratio: 5.00
  Value: 120, Weight: 30, Ratio: 4.00

Selected items:
  Item (V:60, W:10) - 100.0% taken
  Item (V:100, W:20) - 100.0% taken
  Item (V:120, W:30) - 66.7% taken

Maximum value: 240.00
Time Complexity: O(n log n) due to sorting
```

---

## Common Mistakes

### 1. Not Sorting First
```python
# ✗ Wrong - greedy without sorting
for item in items:
    if capacity >= item.weight:
        # Takes items in input order

# ✓ Correct - sort by ratio first
items.sort(key=lambda x: x.ratio, reverse=True)
for item in items:
```

### 2. Wrong Slot Assignment (Job Sequencing)
```python
# ✗ Wrong - assigns to first free slot
for slot in range(max_deadline):
    if slots[slot] == -1:
        slots[slot] = job.id

# ✓ Correct - assigns to last free slot before deadline
for slot in range(min(max_deadline, job.deadline) - 1, -1, -1):
    if slots[slot] == -1:
        slots[slot] = job.id
```

### 3. Forgetting to Break (Fractional Knapsack)
```python
# ✗ Wrong - continues after knapsack is full
for item in items:
    if capacity >= item.weight:
        capacity -= item.weight
    else:
        fraction = capacity / item.weight
        # Missing break!

# ✓ Correct
for item in items:
    if capacity >= item.weight:
        capacity -= item.weight
    else:
        fraction = capacity / item.weight
        break  # Knapsack is full!
```

---

## Applications

### Fractional Knapsack
1. **Resource Allocation**: Distributing budgets
2. **Portfolio Optimization**: Investing money
3. **Network Bandwidth**: Allocating bandwidth

### Job Sequencing
1. **CPU Scheduling**: Process scheduling
2. **Project Management**: Task deadlines
3. **Manufacturing**: Production scheduling

---

## Key Takeaways

1. **Greedy Strategy**: Make locally optimal choice
2. **Fractional Knapsack**: Sort by ratio, greedy is OPTIMAL
3. **Job Sequencing**: Sort by profit, assign to latest slot
4. **Python Features**: Classes, lambda, sorting, generators
5. **Time Complexity**: O(n log n) for both (dominated by sorting)
6. **When Greedy Fails**: 0/1 Knapsack needs DP, not greedy

---

## Next Steps
- **Practical 5**: Compare Greedy vs DP for 0/1 Knapsack
- **Understand**: When greedy works vs when it doesn't
- **Practice**: More greedy problems (Huffman coding, Activity selection)
