FROM golang:1.16-alpine

RUN mkdir /app

COPY . /app

WORKDIR /app/src

COPY go.mod ./

RUN go mod download

RUN go get -d github.com/gorilla/mux

RUN go get -u gorm.io/driver/sqlite

RUN go get -u gorm.io/gorm

RUN go build -o main .

EXPOSE 8080

CMD ["/app/src/main"]
