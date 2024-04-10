from abc import ABC, abstractmethod
import requests


class HHapiABC(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_vacancies(self, params):
        pass


class HeadHunterAPI(HHapiABC):
    def __init__(self, url_get):
        self.url_get = url_get
        self.status_code = 0

    def get_vacancies(self, params):
        response = requests.get(self.url_get, params=params)
        self.status_code = response.status_code
        return response.json()

    def get_status_code(self):
        return self.status_code
