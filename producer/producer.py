from kafka import KafkaProducer
import json
import random
from datetime import datetime

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v:
        json.dumps(v).encode('utf-8')
)

countries = [
    "India",
    "USA",
    "UK",
    "Germany"
]

for i in range(1000):

    order = {
        "order_id": i,
        "user_id": random.randint(1,100),
        "amount": random.randint(100,5000),
        "country": random.choice(countries),
        "event_time": str(datetime.now())
    }

    producer.send("orders", order)
    
producer.flush()
producer.close()

print("Done")
