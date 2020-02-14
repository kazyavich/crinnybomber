from service import Service


class RuTaxi(Service):
    async def run(self):
        if self.phone_code == "7":
            await self.post(
                "https://rutaxi.ru/ajax_auth.html", data={"l": self.phone, "c": "3"},
            )
