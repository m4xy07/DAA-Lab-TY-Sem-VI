#include <iostream>
#include <climits>
#include <cstring>
using namespace std;

#define N 10

int n;
int cost[N][N];
int final_path[N + 1];
bool visited[N];
int final_cost = INT_MAX;

void copyToFinal(int curr_path[])
{
    for (int i = 0; i < n; i++)
        final_path[i] = curr_path[i];
    final_path[n] = curr_path[0];
}

int firstMin(int i)
{
    int min = INT_MAX;
    for (int k = 0; k < n; k++)
        if (cost[i][k] < min && i != k)
            min = cost[i][k];
    return min;
}

int secondMin(int i)
{
    int first = INT_MAX, second = INT_MAX;
    for (int j = 0; j < n; j++)
    {
        if (i == j)
            continue;

        if (cost[i][j] <= first)
        {
            second = first;
            first = cost[i][j];
        }
        else if (cost[i][j] <= second && cost[i][j] != first)
        {
            second = cost[i][j];
        }
    }
    return second;
}

void TSPRec(int curr_bound, int curr_weight, int level, int curr_path[])
{
    if (level == n)
    {
        // Check if there is an edge from last vertex to first vertex
        if (cost[curr_path[level - 1]][curr_path[0]] != 0)
        {
            int curr_res = curr_weight + cost[curr_path[level - 1]][curr_path[0]];

            if (curr_res < final_cost)
            {
                copyToFinal(curr_path);
                final_cost = curr_res;
            }
        }
        return;
    }

    for (int i = 0; i < n; i++)
    {
        if (cost[curr_path[level - 1]][i] != 0 && !visited[i])
        {
            int temp = curr_bound;
            curr_weight += cost[curr_path[level - 1]][i];

            if (level == 1)
                curr_bound -= ((firstMin(curr_path[level - 1]) + firstMin(i)) / 2);
            else
                curr_bound -= ((secondMin(curr_path[level - 1]) + firstMin(i)) / 2);

            if (curr_bound + curr_weight < final_cost)
            {
                curr_path[level] = i;
                visited[i] = true;

                TSPRec(curr_bound, curr_weight, level + 1, curr_path);
            }

            curr_weight -= cost[curr_path[level - 1]][i];
            curr_bound = temp;

            memset(visited, false, sizeof(visited));
            for (int j = 0; j <= level - 1; j++)
                visited[curr_path[j]] = true;
        }
    }
}

void TSP()
{
    int curr_path[N + 1];
    int curr_bound = 0;
    memset(curr_path, -1, sizeof(curr_path));
    memset(visited, false, sizeof(visited));

    for (int i = 0; i < n; i++)
        curr_bound += (firstMin(i) + secondMin(i));

    curr_bound = (curr_bound == 1) ? curr_bound / 2 + 1 : curr_bound / 2;

    visited[0] = true;
    curr_path[0] = 0;

    TSPRec(curr_bound, 0, 1, curr_path);
}

int main()
{
    cout << "Enter number of cities: ";
    cin >> n;

    cout << "Enter cost matrix (use 0 for no direct path):\n";
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cout << "Cost[" << i << "][" << j << "]: ";
            cin >> cost[i][j];
        }
    }

    TSP();

    cout << "\nMinimum cost: " << final_cost << endl;
    cout << "Path taken: ";
    for (int i = 0; i <= n; i++)
    {
        cout << final_path[i];
        if (i < n)
            cout << " -> ";
    }
    cout << endl;

    return 0;
}
