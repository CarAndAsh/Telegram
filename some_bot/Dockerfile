FROM python:3.13.5-slim-bookworm
WORKDIR /image_bot
COPY . .
RUN pip install uv

RUN uv sync
CMD uv run pic_bot.py