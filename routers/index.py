from fastapi import APIRouter, Response

from utils.feed_generator import feed_generator


router = APIRouter()

data = [
    {
        'title': 'Anime Calendar',
        'url': '/anilist/calendar',
        'description': 'The anime calendar fetches anime released in the past week and uses GraphQL to showcase my skills with the tool.'
    }
]

@router.get('/', status_code = 200, response_class = Response)
async def anilist_calendar_rss():
    fg = feed_generator('My Feeds RSS', 'Feed RSS.')

    for i, item in enumerate(data):
        fe = fg.add_entry()

        fe.id(str(i))
        fe.title(item['title'])
        fe.link(href = item['url'])
        fe.description(item['description'])

    return Response(content = fg.rss_str(pretty = True), media_type = 'application/rss+xml')
