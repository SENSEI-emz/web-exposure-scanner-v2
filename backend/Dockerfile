FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    chromium-browser \
    chromium-common \
    libcurl4 \
    libssl3 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p logs screenshots reports

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
