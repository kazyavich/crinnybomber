from service import Service


class OkeanSushi(Service):
    async def run(self):
        if self.phone_code == "7" and len(self.formatted_phone) == 11:
            await self.get("https://okeansushi.ru/includes/contact.php",
                params={
                    "call_mail": "1",
                    "ajax": "1",
                    "name": self.russian_name,
                    "phone": self.format(
                        self.phone, "8 (***) ***-**-**"
                    ),
                    "call_time": "1",
                    "pravila2": "on",
                },
            )
