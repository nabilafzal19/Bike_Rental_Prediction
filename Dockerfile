FROM python:3.14-slim AS base

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app
COPY models ./models


FROM base AS test

RUN pip install --no-cache-dir pytest

COPY tests ./tests

CMD ["python", "-m", "pytest", "-v"]


FROM base AS production

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]