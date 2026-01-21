#include <iostream>
#include <climits>
#include <chrono>
using namespace std;
using namespace chrono;

struct Edge
{
    int src, dest, weight;
};

void bellmanFord(Edge edges[], int V, int E, int src)
{
    int dist[V];

    // Initialize distances
    for (int i = 0; i < V; i++)
        dist[i] = INT_MAX;
    dist[src] = 0;

    auto start = high_resolution_clock::now();

    // Relax all edges V-1 times
    for (int i = 1; i <= V - 1; i++)
    {
        for (int j = 0; j < E; j++)
        {
            int u = edges[j].src;
            int v = edges[j].dest;
            int weight = edges[j].weight;

            if (dist[u] != INT_MAX && dist[u] + weight < dist[v])
                dist[v] = dist[u] + weight;
        }
    }

    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<microseconds>(stop - start);

    // Check for negative-weight cycles
    bool hasNegativeCycle = false;
    for (int i = 0; i < E; i++)
    {
        int u = edges[i].src;
        int v = edges[i].dest;
        int weight = edges[i].weight;

        if (dist[u] != INT_MAX && dist[u] + weight < dist[v])
        {
            hasNegativeCycle = true;
            break;
        }
    }

    if (hasNegativeCycle)
    {
        cout << "Graph contains negative weight cycle" << endl;
    }
    else
    {
        cout << "\nShortest distances from source vertex " << src << ":\n";
        cout << "Vertex\t\tDistance" << endl;
        for (int i = 0; i < V; i++)
        {
            cout << i << "\t\t";
            if (dist[i] == INT_MAX)
                cout << "INF" << endl;
            else
                cout << dist[i] << endl;
        }
    }

    cout << "\nTime Complexity: O(V*E) = O(" << V << "*" << E << ")" << endl;
    cout << "Execution Time: " << duration.count() << " microseconds" << endl;
}

int main()
{
    int V, E;
    cout << "Enter number of vertices: ";
    cin >> V;
    cout << "Enter number of edges: ";
    cin >> E;

    Edge edges[E];
    cout << "Enter edges (source destination weight):\n";
    for (int i = 0; i < E; i++)
    {
        cout << "Edge " << i + 1 << " - Source: ";
        cin >> edges[i].src;
        cout << "Edge " << i + 1 << " - Destination: ";
        cin >> edges[i].dest;
        cout << "Edge " << i + 1 << " - Weight: ";
        cin >> edges[i].weight;
    }

    int src;
    cout << "Enter source vertex: ";
    cin >> src;

    bellmanFord(edges, V, E, src);

    return 0;
}
