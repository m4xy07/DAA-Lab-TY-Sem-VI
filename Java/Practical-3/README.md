# Practical 3: Advanced Sorting Techniques - Java

## Overview
This practical implements three efficient sorting algorithms in Java: Merge Sort, Heap Sort, and Quick Sort. All have better average-case time complexity (O(n log n)) compared to basic sorting algorithms.

---

## 1. Merge Sort (`MergeSort.java`)

### Algorithm Explanation
Merge Sort is a divide-and-conquer algorithm that divides the array into two halves, recursively sorts them, and then merges the sorted halves.

### How It Works
1. **Divide**: Split the array into two halves
2. **Conquer**: Recursively sort both halves
3. **Combine**: Merge the two sorted halves into a single sorted array

### Java Implementation
```java
public static void mergeSort(int[] arr, int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        mergeSort(arr, left, mid);      // Sort left half
        mergeSort(arr, mid + 1, right); // Sort right half
        merge(arr, left, mid, right);   // Merge both halves
    }
}
```

### Merge Function
```java
public static void merge(int[] arr, int left, int mid, int right) {
    // Create temporary arrays
    int[] L = new int[n1];
    int[] R = new int[n2];
    
    // Copy data to temp arrays
    // Merge back to original array
}
```

### Time Complexity
- **Best Case**: O(n log n)
- **Average Case**: O(n log n)
- **Worst Case**: O(n log n)

### Space Complexity
O(n) - Requires additional space for temporary arrays

### Example
```
Input: [38, 27, 43, 3, 9, 82, 10]

Divide Phase:
[38, 27, 43, 3, 9, 82, 10]
    ↓
[38, 27, 43, 3] | [9, 82, 10]
    ↓                  ↓
[38, 27] [43, 3]   [9, 82] [10]
    ↓      ↓           ↓      ↓
[38] [27] [43] [3]  [9] [82] [10]

Merge Phase:
[27, 38] [3, 43]   [9, 82] [10]
    ↓                  ↓
[3, 27, 38, 43]    [9, 10, 82]
    ↓___________________↓
[3, 9, 10, 27, 38, 43, 82]
```

---

## 2. Heap Sort (`HeapSort.java`)

### Algorithm Explanation
Heap Sort builds a max heap from the array and repeatedly extracts the maximum element, placing it at the end of the sorted portion.

### How It Works
1. **Build Max Heap**: Convert array into a max heap
2. **Extract Max**: Swap root (max) with last element
3. **Heapify**: Restore heap property for remaining elements
4. **Repeat**: Until heap size becomes 1

### Java Implementation
```java
public static void heapSort(int[] arr) {
    int n = arr.length;
    
    // Build max heap
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);
    
    // Extract elements one by one
    for (int i = n - 1; i > 0; i--) {
        // Swap root with last element
        int temp = arr[0];
        arr[0] = arr[i];
        arr[i] = temp;
        
        // Heapify reduced heap
        heapify(arr, i, 0);
    }
}
```

### Heapify Function
```java
public static void heapify(int[] arr, int n, int i) {
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;
    
    // Find largest among root, left, right
    if (left < n && arr[left] > arr[largest])
        largest = left;
    if (right < n && arr[right] > arr[largest])
        largest = right;
    
    // Recursively heapify if needed
    if (largest != i) {
        int temp = arr[i];
        arr[i] = arr[largest];
        arr[largest] = temp;
        heapify(arr, n, largest);
    }
}
```

### Time Complexity
- **Best Case**: O(n log n)
- **Average Case**: O(n log n)
- **Worst Case**: O(n log n)

### Space Complexity
O(1) - In-place sorting

### Example
```
Input: [4, 10, 3, 5, 1]

Step 1: Build Max Heap
[4, 10, 3, 5, 1] → [10, 5, 3, 4, 1]

Step 2: Extract Max and Heapify
[10, 5, 3, 4, 1] → [1, 5, 3, 4 | 10]
Heapify: [5, 4, 3, 1 | 10]

Final: [1, 3, 4, 5, 10]
```

---

## 3. Quick Sort (`QuickSort.java`)

### Algorithm Explanation
Quick Sort is a divide-and-conquer algorithm that selects a pivot element and partitions the array around it, then recursively sorts the subarrays.

### How It Works
1. **Choose Pivot**: Select an element as pivot (last element)
2. **Partition**: Rearrange so elements < pivot are on left, > pivot on right
3. **Recursively Sort**: Apply quick sort to left and right subarrays

### Java Implementation
```java
public static void quickSort(int[] arr, int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);  // Sort left
        quickSort(arr, pi + 1, high); // Sort right
    }
}
```

