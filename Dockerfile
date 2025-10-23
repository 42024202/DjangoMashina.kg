FROM python:3.12-slim

WORKDIR /app

ARG UID=1000
ARG GID=1000
RUN addgroup --gid $GID appgroup && \
    adduser --disabled-password --gecos "" --uid $UID --gid $GID appuser

# Устанавливаем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем проект
COPY . .

# Меняем владельца папки
RUN chown -R appuser:appgroup /app

# Переходим на нового пользователя
USER appuser

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

