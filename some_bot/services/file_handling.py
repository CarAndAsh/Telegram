import os
import sys
from re import findall

from log_config import logger

BOOK_PATH = './book/Несломленный.txt'
PAGE_SIZE = 1050
SIGNS = '!?;:.,'
book: dict[int, str] = dict()


# def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
#     end_signs = ',.!:;?'
#     counter = 0
#     if len(text) < start + size:
#         size = len(text) - start
#         text = text[start:start + size]
#     else:
#         if text[start + size] == '.' and text[start + size - 1] in end_signs:
#             text = text[start:start + size - 2]
#             size -= 2
#         else:
#             text = text[start:start + size]
#         for i in range(size - 1, 0, -1):
#             if text[i] in end_signs:
#                 break
#             counter = size - i
#     page_text = text[:size - counter]
#     page_size = size - counter
#     return page_text, page_size
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    words = findall('[\s]*.+?[!?;:.,]{1,}', text[start:])
    res = ''
    word = words.pop(0) if words else None
    while word and (len(res + word) <= size):
        res += word
        word = words.pop(0) if words else None
    return res, len(res)


def prepare_book(path: str):
    page_num = 1
    cursor = 0
    with open(path, 'r', encoding='utf-8') as file:
        text = file.read()
    while cursor < len(text):
        page, page_size = _get_part_text(text, cursor, PAGE_SIZE)
        cursor += page_size
        book[page_num] = page.strip()
        logger.info(f'{book[page_num]}')
        page_num += 1


prepare_book(BOOK_PATH)
logger.info(f'{book}')
