# Practical 3: Advanced Sorting Techniques

## Overview
This practical implements three efficient sorting algorithms: Merge Sort, Heap Sort, and Quick Sort. All have better average-case time complexity (O(n log n)) compared to basic sorting algorithms.

---

## 1. Merge Sort (`merge_sort.cpp`)

### Algorithm Explanation
Merge Sort is a divide-and-conquer algorithm that divides the array into two halves, recursively sorts them, and then merges the sorted halves.

### How It Works
1. **Divide**: Split the array into two halves
2. **Conquer**: Recursively sort both halves
3. **Combine**: Merge the two sorted halves into a single sorted array

### Detailed Steps
```
mergeSort(arr, left, right):
    if left < right:
        mid = (left + right) / 2
        mergeSort(arr, left, mid)      // Sort left half
        mergeSort(arr, mid+1, right)   // Sort right half
        merge(arr, left, mid, right)   // Merge both halves
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

### Characteristics
- **Stable**: Maintains relative order of equal elements
- **Not In-Place**: Requires extra space
- **Predictable**: Always O(n log n) performance

---

## 2. Heap Sort (`heap_sort.cpp`)

### Algorithm Explanation
Heap Sort builds a max heap from the array and repeatedly extracts the maximum element, placing it at the end of the sorted portion.

### How It Works
1. **Build Max Heap**: Convert array into a max heap
2. **Extract Max**: Swap root (max) with last element
3. **Heapify**: Restore heap property for remaining elements
4. **Repeat**: Until heap size becomes 1

### Heapify Process
```
heapify(arr, n, i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2
    
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        swap(arr[i], arr[largest])
        heapify(arr, n, largest)
```

### Time Complexity
- **Best Case**: O(n log n)
- **Average Case**: O(n log n)
- **Worst Case**: O(n log n)

### Space Complexity
O(1) - In-place sorting (excluding recursion stack)

### Example
```
Input: [4, 10, 3, 5, 1]

Step 1: Build Max Heap
[4, 10, 3, 5, 1] → [10, 5, 3, 4, 1]

Step 2: Extract Max and Heapify
[10, 5, 3, 4, 1] → [1, 5, 3, 4 | 10]
Heapify: [5, 4, 3, 1 | 10]

Step 3: Continue
[5, 4, 3, 1 | 10] → [1, 4, 3 | 5, 10]
Heapify: [4, 1, 3 | 5, 10]

Step 4: Continue
[4, 1, 3 | 5, 10] → [3, 1 | 4, 5, 10]
Heapify: [3, 1 | 4, 5, 10]

Step 5: Continue
[3, 1 | 4, 5, 10] → [1 | 3, 4, 5, 10]

Final: [1, 3, 4, 5, 10]
```

### Characteristics
- **Not Stable**: May change relative order of equal elements
- **In-Place**: Minimal extra space required
- **No Worst Case Degradation**: Always O(n log n)

---

## 3. Quick Sort (`quick_sort.cpp`)

### Algorithm Explanation
Quick Sort is a divide-and-conquer algorithm that selects a pivot element and partitions the array around it, then recursively sorts the subarrays.

### How It Works
1. **Choose Pivot**: Select an element as pivot (last element in this implementation)
2. **Partition**: Rearrange array so elements < pivot are on left, elements > pivot are on right
3. **Recursively Sort**: Apply quick sort to left and right subarrays

### Partition Process
```
partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    
    for j = low to high-1:
        if arr[j] < pivot:
            i++
            swap(arr[i], arr[j])
    
    swap(arr[i+1], arr[high])
    return i+1
```

### Time Complexity
- **Best Case**: O(n log n) - when pivot divides array evenly
- **Average Case**: O(n log n)
- **Worst Case**: O(n²) - when array is already sorted (pivot is always min/max)

### Space Complexity
- O(log n) - Recursion stack for average case
- O(n) - Worst case recursion depth

### Example
```
Input: [10, 7, 8, 9, 1, 5]
Pivot: 5 (last element)

Step 1: Partition around 5
[1, 5, 8, 9, 10, 7]
     ↑ (pivot at index 1)

Step 2: Sort left [1]
Already sorted

Step 3: Sort right [8, 9, 10, 7]
Pivot: 7
[7, 9, 10, 8]
 ↑

Step 4: Sort left []
Empty

Step 5: Sort right [9, 10, 8]
Pivot: 8
[8, 10, 9]
 ↑

Continue until fully sorted:
[1, 5, 7, 8, 9, 10]
```

### Characteristics
- **Not Stable**: May change relative order of equal elements
- **In-Place**: Requires minimal extra space
- **Cache Efficient**: Good locality of reference
- **Fastest in Practice**: Despite O(n²) worst case

---

## Comparison of All Three Algorithms

| Algorithm | Time (Best) | Time (Avg) | Time (Worst) | Space | Stable | In-Place |
|-----------|-------------|------------|--------------|-------|--------|----------|
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes | No |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | No | Yes |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | No | Yes |

### When to Use Each
- **Merge Sort**: 
  - When stability is required
  - For linked lists
  - When worst-case O(n log n) is critical
  
- **Heap Sort**: 
  - When space is limited
  - When consistent O(n log n) is needed
  - For priority queue implementation
  
- **Quick Sort**: 
  - General-purpose sorting (fastest in practice)
  - When average-case performance matters most
  - Internal sorting of arrays

---

## Performance Comparison Example

For array of 10,000 elements:

| Algorithm | Comparisons (approx) | Extra Space |
|-----------|----------------------|-------------|
| Merge Sort | ~120,000 | 10,000 |
| Heap Sort | ~150,000 | 1 |
| Quick Sort | ~100,000 (avg) | ~15 |

---

## How to Compile and Run

```bash
# Compile
g++ merge_sort.cpp -o merge_sort
g++ heap_sort.cpp -o heap_sort
g++ quick_sort.cpp -o quick_sort

# Run
./merge_sort
./heap_sort
./quick_sort
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

## Key Takeaways
1. All three algorithms are more efficient than O(n²) sorting algorithms
2. Merge Sort guarantees O(n log n) but needs extra space
3. Heap Sort is in-place with O(n log n) guarantee
4. Quick Sort is fastest in practice but has O(n²) worst case
5. Choice depends on: stability requirements, space constraints, and data characteristics
