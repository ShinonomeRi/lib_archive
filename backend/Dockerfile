# 1. Базовый образ — берём лёгкий Python
FROM python:3.12-slim

# 2. Чтобы Python писал логи сразу в консоль, а не в буфер
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Делаем рабочую папку внутри контейнера
WORKDIR /app

# 4. Копируем зависимости
COPY requirements.txt .

# 5. Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# 6. Копируем исходный код
COPY app ./app

# 7. Запускаем FastAPI через uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
