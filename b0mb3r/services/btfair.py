from service import Service


class Betfair(Service):
    async def run(self):
        await self.post(
            "https://btfair.site/api/user/phone/code", json={"phone": "+" + self.formatted_phone,},
        )
