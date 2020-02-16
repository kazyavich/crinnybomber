from service import Service


class SushiProfi(Service):
    async def run(self):
        if self.phone_code == "7":
            await self.post(
                "https://www.tanuki.ru/api/", json={"phone": self.phone, "name": self.russian_name}
            )