### Partition Function
```java
public static int partition(int[] arr, int low, int high) {
    int pivot = arr[high];
    int i = low - 1;
    
    for (int j = low; j < high; j++) {
        if (arr[j] < pivot) {
            i++;
            // Swap arr[i] and arr[j]
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }
    
    // Swap arr[i+1] and arr[high] (pivot)
    int temp = arr[i + 1];
    arr[i + 1] = arr[high];
    arr[high] = temp;
    
    return i + 1;
}
```

### Time Complexity
- **Best Case**: O(n log n)
- **Average Case**: O(n log n)
- **Worst Case**: O(n²) - when array is already sorted

### Space Complexity
O(log n) - Recursion stack

### Example
```
Input: [10, 7, 8, 9, 1, 5]
Pivot: 5

Step 1: Partition
[1, 5, 8, 9, 10, 7]
     ↑ pivot at index 1

Step 2: Recursively sort [1] and [8, 9, 10, 7]
Final: [1, 5, 7, 8, 9, 10]
```

---

## Comparison Table

| Algorithm | Time (Best) | Time (Avg) | Time (Worst) | Space | Stable | In-Place |
|-----------|-------------|------------|--------------|-------|--------|----------|
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes | No |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | No | Yes |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | No | Yes |

---

## Java-Specific Implementation Details

### Array Swapping
```java
// Java doesn't have built-in swap for primitives
int temp = arr[i];
arr[i] = arr[j];
arr[j] = temp;
```

### Array Copying
```java
// For Merge Sort
int[] L = new int[n1];
for (int i = 0; i < n1; i++)
    L[i] = arr[left + i];
```

### Method Calls
```java
// Recursive calls
mergeSort(arr, left, mid);
mergeSort(arr, mid + 1, right);
```

---

## How to Compile and Run

```bash
# Compile
javac MergeSort.java
javac HeapSort.java
javac QuickSort.java

# Run
java MergeSort
java HeapSort
java QuickSort
```

### Sample Input
```
Enter number of elements: 8
Enter elements: 64 34 25 12 22 11 90 88
```

### Sample Output
```
Original array: 64 34 25 12 22 11 90 88
Sorted array: 11 12 22 25 34 64 88 90
```

---

## When to Use Each Algorithm

### Merge Sort
- When stability is required
- For linked lists
- When worst-case O(n log n) is critical
- External sorting (large datasets)

### Heap Sort
- When space is limited
- When consistent O(n log n) is needed
- Priority queue implementation
- When no worst-case degradation acceptable

### Quick Sort
- General-purpose sorting (fastest in practice)
- When average-case performance matters most
- Internal sorting of arrays
- When memory writes are not costly

---

## Common Mistakes to Avoid

### 1. Merge Sort - Array Bounds
```java
// ✗ Wrong
int n1 = mid - left;  // Should add 1
int n2 = right - mid;

// ✓ Correct
int n1 = mid - left + 1;
int n2 = right - mid;
```

### 2. Heap Sort - Parent-Child Relation
```java
// Parent of node i
int parent = (i - 1) / 2;

// Children of node i
int left = 2 * i + 1;
int right = 2 * i + 2;
```

### 3. Quick Sort - Pivot Choice
```java
// Last element as pivot (current implementation)
int pivot = arr[high];

// Alternatives:
// - First element: arr[low]
// - Middle element: arr[(low + high) / 2]
// - Random: arr[low + rand.nextInt(high - low + 1)]
```

---

## Performance Analysis

### For 10,000 Elements

| Algorithm | Comparisons (approx) | Extra Space |
|-----------|----------------------|-------------|
| Merge Sort | ~120,000 | 10,000 |
| Heap Sort | ~150,000 | 1 |
| Quick Sort | ~100,000 (avg) | ~15 |

---

## Key Takeaways

1. **All three** are more efficient than O(n²) algorithms
2. **Merge Sort**: Guaranteed O(n log n), needs extra space
3. **Heap Sort**: In-place with O(n log n) guarantee
4. **Quick Sort**: Fastest average case, but O(n²) worst case
5. **Divide and Conquer**: Common theme in all three
6. **Java Arrays**: Use `Arrays.sort()` for built-in sorting (uses Dual-Pivot Quicksort)

---

## Java Built-in Sorting

```java
import java.util.Arrays;

int[] arr = {64, 34, 25, 12, 22, 11, 90, 88};

// Uses Dual-Pivot Quicksort (primitive types)
Arrays.sort(arr);

// Uses TimSort (Object types) - stable
Integer[] arrObj = {64, 34, 25, 12, 22, 11, 90, 88};
Arrays.sort(arrObj);
```

---

## Next Steps

After mastering these sorting algorithms:
- **Practical 4**: Greedy algorithms (Knapsack, Job Sequencing)
- **Understand trade-offs**: Space vs Time, Stable vs Unstable
- **Practice**: Solve problems on LeetCode/HackerRank
