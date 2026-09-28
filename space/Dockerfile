FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY extract_app.py app.py.gz.b64.part1 app.py.gz.b64.part2 ./
RUN python extract_app.py

ENV GRADIO_SERVER_NAME=0.0.0.0
ENV GRADIO_SERVER_PORT=7860
EXPOSE 7860

CMD ["python", "app.py"]
