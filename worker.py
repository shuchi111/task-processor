import time
from datetime import datetime


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
        "status": "completed"
    }
    return result


def save_result(result):
    """Simulate saving result to database"""
    print(f"Saved: {result['task_id']}")


def run_worker():
    """Main worker loop"""
    while True:
        tasks = fetch_pending_tasks()
        
        for task in tasks:
            result = process_task(task)
            save_result(result)
        
        time.sleep(5)


if __name__ == "__main__":
    print("Starting background worker...")
    run_worker()
