from service import Service


class RedmondEda(Service):
    async def run(self):
        await self.post(
            "https://app.redmondeda.ru/api/v1/app/sendverificationcode",
            headers={"token": "."},
            data={"phone": self.formatted_phone},
        )
