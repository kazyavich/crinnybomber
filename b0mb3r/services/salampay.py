from service import Service


class SalamPay(Service):
    async def run(self):
        await self.post(
            "https://app.salampay.com/api/system/sms/c549d0c2-ee78-4a98-659d-08d682a42b29",
            data={"caller_number": self.formatted_phone},
        )
