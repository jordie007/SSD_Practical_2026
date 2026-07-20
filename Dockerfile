# Dockerfile
FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y git && \
    rm -rf /var/lib/apt/lists/*

RUN git config --global user.name "LimShangWeiBryan" && \
    git config --global user.email "bryanlimshangwei@gmail.com"

COPY web/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY web/ .

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
