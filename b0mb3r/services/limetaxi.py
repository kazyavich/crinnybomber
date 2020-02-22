from random import choice

from service import Service


class LimeTaxi(Service):
    phone_codes = ["380"]

    async def run(self):
        locations = [
            "С Гуливер (пл. Спортивная 1)",
            "ЦИРК (пл.Победы2)",
            "АЭРОПОРТ БОРИСПОЛЬ",
            "Метро Героев Днепра",
        ]
        await self.post(
            "https://limetaxi.com.ua/dynamicframe/index.php?order=1",
            data={
                "type_mesto_1": "object2",
                "route[0][name]": choice(locations),
                "route[0][number]": "",
                "route[0][route_address_entrance_from]": "",
                "type_mesto_2": "",
                "route[1][number]": "",
                "route[1][name]": "",
                "comment": "",
                "user_phone": self.format(self.formatted_phone, "+**(***)***-**-**"),
                "time": "",
                "dt": "",
                "minibus": "false",
                "wagon": "false",
                "premium": "true",
                "baggage": "false",
                "animal": "false",
                "conditioner": "false",
                "courier_delivery": "false",
                "receipt": "false",
                "user_full_name": "widget",
                "route_undefined": "true",
                "add_cost": "20",
            },
        )
