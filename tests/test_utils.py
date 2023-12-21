import json
from typing import Any

import pytest

from config import CSV_SAVER_PATH, JSON_SAVER_PATH
from src.funcs_for_save import open_csv_file, open_json_file
from src.utils import concatenate_dicts, delete_vacancy, get_vacancy_by_index, make_description, view_all_user_vacancy


@pytest.fixture
def json_file() -> Any:
    return open_json_file(JSON_SAVER_PATH)


@pytest.fixture
def csv_file() -> Any:
    return open_csv_file(CSV_SAVER_PATH)


def test_concatenate_dicts(json_file: Any, csv_file: Any) -> None:
    empty_json_file: list = []
    empty_csv_file: list = []

    result = concatenate_dicts(json_file, csv_file)

    assert isinstance(result, str) is True

    result = concatenate_dicts(empty_json_file, empty_csv_file)

    assert result == "В файлах ничего не найдено :("


def test_view_all_user_vacancy() -> None:
    result = view_all_user_vacancy()

    assert isinstance(result, str) is True
    assert "json_vacancy" in result
    assert "csv_vacancy" in result


@pytest.fixture
def vacancy_list() -> list:
    return ["vacancy_1", "vacancy_2", "vacancy_3", "vacancy_4", "vacancy_5", "vacancy_6", "vacancy_7"]


def test_delete_vacancy(vacancy_list: list) -> None:
    result = delete_vacancy(vacancy_list, "1")
    assert result == ["vacancy_2", "vacancy_3", "vacancy_4", "vacancy_5", "vacancy_6", "vacancy_7"]

    result = delete_vacancy(vacancy_list, "6")
    assert result == ["vacancy_2", "vacancy_3", "vacancy_4", "vacancy_5", "vacancy_6"]

    result = delete_vacancy(vacancy_list, "1020")
    assert result == "Index error"

    with pytest.raises(ValueError, match="Введённое значение не совпадает с целым числом."):
        delete_vacancy(vacancy_list, "number")


@pytest.fixture
def top_vacancies() -> str:
    return json.dumps(
        ["vacancy_1", "vacancy_2", "vacancy_3", "vacancy_4", "vacancy_5", "vacancy_6", "vacancy_7"], ensure_ascii=False
    )


def test_get_vacancy_by_index(top_vacancies: str) -> None:
    result = get_vacancy_by_index(top_vacancies, "2790")
    assert result == "Index error"

    with pytest.raises(ValueError, match="Введённое значение не совпадает с целым числом."):
        get_vacancy_by_index(top_vacancies, "number")


def test_make_description() -> None:
    assert make_description({}) == "Нет данных."
