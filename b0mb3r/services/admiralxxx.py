from service import Service


class AdmiralX(Service):
    async def run(self):
        await self.post(
            "https://win.1admiralxxx.ru/api/en/register.json",
            json={
                "mobile": self.formatted_phone,
                "bonus": "signup",
                "agreement": 1,
                "currency": "RUB",
                "submit": 1,
                "email": "",
                "lang": "en",
            },
        )
