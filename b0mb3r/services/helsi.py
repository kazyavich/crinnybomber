from service import Service


class Helsi(Service):
    async def run(self):
        await self.post(
            "https://helsi.me/api/healthy/accounts/login",
            json={"phone": self.formatted_phone, "platform": "PISWeb"},
        )
