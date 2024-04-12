class Vacancy:
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
                salary_item = cls.salary(vacancy['salary'])
                vacancies_list.append(cls(idv=vacancy["id"],
                                      name=vacancy["name"],
                                      area=vacancy['area']['name'],
                                      requirement=vacancy['snippet']['requirement'],
                                      salary_min=salary_item[0],
                                      salary_max=salary_item[1],
                                      currency=salary_item[2],
                                      emp_name=vacancy['employer']['name'],
                                      emp_url=vacancy['alternate_url']))
                print(vacancy["id"])
        else:
            print('Ошибочный формат файла.')

    @staticmethod
    def check_requirement(self):
        return ''

    @staticmethod
    def salary(salary_item):
        if salary_item is None:
            salary_min = 0
            salary_max = 0
            currency = ''
        else:
            salary_min = salary_item['from'],
            salary_max = salary_item['to'],
            currency = salary_item['currency']
        return [salary_min, salary_max, currency]
