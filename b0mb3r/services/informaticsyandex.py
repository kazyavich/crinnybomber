from service import Service


class InformaticsYandex(Service):
    phone_codes = ["7"]

    async def run(self):
        await self.post(
            "https://informatics.yandex/api/v1/rest-auth/password/reset/",
            data={
                "authorization_type": "phone",
                "csrfmiddlewaretoken": "",
                "phone": self.format(self.formatted_phone, "+* *** *** ** **"),
            },
        )
