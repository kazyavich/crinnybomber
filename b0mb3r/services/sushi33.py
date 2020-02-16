from service import Service


class Sushi33(Service):
    async def run(self):
        if self.phone_code == "380":
            await self.get("https://auth.pizza33.ua/ua/join/check/",
                params={
                    "callback": "angular.callbacks._1",
                    "email": self.email,
                    "password": self.password,
                    "phone": self.phone,
                    "utm_current_visit_started": 0,
                    "utm_first_visit": 0,
                    "utm_previous_visit": 0,
                    "utm_times_visited": 0,
                },
            )
