from service import Service


class Moyo(Service):
    async def run(self):
        if self.phone_code == "380":
            await self.post(
                "https://www.moyo.ua/identity/registration",
                data={
                    "firstname": self.russian_name,
                    "phone": self.formatted_phone,
                    "email": self.email,
                },
            )
