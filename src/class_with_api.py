import json
import os
from abc import ABC, abstractmethod
from typing import Any

from config import JSON_PATH
from src.funcs_for_save import write_to_json_file, open_json_file

import requests
from dotenv import load_dotenv

from src.utils import convert_vacancies_to_list

load_dotenv()


class SearchVacancy(ABC):
    """
    Класс является абстрактным для работы с API сайтов с вакансиями
    """

    @abstractmethod
    def get_vacancies(self, text: str) -> None:
        pass


class HeadHunterAPI(SearchVacancy):
    """
    Класс-потомок для работы с API HeadHunter
    """

    def get_vacancies(self, text: Any) -> Any:
        """
        Метод принимает информацию из API HeadHunter и преобразует в список словарей для сохранения в json-файл
        """
        if not isinstance(text, str):
            return "Неверный ввод! Текст должен быть в виде строки."
        url = f"https://api.hh.ru/vacancies?text={text}&per_page=100"
        response = requests.get(url)
        vacancies = json.loads(response.content)
        headhunter_vacancies = convert_vacancies_to_list(vacancies)
        if not headhunter_vacancies:
            headhunter_vacancies = []
        write_to_json_file(JSON_PATH, headhunter_vacancies)


class SuperJobAPI(SearchVacancy):
    """
    Класс-потомок для работы с API SuperJob
    """

    def get_vacancies(self, text: Any) -> Any:
        """
        Метод принимает информацию из API SuperJob и преобразует в список словарей для сохранения в json-файл
        """
        if not isinstance(text, str):
            return "Неверный ввод! Текст должен быть в виде строки."
        url = f"https://api.superjob.ru/2.0/vacancies/?keywords={text}&count=100"
        response = requests.get(url, headers={"X-Api-App-Id": os.getenv("SUPERJOB_API")})
        vacancies = json.loads(response.content)
        headhunter_vacancies = open_json_file(JSON_PATH)
        superjob_vacancies = convert_vacancies_to_list(vacancies)
        if not superjob_vacancies:
            superjob_vacancies = []
        headhunter_vacancies.extend(superjob_vacancies)
        write_to_json_file(JSON_PATH, headhunter_vacancies)
