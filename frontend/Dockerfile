FROM python:3.9-alpine

ENV APP_API_ENDPOINT localhost:8080

WORKDIR /app

COPY . /app/

RUN python /app/setup.py develop

ENTRYPOINT ["gunicorn", "webapp:app"]
CMD ["-b", "0.0.0.0:80"]
