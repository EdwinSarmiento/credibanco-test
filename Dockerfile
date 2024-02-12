
FROM python:3.8-slim-bookworm

WORKDIR /app

COPY web.py /app

RUN pip install flask

CMD ["python", "web.py"]