from service import Service


class TikTok(Service):
    async def run(self):
        if self.phone_code in self.country_codes:
            await self.post(
                "https://m.tiktok.com/node/send/download_link",
                json={
                    "slideVerify": 0,
                    "language": "en",
                    "PhoneRegin": self.country_codes[self.phone_code].upper(),
                    "Mobile": self.phone,
                    "page": {"af_adset_id": 0, "pid": 0},
                },
            )
