# Practical 2: Binary Search (Divide and Conquer) - Java

## Overview
This practical implements Binary Search using the Divide and Conquer approach with recursion in Java. Binary Search is an efficient algorithm for finding an element in a sorted array.

---

## Binary Search (`BinarySearch.java`)

### Problem Statement
Given a sorted array and a target element, find the index of the target element. If not found, return -1.

---

## Algorithm Explanation

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

### Java Implementation
```java
public static int binarySearch(int[] arr, int low, int high, int key) {
    if (low <= high) {
        int mid = low + (high - low) / 2;  // Prevents overflow
        
        if (arr[mid] == key) {
            return mid;
        }
        
        if (arr[mid] > key) {
            return binarySearch(arr, low, mid - 1, key);  // Search left
        }
        
        return binarySearch(arr, mid + 1, high, key);    // Search right
    }
    
    return -1;  // Element not found
}
```

---

## Time Complexity

### Analysis
- Each recursive call reduces search space by half
- **Best Case**: O(1) - element at middle
- **Average Case**: O(log n)
- **Worst Case**: O(log n) - element at end or not present

### Recurrence Relation
```
T(n) = T(n/2) + O(1)
```
Using Master's Theorem: T(n) = O(log n)

---

## Space Complexity

- **Recursive Implementation**: O(log n) - due to recursion stack
- **Iterative Implementation**: O(1)

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

## Java-Specific Implementation Details

### Method Signature
```java
public static int binarySearch(int[] arr, int low, int high, int key)
```
- `static`: Can be called without creating object
- `int[]`: Java array syntax
- Returns int (-1 for not found)

### Array Indexing
```java
int mid = low + (high - low) / 2;  // 0-based indexing
```

### Recursion
```java
return binarySearch(arr, low, mid - 1, key);  // Tail recursion
```

### Main Method
```java
public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    // ... input handling ...
    int result = binarySearch(arr, 0, n - 1, key);
    sc.close();
}
```

---

## Why `low + (high - low) / 2`?

### Overflow Prevention
```java
// ✗ Can overflow for large arrays
int mid = (low + high) / 2;

// ✓ Safe from overflow
int mid = low + (high - low) / 2;
```

### Example
```
low = 2000000000
high = 2000000100

(low + high) / 2 = 4000000100 / 2  // Overflow in int!

low + (high - low) / 2 = 2000000000 + 50 = 2000000050 ✓
```

---

## Comparison with Linear Search

| Aspect | Linear Search | Binary Search |
|--------|---------------|---------------|
| Time Complexity | O(n) | O(log n) |
| Prerequisite | None | Sorted array |
| Data Structure | Any | Array required |
| Best for | Small/Unsorted | Large/Sorted |

### Performance Example
For array of 1,000,000 elements:
- **Linear Search**: Up to 1,000,000 comparisons
- **Binary Search**: Maximum 20 comparisons

```
log₂(1,000,000) ≈ 20
```

---

## Iterative vs Recursive Implementation

### Recursive (Current Implementation)
```java
public static int binarySearch(int[] arr, int low, int high, int key) {
    if (low <= high) {
        int mid = low + (high - low) / 2;
        if (arr[mid] == key) return mid;
        if (arr[mid] > key) return binarySearch(arr, low, mid - 1, key);
        return binarySearch(arr, mid + 1, high, key);
    }
    return -1;
}
```

### Iterative Alternative
```java
public static int binarySearchIterative(int[] arr, int key) {
    int low = 0, high = arr.length - 1;
    
    while (low <= high) {
        int mid = low + (high - low) / 2;
        
        if (arr[mid] == key) {
            return mid;
        } else if (arr[mid] > key) {
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }
    return -1;
}
```

### Comparison
| Aspect | Recursive | Iterative |
|--------|-----------|-----------|
| Space | O(log n) | O(1) |
| Readability | Cleaner | More lines |
| Performance | Slightly slower | Slightly faster |
| Stack | Uses call stack | No recursion |

---

## How to Compile and Run

