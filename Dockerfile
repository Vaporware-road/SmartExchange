FROM node:20-bookworm-slim AS node-runtime

FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=MrExchangePanel.settings

WORKDIR /app

# Reuse Node runtime files from official image to avoid extra apt downloads.
COPY --from=node-runtime /usr/local/bin/node /usr/local/bin/node
COPY --from=node-runtime /usr/local/lib/node_modules /usr/local/lib/node_modules
RUN ln -sf /usr/local/lib/node_modules/npm/bin/npm-cli.js /usr/local/bin/npm \
    && ln -sf /usr/local/lib/node_modules/npm/bin/npx-cli.js /usr/local/bin/npx

COPY backend/requirements.txt /app/backend/requirements.txt
RUN pip install --no-cache-dir -r /app/backend/requirements.txt \
    && pip install --no-cache-dir supervisor

COPY frontend/package*.json /app/frontend/
RUN cd /app/frontend && npm ci

COPY backend/ /app/backend/
COPY frontend/ /app/frontend/

RUN mkdir -p /app/backend/public/media /app/backend/public/staticfiles /app/backend/data

COPY docker/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

EXPOSE 8000 5173
