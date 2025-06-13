import json
import random
from datetime import datetime, timedelta
 
# Define log levels and messages
log_levels = ["INFO", "ERROR", "DEBUG"]
log_messages = [
    "Service started",
    "Timeout occurred",
    "User not found",
    "Cache refreshed successfully",
    "Database reconnected",
    "Retry limit reached",
    "Health check passed",
    "Authentication failed"
]
 
# Generate one record per day for the last 1 year (365 days)
with open('combined.json', 'w') as f:
    for day_offset in range(365):
        timestamp = (datetime.now() - timedelta(days=day_offset, hours=random.randint(0, 23), minutes=random.randint(0, 59))).isoformat()
 
        sample_record = {
            "timestamp": timestamp,
            "log": {
                "level": random.choice(log_levels),
                "message": random.choice(log_messages)
            },
            "metrics": {
                "cpu": round(random.uniform(10, 95), 2),
                "latency": round(random.uniform(50, 2000), 2)
            }
        }
 
        f.write(json.dumps(sample_record) + "\n")