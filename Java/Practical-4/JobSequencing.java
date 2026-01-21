import java.util.*;

class Job {
    int id;
    int deadline;
    int profit;

    Job(int id, int deadline, int profit) {
        this.id = id;
        this.deadline = deadline;
        this.profit = profit;
    }
}

public class JobSequencing {

    public static void jobSequencing(Job[] jobs) {
        int n = jobs.length;

        // Sort jobs by profit in descending order
        Arrays.sort(jobs, (a, b) -> b.profit - a.profit);

        // Find maximum deadline
        int maxDeadline = 0;
        for (int i = 0; i < n; i++) {
            if (jobs[i].deadline > maxDeadline)
                maxDeadline = jobs[i].deadline;
        }

        // Create array to track time slots
        int[] slot = new int[maxDeadline];
        boolean[] filled = new boolean[maxDeadline];

        int totalProfit = 0;
        int jobCount = 0;

        System.out.println("\nSelected Jobs:");

        // Assign jobs to slots
        for (int i = 0; i < n; i++) {
            // Find a free slot for this job (starting from last possible slot)
            for (int j = Math.min(maxDeadline, jobs[i].deadline) - 1; j >= 0; j--) {
                if (!filled[j]) {
                    filled[j] = true;
                    slot[j] = jobs[i].id;
                    totalProfit += jobs[i].profit;
                    jobCount++;
                    System.out.println("Job " + jobs[i].id + " (Profit: " + jobs[i].profit
                            + ", Deadline: " + jobs[i].deadline + ")");
                    break;
                }
            }
        }

        System.out.println("\nTotal Jobs: " + jobCount);
        System.out.println("Total Profit: " + totalProfit);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of jobs: ");
        int n = sc.nextInt();

        Job[] jobs = new Job[n];
        System.out.println("Enter job details (ID, Deadline, Profit):");
        for (int i = 0; i < n; i++) {
            System.out.print("Job " + (i + 1) + " - ID: ");
            int id = sc.nextInt();
            System.out.print("Job " + (i + 1) + " - Deadline: ");
            int deadline = sc.nextInt();
            System.out.print("Job " + (i + 1) + " - Profit: ");
            int profit = sc.nextInt();
            jobs[i] = new Job(id, deadline, profit);
        }

        jobSequencing(jobs);

        sc.close();
    }
}
