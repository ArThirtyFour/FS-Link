FROM python:3.9-slim-buster

WORKDIR /app

EXPOSE 5000
RUN pip install flask
COPY . /app
CMD ["python3", "da.py"]
