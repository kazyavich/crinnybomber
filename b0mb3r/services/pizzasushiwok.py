from service import Service


class PizzaSushiWok(Service):
    async def run(self):
        if self.phone_code == "7" and len(self.formatted_phone) == 11:
            phone = self.phone
            phone_with_mask = f"8-{phone[:3]}-{phone[3:6]}-{phone[6:8]}-{phone[8:10]}"
            await self.post("https://pizzasushiwok.ru/index.php",
                data={
                    "mod_name": "call_me",
                    "task": "request_call",
                    "name": self.russian_name,
                    "phone": phone_with_mask,
                }
            )
