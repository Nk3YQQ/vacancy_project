import json

from config import JSON_PATH
from src.class_with_api import HeadHunterAPI, SuperJobAPI


def test_HeadHunterAPI() -> None:
    hh_api = HeadHunterAPI()

    hh_api.get_vacancies("Python")

    with open(JSON_PATH, "r", encoding="utf-8") as file:
        vacancies = json.load(file)
        assert isinstance(vacancies, list) is True
        assert len(vacancies) != 0

    hh_vacancies = hh_api.get_vacancies(1)
    assert hh_vacancies == "Неверный ввод! Текст должен быть в виде строки."

    hh_api.get_vacancies("dldlldldlldldlld")
    with open(JSON_PATH, "r", encoding="utf-8") as file:
        vacancies = json.load(file)
        assert isinstance(vacancies, list) is True
        assert len(vacancies) == 0


def test_SuperJobAPI() -> None:
    hh_api = HeadHunterAPI()
    superjob_api = SuperJobAPI()

    hh_api.get_vacancies("Python")
    superjob_api.get_vacancies("Python")

    with open(JSON_PATH, "r", encoding="utf-8") as file:
        vacancies = json.load(file)
        assert isinstance(vacancies, list) is True
        assert len(vacancies) != 0

    superjob_vacancies = superjob_api.get_vacancies(1)
    assert superjob_vacancies == "Неверный ввод! Текст должен быть в виде строки."

    superjob_api.get_vacancies("dldlldldlldldlld")
    with open(JSON_PATH, "r", encoding="utf-8") as file:
        vacancies = json.load(file)
        assert isinstance(vacancies, list) is True
        assert len(vacancies) != 0
