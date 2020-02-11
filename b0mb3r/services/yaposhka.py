from service import Service


class Yaposhka(Service):
    async def run(self):
        await self.post(
            "https://www.yaposhka.kh.ua/customer/account/createpost/",
            data={
                "success_url": "",
                "error_url": "",
                "is_subscribed": "0",
                "firstname": self.russian_name,
                "lastname": self.russian_name,
                "email": self.email,
                "password": self.password,
                "password_confirmation": self.password,
                "telephone": self.formatted_phone,
            },
        )
