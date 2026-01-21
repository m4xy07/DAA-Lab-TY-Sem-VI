# Quick Sort Algorithm (Divide and Conquer)
# Time Complexity: O(n log n) average, O(n^2) worst
# Space Complexity: O(log n)

import time

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


def main():
    print("=== Quick Sort (Divide and Conquer) ===\n")
    
    # Input
    n = int(input("Enter number of elements: "))
    arr = []
    print("Enter elements:")
    for i in range(n):
        arr.append(int(input(f"Element {i + 1}: ")))
    
    print(f"\nOriginal array: {arr}")
    
    # Sort
    start = time.perf_counter()
    comparisons, swaps = quick_sort(arr, 0, len(arr) - 1)
    end = time.perf_counter()
    
    print(f"Sorted array: {arr}")
    print(f"\nTotal comparisons: {comparisons}")
    print(f"Total swaps: {swaps}")
    print(f"Time taken: {(end - start) * 1000000:.2f} microseconds")
    print(f"Time Complexity: O(n log n) = O({n} log {n})")


if __name__ == "__main__":
    main()
