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

double fractionalKnapsack(Item items[], int n, int capacity)
{
    // Sort items by value/weight ratio
    sort(items, items + n, compare);

    double totalValue = 0.0;

    for (int i = 0; i < n; i++)
    {
        if (capacity >= items[i].weight)
        {
            // Take whole item
            capacity -= items[i].weight;
            totalValue += items[i].value;
            cout << "Item " << i + 1 << ": Weight = " << items[i].weight
                 << ", Value = " << items[i].value << " (Full)" << endl;
        }
        else
        {
            // Take fraction of item
            double fraction = (double)capacity / items[i].weight;
            totalValue += items[i].value * fraction;
            cout << "Item " << i + 1 << ": Weight = " << capacity
                 << ", Value = " << items[i].value * fraction << " (Fraction = " << fraction << ")" << endl;
            break;
        }
    }

    return totalValue;
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

    cout << "\nItems selected:\n";
    double maxValue = fractionalKnapsack(items, n, capacity);

    cout << "\nMaximum value in knapsack: " << maxValue << endl;

    return 0;
}
