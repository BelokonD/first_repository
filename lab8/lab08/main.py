import sentry_sdk
from dotenv import load_dotenv
import os

load_dotenv()

SENTRY_DSN = os.getenv("SENTRY_DSN")

sentry_sdk.init(
    dsn="https://7c77284408705c7726fdc3f7b8e0d88a@o4511285617950720.ingest.de.sentry.io/4511285637808208",
    traces_sample_rate=1.0
)


def analyze_log(log_data: str) -> int:
    if not log_data.strip():
        raise ValueError("Помилка: введено порожній рядок")

    return len(log_data)


def main():
    try:
        user_input = input("Введіть лог для аналізу: ")
        count = analyze_log(user_input)
        print(f"Кількість символів: {count}")

    except Exception as e:
        sentry_sdk.capture_exception(e)
        print(f"Сталася помилка: {e}")


if __name__ == "__main__":
    main()
