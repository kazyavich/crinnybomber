from service import Service


class OnlineUa(Service):
    async def run(self):
        await self.get(
            "https://secure.online.ua/ajax/check_phone/", params={"reg_phone": self.phone},
        )
