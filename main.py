import uuid
from datetime import datetime
from faker import Faker
from kafka import KafkaProducer
import json

# Kafka details
bootstrap_servers = 'kafka-jesperrellme-jesper-9f34.aivencloud.com:27523'  # Note the SSL port (9093)
topic = 'jesperrellme_topic'
cert_folder = "./certs"
# cert_folder = "/Users/jesperrellme/Documents/GitHub/Aiven-send-json-to-kafka/certs"

# API key and secret
#api_key = ''
#api_secret = 'your-api-secret'

# Path to SSL certificate and key files
#ssl_cafile = './certs/ca-cert.crt'
#ssl_certfile = './certs/client-cert.crt'
#ssl_keyfile = '/path/to/client-key.key'

#ssl_cafile=cert_folder + "/ca.pem",
#ssl_certfile=cert_folder + "/service.cert",
#ssl_keyfile=cert_folder + "/service.key",

# print("ssl_cafile: {}".format(ssl_cafile))
# Create a Kafka producer instance with SSL settings
#producer = KafkaProducer(
 #   bootstrap_servers=bootstrap_servers,
  #  security_protocol='SSL',
   # ssl_cafile=ssl_cafile,
   # ssl_certfile=ssl_certfile,
   # ssl_keyfile=ssl_keyfile,
   # value_serializer=lambda v: json.dumps(v).encode("ascii"),
   # key_serializer=lambda v: json.dumps(v).encode("ascii")
#)

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

# Generate a random UUID as the key
uuid_key = str(uuid.uuid4())

# Create a mock event payload using Faker
event = {
    'id': uuid_key,
    'type': 'iot_sensor',
    'value': faker.pyfloat(min_value=0, max_value=100, right_digits=2),
    'timestamp': datetime.utcnow().isoformat()
}

# Send the event to the Kafka topic
producer.send(topic, key=uuid_key, value=event)

# Close the producer
producer.close()

print("Event sent successfully")

