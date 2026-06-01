import psycopg2
from kafka import KafkaConsumer
import json
conn = psycopg2.connect(
    host='localhost',
    database='smartcity',
    user='admin',
    password='admin123',
    port=5432
)
cur = conn.cursor()
consumer=KafkaConsumer("traffic-data",bootstrap_servers='localhost:9092',auto_offset_reset='earliest')
insertquery = """
insert into traffic_data (vehicle_id, vehicle_count, avg_speed, trafficlevel, timstamp) values (%s, %s, %s, %s, %s)
"""
while True:
    for message in consumer:
        traffic_data=json.loads(message.value.decode('utf-8'))
        cur.execute(insertquery, (
            traffic_data["vehicle_id"], traffic_data["vehicle_count"], traffic_data["avg_speed"], traffic_data["trafficlevel"], traffic_data["timstamp"]))
        conn.commit()
        print(f"inserted data: {traffic_data}")