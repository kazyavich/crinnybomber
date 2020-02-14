from service import Service


class UberClean(Service):
    async def run(self):
        if self.phone_code == "7":
            phone = self.formatted_phone
            phone_with_mask = f"+{phone[0]} ({phone[1:4]}) {phone[4:7]}-{phone[7:9]}{phone[9:11]}"
            await self.post(
                "https://uberclean24.ru/feedback/create",
                data={
                    "feedbackType": "4",
                    "CallMeBackForm[feedbackName]": "Форма заказа обратного звонка",
                    "CallMeBackForm[name]": self.russian_name,
                    "CallMeBackForm[phone]": phone_with_mask
                },
            )
