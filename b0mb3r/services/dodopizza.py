from service import Service


class Dodopizza(Service):
    async def run(self):
        await self.post(
            f"https://mapi.dodopizza.ru/api/v1/login/sendPinCode?phoneNumber=+{self.formatted_phone}&Language=ru-RU&CountryCode=643",
            data='',
        )