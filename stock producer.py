from kafka import KafkaProducer
import json
import random
import time
from datetime import datetime

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

stocks = ["AAPL", "MSFT", "GOOGL", "AMZN"]

while True:
    data = {
        "symbol": random.choice(stocks),
        "price": round(random.uniform(100, 500), 2),
        "timestamp": str(datetime.now())
    }

    producer.send("stock_topic", data)
    print(data)

    time.sleep(2)
