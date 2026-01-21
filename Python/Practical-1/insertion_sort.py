# Insertion Sort Algorithm
# Time Complexity: O(n^2)
# Space Complexity: O(1)

def insertion_sort(arr):
    """Sort array using Insertion Sort algorithm"""
    n = len(arr)
    comparisons = 0
    shifts = 0
    
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        # Move elements greater than key one position ahead
        while j >= 0 and arr[j] > key:
            comparisons += 1
            arr[j + 1] = arr[j]
            shifts += 1
            j -= 1
        
        if j >= 0:
            comparisons += 1
        
        arr[j + 1] = key
    
    return comparisons, shifts


def main():
    print("=== Insertion Sort ===\n")
    
    # Input
    n = int(input("Enter number of elements: "))
    arr = []
    print("Enter elements:")
    for i in range(n):
        arr.append(int(input(f"Element {i + 1}: ")))
    
    print(f"\nOriginal array: {arr}")
    
    # Sort
    comparisons, shifts = insertion_sort(arr)
    
    print(f"Sorted array: {arr}")
    print(f"\nTotal comparisons: {comparisons}")
    print(f"Total shifts: {shifts}")
    print(f"Time Complexity: O(n^2) = O({n}^2)")


if __name__ == "__main__":
    main()
