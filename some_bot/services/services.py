import PIL
from aiogram import Bot
from log_cofig import logger


def edit_image(image_id: str, operation_id: int):
    match operation_id:
        case 1:
            logger.info(f'1')
            return image_id
        case 2:
            logger.info('2')
            return image_id
        case 3:
            logger.info('3')
            return image_id
        case 4:
            logger.info('4')
            return image_id
        case 5:
            logger.info('5')
            return image_id
