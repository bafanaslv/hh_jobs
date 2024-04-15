import json
from src.class_abstract import Connector


class JSONSaver(Connector):
    def create_vacancies_list(self, vacancies):
        vacancies_list = []
        for vacancy in vacancies:
            vacancy_dict = {"id": vacancy.id,
                        "name": vacancy.name,
                        "area": vacancy.area,
                        "requirement": vacancy.requirement,
                        "responsibility": vacancy.responsibility,
                        "salary_min": vacancy.salary_min,
                        "salary_max": vacancy.salary_max,
                        "currency": vacancy.currency,
                        "employer": vacancy.employer,
                        "employer_url": vacancy.employer_url}
            vacancies_list.append(vacancy_dict)
        return vacancies_list

    def save_json_file(self, vacancies_list, json_file):
        with open(json_file, 'w', encoding="UTF-8") as file:
            vacancy_json = json.dumps(vacancies_list, ensure_ascii=False, indent=4)
            file.write(vacancy_json)

    def add_vacancy(self, vacancies_list, json_file):
        with open(json_file, 'w', encoding="UTF-8") as file:
            vacancy_json = json.dumps(vacancies_list, ensure_ascii=False, indent=4)
            file.write(vacancy_json)

    def del_vacancy(self):
        pass

    def select_vacancies(self):
        pass
