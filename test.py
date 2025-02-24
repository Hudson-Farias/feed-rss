from asyncio import run

from anilist.calendary import anilist_calendary

from utils.json import json_creater


async def main():
    data = await anilist_calendary()
    json_creater(data)


run(main())
