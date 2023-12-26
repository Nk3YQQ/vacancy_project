from pathlib import Path

import pytest

from src.funcs_for_save import is_vacancy_in_file, open_csv_file, open_json_file


@pytest.fixture
def fake_path() -> str:
    return "data/fake_path"


@pytest.fixture
def fake_data() -> list:
    return ["vacancy_1", "vacancy_2", "vacancy_3", "vacancy_4", "vacancy_5", "vacancy_6", "vacancy_7"]


def test_utils_with_open_and_write_files(fake_path: Path, fake_data: list) -> None:
    with pytest.raises(FileNotFoundError, match="Указанный файл не найден."):
        open_json_file(fake_path)

    with pytest.raises(FileNotFoundError, match="Указанный файл не найден."):
        open_csv_file(fake_path)


@pytest.fixture
def vacancy_1() -> dict:
    return {
        "vacancy": "Junior Python Developer",
        "url": "https://hh.ru/vacancy/90906538",
        "salary": 0,
        "description": "Требования: Опыт программирования на <highlighttext>Python</highlighttext> от 1 года. Знание "
        "SQL и опыт работы с БД. Желательно знание Regex. Обязательно знание Linux.... Обязанности: "
        "Разработка алгоритмов обработки текста: написание парсеров, разметка текста, классификация "
        "текста, извлечения сущностей, кластеризация.",
    }


@pytest.fixture
def vacancy_2() -> dict:
    return {
        "vacancy": "BI-аналитик / начинающий аналитик данных (удаленно)",
        "url": "https://hh.ru/vacancy/89838927",
        "salary": 70000,
        "description": "Требования: ...и G Analytics. Опыт настройки сквозной аналитики. Опыт решения задач по "
        "выгрузке данных через API запросы. Знания <highlighttext>Python</highlighttext>. Усидчивость. "
        "Азарт.. Обязанности: Выстраивать систему аналитики в проектах. Собирать данные / "
        "автоматизировать сбор данных из разных источников и упаковывать их в информативные "
        "таблицы/дашборды.",
    }


@pytest.fixture
def vacancies() -> list:
    return [
        {
            "vacancy": "BI-аналитик / начинающий аналитик данных (удаленно)",
            "url": "https://hh.ru/vacancy/89838927",
            "salary": 70000,
            "description": "Требования: ...и G Analytics. Опыт настройки сквозной аналитики. Опыт решения задач по "
            "выгрузке данных через API запросы. Знания <highlighttext>Python</highlighttext>. "
            "Усидчивость."
            "Азарт.. Обязанности: Выстраивать систему аналитики в проектах. Собирать данные / "
            "автоматизировать сбор данных из разных источников и упаковывать их в информативные "
            "таблицы/дашборды.",
        },
        {
            "vacancy": "Стажер/разработчик Python",
            "url": "https://hh.ru/vacancy/90415076",
            "salary": 0,
            "description": "Требования: Знания Linux. Будет плюсом задание Go/C/C++, знание сетей.. Обязанности: "
            "Разработка backend микросервисов на <highlighttext>Python</highlighttext>.",
        },
    ]


def test_is_vacancy_in_file(vacancy_1: dict, vacancy_2: dict, vacancies: list) -> None:
    assert is_vacancy_in_file(vacancy_1, vacancies) is False
    assert is_vacancy_in_file(vacancy_2, vacancies) is True
