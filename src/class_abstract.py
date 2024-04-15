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
    @abstractmethod
    def save_json_file(self, vacancies, json_file):
        pass

    @abstractmethod
    def add_vacancy(self):
        pass

    @abstractmethod
    def del_vacancy(self):
        pass

    @abstractmethod
    def select_vacancies(self):
        pass
