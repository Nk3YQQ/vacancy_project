from src.class_convert_vacancy import ConvertVacancy
from src.class_filtered_vacancies import FilteredVacancy
from src.class_with_api import HeadHunterAPI, SuperJobAPI
from src.class_with_vacancy import Vacancy


def test_ConvertVacancy() -> None:
    convector = ConvertVacancy()

    filter_words_1 = ["python", "django", "flask", "postgresql"]
    filter_words_2: list = []

    hh_api = HeadHunterAPI()
    superjob_api = SuperJobAPI()

    hh_api.get_vacancies("Python")
    superjob_api.get_vacancies("Python")

    filtered_vacancies = FilteredVacancy()
    filtered_vacancies.filter_vacancies(filter_words_1)

    convector.convert_to_object(filtered_vacancies.filtered_vacancies_list)

    convert_vacancies = Vacancy.vacancies

    assert len(convert_vacancies) != 0

    top_vacancies = Vacancy.get_top_vacancies(5)
    convert_top_vacancies = convector.convert_to_json(top_vacancies)

    assert isinstance(convert_top_vacancies, str) is True

    filtered_vacancies.filter_vacancies(filter_words_2)

    convector.convert_to_object(filtered_vacancies.filtered_vacancies_list)

    assert len(convert_vacancies) != 0
