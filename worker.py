import time
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Memory leak: This list grows forever
processed_tasks = []


def fetch_pending_tasks():
    """Simulate fetching tasks from a queue"""
    logger.info("Fetching pending tasks...")
    return [
        {"id": i, "data": f"task_{i}"} 
        for i in range(10)
    ]


def process_task(task):
    """Process a single task"""
    logger.debug(f"Processing task {task['id']}")
    result = {
        "task_id": task["id"],
        "processed_at": datetime.now().isoformat(),
        "status": "completed"
    }
    return result


def save_result(result):
    """Simulate saving result to database"""
    logger.info(f"Saved task {result['task_id']} - Status: {result['status']}")


def run_worker():
    """Main worker loop"""
    logger.info("Worker started successfully")
    
    while True:
        tasks = fetch_pending_tasks()
        logger.info(f"Found {len(tasks)} tasks to process")
        
        for task in tasks:
            result = process_task(task)
            processed_tasks.append(result)  # BUG: Never cleared!
            save_result(result)
        
        logger.info(f"Batch complete. Total processed: {len(processed_tasks)}")
        time.sleep(5)


if __name__ == "__main__":
    logger.info("Starting background worker...")
    run_worker()
