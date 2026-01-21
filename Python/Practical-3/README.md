# Practical 3: Advanced Sorting Techniques - Python

## Overview
This practical implements three advanced sorting algorithms in Python: Merge Sort, Heap Sort, and Quick Sort. All have O(n log n) average time complexity, making them efficient for large datasets.

---

## 1. Merge Sort (`merge_sort.py`)

### Algorithm (Divide and Conquer)
1. **Divide**: Split array into two halves
2. **Conquer**: Recursively sort both halves
3. **Combine**: Merge the sorted halves

### Python Implementation

```python
def merge(arr, left, mid, right):
    """Merge two sorted subarrays"""
    # Create temporary arrays using slicing
    left_arr = arr[left:mid + 1]
    right_arr = arr[mid + 1:right + 1]
    
    i = j = 0
    k = left
    comparisons = 0
    
    # Merge the temp arrays back
    while i < len(left_arr) and j < len(right_arr):
        comparisons += 1
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
    
    # Copy remaining elements
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1
    
    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1
    
    return comparisons


def merge_sort(arr, left, right):
    """Sort array using Merge Sort"""
    comparisons = 0
    
    if left < right:
        mid = (left + right) // 2
        
        # Sort first and second halves
        comparisons += merge_sort(arr, left, mid)
        comparisons += merge_sort(arr, mid + 1, right)
        
        # Merge the sorted halves
        comparisons += merge(arr, left, mid, right)
    
    return comparisons
```

### How It Works

```
Initial: [38, 27, 43, 3, 9, 82, 10]

DIVIDE PHASE:
            [38, 27, 43, 3, 9, 82, 10]
                    /          \
        [38, 27, 43, 3]      [9, 82, 10]
            /    \              /    \
      [38, 27]  [43, 3]    [9, 82]  [10]
        /  \      /  \       /  \      |
      [38] [27] [43] [3]   [9] [82]  [10]

CONQUER PHASE (Merge):
      [38] [27] [43] [3]   [9] [82]  [10]
        \  /      \  /       \  /      |
      [27, 38]  [3, 43]    [9, 82]  [10]
            \    /              \    /
        [3, 27, 38, 43]      [9, 10, 82]
                    \          /
              [3, 9, 10, 27, 38, 43, 82] ✓
```

### Merge Step Example

```
Merging [27, 38] and [3, 43]:

left_arr = [27, 38]    right_arr = [3, 43]
i=0, j=0

Compare 27 vs 3  → 3 smaller  → result = [3]
i=0, j=1

Compare 27 vs 43 → 27 smaller → result = [3, 27]
i=1, j=1

Compare 38 vs 43 → 38 smaller → result = [3, 27, 38]
i=2, j=1

Left exhausted, copy remaining: result = [3, 27, 38, 43] ✓
```

### Python Features

#### List Slicing
```python
# Create subarray from index a to b (inclusive)
left_arr = arr[left:mid + 1]
right_arr = arr[mid + 1:right + 1]
```

#### Multiple Conditions
```python
while i < len(left_arr) and j < len(right_arr):
```

### Complexity
- **Time**: O(n log n) - all cases
- **Space**: O(n) - temporary arrays
- **Stable**: Yes - maintains order of equal elements

### Advantages
- Guaranteed O(n log n)
- Stable sort
- Predictable performance
- Good for linked lists

---

## 2. Heap Sort (`heap_sort.py`)

### Algorithm
1. Build a Max Heap from array
2. Repeatedly extract maximum (root) and rebuild heap

### Max Heap Property
For every node i:
- Parent value ≥ Children values
- `parent[i] ≥ left_child[2i+1]` and `right_child[2i+2]`

### Python Implementation

```python
def heapify(arr, n, i):
    """Convert subtree rooted at i into a max heap"""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    comparisons = 0
    
    # Check if left child exists and is greater
    if left < n:
        comparisons += 1
        if arr[left] > arr[largest]:
            largest = left
    
    # Check if right child exists and is greater
    if right < n:
        comparisons += 1
        if arr[right] > arr[largest]:
            largest = right
    
    # Swap and heapify if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        comparisons += heapify(arr, n, largest)
    
    return comparisons


def heap_sort(arr):
    """Sort array using Heap Sort"""
    n = len(arr)
    comparisons = 0
    
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        comparisons += heapify(arr, n, i)
    
    # Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        # Move current root to end
        arr[0], arr[i] = arr[i], arr[0]
        
        # Heapify the reduced heap
        comparisons += heapify(arr, i, 0)
    
    return comparisons
```

