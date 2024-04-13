from src.class_abstract import VacancyABC
import json

class Vacancy(VacancyABC):
    """ Класс для работы с вакансиями. """
    idv: int          # идетификатор вакансии
    name: str         # Нименование вакансии
    area: str         # регион где находится вакансия
    requirement: str  # требования к соискателю
    salary_min: int   # мминимальная зарплата
    salary_max: int   # максимальная зарплата
    currency: str     # валюта зарплаты
    emp_name: str     # работодатель
    emp_url: str      # ссылка на вакансию

    def __init__(self, idv, name, area, requirement, salary_max, salary_min, currency, emp_name, emp_url):
        self.idv = idv
        self.name = name
        self.area = area
        self.requirement = requirement
        self.salary_min = salary_min
        self.salary_max = salary_max
        self.currency = currency
        self.emp_name = emp_name
        self.emp_url = emp_url

    @classmethod
    def create_objects_vacancy(cls, hh_vacancies):
        if isinstance(hh_vacancies, dict):
            vacancies_list = []
            for vacancy in hh_vacancies["items"]:
                salary_min, salary_max, currency = cls.salary_valid(vacancy['salary'])
                requirement = cls.requirement_valid(vacancy['snippet'])
                vacancies_list.append(cls(idv=vacancy["id"],
                                      name=vacancy["name"],
                                      area=vacancy['area']['name'],
                                      requirement=requirement,
                                      salary_min=salary_min,
                                      salary_max=salary_max,
                                      currency=currency,
                                      emp_name=vacancy['employer']['name'],
                                      emp_url=vacancy['alternate_url']))
            print(vacancies_list[51])
        else:
            print('Ошибочный формат файла.')

    @staticmethod
    def requirement_valid(requirement_item):
        if requirement_item is None:
            return ''
        else:
            return requirement_item["requirement"]

    @staticmethod
    def salary_valid(salary_item):
        if salary_item is None:
            salary_min = 0
            salary_max = 0
            currency = ''
        else:
            if salary_item['from'] == "None":
                salary_min = 0
            else:
                salary_min = salary_item['from']

            if salary_item['to'] == "None":
                salary_max = 0
            else:
                salary_max = salary_item['to']

            if salary_item['currency'] == "None":
                currency = ''
            else:
                currency = salary_item['currency']

        return salary_min, salary_max, currency

    def __str__(self):
        return f'{self.requirement} c зп {self.salary_min} {self.salary_max} {self.currency}'


    with open('data.json', 'w') as file:
    json.dump(data, file)