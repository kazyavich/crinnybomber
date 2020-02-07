from service import Service


class GinzaDelivery(Service):
    async def run(self):
        await self.post(
            "https://ginzadelivery.ru/v1/auth", json={"phone": self.formatted_phone},
        )
