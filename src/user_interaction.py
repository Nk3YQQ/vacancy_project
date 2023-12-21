import json
import time

from src.class_convert_vacancy import ConvertVacancy
from src.class_filtered_vacancies import FilteredVacancy
from src.class_saver import JSONSaver, CSVSaver
from src.class_with_api import HeadHunterAPI, SuperJobAPI
from src.class_with_vacancy import Vacancy
from src.utils import get_vacancy_by_index, concatenate_dicts, view_all_user_vacancy


def user_interaction():
    """
    Функция создаёт интерфейс для взаимодействия с пользователем
    """
    try:
        # Логическая ступень №1

        hh_api = HeadHunterAPI()
        superjob_api = SuperJobAPI()

        vacancy_input = input('Название вакансии: ')
        top_n = int(input('Количество вакансий для вывода в топ N: '))

        hh_api.get_vacancies(vacancy_input)
        superjob_api.get_vacancies(vacancy_input)

        filter_words = input('Введите ключевые слова для фильтрации вакансий: ').split()

        filtered_vacancies = FilteredVacancy()
        filtered_vacancies.filter_vacancies(filter_words)

        if not filtered_vacancies.filtered_vacancies_list:
            return 'Нет вакансий, соответствующих заданным критериям.'

        print(json.dumps(filtered_vacancies.filtered_vacancies_list, ensure_ascii=False, indent=4))

        # Логическая ступень №2

        convector = ConvertVacancy()
        convector.convert_to_object(filtered_vacancies.filtered_vacancies_list)

        top_vacancies = Vacancy.get_top_vacancies(top_n)

        top_vacancies_input = input('Чтобы посмотреть топ вакансий, нажмите введите "топ": ').lower()

        if top_vacancies_input != 'топ':
            return 'Походу вы ввели команду, которую я не понял.'

        convert_top_vacancies = convector.convert_to_json(top_vacancies)
        print(convert_top_vacancies)

        # Логическая ступень №3

        choose_vacancy_input = input('Введите номер вакансии, которую хотите добавить в избранное: ')
        format_to_save_input = input('Введите формат для сохранения вакансии - "json" или "csv": ')

        top = get_vacancy_by_index(convert_top_vacancies, choose_vacancy_input)

        if top == 'Index error':
            return 'Указанный индекс превышает количество вакансий в списке или меньше 0'

        json_saver = JSONSaver()
        csv_saver = CSVSaver()

        if format_to_save_input == "json":
            json_saver.add_vacancy(top)
            print('Данные успешно добавлены в файл!')

        elif format_to_save_input == "csv":
            csv_saver.add_vacancy(top)
            print('Данные успешно добавлены в файл!')

        else:
            return 'Вы ввели формат, который не поддерживается для сохранения данных.'

        # Логическая ступень №4

        salary_input = int(input('Если Вы хотите найти вакансию по зарплате, введите сумму заплаты: '))
        json_salary = json_saver.get_vacancies_by_salary(salary_input)
        csv_salary = csv_saver.get_vacancies_by_salary(salary_input)

        print(concatenate_dicts(json_salary, csv_salary))

        # Логическая ступень №5

        delete_vacancy_input = input('Если Вы хотите убрать вакансию из избранного, введите "удалить": ').lower()

        if delete_vacancy_input != 'удалить':
            return 'Походу вы ввели команду, которую я не понял.'

        print('Сейчас перед Вами будет представлен список всех добавленных Вами вакансий:')

        time.sleep(5)

        print(view_all_user_vacancy())

        format_to_delete_input = input('Введите формат для удаления вакансии - "json" или "csv": ')
        choose_vacancy_input = input('Введите номер вакансии, которую хотите удалить из избранного списка: ')

        if format_to_delete_input == "json":
            json_saver.delete_vacancy(choose_vacancy_input)
            print('Вакансия успешно удалена!')

        elif format_to_delete_input == "csv":
            csv_saver.delete_vacancy(choose_vacancy_input)
            print('Вакансия успешно удалена!')

        else:
            return 'Вы ввели формат, который не поддерживается для сохранения данных.'

        return 'Программа завершила работу. Удачного Вам дня!'

    except ValueError:
        raise ValueError('Упс, походу Вы ввели что-то нецелочисленное, когда нужно было ввести целое число :(')


if __name__ == '__main__':
    print(user_interaction())
