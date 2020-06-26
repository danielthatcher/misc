FROM golang:latest
RUN mkdir /app
WORKDIR /app
COPY ./main.go /app/main.go
EXPOSE 80
ENTRYPOINT go run main.go -listen 0.0.0.0:80
