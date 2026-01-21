#include <iostream>
#include <algorithm>
using namespace std;

struct Job
{
    int id;
    int deadline;
    int profit;
};

bool compare(Job a, Job b)
{
    return a.profit > b.profit;
}

void jobSequencing(Job jobs[], int n)
{
    // Sort jobs by profit in descending order
    sort(jobs, jobs + n, compare);

    // Find maximum deadline
    int maxDeadline = 0;
    for (int i = 0; i < n; i++)
    {
        if (jobs[i].deadline > maxDeadline)
            maxDeadline = jobs[i].deadline;
    }

    // Create array to track time slots
    int slot[maxDeadline];
    bool filled[maxDeadline];

    for (int i = 0; i < maxDeadline; i++)
        filled[i] = false;

    int totalProfit = 0;
    int jobCount = 0;

    cout << "\nSelected Jobs:\n";

    // Assign jobs to slots
    for (int i = 0; i < n; i++)
    {
        // Find a free slot for this job (starting from last possible slot)
        for (int j = min(maxDeadline, jobs[i].deadline) - 1; j >= 0; j--)
        {
            if (!filled[j])
            {
                filled[j] = true;
                slot[j] = jobs[i].id;
                totalProfit += jobs[i].profit;
                jobCount++;
                cout << "Job " << jobs[i].id << " (Profit: " << jobs[i].profit
                     << ", Deadline: " << jobs[i].deadline << ")" << endl;
                break;
            }
        }
    }

    cout << "\nTotal Jobs: " << jobCount << endl;
    cout << "Total Profit: " << totalProfit << endl;
}

int main()
{
    int n;
    cout << "Enter number of jobs: ";
    cin >> n;

    Job jobs[n];
    cout << "Enter job details (ID, Deadline, Profit):\n";
    for (int i = 0; i < n; i++)
    {
        cout << "Job " << i + 1 << " - ID: ";
        cin >> jobs[i].id;
        cout << "Job " << i + 1 << " - Deadline: ";
        cin >> jobs[i].deadline;
        cout << "Job " << i + 1 << " - Profit: ";
        cin >> jobs[i].profit;
    }

    jobSequencing(jobs, n);

    return 0;
}
