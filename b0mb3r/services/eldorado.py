from service import Service


class EldoradoUA(Service):
    phone_codes = ["380"]

    async def run(self):
        await self.options(
            "https://api.eldorado.ua/v1/sign/",
            params={
                "login": self.formatted_phone,
                "step": "phone-check",
                "fb_id": None,
                "fb_token": None,
                "lang": "ru",
            },
        )
        await self.get(
            "https://api.eldorado.ua/v1/sign/",
            params={
                "login": self.formatted_phone,
                "step": "phone-check",
                "fb_id": None,
                "fb_token": None,
                "lang": "ru",
            },
        )
