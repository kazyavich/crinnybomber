from service import Service


class MenzaCafe(Service):
    async def run(self):
        if self.phone_code == "7" and len(self.formatted_phone) == 11:
            await self.get("https://menza-cafe.ru/system/call_me.php",
                params={
                    "fio": self.russian_name,
                    "phone": self.formatted_phone,
                    "phone_number": "1",
                },
            )
