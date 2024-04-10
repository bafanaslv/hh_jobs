from abc import ABC, abstractmethod
from src.class_internet_errors import Internet_connection_error
import requests


class HHapiabc(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass


class HeadHunterAPI(HHapiabc):
    def __init__(self, url_get):
        self.url_get = url_get

    def get_vacancies(self):
        response = requests.get(self.url_get)
        if response.status_code != 200:
            raise Internet_connection_error
        return response.json()
