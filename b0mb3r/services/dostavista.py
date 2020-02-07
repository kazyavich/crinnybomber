from service import Service


class Dostavista(Service):
    async def run(self):
        await self.post(
            "https://dostavista.ru/backend/send-verification-sms", data={"phone": self.phone},
        )
