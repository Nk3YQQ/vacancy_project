import json
from typing import Any

from src.class_with_vacancy import Vacancy


class ConvertVacancy:
    """
    Класс конвертирует данные из формиата json в объект класса Vacancy и наоборот
    """

    @staticmethod
    def convert_to_object(vacancies: Any) -> None:
        """
        Метод создаёт экземпляр из вакансий и добавляет вакансии в список класса Vacancy
        """
        for vacancy in vacancies:
            object_vacancy = Vacancy(vacancy["vacancy"], vacancy["url"], vacancy["salary"], vacancy["description"])
            Vacancy.append_vacancy(object_vacancy)

    @staticmethod
    def convert_to_json(vacancies: list[Vacancy]) -> str:
        """
        Метод конвертирует экземпляры класса Vacancy в json-файл
        """
        json_list = []

        for vacancy in vacancies:
            json_vacancy = {
                "vacancy": vacancy.vacancy_name,
                "url": vacancy.vacancy_url,
                "salary": vacancy.salary,
                "description": vacancy.description,
            }
            json_list.append(json_vacancy)

        return json.dumps(json_list, ensure_ascii=False, indent=4)
