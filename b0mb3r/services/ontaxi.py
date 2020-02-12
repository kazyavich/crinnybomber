from service import Service


class OnTaxi(Service):
    async def run(self):
        country_codes = {"7": "ru", "375": "by", "380": "ua"}
        if self.phone_code in country_codes:
            await self.post(
                "https://ontaxi.com.ua/api/v2/web/client",
                json={
                    "country": country_codes[self.phone_code].upper(),
                    "phone": self.phone,
                },
            )
