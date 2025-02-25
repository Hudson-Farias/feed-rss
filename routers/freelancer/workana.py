from fastapi import APIRouter, Response

from utils.feed_generator import feed_generator
from crawlers.freelancer.workana import workana_crawler


router = APIRouter()

@router.get('/workana', status_code = 200, response_class = Response)
async def anilist_calendar_rss():
    fg = feed_generator('Workana crawler RSS', 'Workana crawler RSS.')

    data = await workana_crawler()

    for i, item in enumerate(data):
        fe = fg.add_entry()
        fe.id(str(i))

        fe.title(item['title'])
        fe.link(href = item['link'])
        fe.description(item['description'])

    return Response(content = fg.rss_str(pretty = True), media_type = 'application/rss+xml')