```bash
# Compile
javac BinarySearch.java

# Run
java BinarySearch
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

## Common Mistakes to Avoid

### 1. Unsorted Array
```java
// ✗ Wrong - Binary search requires sorted array
int[] arr = {5, 2, 8, 1, 9};
binarySearch(arr, 0, 4, 8);  // May not work!

// ✓ Correct - Sort first
Arrays.sort(arr);
binarySearch(arr, 0, 4, 8);
```

### 2. Off-by-One Errors
```java
// ✗ Wrong
binarySearch(arr, 0, n, key);  // Should be n-1

// ✓ Correct
binarySearch(arr, 0, n - 1, key);
```

### 3. Incorrect Base Case
```java
// ✗ Wrong
if (low < high)  // Misses single element case

// ✓ Correct
if (low <= high)  // Includes single element
```

---

## Advantages and Disadvantages

### Advantages
1. **Very Efficient**: O(log n) time complexity
2. **Predictable**: Always takes log n comparisons
3. **Simple**: Easy to implement and understand
4. **No Extra Space**: O(1) for iterative version

### Disadvantages
1. **Requires Sorted Array**: Must sort first if unsorted
2. **Array Only**: Doesn't work on linked lists efficiently
3. **Static Data**: Not ideal for frequently changing data

---

## Applications of Binary Search

1. **Dictionary**: Word lookup
2. **Databases**: Index searching
3. **Libraries**: Book searching systems
4. **Games**: Finding optimal moves
5. **File Systems**: File searching

---

## Java Built-in Binary Search

Java provides built-in binary search in `Arrays` class:

```java
import java.util.Arrays;

int[] arr = {10, 20, 30, 40, 50};
int index = Arrays.binarySearch(arr, 30);  // Returns 2

// If not found, returns: -(insertion_point) - 1
int notFound = Arrays.binarySearch(arr, 25);  // Returns -2
```

---

## Extensions and Variations

### 1. First Occurrence
Find the first occurrence of a duplicate element:
```java
int firstOccurrence(int[] arr, int key) {
    int result = -1;
    int low = 0, high = arr.length - 1;
    
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (arr[mid] == key) {
            result = mid;
            high = mid - 1;  // Continue searching left
        } else if (arr[mid] > key) {
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }
    return result;
}
```

### 2. Last Occurrence
```java
int lastOccurrence(int[] arr, int key) {
    int result = -1;
    int low = 0, high = arr.length - 1;
    
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (arr[mid] == key) {
            result = mid;
            low = mid + 1;  // Continue searching right
        } else if (arr[mid] > key) {
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }
    return result;
}
```

### 3. Count Occurrences
```java
int countOccurrences(int[] arr, int key) {
    int first = firstOccurrence(arr, key);
    if (first == -1) return 0;
    int last = lastOccurrence(arr, key);
    return last - first + 1;
}
```

---

## Testing Scenarios

### Test Case 1: Single Element
```
Input: arr = [5], key = 5
Output: 0
```

### Test Case 2: Two Elements
```
Input: arr = [3, 7], key = 7
Output: 1
```

### Test Case 3: Element at Start
```
Input: arr = [1, 2, 3, 4, 5], key = 1
Output: 0
```

### Test Case 4: Element at End
```
Input: arr = [1, 2, 3, 4, 5], key = 5
Output: 4
```

### Test Case 5: Not Present
```
Input: arr = [1, 2, 3, 4, 5], key = 6
Output: -1
```

---

## Key Takeaways

1. **Divide and Conquer**: Classic example of the paradigm
2. **Efficiency**: O(log n) vs O(n) for linear search
3. **Prerequisite**: Array must be sorted
4. **Implementation**: Both recursive and iterative work
5. **Overflow Safety**: Use `low + (high - low) / 2`
6. **Java Arrays**: 0-indexed, length property available

---

## Next Steps

After mastering binary search, explore:
- **Practical 3**: Advanced Sorting (Merge Sort uses divide and conquer)
- **Binary Search on Answer**: Find optimal value in search space
- **Ternary Search**: For unimodal functions
