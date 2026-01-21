# Bellman-Ford Algorithm using Dynamic Programming
# Time Complexity: O(V * E)
# Space Complexity: O(V)

import time

class Edge:
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight


def bellman_ford(edges, num_vertices, num_edges, source):
    """
    Find shortest paths from source to all vertices using Bellman-Ford
    Returns: (distances, has_negative_cycle)
    """
    # Initialize distances
    dist = [float('inf')] * num_vertices
    dist[source] = 0
    
    # Relax all edges V-1 times
    for i in range(num_vertices - 1):
        for edge in edges:
            if dist[edge.src] != float('inf') and \
               dist[edge.src] + edge.weight < dist[edge.dest]:
                dist[edge.dest] = dist[edge.src] + edge.weight
    
    # Check for negative-weight cycles
    has_negative_cycle = False
    for edge in edges:
        if dist[edge.src] != float('inf') and \
           dist[edge.src] + edge.weight < dist[edge.dest]:
            has_negative_cycle = True
            break
    
    return dist, has_negative_cycle


def main():
    print("="*60)
    print("BELLMAN-FORD ALGORITHM (Dynamic Programming)")
    print("="*60)
    
    # Input
    num_vertices = int(input("\nEnter number of vertices: "))
    num_edges = int(input("Enter number of edges: "))
    
    edges = []
    print(f"\nEnter {num_edges} edges (source destination weight):")
    for i in range(num_edges):
        src = int(input(f"Edge {i + 1} - Source: "))
        dest = int(input(f"Edge {i + 1} - Destination: "))
        weight = int(input(f"Edge {i + 1} - Weight: "))
        edges.append(Edge(src, dest, weight))
    
    source = int(input("\nEnter source vertex: "))
    
    # Run algorithm
    print("\n" + "="*60)
    print("RUNNING BELLMAN-FORD ALGORITHM...")
    print("="*60)
    
    start_time = time.perf_counter()
    dist, has_negative_cycle = bellman_ford(edges, num_vertices, num_edges, source)
    end_time = time.perf_counter()
    
    # Output
    if has_negative_cycle:
        print("\n⚠ Graph contains negative weight cycle!")
        print("Shortest paths are not defined.")
    else:
        print("\nShortest distances from source vertex", source)
        print("-" * 30)
        print(f"{'Vertex':<10} {'Distance':<10}")
        print("-" * 30)
        for i in range(num_vertices):
            if dist[i] == float('inf'):
                print(f"{i:<10} {'INF':<10}")
            else:
                print(f"{i:<10} {dist[i]:<10}")
    
    # Complexity analysis
    duration_us = (end_time - start_time) * 1_000_000
    print("\n" + "="*60)
    print("TIME COMPLEXITY ANALYSIS:")
    print("="*60)
    print(f"Vertices (V): {num_vertices}")
    print(f"Edges (E): {num_edges}")
    print(f"Time Complexity: O(V × E) = O({num_vertices} × {num_edges})")
    print(f"Execution Time: {duration_us:.2f} microseconds")
    print("="*60)


if __name__ == "__main__":
    main()
