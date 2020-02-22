from json import dumps
from random import choice

from service import Service


class Taxi292(Service):
    async def run(self):
        locations = [
            {
                "name": "Гуливер тц (Спортивная пл.1)",
                "lat": 50.4373112240241,
                "lng": 30.520967206634,
            },
            {"name": "ЦИРК (пл.Победы2)", "lat": 50.447202162029, "lng": 30.492127674114},
            {
                "name": "Аэропорт Борисполь терминал F✈",
                "lat": 50.3428132658132,
                "lng": 30.8902956980719,
            },
            {
                "name": "ШЕВЕЛЕВА ЮРИЯ УЛ.",
                "lat": 50.4248647934474,
                "lng": 30.6631460783441,
                "number": "48",
            },
        ]
        servers = ["http://91.211.117.3:7201", "http://91.211.117.4:7200"]
        await self.post(
            "https://ap4.taxi/api/TaxiAPI.php",
            data={
                "action": "order_create",
                "address": choice(servers),
                "args": dumps(
                    {
                        "user_full_name": "Taksico WEB",
                        "user_phone": self.formatted_phone,
                        "reservation": False,
                        "comment": "перезвонить для уточнения",
                        "minibus": False,
                        "wagon": False,
                        "premium": True,
                        "flexible_tariff_name": None,
                        "baggage": False,
                        "animal": False,
                        "conditioner": False,
                        "courier_delivery": False,
                        "route_undefined": False,
                        "terminal": False,
                        "receipt": False,
                        "add_cost": 0,
                        "taxiColumnId": 0,
                        "payment_type": 0,
                        "route": [choice(locations), choice(locations)],
                    }
                ),
            },
        )
