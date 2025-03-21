FROM python:3.9-slim-buster

WORKDIR /app

EXPOSE 5000
RUN pip install flask sqlalchemy
COPY . /app
CMD ["python3", "da.py"]
