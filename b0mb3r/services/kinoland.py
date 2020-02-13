from service import Service


class Kinoland(Service):
    async def run(self):
        if self.phone_code == "380":
            await self.post(
                "https://api.kinoland.com.ua/api/v1/service/send-sms",
                headers={"Agent": "website"},
                json={"Phone": self.formatted_phone, "Type": 1},
            )
