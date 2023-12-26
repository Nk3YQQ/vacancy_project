from typing import Any


class Vacancy:
    """
    Класс, предназначенный для работы с вакансиями
    """

    vacancies: list = []

    def __init__(self, vacancy_name: str, vacancy_url: str, salary: int, description: str) -> None:
        self._vacancy_name = vacancy_name
        self._vacancy_url = vacancy_url
        self._salary = salary
        self._description = description

    def __repr__(self) -> str:
        return f"Vacancy({self.vacancy_name}, {self.vacancy_url}, {self.salary}, {self.description})"

    def __gt__(self, other: Any) -> bool:
        return int(self._salary) > int(other.salary)

    def __ge__(self, other: Any) -> bool:
        return int(self._salary) >= int(other.salary)

    def __lt__(self, other: Any) -> bool:
        return int(self._salary) < int(other.salary)

    def __le__(self, other: Any) -> bool:
        return int(self._salary) <= int(other.salary)

    def __eq__(self, other: Any) -> bool:
        return int(self._salary) == int(other.salary)

    @property
    def vacancy_name(self) -> str:
        return self._vacancy_name

    @property
    def vacancy_url(self) -> str:
        return self._vacancy_url

    @property
    def salary(self) -> int:
        return self._salary

    @property
    def description(self) -> str:
        return self._description

    @classmethod
    def append_vacancy(cls, vacancy: Any) -> None:
        cls.vacancies.append(vacancy)

    @classmethod
    def get_top_vacancies(cls, top_n: int) -> list:
        """
        Метод возвращает топ вакансии по заданному числу
        """
        top_n_list = []
        sorted_vacancies = sorted(cls.vacancies, key=lambda x: x.salary, reverse=True)
        for vacancy in sorted_vacancies[:top_n]:
            top_n_list.append(vacancy)
        return top_n_list
