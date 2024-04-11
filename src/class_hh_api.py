from abc import ABC, abstractmethod
import json
import requests


class HHapiABC(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_status_code(self):
        pass

    @abstractmethod
    def get_vacancies(self, params):
        pass

    @abstractmethod
    def create_json_file(self, hh_vacancies, vacansies_file):
        pass


class HeadHunterAPI(HHapiABC):
    """ Класс для получения данных с HH."""
    def __init__(self, url_get, params, status_code=0):
        self.url_get = url_get
        self.params = params
        self.status_code = status_code

    def get_status_code(self):
        """ Возврат статуса запроса к ресурсу url_get. """
        return self.status_code

    def get_vacancies(self):
        """ Получение вакансий с ресурса url_get и возврат их в json-формате. """
        response = requests.get(self.url_get, params=self.params)
        self.status_code = response.status_code
        return response.json()

    def create_json_file(self, hh_vacancies, vacansies_file):
        """ Запись вакансий в файл vacansies_file """
        with open(vacansies_file, "w", encoding="utf8") as file:
            vacancies_json = json.dumps(hh_vacancies, ensure_ascii=False)
            file.write(vacancies_json)
