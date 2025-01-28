FROM python:3.10
RUN pip install poetry
WORKDIR /bot
COPY poetry.lock pyproject.toml /bot/
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi
COPY . /bot
CMD python bot.py