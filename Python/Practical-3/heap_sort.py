# Heap Sort Algorithm
# Time Complexity: O(n log n)
# Space Complexity: O(1)

import time

def heapify(arr, n, i):
    """Convert subtree rooted at i into a max heap"""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    comparisons = 0
    
    # Check if left child exists and is greater
    if left < n:
        comparisons += 1
        if arr[left] > arr[largest]:
            largest = left
    
    # Check if right child exists and is greater
    if right < n:
        comparisons += 1
        if arr[right] > arr[largest]:
            largest = right
    
    # Swap and heapify if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        comparisons += heapify(arr, n, largest)
    
    return comparisons


def heap_sort(arr):
    """Sort array using Heap Sort"""
    n = len(arr)
    comparisons = 0
    
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        comparisons += heapify(arr, n, i)
    
    # Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        # Move current root to end
        arr[0], arr[i] = arr[i], arr[0]
        
        # Heapify the reduced heap
        comparisons += heapify(arr, i, 0)
    
    return comparisons


def main():
    print("=== Heap Sort ===\n")
    
    # Input
    n = int(input("Enter number of elements: "))
    arr = []
    print("Enter elements:")
    for i in range(n):
        arr.append(int(input(f"Element {i + 1}: ")))
    
    print(f"\nOriginal array: {arr}")
    
    # Sort
    start = time.perf_counter()
    comparisons = heap_sort(arr)
    end = time.perf_counter()
    
    print(f"Sorted array: {arr}")
    print(f"\nTotal comparisons: {comparisons}")
    print(f"Time taken: {(end - start) * 1000000:.2f} microseconds")
    print(f"Time Complexity: O(n log n) = O({n} log {n})")


if __name__ == "__main__":
    main()
