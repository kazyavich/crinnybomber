import random
import string

import aiohttp


class Service:
    user_agent = "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36"
    client = aiohttp.ClientSession()

    def __init__(self, phone, phone_code):
        self.phone = phone
        self.phone_code = phone_code
        self.formatted_phone = self.phone_code + self.phone

        self.client.headers = {"User-Agent": self.user_agent}

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
