from service import Service


class Metropolis(Service):
    async def run(self):
        await self.post(
            "http://mobile-api.metropolis.moscow/v1/register",
            data={"phone": self.formatted_phone,},
        )
        await self.post(
            "http://mobile-api.metropolis.moscow/v1/send-code",
            data={"phone": self.formatted_phone,},
        )
