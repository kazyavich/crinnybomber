from service import Service


class Multiplex(Service):
    async def run(self):
        if self.phone_code == "380":
            await self.post(
                "https://auth.multiplex.ua/login", json={"login": self.formatted_phone},
            )
