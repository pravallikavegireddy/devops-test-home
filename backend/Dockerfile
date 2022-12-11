FROM golang:1.16-alpine3.13

RUN mkdir /app

WORKDIR /app

COPY . /app

RUN go build -o main .

EXPOSE 8080

CMD ["/app/main"]
