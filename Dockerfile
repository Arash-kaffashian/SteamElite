# Dockerfile
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install dockerize (برای انتظار سرویس‌ها)
RUN curl -L https://github.com/jwilder/dockerize/releases/download/v0.6.1/dockerize-linux-amd64-v0.6.1.tar.gz \
    | tar -C /usr/local/bin -xzvf -

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project
COPY . .

# Collect static files (اختیاری)
# RUN python manage.py collectstatic --noinput

# Default CMD (می‌توان در docker-compose override کرد)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
