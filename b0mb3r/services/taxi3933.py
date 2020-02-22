from json import dumps
from random import choice

from service import Service


class Taxi3933(Service):
    phone_codes = ["380"]

    async def run(self):
        locations = [
            {"street": "С Гуливер (Спортивная Пл. 1)", "streetId": "4818"},
            {"street": "Цирк (Победы Пл. 2)", "streetId": "5422"},
            {"street": "Аэропорт Борисполь Туда", "streetId": "49"},
            {"street": "Шевелева Юрия ул.", "streetId": "10631", "building": "48"},
        ]
        names = ["Анна", "Юля", "Натали", "Олег", "Андрей", "Иван"]
        await self.post(
            "https://form-kiev.taxi3933.ua/newBooking",
            data=dumps(
                {
                    "version": "2",
                    "client": "0.0.1",
                    "channel": "web",
                    "platform": "webkit-537.36",
                    "lang": "ru",
                    "city": "kiev",
                    "phone": self.formatted_phone,
                    "route": [choice(locations)],
                    "clComment": "",
                    "class": "Standart",
                    "name": choice(names),
                    "dstUnknown": True,
                }
            ),
        )
