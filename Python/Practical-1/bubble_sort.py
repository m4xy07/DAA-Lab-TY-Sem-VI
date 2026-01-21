# Bubble Sort Algorithm
# Time Complexity: O(n^2)
# Space Complexity: O(1)

def bubble_sort(arr):
    """Sort array using Bubble Sort algorithm"""
    n = len(arr)
    comparisons = 0
    swaps = 0
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                # Swap elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
                swapped = True
        
        # If no swaps, array is sorted
        if not swapped:
            break
    
    return comparisons, swaps


def main():
    print("=== Bubble Sort ===\n")
    
    # Input
    n = int(input("Enter number of elements: "))
    arr = []
    print("Enter elements:")
    for i in range(n):
        arr.append(int(input(f"Element {i + 1}: ")))
    
    print(f"\nOriginal array: {arr}")
    
    # Sort
    comparisons, swaps = bubble_sort(arr)
    
    print(f"Sorted array: {arr}")
    print(f"\nTotal comparisons: {comparisons}")
    print(f"Total swaps: {swaps}")
    print(f"Time Complexity: O(n^2) = O({n}^2)")


if __name__ == "__main__":
    main()
