# Practical 2: Binary Search (Divide and Conquer) - Python

## Overview
This practical implements Binary Search algorithm using both iterative and recursive approaches in Python. Binary Search is a highly efficient search algorithm with O(log n) time complexity that works on sorted arrays.

---

## Binary Search Algorithm (`binary_search.py`)

### Problem Statement
Given a **sorted** array and a target value, find the index of the target in the array. If not found, return -1.

### Prerequisite
⚠️ **Array must be sorted!** Binary Search only works on sorted data.

---

## Divide and Conquer Strategy

### Core Idea
1. **Divide**: Split search space in half by finding middle element
2. **Conquer**: 
   - If middle = target → Found!
   - If middle < target → Search right half
   - If middle > target → Search left half
3. **Repeat** until found or search space exhausted

### Why O(log n)?
Each comparison eliminates half the remaining elements:
```
n → n/2 → n/4 → n/8 → ... → 1
Number of steps = log₂(n)
```

---

## Implementation 1: Iterative Approach

```python
def binary_search(arr, target):
    """
    Search for target in sorted array using Binary Search
    Returns: (index, comparisons) or (-1, comparisons) if not found
    """
    left = 0
    right = len(arr) - 1
    comparisons = 0
    
    while left <= right:
        mid = (left + right) // 2
        comparisons += 1
        
        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1, comparisons
```

### Python Features

#### 1. Integer Division
```python
# Python 3: // for integer division
mid = (left + right) // 2

# Regular division gives float
mid = (left + right) / 2  # Not what we want!
```

#### 2. Multiple Return Values
```python
index, comparisons = binary_search(arr, target)
```

#### 3. len() Function
```python
right = len(arr) - 1  # Last index
```

---

## Implementation 2: Recursive Approach

```python
def binary_search_recursive(arr, target, left, right, comparisons=0):
    """Recursive implementation of Binary Search"""
    if left > right:
        return -1, comparisons
    
    mid = (left + right) // 2
    comparisons += 1
    
    if arr[mid] == target:
        return mid, comparisons
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right, comparisons)
    else:
        return binary_search_recursive(arr, target, left, mid - 1, comparisons)
```

### Recursion Breakdown

**Base Case**: `left > right` (search space exhausted)

**Recursive Cases**:
- Found: Return index
- Target greater: Recurse on right half
- Target smaller: Recurse on left half

---

## Step-by-Step Example

### Search for 23 in [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]

```
Step 1:
Array: [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
Left = 0, Right = 9
Mid = (0 + 9) // 2 = 4
arr[4] = 16
16 < 23 → Search right half

Step 2:
Array: [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
                        ↑
Left = 5, Right = 9
Mid = (5 + 9) // 2 = 7
arr[7] = 56
56 > 23 → Search left half

Step 3:
Array: [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
                        ↑
Left = 5, Right = 6
Mid = (5 + 6) // 2 = 5
arr[5] = 23
23 == 23 → FOUND at index 5! ✓

Total Comparisons: 3
```

### Comparison with Linear Search
```
Linear Search: Would need 6 comparisons
Binary Search: Only needed 3 comparisons

For n=10: log₂(10) ≈ 3.32 comparisons
```

---

## Time Measurement in Python

```python
import time

start = time.perf_counter()
# ... algorithm execution ...
end = time.perf_counter()

duration = (end - start) * 1000000  # Convert to microseconds
print(f"Time taken: {duration:.2f} microseconds")
```

### Python Timing Functions

| Function | Resolution | Use Case |
|----------|-----------|----------|
| `time.time()` | ~1 second | Long operations |
| `time.perf_counter()` | Microseconds | Performance measurement |
| `time.process_time()` | CPU time | CPU-bound tasks |

---

## Complexity Analysis

### Time Complexity

| Case | Complexity | Explanation |
|------|-----------|-------------|
| **Best** | O(1) | Target at middle on first try |
| **Average** | O(log n) | Target somewhere in array |
| **Worst** | O(log n) | Target at end or not present |

### Space Complexity

| Implementation | Space | Reason |
|----------------|-------|--------|
| **Iterative** | O(1) | Only variables |
| **Recursive** | O(log n) | Call stack depth |

### Why Binary Search is Fast

```
Array Size    Linear Search    Binary Search
    10              10               4
   100             100               7
  1000            1000              10
 10000           10000              14
100000          100000              17

For 1 million elements:
Linear: 1,000,000 comparisons
Binary: Only 20 comparisons! 🚀
```

---

## Detailed Trace Example

### Search for 7 in [1, 3, 5, 7, 9, 11, 13, 15]

```python
Initial:
arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7
left = 0, right = 7

Iteration 1:
mid = (0 + 7) // 2 = 3
arr[3] = 7
7 == 7 → FOUND! ✓
```

### Search for 14 in [1, 3, 5, 7, 9, 11, 13, 15]

