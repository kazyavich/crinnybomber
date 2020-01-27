from service import Service


class SberFood(Service):
    async def run(self):
        await self.post(
            "https://app.sberfood.ru/api/mobile/v3/auth/sendSms",
            json={"userPhone": "+" + self.formatted_phone},
            headers={"AppKey": "WebApp-3a2605b0cf2a4c9d938752a84b7e97b6"},
        )
