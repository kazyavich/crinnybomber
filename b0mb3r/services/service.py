import random
import string
from abc import ABC, abstractmethod

import aiohttp


class Service(ABC):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
    }
    country_codes = {"7": "ru", "375": "by", "380": "ua"}
    phone_codes = []
    client = aiohttp.ClientSession(headers=headers)

    def __init__(self, phone: str, phone_code: str):
        self.phone = phone
        self.phone_code = phone_code
        self.formatted_phone = self.phone_code + self.phone

        self.russian_name = "".join(
            random.choice("АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя")
            for _ in range(5)
        )
        self.username = self.password = "".join(
            random.choice(string.ascii_letters) for _ in range(12)
        )
        self.email = self.username + "@gmail.com"

        self.get = self.client.get
        self.post = self.client.post
        self.options = self.client.options

    @staticmethod
    def format(phone: str, mask: str, mask_symbol: str = "*"):
        if len(phone) == mask.count(mask_symbol):
            formatted_phone = ""
            for symbol in mask:
                if symbol == mask_symbol:
                    formatted_phone += phone[0]
                    phone = phone[(len(phone) - 1) * -1 :]
                else:
                    formatted_phone += symbol
        else:
            formatted_phone = phone
        return formatted_phone

    @abstractmethod
    async def run(self):
        pass
