# FROM python:3.9-slim
# WORKDIR /app
# COPY . /app/
# RUN pip install -r requirements.txt
# CMD ["python","app.py"]

FROM python:3.9-slim
WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

COPY . /app/
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "app.py"]