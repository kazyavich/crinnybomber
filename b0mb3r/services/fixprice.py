from service import Service


class FixPrice(Service):
    async def run(self):
        await self.get(
            "https://fix-price.ru/ajax/register_phone_code.php",
            data={"register_call": "Y", "action": "getCode", "phone": "+" + self.formatted_phone},
        )
