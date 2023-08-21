from faker.providers import BaseProvider
import random
import time
import uuid
from datetime import datetime

class IoTProvider(BaseProvider):
    def iot_device(self):
        valid_iot_devices = [
            "Dishwasher",
            "Refrigerator",
            "Coffee_machine",
            "Smart_watch",
            "Heater",
            "Car",
        ]
        return random.choice(valid_iot_devices)

    def cpu_id(self):
        validIds = ["cpu1", "cpu2", "cpu3", "cpu4", "cpu5"]
        return validIds[random.randint(0, len(validIds) - 1)]

    def usage(self):
        return random.random() * 30 + 70

    def temp(self):
        return random.randint(20, 100)

    def moisture(self):
        return random.randint(1, 20)

    def produce_msg(self):
        iot_device = self.iot_device()
        ts = time.time()
        message = {
            "iot_device": iot_device,
            "cpu": self.cpu_id(),
            "cpu_usage": self.usage(),
            "temp": self.temp(),
            "moisture": self.moisture(),
            "timestamp": datetime.utcnow().isoformat(),
        }
        # Generate a random UUID as the key
        uuid_key = str(uuid.uuid4())
        key = {"iot_id": uuid_key}

        return message, key
