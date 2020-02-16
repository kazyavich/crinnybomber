from service import Service


class FoodBand(Service):
    async def run(self):
        if self.phone_code == "7" and len(self.formatted_phone) == 11:
            await self.post(
                "https://foodband.ru/api?call=calls",
                data={
                    "customerName": self.russian_name,
                    "phone": self.format(
                        self.formatted_phone, "+* (***) ***-**-**"
                    ),
                    "g-recaptcha-response": "",
                },
            )
            await self.get(
                "https://foodband.ru/api/",
                params={
                    "call": "customers/sendVerificationCode",
                    "phone": self.phone,
                    "g-recaptcha-response": "",
                },
            )
