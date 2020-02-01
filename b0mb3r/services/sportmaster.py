from service import Service


class Sportmaster(Service):
    async def run(self):
        await self.get(
            "https://www.sportmaster.ua/",
            params={"module": "users", "action": "SendSMSReg", "phone": self.formatted_phone},
        )
