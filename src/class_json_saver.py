import json
from src.class_abstract import Connector


class JSONSaver(Connector):
    def save_json_file(self, vacancies, json_file):
        vacancies_json = []
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
            vacancies_json.append(vacancy_dict)

        with open(json_file, 'w', encoding="UTF-8") as file:
            vacancy_json = json.dumps(vacancies_json, ensure_ascii=False, indent=4)
            file.write(vacancy_json)
