from service import Service


class PlanetaKino(Service):
    async def run(self):
        if self.phone_code == "380":
            await self.get(
                "https://cabinet.planetakino.ua/service/sms", params={"phone": self.formatted_phone}
            )
