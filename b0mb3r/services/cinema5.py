from service import Service


class Cinema5(Service):
    phone_codes = ["7"]

    async def run(self):
        await self.post(
            "https://cinema5.ru/api/phone_code",
            data={"phone": self.format(self.formatted_phone, "+* (***) ***-**-**"),},
        )
