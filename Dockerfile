FROM python:3.9

WORKDIR /app

COPY main.py /app/
COPY gewinner.db /app/

RUN apt-get update && apt-get install -y \
    python3-tk \
    sqlite3 \
    && rm -rf /var/lib/apt/lists/*

CMD ["python", "./main.py"]