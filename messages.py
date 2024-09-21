from config import config
from models import Poster


def poster_message(poster: Poster):
    link = f"[КУПИТЬ БИЛЕТЫ]({config.base_url}{poster.id})"
    return f"""***{poster.title}***
*{poster.date}*

{link}
    """
