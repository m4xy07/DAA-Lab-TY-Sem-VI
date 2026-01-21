# Practical 4: Greedy Algorithms - Selection Problems (Java)

## Overview
This practical implements two classic greedy algorithms in Java: Fractional Knapsack Problem and Job Sequencing with Deadlines.

---

## 1. Fractional Knapsack (`FractionalKnapsack.java`)

### Problem Statement
Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value. You can break items (take fractions) to maximize value.

### Greedy Strategy
**Always pick the item with the highest value-to-weight ratio first.**

### Algorithm
```java
1. Calculate ratio = value/weight for each item
2. Sort items by ratio (descending)
3. Take items greedily:
   - If item fits completely, take it
   - If item doesn't fit, take fraction
4. Return total value
```

### Java Implementation Details

#### Item Class
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

#### Sorting with Lambda
```java
// Sort items by ratio in descending order
Arrays.sort(items, (a, b) -> Double.compare(b.ratio, a.ratio));
```

#### Greedy Selection
```java
for (int i = 0; i < items.length; i++) {
    if (capacity >= items[i].weight) {
        // Take whole item
        capacity -= items[i].weight;
        totalValue += items[i].value;
    } else {
        // Take fraction
        double fraction = (double) capacity / items[i].weight;
        totalValue += items[i].value * fraction;
        break;
    }
}
```

### Time Complexity
O(n log n) - dominated by sorting

### Space Complexity
O(n) - for storing items

### Example
```
Items:
Item 1: Value=60, Weight=10, Ratio=6.0
Item 2: Value=100, Weight=20, Ratio=5.0
Item 3: Value=120, Weight=30, Ratio=4.0
Capacity = 50

Solution:
- Take Item 1 (full): 60
- Take Item 2 (full): 100
- Take Item 3 (20/30): 80
Total = 240 ✓
```

---

## 2. Job Sequencing with Deadlines (`JobSequencing.java`)

### Problem Statement
Given n jobs where each job has a deadline and profit. Each job takes 1 unit of time. Only one job can be scheduled at a time. Maximize total profit by scheduling jobs before their deadlines.

### Greedy Strategy
**Always schedule the job with highest profit first, as late as possible before its deadline.**

### Algorithm
```java
1. Sort jobs by profit (descending)
2. Find maximum deadline
3. For each job (in sorted order):
   - Find latest free slot before its deadline
   - If slot found, schedule job there
4. Return total profit
```

### Java Implementation Details

#### Job Class
```java
class Job {
    int id;
    int deadline;
    int profit;
    
    Job(int id, int deadline, int profit) {
        this.id = id;
        this.deadline = deadline;
        this.profit = profit;
    }
}
```

#### Sorting Jobs
```java
// Sort by profit in descending order
Arrays.sort(jobs, (a, b) -> b.profit - a.profit);
```

#### Slot Management
```java
int[] slot = new int[maxDeadline];
boolean[] filled = new boolean[maxDeadline];

// Find free slot for job
for (int j = Math.min(maxDeadline, jobs[i].deadline) - 1; j >= 0; j--) {
    if (!filled[j]) {
        filled[j] = true;
        slot[j] = jobs[i].id;
        totalProfit += jobs[i].profit;
        break;
    }
}
```

### Time Complexity
- **Sorting**: O(n log n)
- **Scheduling**: O(n × d) where d = max deadline
- **Total**: O(n log n + n×d)

### Space Complexity
O(d) - for slot tracking

### Example
```
Jobs:
Job 1: ID=1, Deadline=2, Profit=100
Job 2: ID=2, Deadline=1, Profit=19
Job 3: ID=3, Deadline=2, Profit=27
Job 4: ID=4, Deadline=1, Profit=25
Job 5: ID=5, Deadline=3, Profit=15

Solution:
Sort by profit: [J1(100), J3(27), J4(25), J2(19), J5(15)]

Schedule:
- J1 at slot 1 (deadline 2)
- J3 at slot 0 (deadline 2, slot 1 taken)
- J5 at slot 2 (deadline 3)

Total Profit: 142
```

---

## Java-Specific Features

### Lambda Expressions
```java
// Compact comparator for sorting
Arrays.sort(items, (a, b) -> Double.compare(b.ratio, a.ratio));
```

### Arrays.sort() with Custom Comparator
```java
// Sort Job objects by profit
Arrays.sort(jobs, (a, b) -> b.profit - a.profit);

// Alternative: Using Comparator interface
Arrays.sort(jobs, new Comparator<Job>() {
    public int compare(Job a, Job b) {
        return b.profit - a.profit;
    }
});
```

### Type Casting
```java
// Double division for accurate ratio
double ratio = (double) value / weight;

// Fraction calculation
double fraction = (double) capacity / weight;
```

### Math.min()
```java
// Find minimum of two values
int limit = Math.min(maxDeadline, jobs[i].deadline);
```

---

## How to Compile and Run

```bash
# Compile
javac FractionalKnapsack.java
javac JobSequencing.java

# Run
java FractionalKnapsack
java JobSequencing
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
Item 3: Weight = 20, Value = 80.0 (Fraction = 0.6666666666666666)

Maximum value in knapsack: 240.0
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

## Why Greedy Works

### Fractional Knapsack
- **Greedy Choice Property**: Taking highest ratio item is always part of optimal solution
- **Optimal Substructure**: Optimal solution contains optimal solutions to subproblems
- Items can be broken, so local optimum = global optimum

### Job Sequencing
- Scheduling high-profit jobs first maximizes profit
- Placing jobs as late as possible keeps earlier slots available
- This strategy guarantees optimal solution

---

## Comparison with Other Approaches

| Problem | Greedy | Dynamic Programming |
|---------|--------|---------------------|
| Fractional Knapsack | ✓ Optimal | ✓ Optimal (overkill) |
| 0/1 Knapsack | ✗ Suboptimal | ✓ Optimal |
| Job Sequencing | ✓ Optimal | ✓ Optimal (overkill) |

---

## Common Mistakes to Avoid

### 1. Sorting Direction
```java
// ✗ Wrong - ascending order
Arrays.sort(items, (a, b) -> Double.compare(a.ratio, b.ratio));

// ✓ Correct - descending order
Arrays.sort(items, (a, b) -> Double.compare(b.ratio, a.ratio));
```

### 2. Integer Division
```java
// ✗ Wrong - integer division loses precision
double ratio = value / weight;

// ✓ Correct - cast to double
double ratio = (double) value / weight;
```

### 3. Array Indexing
```java
// ✗ Wrong - deadline is 1-based, array is 0-based
slot[jobs[i].deadline] = jobs[i].id;

// ✓ Correct - subtract 1
slot[jobs[i].deadline - 1] = jobs[i].id;
```

---

## Key Takeaways

1. **Greedy algorithms** make locally optimal choices
2. **Fractional Knapsack**: Sort by value/weight ratio
3. **Job Sequencing**: Sort by profit, schedule late
4. Both achieve **optimal solutions** using greedy approach
5. Time complexity: **O(n log n)** due to sorting
6. **Java features**: Lambda expressions, custom comparators

---

## Applications

### Fractional Knapsack
- Resource allocation
- Budget optimization
- Load balancing
- Investment portfolios

### Job Sequencing
- Task scheduling
- CPU scheduling
- Project management
- Manufacturing scheduling

---

## Next Steps

- **Practical 5**: Compare Greedy vs DP for Knapsack
- **Understand**: When greedy works and when it doesn't
- **Practice**: More greedy problems (Activity Selection, Huffman Coding)
