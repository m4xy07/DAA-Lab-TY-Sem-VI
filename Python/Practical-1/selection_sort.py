# Selection Sort Algorithm
# Time Complexity: O(n^2)
# Space Complexity: O(1)

def selection_sort(arr):
    """Sort array using Selection Sort algorithm"""
    n = len(arr)
    comparisons = 0
    swaps = 0
    
    for i in range(n):
        # Find minimum element in unsorted array
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap minimum element with first element
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1
    
    return comparisons, swaps


def main():
    print("=== Selection Sort ===\n")
    
    # Input
    n = int(input("Enter number of elements: "))
    arr = []
    print("Enter elements:")
    for i in range(n):
        arr.append(int(input(f"Element {i + 1}: ")))
    
    print(f"\nOriginal array: {arr}")
    
    # Sort
    comparisons, swaps = selection_sort(arr)
    
    print(f"Sorted array: {arr}")
    print(f"\nTotal comparisons: {comparisons}")
    print(f"Total swaps: {swaps}")
    print(f"Time Complexity: O(n^2) = O({n}^2)")


if __name__ == "__main__":
    main()
