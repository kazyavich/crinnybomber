from service import Service


class MakiMaki(Service):
    async def run(self):
        if self.phone_code == "7" and len(self.formatted_phone) == 11:
            phone = self.phone
            phone_with_mask = f"+7 {phone[:3]} {phone[3:6]} {phone[6:8]} {phone[8:10]}"
            await self.get(
                "https://makimaki.ru/system/callback.php",
                params={"cb_fio": self.russian_name, "cb_phone": phone_with_mask},
            )
