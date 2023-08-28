from faker import Faker
from iot_producer import IoTProvider
from gordon_tech_iot_producer import GordonTechIoTProvider
from kafka import KafkaProducer
import json
import time
import random


# Kafka details
bootstrap_servers = 'kafka-jesperrellme-jesper-9f34.aivencloud.com:27523'
topic = 'jesperrellme_topic'
cert_folder = "./certs"

producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            security_protocol="SSL",
            ssl_cafile=cert_folder + "/ca.pem",
            ssl_certfile=cert_folder + "/service.cert",
            ssl_keyfile=cert_folder + "/service.key",
            value_serializer=lambda v: json.dumps(v).encode("ascii"),
            key_serializer=lambda v: json.dumps(v).encode("ascii"),
        )

# Initialize the Faker instance
faker = Faker()

i = 0
number_of_messages = 2500

#faker.add_provider(IoTProvider)
faker.add_provider(GordonTechIoTProvider)

while i < number_of_messages:

    message, key = faker.produce_msg()
    print("Sending: {}".format(message))
    # sending the message to Kafka
    producer.send(topic, key=key, value=message)
    # Sleeping time
    sleep_time = (
            random.randint(0, int(5 * 10000)) / 10000
    )
    print("Sleeping for..." + str(sleep_time) + "s")
    time.sleep(sleep_time)

    # Force flushing of all messages
    if (i % 100) == 0:
        producer.flush()
    i = i + 1
producer.flush()
# Close the producer
producer.close()

print("Events sent successfully")
