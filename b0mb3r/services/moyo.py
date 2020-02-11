from service import Service


class Moyo(Service):
    async def run(self):
        if self.formatted_phone.startswith("380"):
            await self.post(
                "https://www.moyo.ua/identity/registration",
                headers={"X-Requested-With": "XMLHttpRequest"},
                data={
                    "firstname": self.russian_name,
                    "phone": self.formatted_phone,
                    "email": self.email,
                },
            )
