from kafka import KafkaProducer
import json
import random
import time
from datetime import datetime
producer = KafkaProducer(bootstrap_servers='localhost:9092')
id = 1
while True:
    traffic = {
      "vehicle_id" : "t"+ str(id),
      "vehicle_count" : random.randint(0,100),
      "avg_speed" : random.randint(20,120),
      "trafficlevel":random.choice(["low","medium","high"]),
      "timstamp" : datetime.now().isoformat()
    }
    producer.send('traffic-data', value=json.dumps(traffic).encode('utf-8'))
    print(traffic)
    id+=1
    time.sleep(2)