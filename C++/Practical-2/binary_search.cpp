#include <iostream>
using namespace std;

// Recursive Binary Search using Divide and Conquer
int binarySearch(int arr[], int low, int high, int key)
{
    if (low <= high)
    {
        int mid = low + (high - low) / 2;

        // Element found at mid
        if (arr[mid] == key)
        {
            return mid;
        }

        // Search in left half
        if (arr[mid] > key)
        {
            return binarySearch(arr, low, mid - 1, key);
        }

        // Search in right half
        return binarySearch(arr, mid + 1, high, key);
    }

    // Element not found
    return -1;
}

int main()
{
    int n, key;
    cout << "Enter number of elements: ";
    cin >> n;

    int arr[n];
    cout << "Enter sorted elements: ";
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }

    cout << "Enter element to search: ";
    cin >> key;

    int result = binarySearch(arr, 0, n - 1, key);

    if (result != -1)
    {
        cout << "Element found at index: " << result << endl;
    }
    else
    {
        cout << "Element not found in array" << endl;
    }

    return 0;
}
