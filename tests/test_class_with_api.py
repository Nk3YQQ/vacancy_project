from src.class_with_api import HeadHunterAPI, SuperJobAPI


def test_HeadHunterAPI() -> None:
    hh_api = HeadHunterAPI()

    hh_vacancies = hh_api.get_vacancies("Python")

    assert isinstance(hh_vacancies, dict) is True
    assert len(hh_vacancies["items"]) == 10

    hh_vacancies = hh_api.get_vacancies(1)
    assert hh_vacancies == "Неверный ввод! Текст должен быть в виде строки."

    hh_vacancies = hh_api.get_vacancies("dldlldldlldldlld")
    assert hh_vacancies == "По вашему запросу ничего не было найдено."


def test_SuperJobAPI() -> None:
    superjob_api = SuperJobAPI()

    superjob_vacancies = superjob_api.get_vacancies("Python")
    assert isinstance(superjob_vacancies, dict) is True
    assert len(superjob_vacancies["objects"]) == 10

    hh_vacancies = superjob_api.get_vacancies(1)
    assert hh_vacancies == "Неверный ввод! Текст должен быть в виде строки."

    hh_vacancies = superjob_api.get_vacancies("dldlldldlldldlld")
    assert hh_vacancies == "По вашему запросу ничего не было найдено."
