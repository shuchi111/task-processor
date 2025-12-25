import time
from datetime import datetime

# Store all processed task results for tracking
processed_tasks = []


def fetch_pending_tasks():
    """Simulate fetching tasks from a queue"""
    return [
        {"id": i, "data": f"task_{i}"} 
        for i in range(10)
    ]


def process_task(task):
    """Process a single task"""
    result = {
        "task_id": task["id"],
        "processed_at": datetime.now().isoformat(),
        "status": "completed",
        "data": task["data"] * 100  # Store some data with each result
    }
    return result


def save_result(result):
    """Simulate saving result to database"""
    print(f"Saved: {result['task_id']}")


def run_worker():
    """
    Main worker loop - runs continuously in production.
    Processes tasks every 5 seconds, 24/7.
    """
    print("Worker started - running continuously...")
    
    while True:
        tasks = fetch_pending_tasks()
        
        for task in tasks:
            result = process_task(task)
            
            # Keep track of everything we've processed
            processed_tasks.append(result)
            
            save_result(result)
        
        # Log progress
        print(f"Batch complete. Total tasks processed: {len(processed_tasks)}")
        
        time.sleep(5)


if __name__ == "__main__":
    print("Starting background worker...")
    run_worker()
