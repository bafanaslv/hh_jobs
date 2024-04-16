from config import ROOT_DIR
from src.functions import create_json_file
from src.class_json_saver import JSONSaver
from src.class_vacancy import Vacancy

VACANCIES_FILE = ROOT_DIR+'/data/vacancies.json'  # json-файл с вакансиями
MY_VACANCIES_FILE = ROOT_DIR+'/data/my_vacancies.json'  # json-файл с моими вакасиями для добавления
URL_GET = "https://api.hh.ru/vacancies"  # адрес HH для отправки запроса

if __name__ == '__main__':
    vacancy_name = input(f'Введите поисковый запрос:\n')
    if len(vacancy_name) > 0:
        # параметры запроса
        params = {'text': vacancy_name, 'area': '113', 'currency': 'RUR', 'per_page': 100, 'page': 0}
        page_quantity = 1  # количество выбираемых страниц
        # create_json_file - функция для формирования списка объектов вакансий vacancies_objects_list
        vacancies_objects_list = create_json_file(params, page_quantity, URL_GET)
        # получаем список словарей вакансий vacancies_dict_list в новом усеченном формате
        json_manager = JSONSaver()
        vacancies_dict_list = json_manager.create_vacancies_list(vacancies_objects_list)
        # сохраняем список словарей вакансий vacancies_dict_list в json - файл VACANCIES_FILE
        json_manager.save_json_file(vacancies_dict_list, VACANCIES_FILE)
        if len(vacancies_dict_list) > 0:
            print("1.Вывести все\n2.Сохранить с добавлением своих вакансий\n3.Выбор по городу\n4.С удалением города")
            answer = input()
            if answer not in ['1', '2', '3']:
                answer = '0'
            elif answer == '1':
                json_manager.print_vacancies(vacancies_objects_list)
                print(f'Найдено {len(vacancies_dict_list)} вакансий.\n')
                answer = '0'
            elif answer == '2':
                # добавление списка вакансий VACANCIES_FILE из моего json - файла MY_VACANCIES_FILE
                json_manager.add_vacancies(Vacancy.max_id, MY_VACANCIES_FILE, VACANCIES_FILE)
                answer = '0'
            elif answer == '3':
                # Выборка вакансий определенного региона
                json_manager.select_vacancies("Москва", VACANCIES_FILE)
                answer = '0'
            elif answer == '3':
                # Удаление вакансий определенного региона
                json_manager.del_vacancies("Москва", VACANCIES_FILE)
                answer = '0'

        else:
            print('По запросу ничего не найдено!')

    else:
        print('Запрос не введен.')
