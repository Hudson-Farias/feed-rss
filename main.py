from fastapi import FastAPI, Response
from feedgen.feed import FeedGenerator

from anilist.calendary import anilist_calendary

app = FastAPI()

@app.get('/calendary', response_class = Response)
async def rss_feed():
    fg = FeedGenerator()
    fg.id('https://example.com/rss')
    fg.title('Anime calendar RSS')
    fg.link(href = 'https://example.com', rel = 'alternate')
    fg.language('pt-br')
    fg.description('Anime calendar.')


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
