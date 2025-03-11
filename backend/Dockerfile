FROM python:3.11-slim
LABEL authors="Maxim Koltsov"

RUN apt install tzdata
ENV TZ=Europe/Moscow

WORKDIR app
COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

CMD ["python", "api.py"]
