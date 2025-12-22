from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

topic = 'events'

print("Starting producer...")
while True:
    event = {
        "user_id": random.randint(1, 100),
        "action": random.choice(["click", "view", "purchase"]),
        "timestamp": time.time()
    }
    producer.send(topic, event)
    print(f"Sent: {event}")
    time.sleep(1)
