#include <iostream>
using namespace std;

void printSolution(int board[], int n)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (board[i] == j)
                cout << "Q ";
            else
                cout << ". ";
        }
        cout << endl;
    }
    cout << endl;
}

bool isSafe(int board[], int row, int col)
{
    // Check if queen can be placed at board[row][col]
    for (int i = 0; i < row; i++)
    {
        // Check column and diagonals
        if (board[i] == col ||
            board[i] - i == col - row ||
            board[i] + i == col + row)
            return false;
    }
    return true;
}

bool solveNQueens(int board[], int row, int n, int &solutionCount)
{
    if (row == n)
    {
        // All queens are placed successfully
        solutionCount++;
        cout << "Solution " << solutionCount << ":\n";
        printSolution(board, n);
        return true;
    }

    bool foundSolution = false;

    // Try placing queen in all columns of current row
    for (int col = 0; col < n; col++)
    {
        if (isSafe(board, row, col))
        {
            board[row] = col;

            // Recur to place rest of the queens
            if (solveNQueens(board, row + 1, n, solutionCount))
                foundSolution = true;

            // Backtrack - remove queen from this position
            board[row] = -1;
        }
    }

    return foundSolution;
}

int main()
{
    int n;
    cout << "Enter number of queens (N): ";
    cin >> n;

    if (n < 4 && n != 1)
    {
        cout << "No solution exists for N = " << n << endl;
        return 0;
    }

    int board[n];
    for (int i = 0; i < n; i++)
        board[i] = -1;

    int solutionCount = 0;

    cout << "\nSolving " << n << "-Queens Problem using Backtracking...\n\n";

    if (!solveNQueens(board, 0, n, solutionCount))
    {
        cout << "No solution exists" << endl;
    }
    else
    {
        cout << "Total solutions found: " << solutionCount << endl;
    }

    return 0;
}
