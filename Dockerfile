
FROM python:3.9

WORKDIR /app

ADD main.py .

CMD ["python", "./main.py"]