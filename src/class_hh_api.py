from src.class_abstract import HHapiABC
import requests


class HeadHunterAPI(HHapiABC):
    """ Класс для получения данных с HH."""
    def __init__(self):
        self.status_code = 0

    def get_status_code(self):
        """ Возврат статуса запроса к ресурсу url_get. """
        return self.status_code

    def get_vacancies(self, url_get, params):
        """ Получение вакансий с ресурса url_get и возврат их в json-формате. """
        response = requests.get(url_get, params)
        self.status_code = response.status_code
        return response.json()
