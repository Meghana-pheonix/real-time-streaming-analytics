from kafka import KafkaConsumer
import clickhouse_connect
import json

print("Starting consumer...")

consumer = KafkaConsumer(
    "orders",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    group_id="orders-group",
    value_deserializer=lambda m: json.loads(m.decode("utf-8"))
)

print("Connected to Kafka")

client = clickhouse_connect.get_client(
    host='localhost',
    port=8123,
    username='admin',
    password='password'
)

print("Connected to ClickHouse")

for msg in consumer:

    data = msg.value

    print("Received:", data)

    client.insert(
        'analytics.orders',
        [[
            data["order_id"],
            data["user_id"],
            data["amount"],
            data["country"],
            data["event_time"]
        ]],
        column_names=[
            "order_id",
            "user_id",
            "amount",
            "country",
            "event_time"
        ]
    )

    print("Inserted")
