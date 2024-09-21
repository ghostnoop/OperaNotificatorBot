from config import config
from models import Poster


def escape_markdown(text: str) -> str:
    # Escape special characters in MarkdownV2
    escape_chars = ['_', '*', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!']
    for char in escape_chars:
        text = text.replace(char, f'\\{char}')
    return text


def poster_message(poster: Poster):
    link = f"[КУПИТЬ БИЛЕТЫ]({config.base_url}{poster.id})"
    text = f"""***{poster.title}***
*{poster.date}*

{link}
    """
    return escape_markdown(text)
