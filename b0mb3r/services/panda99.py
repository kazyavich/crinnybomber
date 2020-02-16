from service import Service
from time import time


class Panda99(Service):
    async def run(self):
        if self.phone_code == "7" and len(self.formatted_phone) == 11:
            await self.post(f"https://panda99.ru/bdhandlers/order.php?t={int(time())}",
                data={
                    "CB_NAME": self.russian_name,
                    "CB_PHONE": self.format(
                        self.formatted_phone, "+* (***) ***-****"
                    )
                },
            )
