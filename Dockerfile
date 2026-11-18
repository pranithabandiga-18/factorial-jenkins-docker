FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
RUN adduser --disabled-password --gecos "" --uid 10001 appuser
COPY --chown=appuser:appuser factorial.py /app/factorial.py

USER appuser
ENTRYPOINT ["python", "/app/factorial.py"]
CMD ["5"]
