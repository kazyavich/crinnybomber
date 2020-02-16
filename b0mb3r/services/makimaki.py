from service import Service


class MakiMaki(Service):
    async def run(self):
        if self.phone_code == "7" and len(self.formatted_phone) == 11:
            await self.get(
                "https://makimaki.ru/system/callback.php",
                params={
                    "cb_fio": self.russian_name,
                    "cb_phone": self.format(
                        self.formatted_phone, "+* *** *** ** **"
                    )
                },
            )
