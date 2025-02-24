from httpx import AsyncClient
from datetime import datetime, timedelta


async def anilist_calendary():
    with open('anilist/calendary/calendary.gql', 'r', encoding = 'utf8') as file: graphql = file.read()
    data = []

    now = datetime.now()
    yesterday = now - timedelta(days = 6)

    async with AsyncClient() as client:
        has_next_page = True
        page = 1

        while has_next_page:

            json = {
                'query': graphql, 
                'variables': {
                    'page': page,
                    'airingAt_greater': int(yesterday.timestamp()),
                    'airingAt_lesser': int(now.timestamp())
                }
            }

            response = await client.post('https://graphql.anilist.co', json = json)
            payload = response.json()

            data += payload['data']['Page']['airingSchedules']
            has_next_page = payload['data']['Page']['pageInfo']['hasNextPage']
            page += 1

    return data
