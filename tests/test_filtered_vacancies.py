from src.class_filtered_vacancies import FilteredVacancy
from src.class_with_api import HeadHunterAPI, SuperJobAPI


def test_FilteredVacancy() -> None:
    filter_words_1 = ["python", "django", "flask", "postgresql"]
    filter_words_2: list = []

    hh_api = HeadHunterAPI()
    superjob_api = SuperJobAPI()

    hh_api.get_vacancies("Python")
    superjob_api.get_vacancies("Python")

    filtered_vacancies = FilteredVacancy()
    filtered_vacancies.filter_vacancies(filter_words_1)

    assert len(filtered_vacancies.filtered_vacancies_list) != 0

    filtered_vacancies.filter_vacancies(filter_words_2)

    assert len(filtered_vacancies.filtered_vacancies_list) != 0
