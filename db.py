from typing import List

import aiosqlite

from config import config
from models import Poster


async def db_init():
    async with aiosqlite.connect(config.db_name) as db:
        await db.execute("""CREATE TABLE IF NOT EXISTS Poster (
                            id TEXT PRIMARY KEY
                        );""")
        await db.commit()


async def add_poster(poster: Poster):
    async with aiosqlite.connect(config.db_name) as db:
        await db.execute("INSERT INTO Poster (id) VALUES (?)", (poster.id,))
        await db.commit()


async def get_exists_posters(posters: List[Poster]):
    results = set()
    async with aiosqlite.connect(config.db_name) as db:
        query = f"SELECT id FROM Poster WHERE id IN ({','.join(['?'] * len(posters))})"
        async with db.execute(query, [i.id for i in posters]) as cursor:
            rows = await cursor.fetchall()
            for row in rows:
                results.add(row[0])
    return results
