from service import Service


class CloudLoyal(Service):
    async def run(self):
        await self.post(
            "https://app.cloudloyalty.ru/demo/send-code",
            json={
                "country": 2,
                "phone": self.phone,
                "roistatVisit": "47637",
                "experiments": {"new_header_title": "1"},
            },
        )
