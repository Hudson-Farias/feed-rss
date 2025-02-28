from httpx import AsyncClient
from datetime import datetime, timedelta

from utils.redis import set_cache, get_cache

async def anilist_calendar():
    data = get_cache('anilist_calendar')
    if data: return data


    with open('anilist/calendar/calendar.gql', 'r', encoding = 'utf8') as file: graphql = file.read()
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

    set_cache('anilist_calendar', data)
    return data
