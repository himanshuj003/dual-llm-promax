FROM python:3.11-slim

WORKDIR /app

# System deps for some packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY dual_llm_promax.py .
COPY .env.example .

EXPOSE 7860

# Environment variables should be passed at runtime
CMD ["python", "dual_llm_promax.py"]
