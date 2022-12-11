from faker import Faker
from kafka import KafkaProducer
import json
import time

fake = Faker()

def get_registered_data():
    return {
        'name': fake.name(),
        'address': fake.address(),
        'created': fake.year()
    }


def json_serializer(data):
    return json.dumps(data).encode('utf-8')


producer = KafkaProducer(bootstrap_servers=['172.20.10.3:9092'],
                         value_serializer=json_serializer)
if __name__ == "__main__":
    while 1 == 1:
        registered_data = get_registered_data()
        print(registered_data)
        producer.send('registered_user', registered_data)
        time.sleep(2)
