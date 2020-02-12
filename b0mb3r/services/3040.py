from service import Service


class Taxi3040(Service):
    async def run(self):
        if self.formatted_phone.startswith("380"):
            await self.post(
                "https://3040.com.ua/taxi-ordering",
                data={"callback-phone": self.formatted_phone},
            )
