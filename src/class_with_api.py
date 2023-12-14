import json
import os
from abc import ABC, abstractmethod
from typing import Any

import requests
from dotenv import load_dotenv

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
        if not isinstance(text, str):
            return "Неверный ввод! Текст должен быть в виде строки."
        url = f"https://api.hh.ru/vacancies?text={text}&per_page=10"
        response = requests.get(url)
        response_data = json.loads(response.content)
        if not response_data["items"]:
            return "По вашему запросу ничего не было найдено."
        return response_data


class SuperJobAPI(SearchVacancy):
    """
    Класс-потомок для работы с API SuperJob
    """

    def get_vacancies(self, text: Any) -> Any:
        if not isinstance(text, str):
            return "Неверный ввод! Текст должен быть в виде строки."
        url = f"https://api.superjob.ru/2.0/vacancies/?keyword={text}&count=10&page=1"
        response = requests.get(url, headers={"X-Api-App-Id": os.getenv("SUPERJOB_API")})
        response_data = json.loads(response.content)
        if not response_data["objects"]:
            return "По вашему запросу ничего не было найдено."
        return response_data
