import json
from src.class_abstract import Connector


class JSONSaver(Connector):
    @staticmethod
    def create_vacancies_list(vacancies):
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

    @staticmethod
    def load_json_file(json_file):
        """Загрузка json - файла."""
        with open(json_file, 'r', encoding='utf-8') as file:
            return json.load(file)

    def add_vacancies(self, max_id, my_json_file, json_file):
        vacancies_list = self.load_json_file(json_file)
        my_vacancies_list = self.load_json_file(my_json_file)
        for new_vacancy in my_vacancies_list:
            max_id += 1
            new_vacancy["id"] = max_id
            vacancies_list.append(new_vacancy)
        self.save_json_file(vacancies_list, json_file)

    def del_vacancies(self, area_name, json_file):
        my_vacancies_list = []
        vacancies_list = self.load_json_file(json_file)
        for i in range(len(vacancies_list)):
            if vacancies_list[i]['area'] != area_name:
                my_vacancies_list.append(vacancies_list[i])
        self.save_json_file(my_vacancies_list, json_file)

    def select_vacancies(self, area_name, json_file):
        my_vacancies_list = []
        vacancies_list = self.load_json_file(json_file)
        for i in range(len(vacancies_list)):
            if vacancies_list[i]['area'] == area_name:
                my_vacancies_list.append(vacancies_list[i])
        self.save_json_file(my_vacancies_list, json_file)
