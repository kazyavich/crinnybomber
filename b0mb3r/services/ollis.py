from service import Service


class Ollis(Service):
    async def run(self):
        await self.get(
            "https://www.ollis.ru/gql",
            json={
                "query": 'mutation { phone(number:"%s", locale:ru) { token error { code message } } }'
                % self.formatted_phone
            },
        )
