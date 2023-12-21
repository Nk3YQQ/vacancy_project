import random

import pytest

from config import CSV_SAVER_PATH, JSON_SAVER_PATH
from src.class_convert_vacancy import ConvertVacancy
from src.class_filtered_vacancies import FilteredVacancy
from src.class_saver import CSVSaver, JSONSaver
from src.class_with_api import HeadHunterAPI, SuperJobAPI
from src.class_with_vacancy import Vacancy
from src.funcs_for_save import open_csv_file, open_json_file
from src.utils import get_vacancy_by_index


@pytest.fixture
def convert_top_vacancies() -> str:
    hh_api = HeadHunterAPI()
    superjob_api = SuperJobAPI()

    hh_api.get_vacancies("Python")
    superjob_api.get_vacancies("Python")

    filter_words_1 = ["python", "django", "flask", "postgresql"]

    filtered_vacancies = FilteredVacancy()
    filtered_vacancies.filter_vacancies(filter_words_1)

    convector = ConvertVacancy()
    convector.convert_to_object(filtered_vacancies.filtered_vacancies_list)

    top_vacancies = Vacancy.get_top_vacancies(5)

    return convector.convert_to_json(top_vacancies)


def test_JSONSaver(convert_top_vacancies: str) -> None:
    top = get_vacancy_by_index(convert_top_vacancies, "1")

    assert isinstance(top, str) is True

    json_saver = JSONSaver()

    json_saver.add_vacancy(top)

    json_salary = json_saver.get_vacancies_by_salary(160000)

    assert len(json_salary) >= 0

    vacancies_len = len(open_json_file(JSON_SAVER_PATH))

    random_num = random.randint(1, vacancies_len)

    json_saver.delete_vacancy(random_num)

    new_vacancies = open_json_file(JSON_SAVER_PATH)
    assert len(new_vacancies) == vacancies_len - 1


def test_CSVSaver(convert_top_vacancies: str) -> None:
    top = get_vacancy_by_index(convert_top_vacancies, "1")

    assert isinstance(top, str) is True

    csv_saver = CSVSaver()

    csv_saver.add_vacancy(top)

    csv_salary = csv_saver.get_vacancies_by_salary(650000)

    assert len(csv_salary) >= 0

    vacancies_len = len(open_csv_file(CSV_SAVER_PATH))

    random_num = random.randint(1, vacancies_len)

    csv_saver.delete_vacancy(random_num)

    new_vacancies = open_csv_file(CSV_SAVER_PATH)
    assert len(new_vacancies) == vacancies_len - 1
