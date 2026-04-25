FROM python:3.14-slim

WORKDIR /app

COPY requirements.txt .
RUN python -m pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "backend_service_capstone:create_app", "--factory", "--host", "0.0.0.0", "--port", "8000"]
