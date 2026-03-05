

FROM gcc:13 AS builder

WORKDIR /app

COPY . .

RUN make



FROM debian:stable-slim

WORKDIR /app

COPY --from=builder /app/parking_app .

CMD ["./parking_app"]
