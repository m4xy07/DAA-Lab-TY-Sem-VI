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

public class FractionalKnapsack {

    public static double fractionalKnapsack(Item[] items, int capacity) {
        // Sort items by value/weight ratio in descending order
        Arrays.sort(items, (a, b) -> Double.compare(b.ratio, a.ratio));

        double totalValue = 0.0;

        for (int i = 0; i < items.length; i++) {
            if (capacity >= items[i].weight) {
                // Take whole item
                capacity -= items[i].weight;
                totalValue += items[i].value;
                System.out.println("Item " + (i + 1) + ": Weight = " + items[i].weight
                        + ", Value = " + items[i].value + " (Full)");
            } else {
                // Take fraction of item
                double fraction = (double) capacity / items[i].weight;
                totalValue += items[i].value * fraction;
                System.out.println("Item " + (i + 1) + ": Weight = " + capacity
                        + ", Value = " + (items[i].value * fraction) + " (Fraction = " + fraction + ")");
                break;
            }
        }

        return totalValue;
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

        System.out.println("\nItems selected:");
        double maxValue = fractionalKnapsack(items, capacity);

        System.out.println("\nMaximum value in knapsack: " + maxValue);

        sc.close();
    }
}
