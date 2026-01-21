# Practical 1: Basic Iterative Sorting Algorithms

## Overview
This practical implements three fundamental sorting algorithms: Bubble Sort, Selection Sort, and Insertion Sort. All use iterative approaches with O(n²) time complexity.

---

## 1. Bubble Sort (`bubble_sort.cpp`)

### Algorithm Explanation
Bubble Sort repeatedly compares adjacent elements and swaps them if they're in the wrong order. The largest element "bubbles up" to its correct position in each pass.

### How It Works
1. Start from the first element
2. Compare each pair of adjacent elements
3. Swap if the left element is greater than the right
4. After each pass, the largest unsorted element reaches its final position
5. Repeat for n-1 passes

### Time Complexity
- **Best Case**: O(n) - when array is already sorted
- **Average Case**: O(n²)
- **Worst Case**: O(n²) - when array is reverse sorted

### Space Complexity
O(1) - In-place sorting

### Example
```
Input: [5, 2, 8, 1, 9]
Pass 1: [2, 5, 1, 8, 9] → 9 reaches end
Pass 2: [2, 1, 5, 8, 9] → 8 in position
Pass 3: [1, 2, 5, 8, 9] → 5 in position
Output: [1, 2, 5, 8, 9]
```

---

## 2. Selection Sort (`selection_sort.cpp`)

### Algorithm Explanation
Selection Sort divides the array into sorted and unsorted regions. It repeatedly finds the minimum element from the unsorted region and places it at the beginning.

### How It Works
1. Find the minimum element in the unsorted array
2. Swap it with the first element of the unsorted portion
3. Move the boundary of the sorted region one position right
4. Repeat until the entire array is sorted

### Time Complexity
- **Best Case**: O(n²)
- **Average Case**: O(n²)
- **Worst Case**: O(n²)

### Space Complexity
O(1) - In-place sorting

### Example
```
Input: [64, 25, 12, 22, 11]
Step 1: [11, 25, 12, 22, 64] → min=11 swapped with 64
Step 2: [11, 12, 25, 22, 64] → min=12 swapped with 25
Step 3: [11, 12, 22, 25, 64] → min=22 swapped with 25
Step 4: [11, 12, 22, 25, 64] → sorted
```

---

## 3. Insertion Sort (`insertion_sort.cpp`)

### Algorithm Explanation
Insertion Sort builds the sorted array one element at a time by inserting each element into its correct position among the previously sorted elements.

### How It Works
1. Start with the second element (first element is considered sorted)
2. Compare the current element (key) with elements in the sorted portion
3. Shift all elements greater than the key one position to the right
4. Insert the key at its correct position
5. Repeat for all elements

### Time Complexity
- **Best Case**: O(n) - when array is already sorted
- **Average Case**: O(n²)
- **Worst Case**: O(n²) - when array is reverse sorted

### Space Complexity
O(1) - In-place sorting

### Example
```
Input: [12, 11, 13, 5, 6]
Step 1: [11, 12, 13, 5, 6] → 11 inserted before 12
Step 2: [11, 12, 13, 5, 6] → 13 already in place
Step 3: [5, 11, 12, 13, 6] → 5 inserted at start
Step 4: [5, 6, 11, 12, 13] → 6 inserted after 5
```

---

## Comparison of All Three Algorithms

| Algorithm | Best Case | Average Case | Worst Case | Stable | In-Place |
|-----------|-----------|--------------|------------|--------|----------|
| Bubble Sort | O(n) | O(n²) | O(n²) | Yes | Yes |
| Selection Sort | O(n²) | O(n²) | O(n²) | No | Yes |
| Insertion Sort | O(n) | O(n²) | O(n²) | Yes | Yes |

### When to Use
- **Bubble Sort**: Educational purposes, small datasets
- **Selection Sort**: When memory writes are costly (minimizes swaps)
- **Insertion Sort**: Small datasets, nearly sorted arrays, online sorting

---

## How to Compile and Run

### For all programs:
```bash
# Compile
g++ bubble_sort.cpp -o bubble_sort
g++ selection_sort.cpp -o selection_sort
g++ insertion_sort.cpp -o insertion_sort

# Run
./bubble_sort
./selection_sort
./insertion_sort
```

### Sample Input
```
Enter number of elements: 5
Enter elements: 64 34 25 12 22
```

### Sample Output
```
Original array: 64 34 25 12 22
Sorted array: 12 22 25 34 64
```