```python
Initial:
arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 14
left = 0, right = 7

Iteration 1:
mid = (0 + 7) // 2 = 3
arr[3] = 7
7 < 14 → Search right
left = 4, right = 7

Iteration 2:
mid = (4 + 7) // 2 = 5
arr[5] = 11
11 < 14 → Search right
left = 6, right = 7

Iteration 3:
mid = (6 + 7) // 2 = 6
arr[6] = 13
13 < 14 → Search right
left = 7, right = 7

Iteration 4:
mid = (7 + 7) // 2 = 7
arr[7] = 15
15 > 14 → Search left
left = 7, right = 6

left > right → NOT FOUND ✗
```

---

## Python-Specific Features

### 1. F-String Formatting
```python
print(f"Element found at index: {index}")
print(f"Time taken: {duration:.2f} microseconds")
```

### 2. Conditional Expression
```python
# Ternary operator
result = "Found" if index != -1 else "Not found"
```

### 3. Import Statement
```python
import time
start = time.perf_counter()
```

### 4. Default Arguments
```python
def binary_search_recursive(arr, target, left, right, comparisons=0):
    # comparisons defaults to 0 if not provided
```

---

## How to Run

```bash
python binary_search.py
```

### Sample Input
```
Enter number of elements: 8
Enter elements in sorted order:
Element 1: 2
Element 2: 5
Element 3: 8
Element 4: 12
Element 5: 16
Element 6: 23
Element 7: 38
Element 8: 56

Enter element to search: 23
```

### Sample Output
```
=== Binary Search (Divide and Conquer) ===

Array: [2, 5, 8, 12, 16, 23, 38, 56]
Searching for: 23

--- Iterative Binary Search ---
Element found at index: 5
Comparisons: 3
Time taken: 1.50 microseconds

--- Recursive Binary Search ---
Element found at index: 5
Comparisons: 3
Time taken: 2.30 microseconds

Time Complexity: O(log n) = O(log 8)
```

---

## Common Mistakes

### 1. Unsorted Array
```python
# ✗ Wrong - won't work correctly
arr = [5, 2, 8, 1, 9]
binary_search(arr, 8)  # Unpredictable result

# ✓ Correct - sort first
arr = [5, 2, 8, 1, 9]
arr.sort()
binary_search(arr, 8)  # Works correctly
```

### 2. Incorrect Middle Calculation
```python
# ✗ Potential integer overflow (in other languages)
mid = (left + right) / 2

# ✓ Better (avoids overflow)
mid = left + (right - left) // 2

# ✓ Also correct in Python (no overflow)
mid = (left + right) // 2
```

### 3. Wrong Loop Condition
```python
# ✗ Wrong - misses when left == right
while left < right:

# ✓ Correct
while left <= right:
```

### 4. Incorrect Update
```python
# ✗ Wrong - infinite loop possible
left = mid
right = mid

# ✓ Correct - move past mid
left = mid + 1
right = mid - 1
```

---

## Iterative vs Recursive

### Iterative Advantages
- **Faster**: No function call overhead
- **Less Memory**: O(1) space
- **No Stack Overflow**: Safe for large arrays

### Recursive Advantages
- **Cleaner Code**: More intuitive
- **Divide & Conquer**: Clear structure
- **Educational**: Better shows the concept

### Performance Comparison
```python
Array size: 10000
Iterative:  12 comparisons, 15 microseconds
Recursive:  12 comparisons, 18 microseconds

Difference: Minimal for practical purposes
```

---

## Applications of Binary Search

1. **Dictionary Lookup**: Finding words
2. **Database Indexing**: Fast record retrieval
3. **Finding Boundaries**: First/last occurrence
4. **Debugging**: Finding the point where bug starts
5. **Math Problems**: Finding square root, nth root
6. **Game Development**: AI decision trees

---

## Variations

### 1. Find First Occurrence
```python
def find_first(arr, target):
    result = -1
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            right = mid - 1  # Continue searching left
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result
```

### 2. Find Last Occurrence
```python
def find_last(arr, target):
    result = -1
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            left = mid + 1  # Continue searching right
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result
```

---

## Key Takeaways

1. **O(log n) Complexity**: Extremely fast for large datasets
2. **Requires Sorted Data**: Must sort first if unsorted
3. **Divide and Conquer**: Halves search space each time
4. **Two Implementations**: Iterative (faster) vs Recursive (cleaner)
5. **Python Features**: Integer division `//`, tuple unpacking, `time.perf_counter()`
6. **Comparisons**: Much fewer than linear search
7. **Space Trade-off**: Iterative O(1) vs Recursive O(log n)

---

## Practice Problems

1. Find first occurrence of element in array
2. Find last occurrence of element in array
3. Count occurrences of element
4. Find element in rotated sorted array
5. Find square root using binary search

---

## Next Steps
- **Practical 3**: Advanced sorting algorithms (Merge, Heap, Quick Sort)
- **Understand**: Why sorting enables binary search
- **Compare**: Linear search vs Binary search performance
