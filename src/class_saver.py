import json
from abc import ABC, abstractmethod
from src.funcs_for_save import open_json_file, write_to_json_file, open_csv_file, write_to_csv_file

from config import JSON_PATH, CSV_SAVER_PATH, JSON_SAVER_PATH
from src.utils import delete_vacancy


class Saver(ABC):
    """
    Абстрактный класс для реализации классов, сохраняющих файл
    """

    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancies_by_salary(self, salary):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        pass


class JSONSaver(Saver):
    """
    Класс сохраняет файлы в формат json
    """

    def add_vacancy(self, vacancy):
        format_vacancy = json.loads(vacancy)
        vacancies = open_json_file(JSON_SAVER_PATH)
        vacancies.append(format_vacancy)
        write_to_json_file(JSON_SAVER_PATH, vacancies)

    def get_vacancies_by_salary(self, salary):
        vacancies = open_json_file(JSON_SAVER_PATH)
        sorted_vacancies = list(vacancy for vacancy in vacancies if vacancy['salary'] == salary)
        return sorted_vacancies

    def delete_vacancy(self, indicator):
        vacancies = open_json_file(JSON_SAVER_PATH)
        update_vacancies = delete_vacancy(vacancies, indicator)
        if update_vacancies == 'Index error':
            return 'Указанный индекс превышает количество вакансий в списке или меньше 0'
        write_to_json_file(JSON_SAVER_PATH, update_vacancies)


class CSVSaver(Saver):
    """
    Класс сохраняет файлы в формат csv
    """

    def add_vacancy(self, vacancy):
        format_vacancy = json.loads(vacancy)
        vacancies = open_csv_file(CSV_SAVER_PATH)
        vacancies.append(format_vacancy)
        write_to_csv_file(CSV_SAVER_PATH, vacancies)

    def get_vacancies_by_salary(self, salary):
        vacancies = open_csv_file(CSV_SAVER_PATH)
        sorted_vacancies = list(vacancy for vacancy in vacancies if vacancy['salary'] == salary)
        return sorted_vacancies

    def delete_vacancy(self, indicator):
        vacancies = open_csv_file(CSV_SAVER_PATH)
        update_vacancies = delete_vacancy(vacancies, indicator)
        if update_vacancies == 'Index error':
            return 'Указанный индекс превышает количество вакансий в списке или меньше 0'
        write_to_csv_file(CSV_SAVER_PATH, update_vacancies)
