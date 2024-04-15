class Vacancy:
    """ Класс для работы с вакансиями. """
    id: int              # идетификатор вакансии
    name: str            # Нименование вакансии
    area: str            # регион где находится вакансия
    requirement: str     # требования к соискателю
    responsibility: str  # круг обязанностей
    salary_min: int      # мминимальная зарплата
    salary_max: int      # максимальная зарплата
    currency: str        # валюта зарплаты
    emp_name: str        # работодатель
    emp_url: str         # ссылка на вакансию

    def __init__(self, id, name, area, requirement, responsibility, salary_max, salary_min,
                 currency, employer, employer_url):
        self.id = id
        self.name = name
        self.area = area
        self.requirement = requirement
        self.responsibility = responsibility
        self.salary_min = salary_min
        self.salary_max = salary_max
        self.currency = currency
        self.employer = employer
        self.employer_url = employer_url

    @classmethod
    def create_objects_vacancy(cls, hh_vacancies):
        if isinstance(hh_vacancies, dict):
            vacancies_list = []
            for vacancy in hh_vacancies["items"]:
                salary_min, salary_max, currency = cls.salary_valid(vacancy['salary'])
                responsibility = cls.responsibility_valid(vacancy['snippet'])
                vacancies_list.append(cls(id=vacancy["id"],
                                      name=vacancy["name"],
                                      area=vacancy['area']['name'],
                                      requirement=vacancy['snippet']['requirement'],
                                      responsibility=responsibility,
                                      salary_min=salary_min,
                                      salary_max=salary_max,
                                      currency=currency,
                                      employer=vacancy['employer']['name'],
                                      employer_url=vacancy['alternate_url']))
            return vacancies_list
        else:
            print('Ошибочный формат файла.')

    @staticmethod
    def responsibility_valid(responsibility_item):
        if not responsibility_item:
            return ''
        else:
            if not responsibility_item["responsibility"]:
                return 'не указан'
            else:
                return responsibility_item["responsibility"]

    @staticmethod
    def salary_valid(salary_item):
        if salary_item is None:
            salary_min = 0
            salary_max = 0
            currency = ''
        else:
            if not salary_item['from']:
                salary_min = 0
            else:
                salary_min = salary_item['from']

            if not salary_item['to']:
                salary_max = 0
            else:
                salary_max = salary_item['to']

            if not salary_item['currency']:
                currency = ''
            else:
                if salary_item['currency'] == 'RUR':
                    currency = 'руб.'
                else:
                    currency = salary_item['currency']

        return salary_min, salary_max, currency

    def __str__(self):
        sal = ''
        if self.salary_min == 0 and self.salary_max == 0:
            sal = 'не указана'
        elif self.salary_min > 0 and self.salary_max > 0:
            sal = f'от {self.salary_min} до {self.salary_max}'
        elif self.salary_max > 0:
            sal = str(self.salary_max)
        elif self.salary_min > 0:
            sal = str(self.salary_min)

        return (f'Вакансия: {self.name}\n'
                f'Регион:   {self.area}\n'
                f'Требования к соискателю: {self.requirement}\n'
                f'Круг обязанностей: {self.responsibility}\n'
                f'Зарплата {sal} {self.currency}')
