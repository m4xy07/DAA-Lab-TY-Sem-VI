# Binary Search Algorithm (Divide and Conquer)
# Time Complexity: O(log n)
# Space Complexity: O(1)

import time

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


def main():
    print("=== Binary Search (Divide and Conquer) ===\n")
    
    # Input
    n = int(input("Enter number of elements: "))
    arr = []
    print("Enter elements in sorted order:")
    for i in range(n):
        arr.append(int(input(f"Element {i + 1}: ")))
    
    target = int(input("\nEnter element to search: "))
    
    print(f"\nArray: {arr}")
    print(f"Searching for: {target}")
    
    # Iterative Binary Search
    print("\n--- Iterative Binary Search ---")
    start = time.perf_counter()
    index, comparisons = binary_search(arr, target)
    end = time.perf_counter()
    
    if index != -1:
        print(f"Element found at index: {index}")
    else:
        print("Element not found")
    
    print(f"Comparisons: {comparisons}")
    print(f"Time taken: {(end - start) * 1000000:.2f} microseconds")
    
    # Recursive Binary Search
    print("\n--- Recursive Binary Search ---")
    start = time.perf_counter()
    index, comparisons = binary_search_recursive(arr, target, 0, len(arr) - 1)
    end = time.perf_counter()
    
    if index != -1:
        print(f"Element found at index: {index}")
    else:
        print("Element not found")
    
    print(f"Comparisons: {comparisons}")
    print(f"Time taken: {(end - start) * 1000000:.2f} microseconds")
    
    print(f"\nTime Complexity: O(log n) = O(log {n})")


if __name__ == "__main__":
    main()
