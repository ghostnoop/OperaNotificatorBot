import asyncio

from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

import db
import messages
from config import config
import scraper


async def bot_starter():
    await db.db_init()

    bot = Bot(token=config.token, default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN_V2))
    while True:
        posters = await scraper.scrape_theatre()
        for poster in posters:
            await bot.send_photo(chat_id=config.chat_id, photo=poster.image,
                                 caption=messages.poster_message(poster))
            # return
            await db.add_poster(poster)
        await asyncio.sleep(30)


if __name__ == '__main__':
    asyncio.run(bot_starter())
