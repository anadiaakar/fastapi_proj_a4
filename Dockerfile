FROM python:3.9

RUN pip install --ignore-installed fastapi uvicorn poetry wheel virtualenv

EXPOSE 8000

WORKDIR /projectname

ENV PORT 8000
ENV HOST "0.0.0.0"

ENV PATH="/venv/bin:$PATH"

COPY ./project /code/project
COPY ./pyproject.toml /projectname

RUN poetry config virtualenvs.create false \
  && poetry install

CMD ["uvicorn", "main:app"]

