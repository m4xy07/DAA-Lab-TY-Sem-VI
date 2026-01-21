# Practical 1: Basic Iterative Sorting Algorithms (Java)

## Overview
This practical implements three fundamental sorting algorithms in Java: Bubble Sort, Selection Sort, and Insertion Sort. All use iterative approaches with O(n²) time complexity.

---

## 1. Bubble Sort (`BubbleSort.java`)

### Algorithm Explanation
Bubble Sort repeatedly compares adjacent elements and swaps them if they're in the wrong order. The largest element "bubbles up" to its correct position in each pass.

### How It Works
1. Start from the first element
2. Compare each pair of adjacent elements
3. Swap if the left element is greater than the right
4. After each pass, the largest unsorted element reaches its final position
5. Repeat for n-1 passes

### Java Implementation Details
- Uses static methods for sorting and printing
- Scanner class for user input
- Array passed by reference for in-place sorting

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
Pass 3: [1, 2, 5, 8, 9] → sorted
Output: [1, 2, 5, 8, 9]
```

---

## 2. Selection Sort (`SelectionSort.java`)

### Algorithm Explanation
Selection Sort divides the array into sorted and unsorted regions. It repeatedly finds the minimum element from the unsorted region and places it at the beginning.

### How It Works
1. Find the minimum element in the unsorted array
2. Swap it with the first element of the unsorted portion
3. Move the boundary of the sorted region one position right
4. Repeat until the entire array is sorted

### Java Implementation Details
- Uses nested loops for finding minimum
- Swaps elements directly in the array
- No additional data structures needed

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

## 3. Insertion Sort (`InsertionSort.java`)

### Algorithm Explanation
Insertion Sort builds the sorted array one element at a time by inserting each element into its correct position among the previously sorted elements.

### How It Works
1. Start with the second element (first element is considered sorted)
2. Compare the current element (key) with elements in the sorted portion
3. Shift all elements greater than the key one position to the right
4. Insert the key at its correct position
5. Repeat for all elements

### Java Implementation Details
- Uses a key variable to hold the current element
- Shifts elements without swapping
- Efficient for small or nearly sorted arrays

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
javac BubbleSort.java
javac SelectionSort.java
javac InsertionSort.java

# Run
java BubbleSort
java SelectionSort
java InsertionSort
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

---

## Java-Specific Features Used

### Scanner Class
```java
Scanner sc = new Scanner(System.in);
int n = sc.nextInt();  // Read integer
sc.close();             // Close scanner
```

### Array Declaration
```java
int[] arr = new int[n];  // Dynamic array creation
```

### For Loop
```java
for (int i = 0; i < n; i++) {
    // Java uses 0-based indexing
}
```

### Method Signature
```java
public static void bubbleSort(int[] arr) {
    // Static method for utility functions
    // Array passed by reference
}
```

---

## Key Differences from C++

| Aspect | Java | C++ |
|--------|------|-----|
| Array Size | Dynamic (`new int[n]`) | Fixed or dynamic |
| Memory Management | Automatic (GC) | Manual |
| Input | Scanner class | cin or scanf |
| Array Passing | By reference (always) | By value/reference |
| Swap | Manual implementation | Can use std::swap |

---

## Common Mistakes to Avoid

1. **Array Bounds**: Java has strict bounds checking
   ```java
   // ✗ Wrong
   for (int i = 0; i <= n; i++)  // ArrayIndexOutOfBoundsException
   
   // ✓ Correct
   for (int i = 0; i < n; i++)
   ```

2. **Scanner Not Closed**: Always close Scanner
   ```java
   Scanner sc = new Scanner(System.in);
   // ... use scanner ...
   sc.close();  // Important!
   ```

3. **Integer Division**: Java performs integer division
   ```java
   int mid = (left + right) / 2;  // Integer result
   ```

---

## Performance Tips

### Bubble Sort Optimization
```java
boolean swapped;
for (int i = 0; i < n - 1; i++) {
    swapped = false;
    for (int j = 0; j < n - i - 1; j++) {
        if (arr[j] > arr[j + 1]) {
            swap(arr, j, j + 1);
            swapped = true;
        }
    }
    if (!swapped) break;  // Early exit if sorted
}
```

### Insertion Sort Best Practice
```java
// More efficient than repeated swaps
int key = arr[i];
int j = i - 1;
while (j >= 0 && arr[j] > key) {
    arr[j + 1] = arr[j];  // Shift instead of swap
    j--;
}
arr[j + 1] = key;
```

---

## Testing Scenarios

### Test Case 1: Already Sorted
```
Input: [1, 2, 3, 4, 5]
Expected: [1, 2, 3, 4, 5]
Best for: Bubble Sort, Insertion Sort (O(n))
```

### Test Case 2: Reverse Sorted
```
Input: [5, 4, 3, 2, 1]
Expected: [1, 2, 3, 4, 5]
Worst for: All three algorithms (O(n²))
```

### Test Case 3: Random Order
```
Input: [3, 1, 4, 1, 5, 9, 2, 6]
Expected: [1, 1, 2, 3, 4, 5, 6, 9]
Average case: O(n²)
```

### Test Case 4: Duplicates
```
Input: [3, 1, 2, 3, 1]
Expected: [1, 1, 2, 3, 3]
Tests stability
```

---

## Key Takeaways

1. **All three are O(n²)** in average case
2. **Bubble Sort**: Simple but inefficient
3. **Selection Sort**: Minimizes number of swaps
4. **Insertion Sort**: Best for small/nearly sorted data
5. **Java arrays**: Always 0-indexed with bounds checking
6. **Scanner**: Must be closed after use

---

## Next Steps

After mastering these basic sorts, move to:
- **Practical 2**: Binary Search (Divide and Conquer)
- **Practical 3**: Advanced sorting (Merge, Heap, Quick Sort) with O(n log n)

---

## Additional Resources

### Stability Explained
**Stable sort**: Maintains relative order of equal elements
- Bubble Sort: ✓ Stable
- Selection Sort: ✗ Not stable
- Insertion Sort: ✓ Stable

### Example of Stability
```
Input: [(3,a), (1,b), (3,c), (2,d)]
         (value, identifier)

Stable sort: [1b, 2d, 3a, 3c]  // 3a still before 3c
Unstable: [1b, 2d, 3c, 3a]     // Order of 3's changed
```
