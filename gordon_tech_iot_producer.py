from faker.providers import BaseProvider
import random
from datetime import datetime

class GordonTechIoTProvider(BaseProvider):
    def vehicle(self):
        valid_vehicles = [
            ["vehicle_44324", "Jesper Rellme", "van"],
            ["vehicle_66455", "Dave Beech", "small_truck"],
            ["vehicle_44324", "Matt Cornillon", "van"],
            ["vehicle_44324", "Calum Muir", "truck"],
            ["vehicle_44324", "Morvarid Aprin", "cargo_van"]
        ]
        return random.choice(valid_vehicles)

    def temp(self):
        return random.randint(-20, -2)

    def moisture(self):
        return random.randint(1, 20)

    def generate_coordinates(self):
        latitude = random.uniform(-90.0, 90.0)
        longitude = random.uniform(-180.0, 180.0)
        return latitude, longitude

    def produce_msg(self):
        vehicle = self.vehicle()
        lat, lon = self.generate_coordinates()
        message = {
            "vehicle_id": vehicle[0],
            "driver:": vehicle[1],
            "vehicle_type": vehicle[2],
            "Latitude": round(lat,6),
            "Longitude": round(lon,6),
            "temp": self.temp(),
            "moisture": self.moisture(),
            "timestamp": datetime.utcnow().isoformat(),
        }
        print(vehicle)
        # Use vehicle_id as key
        key = {"vehicle_id": vehicle[0]}

        return message, key
