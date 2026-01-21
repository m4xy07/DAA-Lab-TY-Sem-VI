import java.util.*;

class Item {
    int value;
    int weight;
    double ratio;

    Item(int value, int weight) {
        this.value = value;
        this.weight = weight;
        this.ratio = (double) value / weight;
    }
}

public class KnapsackComparison {

    // Fractional Knapsack using Greedy
    public static double fractionalKnapsack(Item[] items, int capacity) {
        Item[] temp = new Item[items.length];
        for (int i = 0; i < items.length; i++) {
            temp[i] = items[i];
        }

        Arrays.sort(temp, (a, b) -> Double.compare(b.ratio, a.ratio));

        double totalValue = 0.0;

        for (int i = 0; i < temp.length; i++) {
            if (capacity >= temp[i].weight) {
                capacity -= temp[i].weight;
                totalValue += temp[i].value;
            } else {
                totalValue += temp[i].value * ((double) capacity / temp[i].weight);
                break;
            }
        }

        return totalValue;
    }

    // 0/1 Knapsack using Dynamic Programming
    public static int knapsack01(Item[] items, int capacity) {
        int n = items.length;
        int[][] dp = new int[n + 1][capacity + 1];

        // Build table in bottom-up manner
        for (int i = 0; i <= n; i++) {
            for (int w = 0; w <= capacity; w++) {
                if (i == 0 || w == 0)
                    dp[i][w] = 0;
                else if (items[i - 1].weight <= w)
                    dp[i][w] = Math.max(items[i - 1].value + dp[i - 1][w - items[i - 1].weight],
                            dp[i - 1][w]);
                else
                    dp[i][w] = dp[i - 1][w];
            }
        }

        return dp[n][capacity];
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of items: ");
        int n = sc.nextInt();

        Item[] items = new Item[n];
        System.out.println("Enter value and weight for each item:");
        for (int i = 0; i < n; i++) {
            System.out.print("Item " + (i + 1) + " - Value: ");
            int value = sc.nextInt();
            System.out.print("Item " + (i + 1) + " - Weight: ");
            int weight = sc.nextInt();
            items[i] = new Item(value, weight);
        }

        System.out.print("Enter knapsack capacity: ");
        int capacity = sc.nextInt();

        System.out.println("\n--- Fractional Knapsack (Greedy) ---");
        double greedyResult = fractionalKnapsack(items, capacity);
        System.out.println("Maximum value: " + greedyResult);

        System.out.println("\n--- 0/1 Knapsack (Dynamic Programming) ---");
        int dpResult = knapsack01(items, capacity);
        System.out.println("Maximum value: " + dpResult);

        System.out.println("\n--- Comparison ---");
        if (greedyResult > dpResult) {
            System.out.println("Greedy approach gives better result for fractional knapsack.");
            System.out.println("However, for 0/1 knapsack, DP is optimal as items cannot be broken.");
        } else if (dpResult > greedyResult) {
            System.out.println("Dynamic Programming gives optimal solution for 0/1 knapsack.");
            System.out.println("Greedy strategy does not work for 0/1 knapsack.");
        } else {
            System.out.println("Both approaches give same result in this case.");
        }

        sc.close();
    }
}
