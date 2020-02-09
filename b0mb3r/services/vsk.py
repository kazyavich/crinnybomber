from service import Service


class VSK(Service):
    async def run(self):
        await self.get(
            "https://shop.vsk.ru/ajax/auth/postSms/", data={"phone": self.formatted_phone}
        )
