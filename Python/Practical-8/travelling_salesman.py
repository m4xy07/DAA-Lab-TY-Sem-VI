# Travelling Salesman Problem using Branch and Bound (LC Strategy)
# Time Complexity: O(n^2 * 2^n) average
# Space Complexity: O(n^2)

import sys

final_path = []
visited = []
final_cost = sys.maxsize


def first_min(cost, i, n):
    """Find minimum edge cost from vertex i"""
    min_cost = sys.maxsize
    for k in range(n):
        if cost[i][k] < min_cost and i != k:
            min_cost = cost[i][k]
    return min_cost


def second_min(cost, i, n):
    """Find second minimum edge cost from vertex i"""
    first = sys.maxsize
    second = sys.maxsize
    
    for j in range(n):
        if i == j:
            continue
        
        if cost[i][j] <= first:
            second = first
            first = cost[i][j]
        elif cost[i][j] <= second and cost[i][j] != first:
            second = cost[i][j]
    
    return second


def tsp_recursive(cost, curr_bound, curr_weight, level, curr_path, n):
    """
    Solve TSP using Branch and Bound with LC strategy
    """
    global final_cost, final_path, visited
    
    # Base case: All cities visited
    if level == n:
        # Check if there's an edge from last city to first
        if cost[curr_path[level - 1]][curr_path[0]] != 0:
            curr_res = curr_weight + cost[curr_path[level - 1]][curr_path[0]]
            
            # Update final result if better solution found
            if curr_res < final_cost:
                final_path = curr_path.copy()
                final_path.append(curr_path[0])  # Return to start
                final_cost = curr_res
        return
    
    # Try all unvisited cities
    for i in range(n):
        if cost[curr_path[level - 1]][i] != 0 and not visited[i]:
            temp = curr_bound
            curr_weight += cost[curr_path[level - 1]][i]
            
            # Update bound
            if level == 1:
                curr_bound -= (
                    (first_min(cost, curr_path[level - 1], n) + 
                     first_min(cost, i, n)) / 2
                )
            else:
                curr_bound -= (
                    (second_min(cost, curr_path[level - 1], n) + 
                     first_min(cost, i, n)) / 2
                )
            
            # Branch only if bound + current weight is promising
            if curr_bound + curr_weight < final_cost:
                curr_path[level] = i
                visited[i] = True
                
                # Recurse to next level
                tsp_recursive(cost, curr_bound, curr_weight, level + 1, curr_path, n)
            
            # Backtrack
            curr_weight -= cost[curr_path[level - 1]][i]
            curr_bound = temp
            
            # Reset visited array
            visited = [False] * n
            for j in range(level):
                visited[curr_path[j]] = True


def solve_tsp(cost, n):
    """
    Main function to solve TSP
    """
    global final_cost, final_path, visited
    
    # Initialize
    curr_path = [-1] * (n + 1)
    visited = [False] * n
    
    # Calculate initial lower bound
    curr_bound = 0
    for i in range(n):
        curr_bound += first_min(cost, i, n) + second_min(cost, i, n)
    
    # Round up if odd
    curr_bound = (curr_bound // 2) if curr_bound % 2 == 0 else (curr_bound // 2) + 1
    
    # Start from vertex 0
    visited[0] = True
    curr_path[0] = 0
    
    # Solve recursively
    tsp_recursive(cost, curr_bound, 0, 1, curr_path, n)


def main():
    global final_cost, final_path
    
    print("="*60)
    print("TRAVELLING SALESMAN PROBLEM - Branch and Bound (LC)")
    print("="*60)
    
    # Input
    n = int(input("\nEnter number of cities: "))
    
    print("\nEnter cost matrix (use 0 for no direct path):")
    cost = []
    for i in range(n):
        row = []
        for j in range(n):
            value = int(input(f"Cost[{i}][{j}]: "))
            row.append(value)
        cost.append(row)
    
    # Display cost matrix
    print("\nCost Matrix:")
    print("    ", end="")
    for j in range(n):
        print(f"{j:4}", end="")
    print()
    for i in range(n):
        print(f"{i:2}: ", end="")
        for j in range(n):
            print(f"{cost[i][j]:4}", end="")
        print()
    
    # Solve TSP
    print("\n" + "="*60)
    print("SOLVING TSP...")
    print("="*60)
    
    final_cost = sys.maxsize
    final_path = []
    
    solve_tsp(cost, n)
    
    # Output
    print("\n" + "="*60)
    print("SOLUTION:")
    print("="*60)
    
    if final_cost == sys.maxsize:
        print("No solution found!")
    else:
        print(f"Minimum cost: {final_cost}")
        print("\nPath taken:")
        path_str = " -> ".join(map(str, final_path))
        print(path_str)
    
    print("\n" + "="*60)
    print("COMPLEXITY ANALYSIS:")
    print("="*60)
    print(f"Number of cities: {n}")
    print(f"Time Complexity: O(n^2 * 2^n)")
    print(f"Space Complexity: O(n^2)")
    print("="*60)


if __name__ == "__main__":
    main()
