from kafka import KafkaConsumer
import json
import time
import pandas as pd
from collections import defaultdict

# Kafka consumer setup
consumer = KafkaConsumer(
    'events',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',  # start from the beginning
    group_id='bigdata-group'
)

# Batch setup
BATCH_SIZE = 10
batch = []

# Running count of actions
action_counts = defaultdict(int)

print("Starting Big Data consumer...")

for message in consumer:
    # Decode and parse JSON
    event = json.loads(message.value.decode('utf-8'))

    # Transformations
    event['timestamp_human'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(event['timestamp']))
    event['user_segment'] = 'VIP' if event['user_id'] > 90 else 'Regular'

    # Update action counts
    action_counts[event['action']] += 1

    # Add to batch
    batch.append(event)

    print(f"Transformed event: {event}")
    print(f"Running action counts: {dict(action_counts)}\n")

    # Write batch to CSV
    if len(batch) >= BATCH_SIZE:
        df = pd.DataFrame(batch)
        df.to_csv('events_output.csv', mode='a', header=not pd.io.common.file_exists('events_output.csv'), index=False)
        print(f"Wrote batch of {len(batch)} events to events_output.csv\n")
        batch = []
