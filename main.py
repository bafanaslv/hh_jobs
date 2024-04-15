from src.class_hh_api import HeadHunterAPI
from src.class_vacancy import Vacancy
from config import ROOT_DIR
from src.class_json_saver import JSONSaver

URL_GET = "https://api.hh.ru/vacancies"  # адрес для отправки запроса
PARAMS = {'text': 'oracle', 'area': '113', 'currency': 'RUR', 'per_page': 2}  # параметры запроса
VACANCIES_FILE = ROOT_DIR+'/data/vacancies.json'  # json-файл с вакансиями


if __name__ == '__main__':
    # Создание экземпляра класса для работы с API сайтом с вакансиями HeadHater.
    hh_api = HeadHunterAPI()

    # Получение вакансий с hh.ru в формате JSON
    hh_vacancies = hh_api.get_vacancies(URL_GET, PARAMS)
    if hh_api.get_status_code() == 200:  # если запрос прошел удачно, то идем дальше.
        vacancies_objects_list, vacancies_id_list = Vacancy.create_objects_vacancy(hh_vacancies)
        json_saver = JSONSaver()
        vacancies_dict_list = json_saver.create_vacancies_list(vacancies_objects_list)
        json_saver.save_json_file(vacancies_dict_list, VACANCIES_FILE)
        for vacancy in vacancies_objects_list:
            print(vacancy)
            print('')

        id_vac = int(max(vacancies_id_list)) + 1
        # Добавление новой вакансии в json - файл.
        new_vacancy_object_list = []
        new_vacancy_object_list.append(Vacancy(id_vac, "Программист PL/SQL уровня junour", "Казань",
                              "Знание SQL запросов", "Знание SQL запросов",
                              100000, 200000, "руб.", "Facebook",
                              "http:\\www.facebook.com"))
        vacancies_dict_list = json_saver.create_vacancies_list(new_vacancy_object_list)
        json_saver.add_vacancy(vacancies_dict_list, VACANCIES_FILE)
        print(new_vacancy_object_list[0])
    else:
        print(hh_api.get_status_code())
