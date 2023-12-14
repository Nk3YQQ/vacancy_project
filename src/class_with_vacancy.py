from abc import ABC, abstractmethod
from typing import Any


class ParseVacancy(ABC):
    @abstractmethod
    def parse_vacancies(self, raw_date: list[dict]) -> None:
        pass


class ParseHeadHunterVacancy(ParseVacancy):
    """
    Класс предназначен для парсинга данных, полученных в результате поиска в SuperJob
    """

    def parse_vacancies(self, raw_date: Any) -> Any:
        vacancies: list = []
        for item in raw_date['items']:
            vacancy_info = {
                "vacancy": item['name'],
                "url": f"https://hh.ru/vacancy/{item['id']}",
                "salary": item['salary'],
                "description": item['snippet']
            }
            vacancies.append(vacancy_info)
        return vacancies


class ParseSuperJobVacancy(ParseVacancy):
    """
    Класс предназначен для парсинга данных, полученных в результате поиска в HeadHunter
    """

    def parse_vacancies(self, raw_date: Any) -> Any:
        vacancies: list = []
        for item in raw_date['objects']:
            vacancy_info = {
                "vacancy": item['profession'],
                "url": item['link'],
                "salary": {'from': item['payment_from'], 'to': item['payment_to'], 'currency': item['currency'],
                           'gross': item['moveable']},
                "description": item['candidat']
            }
            vacancies.append(vacancy_info)
        return vacancies


class Vacancy:
    """
    Класс, предназначенный для работы с вакансиями
    """

    def __init__(self, vacancy: str, url: str, salary: int, description: str):
        self.vacancy = vacancy
        self.url = url
        self.salary = salary
        self.description = description

    def __gt__(self, other: Any) -> bool:
        return int(self.salary) > int(other.salary)

    def __ge__(self, other: Any) -> bool:
        return int(self.salary) >= int(other.salary)

    def __lt__(self, other: Any) -> bool:
        return int(self.salary) < int(other.salary)

    def __le__(self, other: Any) -> bool:
        return int(self.salary) <= int(other.salary)

    def __eq__(self, other: Any) -> bool:
        return int(self.salary) == int(other.salary)
