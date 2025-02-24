from fastapi import APIRouter, Response

from utils.feed_generator import feed_generator
from anilist.calendary import anilist_calendary


router = APIRouter()

@router.get('/anilist/calendary', status_code = 200, response_class = Response)
async def anilist_calendary_rss():
    fg = feed_generator('Anime calendar RSS', 'Anime calendar.')

    data = await anilist_calendary()

    for item in data:
        payload = item['media']
        if payload['isAdult']: continue

        fe = fg.add_entry()
        fe.id(str(item['id']))
        fe.title(payload['title']['romaji'])
        fe.link(href = payload['siteUrl'])
        fe.description(payload['description'])

    return Response(content = fg.rss_str(pretty = True), media_type = 'application/rss+xml')
