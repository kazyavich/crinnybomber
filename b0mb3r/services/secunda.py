from service import Service


class Secunda(Service):
    async def run(self):
        await self.post(
            "https://secunda.com.ua/personalarea/registrationvalidphone",
            data={"ph": "+" + self.formatted_phone},
        )
