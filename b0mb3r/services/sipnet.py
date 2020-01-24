# Работает раз в час на номер. А так вообще классный сервис, стоит добавить.

from service import Service


class SipNet(Service):
    async def run(self):
        await self.post(
            f"https://register.sipnet.ru/cgi-bin/exchange.dll/RegisterHelper?oper=9&callmode=1&phone=%2B{self.formatted_phone}",
        )
