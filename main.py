from src.class_hh_api import HeadHunterAPI
import json
from config import ROOT_DIR

URL_GET = "https://httpbin.org/get"  # используемый адрес для отправки запроса
PARAMS = {'text': "Python", 'area': '1', 'per_page': 100} # параметры запроса
FILE_VACANCIES = ROOT_DIR+'/data/vacansies.json' # файл с вакасиями


if __name__ == '__main__':
    # Создание экземпляра класса для работы с API сайтов с вакансиями
    hh_api = HeadHunterAPI(URL_GET)

    # Получение вакансий с hh.ru в формате JSON
    hh_vacancies = hh_api.get_vacancies(PARAMS)

    # Получение статуса
    print(hh_api.get_status_code())

    """Запись списка вакансий в файл"""
    with open(FILE_VACANCIES, "w", encoding="utf8") as file:
        vacancies_json = json.dumps(hh_vacancies, ensure_ascii=False)
        file.write(vacancies_json)

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
