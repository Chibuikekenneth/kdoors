FROM python:3.9-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app

RUN pip3 install -r requirements.txt --no-cache-dir

COPY  . /app

ENV FLASK_ENV=development
RUN export DATABASE_URL=postgresql://kiwi:test123@localhost:5432/kiwi
ENTRYPOINT [ "python" ]
CMD ["run.py"]