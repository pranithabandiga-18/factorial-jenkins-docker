FROM python:3.12-slim

WORKDIR /app
COPY factorial.py .

ENTRYPOINT ["python", "/app/factorial.py"]
CMD ["5"]
