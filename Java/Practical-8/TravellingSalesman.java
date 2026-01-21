import java.util.*;

public class TravellingSalesman {

    static int n;
    static int[][] cost;
    static int[] finalPath;
    static boolean[] visited;
    static int finalCost = Integer.MAX_VALUE;

    public static void copyToFinal(int[] currPath) {
        for (int i = 0; i < n; i++)
            finalPath[i] = currPath[i];
        finalPath[n] = currPath[0];
    }

    public static int firstMin(int i) {
        int min = Integer.MAX_VALUE;
        for (int k = 0; k < n; k++)
            if (cost[i][k] < min && i != k)
                min = cost[i][k];
        return min;
    }

    public static int secondMin(int i) {
        int first = Integer.MAX_VALUE, second = Integer.MAX_VALUE;
        for (int j = 0; j < n; j++) {
            if (i == j)
                continue;

            if (cost[i][j] <= first) {
                second = first;
                first = cost[i][j];
            } else if (cost[i][j] <= second && cost[i][j] != first) {
                second = cost[i][j];
            }
        }
        return second;
    }

    public static void TSPRec(int currBound, int currWeight, int level, int[] currPath) {
        if (level == n) {
            // Check if there is an edge from last vertex to first vertex
            if (cost[currPath[level - 1]][currPath[0]] != 0) {
                int currRes = currWeight + cost[currPath[level - 1]][currPath[0]];

                if (currRes < finalCost) {
                    copyToFinal(currPath);
                    finalCost = currRes;
                }
            }
            return;
        }

        for (int i = 0; i < n; i++) {
            if (cost[currPath[level - 1]][i] != 0 && !visited[i]) {
                int temp = currBound;
                currWeight += cost[currPath[level - 1]][i];

                if (level == 1)
                    currBound -= ((firstMin(currPath[level - 1]) + firstMin(i)) / 2);
                else
                    currBound -= ((secondMin(currPath[level - 1]) + firstMin(i)) / 2);

                if (currBound + currWeight < finalCost) {
                    currPath[level] = i;
                    visited[i] = true;

                    TSPRec(currBound, currWeight, level + 1, currPath);
                }

                currWeight -= cost[currPath[level - 1]][i];
                currBound = temp;

                Arrays.fill(visited, false);
                for (int j = 0; j <= level - 1; j++)
                    visited[currPath[j]] = true;
            }
        }
    }

    public static void TSP() {
        int[] currPath = new int[n + 1];
        int currBound = 0;
        Arrays.fill(currPath, -1);
        Arrays.fill(visited, false);

        for (int i = 0; i < n; i++)
            currBound += (firstMin(i) + secondMin(i));

        currBound = (currBound == 1) ? currBound / 2 + 1 : currBound / 2;

        visited[0] = true;
        currPath[0] = 0;

        TSPRec(currBound, 0, 1, currPath);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of cities: ");
        n = sc.nextInt();

        cost = new int[n][n];
        finalPath = new int[n + 1];
        visited = new boolean[n];

        System.out.println("Enter cost matrix (use 0 for no direct path):");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print("Cost[" + i + "][" + j + "]: ");
                cost[i][j] = sc.nextInt();
            }
        }

        TSP();

        System.out.println("\nMinimum cost: " + finalCost);
        System.out.print("Path taken: ");
        for (int i = 0; i <= n; i++) {
            System.out.print(finalPath[i]);
            if (i < n)
                System.out.print(" -> ");
        }
        System.out.println();

        sc.close();
    }
}
