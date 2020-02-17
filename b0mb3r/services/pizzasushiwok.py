from service import Service


class PizzaSushiWok(Service):
    async def run(self):
        if self.phone_code == "7" and len(self.formatted_phone) == 11:
            await self.post(
                "https://pizzasushiwok.ru/index.php",
                data={
                    "mod_name": "call_me",
                    "task": "request_call",
                    "name": self.russian_name,
                    "phone": self.format(
                        self.formatted_phone, "8-***-***-**-**"
                    ),
                },
            )