### How It Works

```
Initial: [4, 10, 3, 5, 1]

BUILD MAX HEAP:
Start from last non-leaf: i = n//2 - 1 = 1

Heapify at i=1 (value=10):
      4
     / \
    10  3
   / \
  5   1

Compare 10 with 5,1 → 10 largest, no change

Heapify at i=0 (value=4):
      4
     / \
    10  3
   / \
  5   1

Compare 4 with 10,3 → 10 largest
Swap 4 ↔ 10:
      10
     / \
     4  3
   / \
  5   1

Heapify at i=1:
      10
     / \
     5  3
   / \
  4   1

Max Heap Built! ✓

SORTING PHASE:
Step 1: Swap root(10) with last(1)
[1, 5, 3, 4, 10]
Heapify [1,5,3,4]:
      5
     / \
    4   3
   /
  1
Result: [5, 4, 3, 1, 10]

Step 2: Swap root(5) with last(1)
[1, 4, 3, 5, 10]
Heapify [1,4,3]:
      4
     / \
    1   3
Result: [4, 1, 3, 5, 10]

Step 3: Swap root(4) with last(3)
[3, 1, 4, 5, 10]
Heapify [3,1]:
      3
     /
    1
Result: [3, 1, 4, 5, 10]

Step 4: Swap root(3) with last(1)
[1, 3, 4, 5, 10] ✓ SORTED!
```

### Python Features

#### Reverse Range
```python
# Start from n//2-1, go down to 0
for i in range(n // 2 - 1, -1, -1):
```

#### Floor Division
```python
n // 2  # Integer division, rounds down
```

### Complexity
- **Time**: O(n log n) - all cases
- **Space**: O(1) - in-place sorting
- **Stable**: No

### Advantages
- In-place sorting
- No recursion stack overhead
- Good worst-case performance

---

## 3. Quick Sort (`quick_sort.py`)

### Algorithm (Divide and Conquer)
1. **Choose Pivot**: Select element (usually last)
2. **Partition**: Rearrange so smaller elements left, larger right
3. **Recurse**: Sort left and right subarrays

### Python Implementation

```python
def partition(arr, low, high):
    """Partition array and return pivot index"""
    pivot = arr[high]
    i = low - 1
    comparisons = 0
    swaps = 0
    
    for j in range(low, high):
        comparisons += 1
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            swaps += 1
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    swaps += 1
    
    return i + 1, comparisons, swaps


def quick_sort(arr, low, high):
    """Sort array using Quick Sort"""
    comparisons = 0
    swaps = 0
    
    if low < high:
        # Partition array
        pivot_idx, comp, swap = partition(arr, low, high)
        comparisons += comp
        swaps += swap
        
        # Sort elements before and after partition
        comp1, swap1 = quick_sort(arr, low, pivot_idx - 1)
        comp2, swap2 = quick_sort(arr, pivot_idx + 1, high)
        
        comparisons += comp1 + comp2
        swaps += swap1 + swap2
    
    return comparisons, swaps
```

### How It Works

```
Initial: [10, 80, 30, 90, 40, 50, 70]
Pivot = 70 (last element)

PARTITION:
i = -1 (before start)

j=0: 10 ≤ 70 → i=0, swap arr[0]↔arr[0] → [10, 80, 30, 90, 40, 50, 70]
j=1: 80 > 70  → no swap
j=2: 30 ≤ 70 → i=1, swap arr[1]↔arr[2] → [10, 30, 80, 90, 40, 50, 70]
j=3: 90 > 70  → no swap
j=4: 40 ≤ 70 → i=2, swap arr[2]↔arr[4] → [10, 30, 40, 90, 80, 50, 70]
j=5: 50 ≤ 70 → i=3, swap arr[3]↔arr[5] → [10, 30, 40, 50, 80, 90, 70]

Place pivot: i+1=4, swap arr[4]↔arr[6] → [10, 30, 40, 50, 70, 90, 80]

Pivot 70 now in correct position!
Left subarray: [10, 30, 40, 50]
Right subarray: [90, 80]

RECURSION TREE:
                [10, 80, 30, 90, 40, 50, 70]
                          |
                    pivot=70
                /                    \
       [10, 30, 40, 50]          [90, 80]
            |                        |
        pivot=50                 pivot=80
       /        \                /        \
  [10,30,40]    []          [90]         []
      |
  pivot=40
   /     \
[10,30]   []
   |
pivot=30
 /    \
[10]   []

Final: [10, 30, 40, 50, 70, 80, 90] ✓
```

