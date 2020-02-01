from service import Service


class MobilePlanet(Service):
    async def run(self):
        await self.post(
            "https://mobileplanet.ua/register",
            data={
                "klient_name": self.username,
                "klient_phone": "+" + self.formatted_phone,
                "klient_email": self.email,
            },
        )
