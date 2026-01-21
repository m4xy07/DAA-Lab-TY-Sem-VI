import java.util.Scanner;

public class BinarySearch {

    // Recursive Binary Search using Divide and Conquer
    public static int binarySearch(int[] arr, int low, int high, int key) {
        if (low <= high) {
            int mid = low + (high - low) / 2;

            // Element found at mid
            if (arr[mid] == key) {
                return mid;
            }

            // Search in left half
            if (arr[mid] > key) {
                return binarySearch(arr, low, mid - 1, key);
            }

            // Search in right half
            return binarySearch(arr, mid + 1, high, key);
        }

        // Element not found
        return -1;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of elements: ");
        int n = sc.nextInt();

        int[] arr = new int[n];
        System.out.print("Enter sorted elements: ");
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        System.out.print("Enter element to search: ");
        int key = sc.nextInt();

        int result = binarySearch(arr, 0, n - 1, key);

        if (result != -1) {
            System.out.println("Element found at index: " + result);
        } else {
            System.out.println("Element not found in array");
        }

        sc.close();
    }
}
