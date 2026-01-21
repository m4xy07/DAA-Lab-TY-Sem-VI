#include <iostream>
#include <algorithm>
using namespace std;

struct Item
{
    int value;
    int weight;
    double ratio;
};

bool compare(Item a, Item b)
{
    return a.ratio > b.ratio;
}

// Fractional Knapsack using Greedy
double fractionalKnapsack(Item items[], int n, int capacity)
{
    Item temp[n];
    for (int i = 0; i < n; i++)
    {
        temp[i] = items[i];
    }

    sort(temp, temp + n, compare);

    double totalValue = 0.0;

    for (int i = 0; i < n; i++)
    {
        if (capacity >= temp[i].weight)
        {
            capacity -= temp[i].weight;
            totalValue += temp[i].value;
        }
        else
        {
            totalValue += temp[i].value * ((double)capacity / temp[i].weight);
            break;
        }
    }

    return totalValue;
}

// 0/1 Knapsack using Dynamic Programming
int knapsack01(Item items[], int n, int capacity)
{
    int dp[n + 1][capacity + 1];

    // Build table in bottom-up manner
    for (int i = 0; i <= n; i++)
    {
        for (int w = 0; w <= capacity; w++)
        {
            if (i == 0 || w == 0)
                dp[i][w] = 0;
            else if (items[i - 1].weight <= w)
                dp[i][w] = max(items[i - 1].value + dp[i - 1][w - items[i - 1].weight],
                               dp[i - 1][w]);
            else
                dp[i][w] = dp[i - 1][w];
        }
    }

    return dp[n][capacity];
}

int main()
{
    int n, capacity;
    cout << "Enter number of items: ";
    cin >> n;

    Item items[n];
    cout << "Enter value and weight for each item:\n";
    for (int i = 0; i < n; i++)
    {
        cout << "Item " << i + 1 << " - Value: ";
        cin >> items[i].value;
        cout << "Item " << i + 1 << " - Weight: ";
        cin >> items[i].weight;
        items[i].ratio = (double)items[i].value / items[i].weight;
    }

    cout << "Enter knapsack capacity: ";
    cin >> capacity;

    cout << "\n--- Fractional Knapsack (Greedy) ---" << endl;
    double greedyResult = fractionalKnapsack(items, n, capacity);
    cout << "Maximum value: " << greedyResult << endl;

    cout << "\n--- 0/1 Knapsack (Dynamic Programming) ---" << endl;
    int dpResult = knapsack01(items, n, capacity);
    cout << "Maximum value: " << dpResult << endl;

    cout << "\n--- Comparison ---" << endl;
    if (greedyResult > dpResult)
    {
        cout << "Greedy approach gives better result for fractional knapsack." << endl;
        cout << "However, for 0/1 knapsack, DP is optimal as items cannot be broken." << endl;
    }
    else if (dpResult > greedyResult)
    {
        cout << "Dynamic Programming gives optimal solution for 0/1 knapsack." << endl;
        cout << "Greedy strategy does not work for 0/1 knapsack." << endl;
    }
    else
    {
        cout << "Both approaches give same result in this case." << endl;
    }

    return 0;
}
