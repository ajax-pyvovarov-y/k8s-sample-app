FROM python:3.11.6-alpine3.18

RUN pip3 install Flask==3.0.0

WORKDIR /app
COPY app.py /app/

CMD flask --app app run -h 0.0.0.0 -p 5000
