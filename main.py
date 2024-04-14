from src.class_hh_api import HeadHunterAPI
from src.class_vacancy import Vacancy
from config import ROOT_DIR
from src.class_json_saver import JSONSaver

URL_GET = "https://api.hh.ru/vacancies"  # адрес для отправки запроса
PARAMS = {'text': 'oracle', 'area': '113', 'per_page': 100}  # параметры запроса
VACANCIES_FILE = ROOT_DIR+'/data/vacancies.json'  # json-файл с вакансиями


if __name__ == '__main__':
    # Создание экземпляра класса для работы с API сайтом с вакансиями HeadHater.
    hh_api = HeadHunterAPI()

    # Получение вакансий с hh.ru в формате JSON
    hh_vacancies = hh_api.get_vacancies(URL_GET, PARAMS)
    if hh_api.get_status_code() == 200:  # если запрос прошел удачно, то идем дальше.
        vacancies_list = Vacancy.create_objects_vacancy(hh_vacancies)
        json_saver = JSONSaver()
        json_saver.save_json_file(vacancies_list, VACANCIES_FILE)
        for vacancy in vacancies_list:
            print(vacancy)
    else:
        print(hh_api.get_status_code())
