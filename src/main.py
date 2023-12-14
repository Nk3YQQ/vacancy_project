from src.class_with_api import HeadHunterAPI, SuperJobAPI

from src.class_with_vacancy import ParseHeadHunterVacancy, ParseSuperJobVacancy


hh_api = HeadHunterAPI()
superjob_api = SuperJobAPI()

hh_vacancies = hh_api.get_vacancies("Python", 5)
superjob_vacancies = superjob_api.get_vacancies("Python", 5)

parse_hh_vacancies = ParseHeadHunterVacancy()
parse_superjob_vacancies = ParseSuperJobVacancy()

print(parse_hh_vacancies.parse_vacancies(hh_vacancies))
print(parse_superjob_vacancies.parse_vacancies(superjob_vacancies))
