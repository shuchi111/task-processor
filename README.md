# Task Processor

A simple background worker that processes tasks from a queue.

## Usage

```bash
python worker.py
```

The worker runs continuously and processes tasks every 5 seconds.

## Logging

The worker includes structured logging to track task processing:

- `INFO` - Task fetching, saving, and batch completion
- `DEBUG` - Individual task processing details

Logs are output to stdout with timestamps.
