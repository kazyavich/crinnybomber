from service import Service


class SMSGorod(Service):
    async def run(self):
        await self.post(
            "http://smsgorod.ru/sendsms2.php", data={"number": self.formatted_phone}
        )
