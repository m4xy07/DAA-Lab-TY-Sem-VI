# Fractional Knapsack Problem using Greedy Algorithm
# Time Complexity: O(n log n)
# Space Complexity: O(n)

class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight
    
    def __repr__(self):
        return f"(V:{self.value}, W:{self.weight}, R:{self.ratio:.2f})"


def fractional_knapsack(items, capacity):
    """
    Solve fractional knapsack using greedy approach
    Returns: (max_value, selected_items)
    """
    # Sort items by value-to-weight ratio in descending order
    items.sort(key=lambda x: x.ratio, reverse=True)
    
    max_value = 0
    selected = []
    
    for item in items:
        if capacity >= item.weight:
            # Take entire item
            capacity -= item.weight
            max_value += item.value
            selected.append((item, 1.0))  # 1.0 = 100%
        else:
            # Take fraction of item
            fraction = capacity / item.weight
            max_value += item.value * fraction
            selected.append((item, fraction))
            break  # Knapsack is full
    
    return max_value, selected


def main():
    print("=== Fractional Knapsack Problem (Greedy) ===\n")
    
    # Input
    n = int(input("Enter number of items: "))
    items = []
    
    print("\nEnter items (value weight):")
    for i in range(n):
        value = int(input(f"Item {i + 1} - Value: "))
        weight = int(input(f"Item {i + 1} - Weight: "))
        items.append(Item(value, weight))
    
    capacity = int(input("\nEnter knapsack capacity: "))
    
    # Solve
    max_value, selected = fractional_knapsack(items, capacity)
    
    # Output
    print("\n" + "="*50)
    print("SOLUTION:")
    print("="*50)
    print("\nItems sorted by value/weight ratio:")
    for item in items:
        print(f"  Value: {item.value}, Weight: {item.weight}, Ratio: {item.ratio:.2f}")
    
    print("\nSelected items:")
    for item, fraction in selected:
        print(f"  Item (V:{item.value}, W:{item.weight}) - {fraction*100:.1f}% taken")
    
    print(f"\nMaximum value: {max_value:.2f}")
    print(f"Time Complexity: O(n log n) due to sorting")


if __name__ == "__main__":
    main()
