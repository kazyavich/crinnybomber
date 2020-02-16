from service import Service


class TaxiRitm(Service):
    async def run(self):
        if self.phone_code == "7":
            await self.post("https://taxi-ritm.ru/ajax/ppp/ppp_back_call.php?URL=/",
                data={
                    "RECALL": "Y",
                    "BACK_CALL_PHONE": self.formatted_phone
                }
            )
