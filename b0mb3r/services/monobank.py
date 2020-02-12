from service import Service


class MonoBank(Service):
    async def run(self):
        await self.post(
            "https://www.monobank.com.ua/api/mobapplink/send",
            data={"phone": "+" + self.formatted_phone},
        )
