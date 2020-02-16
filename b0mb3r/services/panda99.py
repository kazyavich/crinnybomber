from service import Service
from time import time


class Panda99(Service):
    async def run(self):
        if self.phone_code == "7" and len(self.formatted_phone) == 11:
            phone = self.phone
            phone_with_mask = f"+7 ({phone[:3]}) {phone[3:6]}-{phone[6:8]}{phone[8:10]}"
            await self.post(f"https://panda99.ru/bdhandlers/order.php?t={int(time())}",
                data={"CB_NAME": self.russian_name, "CB_PHONE": phone_with_mask},
            )
