from service import Service


class City24(Service):
    async def run(self):
        if self.phone_code == "380":
            await self.post(
                "https://city24.ua/personalaccount/account/registration",
                data={"PhoneNumber": self.formatted_phone},
            )
