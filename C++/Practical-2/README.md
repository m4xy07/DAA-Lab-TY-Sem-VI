# Practical 2: Binary Search (Divide and Conquer)

## Overview
This practical implements Binary Search using the Divide and Conquer approach with recursion. Binary Search is an efficient algorithm for finding an element in a sorted array.

---

## Binary Search (`binary_search.cpp`)

### Algorithm Explanation
Binary Search works by repeatedly dividing the search interval in half. It compares the target value with the middle element and eliminates half of the remaining elements based on the comparison.

### Divide and Conquer Strategy
1. **Divide**: Split the array into two halves at the middle
2. **Conquer**: Recursively search in the appropriate half
3. **Combine**: Return the index when element is found

### How It Works
1. Find the middle element of the array
2. If the middle element equals the target, return its index
3. If target < middle element, search in the left half
4. If target > middle element, search in the right half
5. Repeat until element is found or subarray becomes empty

### Pseudocode
```
binarySearch(arr, low, high, key):
    if low > high:
        return -1  // Element not found
    
    mid = low + (high - low) / 2
    
    if arr[mid] == key:
        return mid
    else if arr[mid] > key:
        return binarySearch(arr, low, mid - 1, key)
    else:
        return binarySearch(arr, mid + 1, high, key)
```

### Time Complexity
- **Best Case**: O(1) - when element is at middle
- **Average Case**: O(log n)
- **Worst Case**: O(log n) - when element is at end or not present

### Space Complexity
- **Recursive Implementation**: O(log n) - due to recursion stack
- **Iterative Implementation**: O(1)

### Recurrence Relation
```
T(n) = T(n/2) + O(1)
```
Using Master's Theorem: T(n) = O(log n)

---

## Step-by-Step Example

### Example 1: Element Found
```
Array: [2, 5, 8, 12, 16, 23, 38, 45, 56, 67, 78]
Target: 23

Step 1: low=0, high=10, mid=5
        arr[5]=23 == target
        Found at index 5 ✓

Total comparisons: 1
```

### Example 2: Element in Right Half
```
Array: [2, 5, 8, 12, 16, 23, 38, 45, 56, 67, 78]
Target: 67

Step 1: low=0, high=10, mid=5
        arr[5]=23 < 67 → search right half

Step 2: low=6, high=10, mid=8
        arr[8]=56 < 67 → search right half

Step 3: low=9, high=10, mid=9
        arr[9]=67 == target
        Found at index 9 ✓

Total comparisons: 3
```

### Example 3: Element Not Found
```
Array: [2, 5, 8, 12, 16, 23, 38, 45, 56, 67, 78]
Target: 50

Step 1: low=0, high=10, mid=5
        arr[5]=23 < 50 → search right half

Step 2: low=6, high=10, mid=8
        arr[8]=56 > 50 → search left half

Step 3: low=6, high=7, mid=6
        arr[6]=38 < 50 → search right half

Step 4: low=7, high=7, mid=7
        arr[7]=45 < 50 → search right half

Step 5: low=8, high=7
        low > high → Element not found ✗

Total comparisons: 4
```

---

## Advantages of Binary Search
1. **Efficient**: Much faster than linear search for large datasets
2. **Guaranteed Performance**: Always O(log n) comparisons
3. **Divide and Conquer**: Classic example of the paradigm

## Limitations
1. **Requires Sorted Array**: Array must be sorted beforehand
2. **Random Access**: Requires array data structure (not suitable for linked lists)

---

## Comparison with Linear Search

| Aspect | Linear Search | Binary Search |
|--------|---------------|---------------|
| Time Complexity | O(n) | O(log n) |
| Prerequisite | None | Sorted array |
| Data Structure | Any | Array required |
| Best for | Small/Unsorted | Large/Sorted |

### Example Performance
For array of 1,000,000 elements:
- **Linear Search**: Up to 1,000,000 comparisons
- **Binary Search**: Maximum 20 comparisons

---

## How to Compile and Run

```bash
# Compile
g++ binary_search.cpp -o binary_search

# Run
./binary_search
```

### Sample Input
```
Enter number of elements: 7
Enter sorted elements: 10 20 30 40 50 60 70
Enter element to search: 40
```

### Sample Output
```
Element found at index: 3
```

### Sample Input (Not Found)
```
Enter number of elements: 7
Enter sorted elements: 10 20 30 40 50 60 70
Enter element to search: 35
```

### Sample Output
```
Element not found in array
```

---

## Key Points to Remember
1. Array **MUST** be sorted for binary search to work
2. Recursive implementation uses divide and conquer
3. Each comparison reduces search space by half
4. Logarithmic time complexity makes it very efficient
5. Index calculation: `mid = low + (high - low) / 2` prevents overflow
