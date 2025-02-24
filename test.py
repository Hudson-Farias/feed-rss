from asyncio import run

from anilist.calendar import anilist_calendar

from utils.json import json_creater


async def main():
    data = await anilist_calendar()
    json_creater(data)


run(main())
