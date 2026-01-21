import java.util.Scanner;

public class NQueens {

    static int solutionCount = 0;

    public static void printSolution(int[] board, int n) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i] == j)
                    System.out.print("Q ");
                else
                    System.out.print(". ");
            }
            System.out.println();
        }
        System.out.println();
    }

    public static boolean isSafe(int[] board, int row, int col) {
        // Check if queen can be placed at board[row][col]
        for (int i = 0; i < row; i++) {
            // Check column and diagonals
            if (board[i] == col ||
                    board[i] - i == col - row ||
                    board[i] + i == col + row)
                return false;
        }
        return true;
    }

    public static boolean solveNQueens(int[] board, int row, int n) {
        if (row == n) {
            // All queens are placed successfully
            solutionCount++;
            System.out.println("Solution " + solutionCount + ":");
            printSolution(board, n);
            return true;
        }

        boolean foundSolution = false;

        // Try placing queen in all columns of current row
        for (int col = 0; col < n; col++) {
            if (isSafe(board, row, col)) {
                board[row] = col;

                // Recur to place rest of the queens
                if (solveNQueens(board, row + 1, n))
                    foundSolution = true;

                // Backtrack - remove queen from this position
                board[row] = -1;
            }
        }

        return foundSolution;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of queens (N): ");
        int n = sc.nextInt();

        if (n < 4 && n != 1) {
            System.out.println("No solution exists for N = " + n);
            sc.close();
            return;
        }

        int[] board = new int[n];
        for (int i = 0; i < n; i++)
            board[i] = -1;

        solutionCount = 0;

        System.out.println("\nSolving " + n + "-Queens Problem using Backtracking...\n");

        if (!solveNQueens(board, 0, n)) {
            System.out.println("No solution exists");
        } else {
            System.out.println("Total solutions found: " + solutionCount);
        }

        sc.close();
    }
}
