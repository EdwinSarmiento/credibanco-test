
FROM python:3.8-slim-bookworm

WORKDIR /app

COPY web.py .
COPY requirements.txt . 

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "web.py"]