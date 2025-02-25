from asyncio import run

from crawlers.freelancer.workana import workana_crawler
# from anilist.calendar import anilist_calendar

from utils.json import json_creater


async def main():
    data = await workana_crawler()
    json_creater(data)


run(main())
