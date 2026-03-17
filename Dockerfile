FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY code/ ./code/

ENV PYTHONPATH=/app

CMD ["streamlit", "run", "code/main.py", "--server.port=8501"]
