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
    def add_vacancies(self, max_id, my_json_file, json_file):
        pass

    @abstractmethod
    def del_vacancies(self, area_name, json_file):
        pass

    @abstractmethod
    def select_vacancies(self, area_name, json_file):
        pass
