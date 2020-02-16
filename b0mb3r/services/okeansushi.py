from service import Service


class OkeanSushi(Service):
    async def run(self):
        if self.phone_code == "7" and len(self.formatted_phone) == 11:
            phone = self.phone
            phone_with_mask = f"8 ({phone[:3]}) {phone[3:6]}-{phone[6:8]}-{phone[8:10]}"
            await self.get("https://okeansushi.ru/includes/contact.php",
                params={
                    "call_mail": "1",
                    "ajax": "1",
                    "name": self.russian_name,
                    "phone": phone_with_mask,
                    "call_time": "1",
                    "pravila2": "on",
                },
            )
