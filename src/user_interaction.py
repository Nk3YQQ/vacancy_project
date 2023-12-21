import json
import time
from typing import Any

from src.class_convert_vacancy import ConvertVacancy
from src.class_filtered_vacancies import FilteredVacancy
from src.class_saver import CSVSaver, JSONSaver
from src.class_with_api import HeadHunterAPI, SuperJobAPI
from src.class_with_vacancy import Vacancy
from src.utils import concatenate_dicts, get_vacancy_by_index, view_all_user_vacancy


def user_interaction() -> Any:
    """
    Функция создаёт интерфейс для взаимодействия с пользователем
    """
    try:
        # Логическая ступень №1 Поиск и фильтрация вакансий

        hh_api = HeadHunterAPI()
        superjob_api = SuperJobAPI()

        vacancy_input = input("Название вакансии: ")

        if not vacancy_input:
            return "Вы ничего не ввели :("

        hh_api.get_vacancies(vacancy_input)
        superjob_api.get_vacancies(vacancy_input)

        filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()

        filtered_vacancies = FilteredVacancy()
        filtered_vacancies.filter_vacancies(filter_words)

        if not filtered_vacancies.filtered_vacancies_list:
            return "Нет вакансий, соответствующих заданным критериям."

        print(json.dumps(filtered_vacancies.filtered_vacancies_list, ensure_ascii=False, indent=4))

        # Логическая ступень №2 Выборка топ вакансий из приложенного списка вакансий

        top_n = int(input("Введите количество вакансий для вывода в топ N: "))

        convector = ConvertVacancy()
        convector.convert_to_object(filtered_vacancies.filtered_vacancies_list)

        top_vacancies = Vacancy.get_top_vacancies(top_n)

        top_vacancies_input = input('Чтобы посмотреть топ вакансий, нажмите введите "топ": ').lower()

        if top_vacancies_input != "топ":
            return "Походу вы ввели команду, которую я не понял."

        convert_top_vacancies = convector.convert_to_json(top_vacancies)
        print(convert_top_vacancies)

        # Логическая ступень №3 Сохранение вакансии в избранное (json / csv файл)

        choose_vacancy_input = input("Введите номер вакансии, которую хотите добавить в избранное: ")
        format_to_save_input = input('Введите формат для сохранения вакансии - "json" или "csv": ')

        top = get_vacancy_by_index(convert_top_vacancies, choose_vacancy_input)

        if top == "Index error":
            return "Указанный индекс превышает количество вакансий в списке или меньше 0"

        json_saver = JSONSaver()
        csv_saver = CSVSaver()

        if format_to_save_input == "json":
            if json_saver.add_vacancy(top) == "Error! Vacancy in vacancies":
                return "Вакансия уже добавлена в избранное."
            else:
                json_saver.add_vacancy(top)
                print("Данные успешно добавлены в файл!")

        elif format_to_save_input == "csv":
            if csv_saver.add_vacancy(top) == "Error! Vacancy in vacancies":
                return "Вакансия уже добавлена в избранное."
            else:
                csv_saver.add_vacancy(top)
                print("Данные успешно добавлены в файл!")

        else:
            return "Вы ввели формат, который не поддерживается для сохранения данных."

        # Логическая ступень №4 Поиск вакансий по зарплате в избранном

        salary_input = int(input("Если Вы хотите найти вакансию по зарплате, введите сумму заплаты: "))
        json_salary = json_saver.get_vacancies_by_salary(salary_input)
        csv_salary = csv_saver.get_vacancies_by_salary(salary_input)

        print(concatenate_dicts(json_salary, csv_salary))

        # Логическая ступень №5 Удаление вакансии из избранного

        delete_vacancy_input = input('Если Вы хотите убрать вакансию из избранного, введите "удалить": ').lower()

        if delete_vacancy_input != "удалить":
            return "Походу вы ввели команду, которую я не понял."

        print("Сейчас перед Вами будет представлен список всех добавленных Вами вакансий:")

        time.sleep(5)

        print(view_all_user_vacancy())

        format_to_delete_input = input('Введите формат для удаления вакансии - "json" или "csv": ')
        choose_vacancy_input = input("Введите номер вакансии, которую хотите удалить из избранного списка: ")

        if format_to_delete_input == "json":
            json_saver.delete_vacancy(choose_vacancy_input)
            print("Вакансия успешно удалена!")

        elif format_to_delete_input == "csv":
            csv_saver.delete_vacancy(choose_vacancy_input)
            print("Вакансия успешно удалена!")

        else:
            return "Вы ввели формат, который не поддерживается для сохранения данных."

        return "Программа завершила работу. Удачного Вам дня!"

    except ValueError:
        raise ValueError("Упс, походу Вы ввели что-то нецелочисленное, когда нужно было ввести целое число :(")
