from service import Service


class NovayaLinya(Service):
    async def run(self):
        await self.post(
            "https://www.nl.ua",
            data={
                "component": "bxmaker.authuserphone.login",
                "sessid": "bf70db951f54b837748f69b75a61deb4",
                "method": "sendCode",
                "phone": self.formatted_phone,
                "registration": "N",
            },
        )
