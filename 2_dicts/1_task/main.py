import os
from decimal import Decimal

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SPLIT_SYMBOL = '\n'


def read_file(path: str) -> str:
    with open(path, 'r') as file:
        file_article = file.read()
    return file_article


def get_employees_info() -> list[str]:
    return read_file(os.path.join(
        BASE_DIR, '1_task', 'input_data.txt',
    )).split(SPLIT_SYMBOL)


def get_parsed_employees_info() -> list[dict[str, int | str]]:
    employee_lines = get_employees_info()
    parsed_employees_info = []

    valid_keys = {'id', 'name', 'last_name', 'age', 'salary', 'position'}

    for line in employee_lines:
        words = line.split()
        employee_info = {}

        for i in range(0, len(words), 2):
            key = words[i]
            value = words[i + 1]

            if key in valid_keys:
                if key == 'id':
                    employee_info[key] = int(value)
                elif key == 'age':
                    employee_info[key] = int(value)
                elif key == 'salary':
                    employee_info[key] = Decimal(value)
                else:
                    employee_info[key] = value

        parsed_employees_info.append(employee_info)
    return parsed_employees_info
