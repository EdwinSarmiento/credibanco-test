
FROM python:3.8-slim-bookworm

WORKDIR /app

COPY web.py .

RUN pip install flask

CMD ["python", "web.py"]