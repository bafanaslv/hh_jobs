import json
from src.class_abstract import JsonManager
from src.class_vacancy import Vacancy


class JSONSaver(JsonManager):
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
            new_vacancy["id"] = str(max_id)
            vacancies_list.append(new_vacancy)
            Vacancy.max_id += 1
        self.save_json_file(vacancies_list, json_file)

    def del_vacancies(self, area_name, json_file):
        my_vacancies_list = []
        vacancies_list = self.load_json_file(json_file)
        for i in range(len(vacancies_list)):
            if vacancies_list[i]['area'] != area_name:
                my_vacancies_list.append(vacancies_list[i])
        self.save_json_file(my_vacancies_list, json_file)

    def select_vacancies_top_salary(self, vacancies_dict_list, top_n, json_file):
        pass

    def select_vacancies_by_region(self, vacancies_objects_list, area_name, json_file):
        my_vacancies_list = []
        for i in range(len(vacancies_objects_list)):
            if vacancies_objects_list[i].area == area_name:
                my_vacancies_list.append(vacancies_objects_list[i])
        print(self.print_vacancies(my_vacancies_list))
        print(f'Найдено {len(my_vacancies_list)} вакансий.\n')

    def select_vacancies_by_word(self, vacancies_objects_list, word, json_file):
        my_vacancies_list = []
        for i in range(len(vacancies_objects_list)):
            if word in vacancies_objects_list[i].requirement or word in vacancies_objects_list[i].responsibility:
                my_vacancies_list.append(vacancies_objects_list[i])
        print(self.print_vacancies(my_vacancies_list))
        print(f'Найдено {len(my_vacancies_list)} вакансий.\n')

    @staticmethod
    def print_vacancies(vacancies_list):
        for vacancy in vacancies_list:
            print(vacancy)
