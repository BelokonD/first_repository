Для створення та активування віртуального оточення:

py -m venv venv --without-pip
source venv/Scripts/activate

---------------------------------------------------------------

Для main.py:

Встановити бібліотеку requests
pip install requests

Запуск програми
python main.py

Програма виконує GET-запит до https://api.github.com
та виводить статус-код, заголовки та JSON-відповідь.

---------------------------------------------------------------

Встановлення залежностей:

Створити віртуальне оточення
python -m venv venv

Активувати його
venv/Scripts/activate

Встановити залежності
pip install -r requirements.txt
