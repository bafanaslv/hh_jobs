class Vacancy:
    """ Класс для работы с вакансиями. """
    idv: int             # идентификатор вакансии
    name: str            # наименование вакансии
    area: str            # регион где находится вакансия
    requirement: str     # требования к соискателю
    responsibility: str  # долностные обязанности
    salary_min: int      # мминимальная зарплата
    salary_max: int      # максимальная зарплата
    currency: str        # валюта зарплаты
    employer: str        # работодатель
    employer_url: str    # ссылка на вакансию

    max_id = 0  # максимальный идентификатор вакансии

    def __init__(self, idv, name, area, requirement, responsibility, salary_min, salary_max,
                 currency, employer, employer_url):
        self.idv = idv
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
    def create_objects_vacancy(cls, hh_vacancies, vacancies_list):
        """Метод для создания списка объектов вакансий из списка словарей полученных с HeadHanter hh_vacancies."""
        if isinstance(hh_vacancies, dict):
            vac_id = 0
            for vacancy in hh_vacancies["items"]:
                vac_id = int(vacancy["id"])
                salary_min, salary_max, currency = cls.salary_valid(vacancy['salary'])
                responsibility = cls.responsibility_valid(vacancy['snippet'])
                vacancies_list.append(cls(idv=vacancy["id"],
                                      name=vacancy["name"],
                                      area=vacancy['area']['name'],
                                      requirement=vacancy['snippet']['requirement'],
                                      responsibility=responsibility,
                                      salary_min=salary_min,
                                      salary_max=salary_max,
                                      currency=currency,
                                      employer=vacancy['employer']['name'],
                                      employer_url=vacancy['alternate_url']))
            # по мере формирование словаря vacancies_list выявляется максимальных номер id вакансии.
            # он нам нужен при добаволении новых вакансий для избежания повторения id.
            if vac_id > cls.max_id:
                cls.max_id = vac_id
            return vacancies_list
        else:
            print('Ошибочный формат файла.')

    @staticmethod
    def responsibility_valid(responsibility_item):
        """Валидация должностных обязанностей."""
        if not responsibility_item:
            return ''
        else:
            if not responsibility_item["responsibility"]:
                return 'не указан'
            else:
                return responsibility_item["responsibility"]

    @staticmethod
    def salary_valid(salary_item):
        """Валидация зарплаты и валюты."""
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
        """Подготовка строк вакансий для вывода."""
        sal = ''
        if self.salary_min == 0 and self.salary_max == 0:
            sal = 'не указана'
        elif self.salary_min > 0 and self.salary_max > 0:
            sal = f'от {self.salary_min} до {self.salary_max}'
        elif self.salary_max > 0:
            sal = str(self.salary_max)
        elif self.salary_min > 0:
            sal = str(self.salary_min)

        return (f'id: {self.idv}\n'
                f'Вакансия: {self.name}\n'
                f'Регион:   {self.area}\n'
                f'Требования к соискателю: {self.requirement}\n'
                f'Круг обязанностей: {self.responsibility}\n'
                f'Зарплата {sal} {self.currency}\n'
                f'Работодатель {self.employer}\n'
                f'Описание вакансии {self.employer_url}\n')
