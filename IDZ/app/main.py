import sentry_sdk

sentry_sdk.init(
    dsn="https://46d1b52057bebf1935b14e32e57f2916@o4511285617950720.ingest.de.sentry.io/4511326804443216",
    traces_sample_rate=1.0,
)


def calculate_total(prices: list[float]) -> float:
    if any(price < 0 for price in prices):
        raise ValueError("Ціна не може бути від'ємною")

    return sum(prices)


def main() -> None:
    try:
        user_input = input("Введіть ціни товарів через пробіл: ")
        prices = list(map(float, user_input.split()))
        total = calculate_total(prices)
        print(f"Загальна сума: {total}")
    except ValueError as e:
        print(f"Помилка: {e}")
        raise


if __name__ == "__main__":
    main()
