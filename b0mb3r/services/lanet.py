from service import Service
from urllib.parse import quote
import random


class Lanet(Service):
    async def run(self):
        if self.formatted_phone.startswith("380"):
            params = quote(str({
                "nme": self.russian_name,
                "tel": self.formatted_phone,
                "typ": "2",
                "ip": "",
                "cty": "1",
                "srv_order_info": "Заказ консультации",
                "ssid": f"GA1.2.{random.randint(1111111111,9999999999)}.{random.randint(1111111111,9999999999)}"
            }).replace("'", '"')).replace("%3A", ":").replace("%2C", ",").replace("%20", "")
            await self.get(f"https://backend.lanet.ua/api/v1/setCallBack/{params}")
