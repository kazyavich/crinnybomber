import random
import re
import string
from abc import ABC, abstractmethod

import aiohttp


class Service(ABC):
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 5.0.2; 7045Y Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2728.43 Mobile Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
    }
    country_codes = {"7": "ru", "375": "by", "380": "ua"}
    phone_codes = []
    client = aiohttp.ClientSession(
        headers=headers, connector=aiohttp.TCPConnector(verify_ssl=False)
    )

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

    async def get_csrf_token(self, url: str, pattern):
        response = await self.get(url)
        return re.search(pattern, await response.text()).group(1).strip()

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
