run:
	python app/main.py

test:
	pytest --doctest-modules app/

format:
	black app tests
	flake8 app tests

security:
	bandit -r app

all: format test security
