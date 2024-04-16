from src.class_hh_api import HeadHunterAPI
from src.class_vacancy import Vacancy


def create_json_file(params, page_quantity, url):
    # Создание экземпляра класса для работы с API сайтом с вакансиями HeadHater.
    hh_api = HeadHunterAPI()
    # Получение вакансий с hh.ru в формате JSON
    vacancies_dict_list = []
    vacancies_objects_list = []
    page = 0
    while page < page_quantity:
        params["page"] = page
        hh_vacancies = hh_api.get_vacancies(url, params)
        if hh_api.get_status_code() == 200:  # если запрос прошел удачно, то идем дальше.
            # получаем список объектов вакансий
            vacancies_objects_list = Vacancy.create_objects_vacancy(hh_vacancies, vacancies_dict_list)
            page += 1
        else:
            print(f'Ответ: {hh_api.get_status_code()} - не удалось получить доступ к сайту')
            break
    return vacancies_objects_list
