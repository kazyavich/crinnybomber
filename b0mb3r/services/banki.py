from service import Service


class BankiRu(Service):
    async def run(self):
        await self.get(
            "https://requests.service.banki.ru/form/960/submit",
            params={
                "callback": "submitCallback",
                "name": self.russian_name,
                "phone": "+" + self.formatted_phone,
                "email": self.email,
                "gorod": "Москва",
                "approving_data": "1",
            },
        )
