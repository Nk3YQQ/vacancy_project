import re

from config import JSON_PATH
from src.funcs_for_save import open_json_file


class FilteredVacancy:
    """
    Класс реализует поиск вакансий по ключевым словам, которые находятся в описании вакансии
    """

    def __init__(self) -> None:
        self.filtered_vacancies_list: list = []

    def filter_vacancies(self, filter_words: list[str]) -> None:
        """
        Метод ищет вакансии, полученные из API HeadHunter и SuperJob по ключевым словам
        """
        vacancies = open_json_file(JSON_PATH)

        if not filter_words:
            for vacancy in vacancies:
                self.filtered_vacancies_list.append(vacancy)

        else:
            for vacancy in vacancies:
                description = vacancy.get("description", "").lower()
                if any(re.search(keyword.lower(), description, re.IGNORECASE) for keyword in filter_words):
                    self.filtered_vacancies_list.append(vacancy)
