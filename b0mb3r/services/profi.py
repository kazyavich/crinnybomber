from service import Service


class Profi(Service):
    async def run(self):
        await self.post(
            f"https://api.profi.ru/warp/v2/graphql/",
            data='{"query":"mutation requireCheckContactsAndroid($scenario: ScenarioTypeEnum!, $phone: PhoneNumber!) {\n    requireCheckContacts(input: {scenario: $scenario, phone: $phone}) {\n        sent\n        exists\n    }\n}","variables":"{\"scenario\":\"AUTH_SCENARIO_FORK\",\"phone\":\"+%s\"}"}' % self.formatted_phone,
        )