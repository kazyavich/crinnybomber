from service import Service


class InformaticsYandex(Service):
    async def run(self):
        if self.phone_code in self.country_codes:
            country = {"7": "RU", "380": "UA", "375": "BE"}

            await self.post(
                "https://informatics.yandex/api/v1/registration/confirmation/phone/send/",
                data={
                    "country": country,
                    "csrfmiddlewaretoken": "",
                    "phone": self.formatted_phone,
                },
            )
