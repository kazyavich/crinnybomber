from time import time

from service import Service


class Panda99(Service):
    phone_codes = ["7"]

    async def run(self):
        await self.post(
            f"https://panda99.ru/bdhandlers/order.php?t={int(time())}",
            data={
                "CB_NAME": self.russian_name,
                "CB_PHONE": self.format(self.formatted_phone, "+* (***) ***-****"),
            },
        )
