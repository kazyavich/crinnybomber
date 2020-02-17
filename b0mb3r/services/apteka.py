from service import Service


class Apteka(Service):
    async def run(self):
        if self.phone_code == "7" and len(self.formatted_phone) == 11:
            await self.post(
                "https://apteka.ru/_action/auth/getForm/",
                data={
                    "form[NAME]": "",
                    "form[PERSONAL_GENDER]": "",
                    "form[PERSONAL_BIRTHDAY]": "",
                    "form[EMAIL]": "",
                    "form[LOGIN]": self.format(
                        self.formatted_phone, "+* (***) ***-**-**"
                    ),
                    "form[PASSWORD]": self.password,
                    "get-new-password": "Получите пароль по SMS",
                    "user_agreement": "on",
                    "personal_data_agreement": "on",
                    "formType": "simple",
                    "utc_offset": "120",
                },
            )
