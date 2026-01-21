# Practical 4: Greedy Algorithms - Selection Problems

## Overview
This practical implements two classic greedy algorithms: Fractional Knapsack Problem and Job Sequencing with Deadlines. Both demonstrate the greedy approach of making locally optimal choices.

---

## 1. Fractional Knapsack (`fractional_knapsack.cpp`)

### Problem Statement
Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value. You can break items (take fractions) to maximize value.

### Greedy Strategy
**Always pick the item with the highest value-to-weight ratio first.**

### Algorithm Explanation
1. Calculate value/weight ratio for each item
2. Sort items by ratio in descending order
3. Take items with highest ratio first
4. If an item doesn't fit completely, take a fraction of it
5. Continue until knapsack is full

### How It Works
```
fractionalKnapsack(items[], capacity):
    1. Calculate ratio = value/weight for each item
    2. Sort items by ratio (descending)
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
- **Sorting**: O(n log n)
- **Selection**: O(n)
- **Total**: O(n log n)

### Space Complexity
O(1) - if sorting is done in-place

### Example
```
Items:
Item 1: Value = 60, Weight = 10, Ratio = 6.0
Item 2: Value = 100, Weight = 20, Ratio = 5.0
Item 3: Value = 120, Weight = 30, Ratio = 4.0

Capacity = 50

Solution:
Step 1: Sort by ratio: [Item1(6.0), Item2(5.0), Item3(4.0)]

Step 2: Take Item 1 (full)
    Capacity left = 50 - 10 = 40
    Value = 60

Step 3: Take Item 2 (full)
    Capacity left = 40 - 20 = 20
    Value = 60 + 100 = 160

Step 4: Take Item 3 (partial)
    Can only take 20/30 = 0.667 fraction
    Value = 160 + (120 × 0.667) = 160 + 80 = 240

Maximum Value = 240
```

### Why Greedy Works Here
The fractional knapsack has the **greedy choice property**: taking the item with highest value/weight ratio always leads to optimal solution because items can be broken.

### Proof of Correctness
- If we take an item with lower ratio before higher ratio, we can always improve by swapping
- Taking items in decreasing order of ratio maximizes value per unit weight
- This local optimal choice leads to global optimal solution

---

## 2. Job Sequencing with Deadlines (`job_sequencing.cpp`)

### Problem Statement
Given n jobs where each job has a deadline and profit. Each job takes 1 unit of time. Only one job can be scheduled at a time. Maximize total profit by scheduling jobs before their deadlines.

### Greedy Strategy
**Always schedule the job with highest profit first, as late as possible before its deadline.**

### Algorithm Explanation
1. Sort all jobs by profit in descending order
2. Find maximum deadline to determine time slots needed
3. For each job (in sorted order):
   - Find a free slot before its deadline (prefer latest slot)
   - If found, schedule the job in that slot
4. Calculate total profit from scheduled jobs

### How It Works
```
jobSequencing(jobs[]):
    1. Sort jobs by profit (descending)
    2. maxDeadline = max(job.deadline for all jobs)
    3. Create slots[maxDeadline] = all empty
    4. totalProfit = 0
    
    5. For each job:
        For slot from min(deadline, maxDeadline)-1 to 0:
            if slot is free:
                Schedule job in this slot
                totalProfit += job.profit
                break
    
    6. Return totalProfit
```

### Time Complexity
- **Sorting**: O(n log n)
- **Scheduling**: O(n × d) where d = max deadline
- **Total**: O(n log n + n×d)

### Space Complexity
O(d) - for storing slot information

### Example
```
Jobs:
Job 1: ID=1, Deadline=2, Profit=100
Job 2: ID=2, Deadline=1, Profit=19
Job 3: ID=3, Deadline=2, Profit=27
Job 4: ID=4, Deadline=1, Profit=25
Job 5: ID=5, Deadline=3, Profit=15

Solution:
Step 1: Sort by profit: [J1(100), J3(27), J4(25), J2(19), J5(15)]

