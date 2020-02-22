from base64 import b64encode

from service import Service


class Aitu(Service):
    phone_codes = ["7", "380", "998", "1"]

    async def run(self):
        prefixes = {"7": "\r\n\x0b", "380": "\x0e\n\x0c", "998": "\x0e\n\x0c", "1": "\r\n\x0b"}
        await self.post(
            "https://aitu.io/kz.btsd.messenger.auth.AuthService/SendCode",
            headers={"Content-Type": "application/grpc-web-text"},
            data=b64encode(
                f"\x00\x00\x00\x00{prefixes[self.phone_code]}{self.formatted_phone}".encode()
            ),
        )
