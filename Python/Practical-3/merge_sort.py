# Merge Sort Algorithm (Divide and Conquer)
# Time Complexity: O(n log n)
# Space Complexity: O(n)

import time

def merge(arr, left, mid, right):
    """Merge two sorted subarrays"""
    # Create temporary arrays
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


def main():
    print("=== Merge Sort (Divide and Conquer) ===\n")
    
    # Input
    n = int(input("Enter number of elements: "))
    arr = []
    print("Enter elements:")
    for i in range(n):
        arr.append(int(input(f"Element {i + 1}: ")))
    
    print(f"\nOriginal array: {arr}")
    
    # Sort
    start = time.perf_counter()
    comparisons = merge_sort(arr, 0, len(arr) - 1)
    end = time.perf_counter()
    
    print(f"Sorted array: {arr}")
    print(f"\nTotal comparisons: {comparisons}")
    print(f"Time taken: {(end - start) * 1000000:.2f} microseconds")
    print(f"Time Complexity: O(n log n) = O({n} log {n})")


if __name__ == "__main__":
    main()
