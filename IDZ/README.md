# Додаток для підрахунку суми покупок

Програма обчислює загальну суму покупок за введеними цінами товарів.

## Запуск

```bash
make run  /  python app/main.py

##Тести

```bash
make test  /  py -m pytest

##Форматування

```bash
make format  /  py -m black app tests

##Перевірка безпеки

```bash
make security  /  py -m bandit -r app

##Githooks

```bash
pre-commit install
