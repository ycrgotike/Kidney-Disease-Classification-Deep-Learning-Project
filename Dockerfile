FROM python:3.11-slim-buster

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip && \
    pip install -r requirements.txt --break-system-packages

CMD ["python3", "app.py"]