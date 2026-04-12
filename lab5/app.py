def calculate_average_score(scores):
    if not scores:
        return 0
    return sum(scores) / len(scores)


def is_passed(avg_score):
    """
    Перевіряє, чи студент склав курс.

    >>> is_passed(60)
    True
    >>> is_passed(59)
    False
    """
    return avg_score >= 60


def main():
    scores = [75, 80, 90]
    avg = calculate_average_score(scores)
    passed = is_passed(avg)

    print(f"Середній бал: {avg}")
    print("Студент склав курс" if passed else "Студент не склав курс")


if __name__ == "__main__":
    main()
