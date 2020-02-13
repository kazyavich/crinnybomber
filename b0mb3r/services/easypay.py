from service import Service


class EasyPay(Service):
    async def run(self):
        if self.phone_code == "380":
            await self.post(
                "https://api.easypay.ua/api/auth/register",
                json={"phone": self.formatted_phone, "password": self.password},
            )
