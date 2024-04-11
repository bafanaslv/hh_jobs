class Vacancy:
    #    def __init__(self, name, area, requirement, responsibility, salary, currency, experience, employer, url):
    """ Класс для работы с вакансиями. """
    name: str         # Нименование вакансии
    area: str         # регион где находится вакансия
    requirement: str  # требования к соискателю
    salary_max: int   # максимальная зарплата в руб.
    currency: str     # валюта зарплаты
    emp_name: str     # работодатель
    emp_url: str      # сайт работодателя

    def __init__(self, name, area, requirement, salary, currency, emp_name, emp_url):
        self.name = name
        self.area = area
        self.requirement = self.check_requirement(requirement)
        self.salary_max = self.add_salary_max(salary)
        self.currency = currency
        self.emp_name = emp_name
        self.emp_url = emp_url

    def check_requirement(self):
        pass

    def add_salary_max(self):
        pass

