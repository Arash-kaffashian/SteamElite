FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# system deps (کم تغییر)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# dockerize (کم تغییر)
RUN curl -L https://github.com/jwilder/dockerize/releases/download/v0.6.1/dockerize-linux-amd64-v0.6.1.tar.gz \
    | tar -C /usr/local/bin -xzvf -

# فقط dependencyها
COPY requirements.txt .

# pip با cache
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --upgrade pip && \
    pip install -r requirements.txt

# بعداً کد پروژه
COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
