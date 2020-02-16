from service import Service


class FoodBand(Service):
    async def run(self):
        if self.phone_code == "7" and len(self.formatted_phone) == 11:
            phone = self.phone
            phone_with_mask = f"+7 ({phone[:3]}) {phone[3:6]}-{phone[6:8]}-{phone[8:10]}"
            await self.post(
                "https://foodband.ru/api?call=calls",
                data={
                    "customerName": self.russian_name,
                    "phone": phone_with_mask,
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
