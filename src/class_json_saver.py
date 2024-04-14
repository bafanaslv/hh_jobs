import json
from src.class_abstract import Connector

class JSONSaver(Connector):
    def save_json_file(self, vacancies, json_file):
        vacancies_json = []
        for vacancy in vacancies:
            vac_dict = {"idv": vacancy.idv,
                        "name": vacancy.name,
                        "area": vacancy.area,
                        "requirement": vacancy.requirement,
                        "responsibility": vacancy.responsibility,
                        "salary_min": vacancy.salary_min,
                        "salary_max": vacancy.salary_max,
                        "currency": vacancy.currency,
                        "emp_name": vacancy.emp_name,
                        "emp_url": vacancy.emp_url}
            vacancies_json.append(vac_dict)

        with open(json_file, 'w', encoding="UTF-8") as file:
            vac_json = json.dumps(vacancies_json, ensure_ascii=False, indent=4)
            file.write(vac_json)
