from src.class_hh_api import HeadHunterAPI
from src.class_vacancy import Vacancy
from config import ROOT_DIR
from src.class_json_saver import JSONSaver

URL_GET = "https://api.hh.ru/vacancies"  # адрес для отправки запроса
VACANCIES_FILE = ROOT_DIR+'/data/vacancies.json'  # json-файл с вакансиями
MY_VACANCIES_FILE = ROOT_DIR+'/data/my_vacancies.json'  # json-файл с моими вакасиями для добавления


if __name__ == '__main__':
    # Создание экземпляра класса для работы с API сайтом с вакансиями HeadHater.
    hh_api = HeadHunterAPI()
    json_manager = JSONSaver()

    # Получение вакансий с hh.ru в формате JSON
    vacancies_dict_list = []
    params = {'text': 'oracle', 'area': '113', 'currency': 'RUR', 'per_page': 100, 'page': 0}  # параметры запроса
    params['page'] = 0
    hh_vacancies = hh_api.get_vacancies(URL_GET, params)
    if hh_api.get_status_code() == 200:  # если запрос прошел удачно, то идем дальше.
        # создание json - файла из выборки HeadHanter.
        Vacancy.create_objects_vacancy(hh_vacancies, vacancies_dict_list)
#        vacancies_dict = json_manager.create_vacancies_list(vacancies_objects_list)

        params['page'] = 1
        hh_vacancies = hh_api.get_vacancies(URL_GET, params)
        vacancies_objects_list = Vacancy.create_objects_vacancy(hh_vacancies, vacancies_dict_list)
        vacancies_dict = json_manager.create_vacancies_list(vacancies_objects_list)

        json_manager.save_json_file(vacancies_dict, VACANCIES_FILE)
        # добавление списка вакансий из моего json - файла
        json_manager.add_vacancies(Vacancy.max_id, MY_VACANCIES_FILE, VACANCIES_FILE)
        json_manager.print_vacancies(vacancies_objects_list)
        print(f'Найдено {len(vacancies_objects_list)} вакансий.')
    # # Удаление вакансий определенного региона
    # json_saver.del_vacancies("Тверь", VACANCIES_FILE)
    #
    # # Выборка вакансий определенного региона
    # json_saver.select_vacancies("Новый Уренгой", VACANCIES_FILE)

    else:
        print(f'Ответ: {hh_api.get_status_code()} - не удалось получить доступ к сайту')
