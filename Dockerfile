# Dockerfile
FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y git && \
    rm -rf /var/lib/apt/lists/*

# Use --system so the config applies to all users (including the
# non-root user below), since /etc/gitconfig is world-readable.
RUN git config --system user.name "LimShangWeiBryan" && \
    git config --system user.email "bryanlimshangwei@gmail.com"

COPY web/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY web/ .

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh && useradd --create-home --uid 1000 --shell /usr/sbin/nologin appuser && \
    chown -R appuser:appuser /app /entrypoint.sh
    
# Create a dedicated non-root user and hand over ownership of the
# app directory (entrypoint.sh runs `git init`/`git commit` here,
# so it needs write access) and the entrypoint script itself.

USER appuser

ENTRYPOINT ["/entrypoint.sh"]