from service import Service


class TarantinoFamily(Service):
    async def run(self):
        if self.phone_code == "380":
            await self.post(
                "https://www.tarantino-family.com/wp-admin/admin-ajax.php",
                data={"action": "callback_phonenumber", "phone": self.formatted_phone},
            )
