FROM python:3.8.7-slim-buster

COPY requirements.txt /

RUN pip3 install -r /requirements.txt

COPY . /app

CMD ["python", "/app/main.py"]