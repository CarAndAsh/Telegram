from io import BytesIO

from PIL import Image

from log_config import logger

operations = {
    'mirror h': lambda x: x.transpose(Image.Transpose.FLIP_TOP_BOTTOM),
    'mirror v': lambda x: x.transpose(Image.Transpose.FLIP_LEFT_RIGHT),
    'rotate h': lambda x: x.transpose(Image.Transpose.ROTATE_90),
    'rotate -h': lambda x: x.transpose(Image.Transpose.ROTATE_270),
    'switch scheme': lambda x: x.convert('CMYK') if x.mode == 'RGB' else x.convert('RGB')
}


def edit_image(image_file: BytesIO, operation: str):
    logger.info(f'бот получил файл для {operation}')
    with Image.open(image_file) as image:
        image.load()
    edited_image = operations[operation](image)

    image_file.seek(0)
    edited_image.save(image_file, image.format, mode=image.mode)
