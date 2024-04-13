from abc import ABC, abstractmethod


class VacancyABC(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def create_objects_vacancy(self, hh_vacancies):
        pass

    @abstractmethod
    def __str__(self):
        pass


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

    @abstractmethod
    def create_json_file(self, hh_vacancies, vacansies_file):
        pass
