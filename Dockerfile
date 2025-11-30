FROM python:3.8-slim

WORKDIR /app

COPY kata_app.py /app
COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 6000
CMD ["python", "kata_app.py"]
