from service import Service


class MosPizza(Service):
    async def run(self):
        if self.phone_code == "7":
            await self.post(
                "https://mos.pizza/bitrix/components/custom/callback/templates/.default/ajax.php",
                data={"name": self.russian_name, "phone": self.formatted_phone},
            )
