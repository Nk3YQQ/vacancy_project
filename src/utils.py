import json
from typing import Any

from config import CSV_SAVER_PATH, JSON_SAVER_PATH
from src.funcs_for_save import open_csv_file, open_json_file


def make_salary(salary: dict) -> int:
    """
    Функция принимает словарь, берёт данные из блока "Зарплата" и преобразует в строку
    """
    if not salary:
        return 0
    if not salary["to"]:
        return int(salary["from"])
    elif not salary["from"]:
        return int(salary["to"])
    else:
        return round(int(salary["to"]) + int(salary["from"]) / 2)


def make_description(snippet: dict) -> str:
    if not snippet:
        return "Нет данных."
    if not snippet["requirement"]:
        return f"Обязанности: {snippet['responsibility']}"
    if not snippet["responsibility"]:
        return f"Требования: {snippet['requirement']}"
    else:
        return f"Требования: {snippet['requirement']}. Обязанности: {snippet['responsibility']}"


def reformat_description(text: str) -> str:
    """
    Функция преобразует строку с данными об описании
    """
    return "".join(text.split("\n•")[:6]) + "..." if text else "Описание отсутствует."


def convert_vacancies_to_list(vacancies: dict) -> Any:
    """
    Функция преобразует вакансии в список словарей, где каждый словарь состоит из 4-х ключей
    """
    list_of_vacancies: list = []
    if vacancies.get("items"):
        for vacancy in vacancies["items"]:
            format_vacancy = {
                "vacancy": vacancy["name"],
                "url": f"https://hh.ru/vacancy/{vacancy['id']}",
                "salary": make_salary(vacancy["salary"]),
                "description": make_description(vacancy["snippet"]),
            }
            list_of_vacancies.append(format_vacancy)
        return list_of_vacancies
    elif vacancies.get("objects"):
        for vacancy in vacancies["objects"]:
            vacancy["salary"] = {
                "from": vacancy["payment_from"],
                "to": vacancy["payment_to"],
                "currency": vacancy["currency"],
            }
            format_vacancy = {
                "vacancy": vacancy["profession"],
                "url": vacancy["link"],
                "salary": make_salary(vacancy["salary"]),
                "description": reformat_description(vacancy["candidat"]),
            }
            list_of_vacancies.append(format_vacancy)
        return list_of_vacancies


def get_vacancy_by_index(convert_top_vacancies: str, index: str) -> str:
    """
    Функция возвращает вакансию по её индексу в списке (на одну единицу меньше)
    """
    top_vacancies = json.loads(convert_top_vacancies)
    try:
        int_index = int(index)

    except ValueError:
        raise ValueError("Введённое значение не совпадает с целым числом.")

    else:
        if 0 < int_index and int_index > len(top_vacancies):
            return "Index error"

        top_vacancy = top_vacancies[int_index - 1]
        return json.dumps(top_vacancy, ensure_ascii=False, indent=4)


def concatenate_dicts(json_file: list, csv_file: list) -> str:
    """
    Функция проверяет словари с данными и соединяет их
    """
    if not json_file and not csv_file:
        return "В файлах ничего не найдено :("

    json_file.extend(csv_file)

    return json.dumps(json_file, ensure_ascii=False, indent=4)


def view_all_user_vacancy() -> str:
    """
    Функция показывает все вакансии, добавленные пользователем
    """
    json_vacancy = open_json_file(JSON_SAVER_PATH)
    csv_vacancy = open_csv_file(CSV_SAVER_PATH)

    all_vacancies = {"json_vacancy": json_vacancy, "csv_vacancy": csv_vacancy}

    return json.dumps(all_vacancies, ensure_ascii=False, indent=4)


def delete_vacancy(vacancies: dict, index: str) -> dict | str:
    """
    Функция удаляет вакансию из json/csv файла
    """
    try:
        int_index = int(index)

    except ValueError:
        raise ValueError("Введённое значение не совпадает с целым числом.")

    else:
        if 0 < int_index and int_index > len(vacancies):
            return "Index error"
        vacancies.pop(int_index - 1)
        return vacancies