### Partition Visualization

```
Array: [8, 3, 1, 7, 0, 10, 2]  Pivot = 2

Step-by-step partition:
i=-1  [8, 3, 1, 7, 0, 10, 2]  j=0, 8>2, no change
i=-1  [8, 3, 1, 7, 0, 10, 2]  j=1, 3>2, no change
i=-1  [8, 3, 1, 7, 0, 10, 2]  j=2, 1≤2, i=0, swap
i=0   [1, 3, 8, 7, 0, 10, 2]  j=3, 7>2, no change
i=0   [1, 3, 8, 7, 0, 10, 2]  j=4, 0≤2, i=1, swap
i=1   [1, 0, 8, 7, 3, 10, 2]  j=5, 10>2, no change

Place pivot at i+1=2:
      [1, 0, 2, 7, 3, 10, 8]
             ↑
           Pivot in place!
```

### Python Features

#### Multiple Return Values
```python
pivot_idx, comp, swap = partition(arr, low, high)
comp1, swap1 = quick_sort(arr, low, pivot_idx - 1)
```

#### Augmented Assignment
```python
i += 1
comparisons += comp
```

### Complexity
- **Time**: O(n log n) average, O(n²) worst
- **Space**: O(log n) - recursion stack
- **Stable**: No (can be made stable)

### Advantages
- Fast in practice
- In-place sorting
- Good cache performance

### Disadvantages
- O(n²) worst case (sorted array with last pivot)
- Not stable

---

## Comparison of Three Algorithms

| Feature | Merge Sort | Heap Sort | Quick Sort |
|---------|-----------|-----------|------------|
| **Average Time** | O(n log n) | O(n log n) | O(n log n) |
| **Worst Time** | O(n log n) | O(n log n) | O(n²) |
| **Space** | O(n) | O(1) | O(log n) |
| **Stable** | Yes | No | No |
| **In-place** | No | Yes | Yes |
| **Best For** | Linked lists | Guaranteed time | General purpose |

---

## Python-Specific Features Summary

### 1. List Slicing
```python
left_arr = arr[left:mid + 1]  # Create subarray
```

### 2. Time Measurement
```python
import time
start = time.perf_counter()
# ... algorithm ...
end = time.perf_counter()
duration = (end - start) * 1000000  # microseconds
```

### 3. F-String Formatting
```python
print(f"Time taken: {duration:.2f} microseconds")
```

### 4. Tuple Packing/Unpacking
```python
return i + 1, comparisons, swaps
pivot_idx, comp, swap = partition(arr, low, high)
```

---

## How to Run

```bash
# Run Merge Sort
python merge_sort.py

# Run Heap Sort
python heap_sort.py

# Run Quick Sort
python quick_sort.py
```

### Sample Output (Merge Sort)
```
=== Merge Sort (Divide and Conquer) ===

Enter number of elements: 7
Enter elements:
Element 1: 38
Element 2: 27
Element 3: 43
Element 4: 3
Element 5: 9
Element 6: 82
Element 7: 10

Original array: [38, 27, 43, 3, 9, 82, 10]
Sorted array: [3, 9, 10, 27, 38, 43, 82]

Total comparisons: 13
Time taken: 8.50 microseconds
Time Complexity: O(n log n) = O(7 log 7)
```

---

## When to Use Which?

### Use Merge Sort When:
- Need stable sort
- Guaranteed O(n log n) required
- Sorting linked lists
- External sorting (data doesn't fit in memory)

### Use Heap Sort When:
- Limited memory (in-place required)
- Guaranteed O(n log n) required
- Don't need stable sort
- Priority queue operations

### Use Quick Sort When:
- Average case performance matters most
- Working with arrays (not linked lists)
- Cache performance is important
- Memory available for recursion stack

---

## Key Takeaways

1. **All O(n log n)**: Much faster than O(n²) for large data
2. **Divide and Conquer**: Merge Sort and Quick Sort use this paradigm
3. **Trade-offs**: Time vs Space vs Stability
4. **Python Features**: Slicing, tuple unpacking, timing
5. **Merge Sort**: Guaranteed performance, needs extra space
6. **Heap Sort**: In-place, not stable
7. **Quick Sort**: Fast in practice, can be O(n²) worst case

---

## Next Steps
- **Practical 4**: Greedy algorithms (Fractional Knapsack, Job Sequencing)
- **Practice**: Implement with different pivot strategies
- **Compare**: Performance on different data distributions
