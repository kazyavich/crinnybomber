from service import Service


class Mousam(Service):
    async def run(self):
        await self.post(
            "https://mousam.ru/api/checkphone",
            data={"phone": self.formatted_phone, "target": "android app v0.0.2"},
        )
