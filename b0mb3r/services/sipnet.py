from service import Service


class SipNet(Service):
    async def run(self):
        await self.get(
            "https://register.sipnet.ru/cgi-bin/exchange.dll/RegisterHelper",
            params={"oper": 9, "callmode": 1, "phone": "+" + self.formatted_phone},
        )
