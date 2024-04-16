from src.class_hh_api import HeadHunterAPI
from src.class_vacancy import Vacancy
from config import ROOT_DIR
from src.class_json_saver import JSONSaver

URL_GET = "https://api.hh.ru/vacancies"  # адрес для отправки запроса
PARAMS = {'text': 'oracle', 'area': '113', 'currency': 'RUR', 'per_page': 2}  # параметры запроса
VACANCIES_FILE = ROOT_DIR+'/data/vacancies.json'  # json-файл с вакансиями
MY_VACANCIES_FILE = ROOT_DIR+'/data/my_vacancies.json'  # json-файл с моими вакасиями для добавления


if __name__ == '__main__':
    # Создание экземпляра класса для работы с API сайтом с вакансиями HeadHater.
    hh_api = HeadHunterAPI()

    # Получение вакансий с hh.ru в формате JSON
    hh_vacancies = hh_api.get_vacancies(URL_GET, PARAMS)
    if hh_api.get_status_code() == 200:  # если запрос прошел удачно, то идем дальше.
        # создание json - файла из выборки HeadHanter.
        vacancies_objects_list = Vacancy.create_objects_vacancy(hh_vacancies)
        json_saver = JSONSaver()
        vacancies_dict_list = json_saver.create_vacancies_list(vacancies_objects_list)
        json_saver.save_json_file(vacancies_dict_list, VACANCIES_FILE)

        # добавление списка вакансий из моего json - файла
        json_saver.add_vacancies(Vacancy.max_id, MY_VACANCIES_FILE, VACANCIES_FILE)

        # # Удаление вакансий определенного региона
        # json_saver.del_vacancies("Тверь", VACANCIES_FILE)
        #
        # # Выборка вакансий определенного региона
        # json_saver.select_vacancies("Новый Уренгой", VACANCIES_FILE)

    else:
        print(hh_api.get_status_code())
