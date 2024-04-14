from abc import ABC, abstractmethod


class HHapiABC(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_status_code(self):
        pass

    @abstractmethod
    def get_vacancies(self, url_get, params):
        pass


class Connector(ABC):
    def save_json_file(self, vacancies, json_file):
        pass
