from src.functions import create_json_file
from config import ROOT_DIR
from src.class_json_saver import JSONSaver
from src.class_vacancy import Vacancy

VACANCIES_FILE = ROOT_DIR+'/data/vacancies.json'  # json-файл с вакансиями
MY_VACANCIES_FILE = ROOT_DIR+'/data/my_vacancies.json'  # json-файл с моими вакасиями для добавления
URL_GET = "https://api.hh.ru/vacancies"  # адрес для отправки запроса

if __name__ == '__main__':
    params = {'text': 'oracle', 'area': '113', 'currency': 'RUR', 'per_page': 100, 'page': 0}  # параметры запроса
    page_quantity = 2  # количество выбираемых страниц
    json_manager = JSONSaver()
    # create_json_file - функция формирование списка объектов вакансий и сохранения их в json - файле
    vacancies_objects_list = create_json_file(params, page_quantity, URL_GET)

    # получаем список словарей вакансий в новом усеченном формате
    vacancies_dict_list = json_manager.create_vacancies_list(vacancies_objects_list)
    # сохраняем список словарей вакансий в json - файл
    json_manager.save_json_file(vacancies_dict_list, VACANCIES_FILE)
    json_manager.print_vacancies(vacancies_objects_list)
    print(f'Найдено {len(vacancies_dict_list)} вакансий.')

    # добавление списка вакансий из моего json - файла
    json_manager.add_vacancies(Vacancy.max_id, MY_VACANCIES_FILE, VACANCIES_FILE)
    # # Удаление вакансий определенного региона
    # json_saver.del_vacancies("Тверь", VACANCIES_FILE)
    #
    # # Выборка вакансий определенного региона
    # json_saver.select_vacancies("Новый Уренгой", VACANCIES_FILE)
