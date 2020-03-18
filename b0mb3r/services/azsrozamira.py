from service import Service


class AzsRozaMira(Service):
    async def run(self):
        await self.post(
            "http://api.rozamira-azs.ru/v1/auth", data={"login": self.formatted_phone,},
        )
