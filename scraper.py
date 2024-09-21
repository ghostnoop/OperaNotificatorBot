import asyncio

import aiohttp
import bs4

from config import config
from db import get_exists_posters
from models import Poster




async def scrape_theatre():
    url = f"{config.base_url}/playbill/"
    async with (aiohttp.ClientSession() as session):
        async with session.get(url) as resp:
            html = await resp.read()
            soup = bs4.BeautifulSoup(html, "html.parser")
            items = soup.find("div", {"class": "poster-container"}).find_all(
                "div", {"class": "poster-item"}
            )
            posters = []
            for item in items:
                available = item.find("a", {"class": "border-btn"})

                poster = Poster(
                    id=item.find("div", {"class": "poster-item__top"}).find("a").get("href"),
                    date=item.find("div", {"class": "poster-item__date"}).get_text().replace("\n"," ").replace("\t","").replace("  "," "),
                    title=item.find("a", {"class": "poster-item__info-name"}).text,
                    is_available=available.text == 'КУПИТЬ БИЛЕТ' if available else False,
                    image=config.base_url+item.find("div", {"class": "poster-item__top"}).find("img").get("src")
                )
                posters.append(poster)

            exists_posters = await get_exists_posters(posters)
            return [i for i in posters if i.id not in exists_posters and i.is_available]



