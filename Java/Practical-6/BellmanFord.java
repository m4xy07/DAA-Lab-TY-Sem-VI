import java.util.Scanner;

class Edge {
    int src, dest, weight;

    Edge(int src, int dest, int weight) {
        this.src = src;
        this.dest = dest;
        this.weight = weight;
    }
}

public class BellmanFord {

    public static void bellmanFord(Edge[] edges, int V, int E, int src) {
        int[] dist = new int[V];

        // Initialize distances
        for (int i = 0; i < V; i++)
            dist[i] = Integer.MAX_VALUE;
        dist[src] = 0;

        long startTime = System.nanoTime();

        // Relax all edges V-1 times
        for (int i = 1; i <= V - 1; i++) {
            for (int j = 0; j < E; j++) {
                int u = edges[j].src;
                int v = edges[j].dest;
                int weight = edges[j].weight;

                if (dist[u] != Integer.MAX_VALUE && dist[u] + weight < dist[v])
                    dist[v] = dist[u] + weight;
            }
        }

        long endTime = System.nanoTime();
        long duration = (endTime - startTime) / 1000; // in microseconds

        // Check for negative-weight cycles
        boolean hasNegativeCycle = false;
        for (int i = 0; i < E; i++) {
            int u = edges[i].src;
            int v = edges[i].dest;
            int weight = edges[i].weight;

            if (dist[u] != Integer.MAX_VALUE && dist[u] + weight < dist[v]) {
                hasNegativeCycle = true;
                break;
            }
        }

        if (hasNegativeCycle) {
            System.out.println("Graph contains negative weight cycle");
        } else {
            System.out.println("\nShortest distances from source vertex " + src + ":");
            System.out.println("Vertex\t\tDistance");
            for (int i = 0; i < V; i++) {
                System.out.print(i + "\t\t");
                if (dist[i] == Integer.MAX_VALUE)
                    System.out.println("INF");
                else
                    System.out.println(dist[i]);
            }
        }

        System.out.println("\nTime Complexity: O(V*E) = O(" + V + "*" + E + ")");
        System.out.println("Execution Time: " + duration + " microseconds");
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of vertices: ");
        int V = sc.nextInt();
        System.out.print("Enter number of edges: ");
        int E = sc.nextInt();

        Edge[] edges = new Edge[E];
        System.out.println("Enter edges (source destination weight):");
        for (int i = 0; i < E; i++) {
            System.out.print("Edge " + (i + 1) + " - Source: ");
            int src = sc.nextInt();
            System.out.print("Edge " + (i + 1) + " - Destination: ");
            int dest = sc.nextInt();
            System.out.print("Edge " + (i + 1) + " - Weight: ");
            int weight = sc.nextInt();
            edges[i] = new Edge(src, dest, weight);
        }

        System.out.print("Enter source vertex: ");
        int src = sc.nextInt();

        bellmanFord(edges, V, E, src);

        sc.close();
    }
}
