from src.class_hh_api import HeadHunterAPI
from src.class_vacancy import Vacancy
from config import ROOT_DIR

URL_GET = "https://api.hh.ru/vacancies"  # адрес для отправки запроса
PARAMS = {'text': "python", 'area': '113', 'per_page': 100}  # параметры запроса
VACANCIES_FILE = ROOT_DIR+'/data/vacansies.json'  # json-файл с вакансиями


if __name__ == '__main__':
    # Создание экземпляра класса для работы с API сайтом с вакансиями HeadHater.
    hh_api = HeadHunterAPI()

    # Получение вакансий с hh.ru в формате JSON
    hh_vacancies = hh_api.get_vacancies(URL_GET, PARAMS)
    if hh_api.get_status_code() == 200:  # если запрос прошел удачно, то идем дальше.
        vacancies_list = Vacancy.create_objects_vacancy(hh_vacancies)


#        hh_api.create_json_file(hh_vacancies, VACANCIES_FILE)  # создание json-файла с вакансиями

    # Преобразование набора данных из JSON в список объектов
    # vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
    #
    # # Пример работы контструктора класса с одной вакансией
    # vacancy = Vacancy("Python Developer", "", "100 000-150 000 руб.", "Требования: опыт работы от 3 лет...")
    #
    # # Сохранение информации о вакансиях в файл
    # json_saver = JSONSaver()
    # json_saver.add_vacancy(vacancy)
    # json_saver.delete_vacancy(vacancy)
