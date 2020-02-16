from service import Service


class Niyama(Service):
    async def run(self):
        if self.phone_code == "7":
            await self.post(
                "https://www.niyama.ru/ajax/sendSMS.php",
                data={
                    "REGISTER[PERSONAL_PHONE]": self.formatted_phone,
                    "code": "",
                    "sendsms": "Выслать код",
                },
            )
