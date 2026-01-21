# Job Sequencing with Deadlines using Greedy Algorithm
# Time Complexity: O(n^2)
# Space Complexity: O(n)

class Job:
    def __init__(self, job_id, deadline, profit):
        self.id = job_id
        self.deadline = deadline
        self.profit = profit
    
    def __repr__(self):
        return f"(J{self.id}, D:{self.deadline}, P:{self.profit})"


def job_sequencing(jobs):
    """
    Solve job sequencing with deadlines using greedy approach
    Returns: (max_profit, sequence)
    """
    # Sort jobs by profit in descending order
    jobs.sort(key=lambda x: x.profit, reverse=True)
    
    # Find maximum deadline
    max_deadline = max(job.deadline for job in jobs)
    
    # Create time slots
    slots = [-1] * max_deadline
    sequence = []
    max_profit = 0
    
    # Schedule jobs
    for job in jobs:
        # Find a free slot for this job (starting from last possible slot)
        for slot in range(min(max_deadline, job.deadline) - 1, -1, -1):
            if slots[slot] == -1:
                slots[slot] = job.id
                sequence.append(job)
                max_profit += job.profit
                break
    
    return max_profit, sequence


def main():
    print("=== Job Sequencing with Deadlines (Greedy) ===\n")
    
    # Input
    n = int(input("Enter number of jobs: "))
    jobs = []
    
    print("\nEnter jobs (deadline profit):")
    for i in range(n):
        deadline = int(input(f"Job {i + 1} - Deadline: "))
        profit = int(input(f"Job {i + 1} - Profit: "))
        jobs.append(Job(i + 1, deadline, profit))
    
    # Solve
    max_profit, sequence = job_sequencing(jobs)
    
    # Output
    print("\n" + "="*50)
    print("SOLUTION:")
    print("="*50)
    print("\nJobs sorted by profit (descending):")
    for job in jobs:
        print(f"  Job {job.id}: Deadline={job.deadline}, Profit={job.profit}")
    
    print("\nSelected job sequence:")
    for i, job in enumerate(sequence):
        print(f"  Slot {i + 1}: Job {job.id} (Deadline={job.deadline}, Profit={job.profit})")
    
    print(f"\nMaximum profit: {max_profit}")
    print(f"Number of jobs completed: {len(sequence)}")
    print(f"Time Complexity: O(n^2)")


if __name__ == "__main__":
    main()