Step 2: Maximum deadline = 3, so we have slots [0, 1, 2]

Step 3: Schedule jobs
    J1 (deadline=2, profit=100):
        Try slot 1 (before deadline 2): Free ✓
        Schedule J1 at slot 1
        Slots: [_, J1, _]
    
    J3 (deadline=2, profit=27):
        Try slot 1: Occupied
        Try slot 0: Free ✓
        Schedule J3 at slot 0
        Slots: [J3, J1, _]
    
    J4 (deadline=1, profit=25):
        Try slot 0: Occupied
        No free slot before deadline 1 ✗
    
    J2 (deadline=1, profit=19):
        Try slot 0: Occupied
        No free slot before deadline 1 ✗
    
    J5 (deadline=3, profit=15):
        Try slot 2: Free ✓
        Schedule J5 at slot 2
        Slots: [J3, J1, J5]

Final Schedule:
Time 0-1: Job 3 (Profit: 27)
Time 1-2: Job 1 (Profit: 100)
Time 2-3: Job 5 (Profit: 15)

Total Jobs Completed: 3
Total Profit: 142
```

### Why Greedy Works Here
- Scheduling high-profit jobs first ensures maximum profit
- Placing jobs as late as possible keeps earlier slots available for other jobs
- This strategy guarantees optimal solution

---

## Comparison: Fractional vs 0/1 Problems

| Aspect | Fractional Knapsack | Job Sequencing |
|--------|---------------------|----------------|
| Greedy Works? | Yes (Optimal) | Yes (Optimal) |
| Can Break Items? | Yes | No |
| Sorting Key | Value/Weight Ratio | Profit |
| Time Complexity | O(n log n) | O(n log n + n×d) |
| Space | O(1) | O(d) |

---

## Greedy Algorithm Characteristics

### Advantages
1. **Simple to Implement**: Easy to understand and code
2. **Efficient**: Usually O(n log n) due to sorting
3. **Fast**: No backtracking needed

### When Greedy Works
- Problem has **Greedy Choice Property**: Local optimal leads to global optimal
- Problem has **Optimal Substructure**: Optimal solution contains optimal solutions to subproblems

### When Greedy Fails
- 0/1 Knapsack (without fractions)
- Traveling Salesman Problem
- Graph Coloring

---

## How to Compile and Run

```bash
# Compile
g++ fractional_knapsack.cpp -o fractional_knapsack
g++ job_sequencing.cpp -o job_sequencing

# Run
./fractional_knapsack
./job_sequencing
```

### Sample Input - Fractional Knapsack
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
Items selected:
Item 1: Weight = 10, Value = 60 (Full)
Item 2: Weight = 20, Value = 100 (Full)
Item 3: Weight = 20, Value = 80 (Fraction = 0.666667)

Maximum value in knapsack: 240
```

### Sample Input - Job Sequencing
```
Enter number of jobs: 4
Job 1 - ID: 1
Job 1 - Deadline: 4
Job 1 - Profit: 20
Job 2 - ID: 2
Job 2 - Deadline: 1
Job 2 - Profit: 10
Job 3 - ID: 3
Job 3 - Deadline: 1
Job 3 - Profit: 40
Job 4 - ID: 4
Job 4 - Deadline: 1
Job 4 - Profit: 30
```

### Sample Output
```
Selected Jobs:
Job 3 (Profit: 40, Deadline: 1)
Job 4 (Profit: 30, Deadline: 1)
Job 1 (Profit: 20, Deadline: 4)

Total Jobs: 3
Total Profit: 90
```

---

## Key Takeaways
1. **Greedy algorithms make locally optimal choices**
2. **Fractional Knapsack**: Sort by value/weight ratio
3. **Job Sequencing**: Sort by profit, schedule as late as possible
4. Both achieve **optimal solutions** using greedy approach
5. Time complexity dominated by sorting: **O(n log n)**
