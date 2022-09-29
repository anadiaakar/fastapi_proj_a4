FROM python:3.9

RUN pip install --ignore-installed fastapi uvicorn poetry wheel virtualenv

EXPOSE 8000

WORKDIR /project

ENV PORT 8000
ENV HOST "0.0.0.0"

ENV PATH="/venv/bin:$PATH"

COPY ./db /project/db
COPY ./pyproject.toml /project/
COPY ./main.py /project/


RUN poetry config virtualenvs.create false \
  && poetry install

CMD ["uvicorn", "main:app", "--host", "0.0.0.0" ,"--port", "80" ]
