# Practical 1: Basic Iterative Sorting Algorithms - Python

## Overview
This practical implements three fundamental sorting algorithms in Python: Bubble Sort, Selection Sort, and Insertion Sort. All have O(n²) time complexity but differ in their approach and performance characteristics.

---

## 1. Bubble Sort (`bubble_sort.py`)

### Algorithm
Repeatedly compares adjacent elements and swaps them if they're in wrong order. The largest element "bubbles up" to the end in each pass.

### Python Implementation

```python
def bubble_sort(arr):
    """Sort array using Bubble Sort algorithm"""
    n = len(arr)
    comparisons = 0
    swaps = 0
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                # Swap using Python tuple unpacking
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
                swapped = True
        
        # Optimization: stop if no swaps
        if not swapped:
            break
    
    return comparisons, swaps
```

### How It Works

**Pass 1:**
```
[64, 34, 25, 12, 22]
Compare 64, 34 → Swap → [34, 64, 25, 12, 22]
Compare 64, 25 → Swap → [34, 25, 64, 12, 22]
Compare 64, 12 → Swap → [34, 25, 12, 64, 22]
Compare 64, 22 → Swap → [34, 25, 12, 22, 64]
Largest (64) in position!
```

**Pass 2:**
```
[34, 25, 12, 22, 64]
Compare 34, 25 → Swap → [25, 34, 12, 22, 64]
Compare 34, 12 → Swap → [25, 12, 34, 22, 64]
Compare 34, 22 → Swap → [25, 12, 22, 34, 64]
Second largest (34) in position!
```

### Python-Specific Features

#### 1. Tuple Unpacking for Swap
```python
# Python way (elegant)
arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Traditional way (verbose)
temp = arr[j]
arr[j] = arr[j + 1]
arr[j + 1] = temp
```

#### 2. Multiple Return Values
```python
def bubble_sort(arr):
    # ... sorting logic ...
    return comparisons, swaps

# Unpack return values
comp, swap = bubble_sort(arr)
```

#### 3. Docstrings
```python
def bubble_sort(arr):
    """Sort array using Bubble Sort algorithm"""
```

### Complexity
- **Time**: O(n²) - nested loops
- **Space**: O(1) - in-place sorting
- **Best Case**: O(n) - with early termination

### When to Use
- Small datasets (n < 100)
- Nearly sorted data (benefits from early termination)
- Educational purposes

---

## 2. Selection Sort (`selection_sort.py`)

### Algorithm
Repeatedly finds the minimum element from unsorted portion and places it at the beginning.

### Python Implementation

```python
def selection_sort(arr):
    """Sort array using Selection Sort algorithm"""
    n = len(arr)
    comparisons = 0
    swaps = 0
    
    for i in range(n):
        # Find minimum element in unsorted array
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap minimum element with first element
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1
    
    return comparisons, swaps
```

### How It Works

```
Initial: [64, 25, 12, 22, 11]

Pass 1:
Find min in [64, 25, 12, 22, 11] → 11 at index 4
Swap 64 ↔ 11
Result: [11, 25, 12, 22, 64]

Pass 2:
Find min in [25, 12, 22, 64] → 12 at index 2
Swap 25 ↔ 12
Result: [11, 12, 25, 22, 64]

Pass 3:
Find min in [25, 22, 64] → 22 at index 3
Swap 25 ↔ 22
Result: [11, 12, 22, 25, 64]

Pass 4:
Find min in [25, 64] → 25 already in position
Result: [11, 12, 22, 25, 64] ✓
```

### Python Features

#### Range Function
```python
# Start from i+1, go to n (exclusive)
for j in range(i + 1, n):
```

#### Conditional Swap
```python
if min_idx != i:
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
```

### Complexity
- **Time**: O(n²) - always, no best case
- **Space**: O(1)
- **Swaps**: O(n) - minimum number of swaps

### Advantages
- Fewer swaps than Bubble Sort
- Simple and intuitive
- Works well when swaps are expensive

---

## 3. Insertion Sort (`insertion_sort.py`)

### Algorithm
Builds sorted array one element at a time by inserting each element into its correct position.

### Python Implementation

```python
def insertion_sort(arr):
    """Sort array using Insertion Sort algorithm"""
    n = len(arr)
    comparisons = 0
    shifts = 0
    
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        # Move elements greater than key one position ahead
        while j >= 0 and arr[j] > key:
            comparisons += 1
            arr[j + 1] = arr[j]
            shifts += 1
            j -= 1
        
        if j >= 0:
            comparisons += 1
        
        arr[j + 1] = key
    
    return comparisons, shifts
```

### How It Works

Think of sorting playing cards in your hand:

