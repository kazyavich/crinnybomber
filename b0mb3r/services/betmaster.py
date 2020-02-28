from service import Service


class GGBet(Service):
    async def run(self):
        await self.post(
            "https://ggbet.ru/api/auth/register-with-phone",
            data={
                "phone": "+" + self.formatted_phone,
                "login": self.email,
                "password": self.password,
                "agreement": "on",
                "oferta": "on",
            },
        )
