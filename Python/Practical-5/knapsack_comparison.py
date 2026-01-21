# Knapsack Comparison: Greedy vs Dynamic Programming
# Demonstrates that Greedy doesn't always give optimal solution for 0/1 Knapsack

class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight


def fractional_knapsack_greedy(items, capacity):
    """Greedy approach for Fractional Knapsack (OPTIMAL for fractional)"""
    items_copy = items.copy()
    items_copy.sort(key=lambda x: x.ratio, reverse=True)
    
    max_value = 0
    for item in items_copy:
        if capacity >= item.weight:
            capacity -= item.weight
            max_value += item.value
        else:
            max_value += item.value * (capacity / item.weight)
            break
    
    return max_value


def knapsack_01_greedy(items, capacity):
    """Greedy approach for 0/1 Knapsack (NOT ALWAYS OPTIMAL)"""
    items_copy = items.copy()
    items_copy.sort(key=lambda x: x.ratio, reverse=True)
    
    max_value = 0
    selected = []
    
    for item in items_copy:
        if capacity >= item.weight:
            capacity -= item.weight
            max_value += item.value
            selected.append(item)
    
    return max_value, selected


def knapsack_01_dp(items, capacity):
    """Dynamic Programming approach for 0/1 Knapsack (OPTIMAL)"""
    n = len(items)
    
    # Create DP table
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # Build table bottom-up
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if items[i - 1].weight <= w:
                # Max of including or excluding current item
                dp[i][w] = max(
                    items[i - 1].value + dp[i - 1][w - items[i - 1].weight],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]
    
    # Backtrack to find selected items
    selected = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.append(items[i - 1])
            w -= items[i - 1].weight
    
    return dp[n][capacity], selected, dp


def print_dp_table(dp, items, capacity):
    """Print DP table for visualization"""
    print("\nDP Table:")
    print("     ", end="")
    for w in range(capacity + 1):
        print(f"{w:4}", end="")
    print()
    
    for i in range(len(dp)):
        if i == 0:
            print("  0: ", end="")
        else:
            print(f"I{i}: ", end="")
        for w in range(capacity + 1):
            print(f"{dp[i][w]:4}", end="")
        print()


def main():
    print("="*60)
    print("KNAPSACK COMPARISON: Greedy vs Dynamic Programming")
    print("="*60)
    
    # Input
    n = int(input("\nEnter number of items: "))
    items = []
    
    print("\nEnter items (value weight):")
    for i in range(n):
        value = int(input(f"Item {i + 1} - Value: "))
        weight = int(input(f"Item {i + 1} - Weight: "))
        items.append(Item(value, weight))
    
    capacity = int(input("\nEnter knapsack capacity: "))
    
    print("\n" + "="*60)
    print("ITEMS:")
    print("="*60)
    for i, item in enumerate(items):
        print(f"Item {i + 1}: Value={item.value}, Weight={item.weight}, Ratio={item.ratio:.2f}")
    
    # Fractional Knapsack (Greedy works optimally)
    print("\n" + "="*60)
    print("1. FRACTIONAL KNAPSACK (Greedy - OPTIMAL)")
    print("="*60)
    frac_value = fractional_knapsack_greedy(items, capacity)
    print(f"Maximum value (fractional allowed): {frac_value:.2f}")
    print("Note: Greedy approach is OPTIMAL for fractional knapsack")
    
    # 0/1 Knapsack with Greedy (NOT always optimal)
    print("\n" + "="*60)
    print("2. 0/1 KNAPSACK - GREEDY APPROACH (NOT ALWAYS OPTIMAL)")
    print("="*60)
    greedy_value, greedy_items = knapsack_01_greedy(items, capacity)
    print(f"Maximum value (greedy): {greedy_value}")
    print("Selected items (greedy):")
    for item in greedy_items:
        print(f"  Value={item.value}, Weight={item.weight}")
    
    # 0/1 Knapsack with DP (OPTIMAL)
    print("\n" + "="*60)
    print("3. 0/1 KNAPSACK - DYNAMIC PROGRAMMING (OPTIMAL)")
    print("="*60)
    dp_value, dp_items, dp_table = knapsack_01_dp(items, capacity)
    print(f"Maximum value (DP): {dp_value}")
    print("Selected items (DP):")
    for item in dp_items:
        print(f"  Value={item.value}, Weight={item.weight}")
    
    print_dp_table(dp_table, items, capacity)
    
    # Comparison
    print("\n" + "="*60)
    print("COMPARISON RESULTS:")
    print("="*60)
    print(f"Fractional Knapsack (Greedy): {frac_value:.2f}")
    print(f"0/1 Knapsack (Greedy):        {greedy_value}")
    print(f"0/1 Knapsack (DP):            {dp_value}")
    
    if greedy_value < dp_value:
        print("\n⚠ GREEDY FAILED! Greedy gave suboptimal solution for 0/1 Knapsack")
        print(f"Difference: {dp_value - greedy_value}")
    else:
        print("\n✓ In this case, Greedy happened to give optimal solution")
        print("  But this is NOT guaranteed for all inputs!")
    
    print("\n" + "="*60)
    print("KEY TAKEAWAY:")
    print("="*60)
    print("• Greedy works OPTIMALLY for FRACTIONAL Knapsack")
    print("• Greedy does NOT guarantee optimal solution for 0/1 Knapsack")
    print("• Dynamic Programming is needed for 0/1 Knapsack")
    print("="*60)


# Counter-example demonstration
def show_counter_example():
    """Show a classic counter-example where Greedy fails"""
    print("\n" + "="*60)
    print("CLASSIC COUNTER-EXAMPLE:")
    print("="*60)
    
    # Items where greedy fails
    items = [
        Item(60, 10),  # Ratio: 6
        Item(100, 20), # Ratio: 5
        Item(120, 30)  # Ratio: 4
    ]
    capacity = 50
    
    print("Items:")
    for i, item in enumerate(items):
        print(f"  Item {i + 1}: Value={item.value}, Weight={item.weight}, Ratio={item.ratio:.2f}")
    print(f"Capacity: {capacity}")
    
    greedy_value, _ = knapsack_01_greedy(items, capacity)
    dp_value, _, _ = knapsack_01_dp(items, capacity)
    
    print(f"\nGreedy Result: {greedy_value}")
    print(f"  (Selects Item 1 + Item 2 based on ratio)")
    print(f"\nDP Result: {dp_value}")
    print(f"  (Selects Item 2 + Item 3 for maximum value)")
    print(f"\nDifference: {dp_value - greedy_value}")


if __name__ == "__main__":
    choice = input("Run with your own input (1) or see counter-example (2)? ")
    
    if choice == "2":
        show_counter_example()
    else:
        main()
