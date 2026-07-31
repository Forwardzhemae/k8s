FROM python:3.11-slim

RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir \
    fastapi \
    uvicorn \
    redis \
    sqlalchemy \
    asyncpg \
    python-dotenv \
    authx \
    pydantic

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]