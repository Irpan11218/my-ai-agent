FROM python:3.12-slim

WORKDIR /app

# system deps
RUN apt-get update && apt-get install -y --no-install-recommends build-essential && rm -rf /var/lib/apt/lists/*

# copy requirements first for caching
COPY requirements.txt .
RUN python3 -m pip install --upgrade pip && pip install -r requirements.txt

# copy project
COPY . .

ENV PYTHONUNBUFFERED=1

# Expose port
EXPOSE 5000

# Use gunicorn to run the Flask app
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:5000", "--workers", "1", "--threads", "4"]