```
Initial: [12, 11, 13, 5, 6]

Step 1: key = 11
[12, 11, 13, 5, 6]
 ↑   ↑
Compare 12 > 11, shift 12 right
[12, 12, 13, 5, 6]
Insert 11 at position 0
[11, 12, 13, 5, 6]

Step 2: key = 13
[11, 12, 13, 5, 6]
     ↑   ↑
13 > 12, already in position
[11, 12, 13, 5, 6]

Step 3: key = 5
[11, 12, 13, 5, 6]
 ↑           ↑
Shift 13, 12, 11 right
[11, 11, 12, 13, 6]
Insert 5 at position 0
[5, 11, 12, 13, 6]

Step 4: key = 6
[5, 11, 12, 13, 6]
 ↑              ↑
Shift 13, 12, 11 right
Insert 6 after 5
[5, 6, 11, 12, 13] ✓
```

### Python Features

#### While Loop
```python
while j >= 0 and arr[j] > key:
    arr[j + 1] = arr[j]
    j -= 1
```

#### Short-circuit Evaluation
```python
# Python evaluates left to right
# If j < 0, doesn't evaluate arr[j]
while j >= 0 and arr[j] > key:
```

### Complexity
- **Time**: O(n²) worst case
- **Best Case**: O(n) - already sorted
- **Space**: O(1)

### Advantages
- Efficient for small datasets
- Efficient for nearly sorted data
- Stable sort (maintains relative order)
- Online algorithm (can sort as data arrives)

---

## Comparison of Three Algorithms

| Feature | Bubble Sort | Selection Sort | Insertion Sort |
|---------|-------------|----------------|----------------|
| **Time Complexity** | O(n²) | O(n²) | O(n²) |
| **Best Case** | O(n) | O(n²) | O(n) |
| **Swaps** | O(n²) | O(n) | O(n²) |
| **Stability** | Yes | No | Yes |
| **Adaptive** | Yes | No | Yes |
| **Use Case** | Nearly sorted | Minimize swaps | Small/Nearly sorted |

### Definitions
- **Stable**: Maintains relative order of equal elements
- **Adaptive**: Performs better on partially sorted data

---

## Python-Specific Features Summary

### 1. List Operations
```python
n = len(arr)  # Get length
arr[i]        # Access element
```

### 2. Input/Output
```python
n = int(input("Enter number: "))
arr = []
arr.append(value)
print(f"Array: {arr}")
```

### 3. F-strings (Python 3.6+)
```python
print(f"Sorted array: {arr}")
print(f"Comparisons: {comparisons}")
```

### 4. Main Guard
```python
if __name__ == "__main__":
    main()
```
Ensures code runs only when executed directly, not when imported.

---

## How to Run

```bash
# Run Bubble Sort
python bubble_sort.py

# Run Selection Sort
python selection_sort.py

# Run Insertion Sort
python insertion_sort.py
```

### Sample Input
```
Enter number of elements: 5
Enter elements:
Element 1: 64
Element 2: 34
Element 3: 25
Element 4: 12
Element 5: 22
```

### Sample Output (Bubble Sort)
```
=== Bubble Sort ===

Original array: [64, 34, 25, 12, 22]
Sorted array: [12, 22, 25, 34, 64]

Total comparisons: 10
Total swaps: 8
Time Complexity: O(n^2) = O(5^2)
```

---

## Performance Analysis

### Test with 1000 elements
```
Bubble Sort:    ~500,000 comparisons
Selection Sort: ~500,000 comparisons, fewer swaps
Insertion Sort: ~250,000 comparisons (if partially sorted)
```

---

## Common Mistakes

### 1. Index Out of Bounds
```python
# ✗ Wrong - goes out of bounds
for j in range(0, n):
    if arr[j] > arr[j + 1]:  # Error when j = n-1

# ✓ Correct
for j in range(0, n - i - 1):
    if arr[j] > arr[j + 1]:
```

### 2. Not Using Early Termination (Bubble Sort)
```python
# ✗ Without optimization
for i in range(n):
    for j in range(n - i - 1):
        # Always completes all passes

# ✓ With optimization
for i in range(n):
    swapped = False
    for j in range(n - i - 1):
        if swap_occurred:
            swapped = True
    if not swapped:
        break  # Already sorted
```

### 3. Incorrect Selection Sort Logic
```python
# ✗ Wrong - swaps immediately
for i in range(n):
    for j in range(i + 1, n):
        if arr[j] < arr[i]:
            arr[i], arr[j] = arr[j], arr[i]  # Multiple swaps

# ✓ Correct - finds minimum first
for i in range(n):
    min_idx = i
    for j in range(i + 1, n):
        if arr[j] < arr[min_idx]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Single swap
```

---

## Key Takeaways

1. **Python Syntax**: Clean and readable
2. **Tuple Unpacking**: Elegant swapping
3. **List Operations**: Built-in functions like `len()`, `append()`
4. **All O(n²)**: Suitable only for small datasets
5. **Insertion Sort**: Best for nearly sorted data
6. **Selection Sort**: Minimizes swaps
7. **Bubble Sort**: Simple but slowest in practice

---

## Next Steps
- **Practical 2**: Binary Search with O(log n)
- **Practical 3**: Advanced sorting with O(n log n)
- **Practice**: Implement these on different data types
