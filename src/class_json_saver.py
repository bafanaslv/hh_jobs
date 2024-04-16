import json
from src.class_abstract import Connector
from src.class_vacancy import Vacancy

class JSONSaver(Connector):
    def create_vacancies_list(self, vacancies):
        vacancies_list = []
        vacancies_id_list = []
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
            vacancies_id_list.append(vacancy_dict["id"])
        return vacancies_list, int(max(vacancies_id_list)) + 1

    def save_json_file(self, vacancies_list, json_file):
        with open(json_file, 'w', encoding="UTF-8") as file:
            vacancy_json = json.dumps(vacancies_list, ensure_ascii=False, indent=4)
            file.write(vacancy_json)

    @staticmethod
    def load_json_file(json_file):
        """Загрузка json - файла."""
        with open(json_file, 'r', encoding='utf-8') as file:
            return json.load(file)

    def add_vacancy(self, new_vacancy_dict, json_file):
        vacancies_list = self.load_json_file(json_file)
        vacancies_list.append(new_vacancy_dict)
        self.save_json_file(vacancies_list, json_file)

    def del_vacancy(self):
        pass

    def select_vacancies(self):
        pass
