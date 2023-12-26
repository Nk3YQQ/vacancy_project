import pytest

from src.class_with_vacancy import Vacancy


@pytest.fixture
def vacancy_1() -> Vacancy:
    return Vacancy("Программист Java", "https://hh.ru/vacancy/90670156", 160000, "Описание вакансии 1")


@pytest.fixture
def vacancy_2() -> Vacancy:
    return Vacancy(
        "Android Developer (Middle / Senior) (Ташкент)",
        "https://hh.ru/vacancy/90892946",
        20000000,
        "Описание вакансии 2",
    )


def test_Vacancy(vacancy_1: Vacancy, vacancy_2: Vacancy) -> None:
    assert vacancy_1.vacancy_name == "Программист Java"
    assert vacancy_1.vacancy_url == "https://hh.ru/vacancy/90670156"
    assert vacancy_1.salary == 160000
    assert vacancy_1.description == "Описание вакансии 1"

    assert vacancy_2.vacancy_name == "Android Developer (Middle / Senior) (Ташкент)"
    assert vacancy_2.vacancy_url == "https://hh.ru/vacancy/90892946"
    assert vacancy_2.salary == 20000000
    assert vacancy_2.description == "Описание вакансии 2"

    assert (
        repr(vacancy_1) == "Vacancy(Программист Java, https://hh.ru/vacancy/90670156, 160000, Описание " "вакансии 1)"
    )
    assert (
        repr(vacancy_2) == "Vacancy(Android Developer (Middle / Senior) (Ташкент), "
        "https://hh.ru/vacancy/90892946, 20000000, Описание вакансии 2)"
    )
