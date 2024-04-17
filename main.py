from config import ROOT_DIR
from src.functions import create_vacancies_list
from src.class_json_saver import JSONSaver

VACANCIES_FILE = ROOT_DIR+'/data/vacancies.json'  # json-файл с вакансиями
MY_VACANCIES_FILE = ROOT_DIR+'/data/my_vacancies.json'  # json-файл с моими вакасиями для добавления
URL_GET = "https://api.hh.ru/vacancies"  # адрес HH для отправки запроса

if __name__ == '__main__':
    vacancy_name = input(f'Введите поисковый запрос:\n')
    if len(vacancy_name) > 0:
        # параметры запроса
        params = {'text': vacancy_name, 'area': '113', 'currency': 'RUR', 'per_page': 100, 'page': 0}
        page_quantity = 2  # количество выбираемых страниц

        # create_vacancies_list - функция для формирования списка объектов вакансий vacancies_objects_list
        vacancies_objects_list = create_vacancies_list(params, page_quantity, URL_GET)

        # Создаем объект manager и одновременно получаем список словарей вакансий в новом усеченном формате
        # и сохраняем его а json - файле VACANCIES_FILE
        json_manager = JSONSaver(vacancies_objects_list, VACANCIES_FILE)

        if len(vacancies_objects_list) > 0:
            print("1.Вывести все вакансии\n"
                  "2.Получить топ N вакансий по зарплате\n"
                  "3.Получить вакансии по региону\n"
                  "4.Получить вакансии с ключевым словом в описании")
            answer = input()
            if answer not in ['1', '2', '3', '4']:
                answer = '0'
            elif answer == '1':
                # Выборка топ N вакансий
                json_manager.print_vacancies(vacancies_objects_list)
                answer = '0'
            elif answer == '2':
                # Выборка топ N вакансий
                json_manager.select_vacancies_top_salary(vacancies_objects_list, 10, VACANCIES_FILE)
                answer = '0'
            elif answer == '3':
                # Выборка вакансий по региону
                json_manager.select_vacancies_by_region(vacancies_objects_list, "Москва", VACANCIES_FILE)
                answer = '0'
            elif answer == '4':
                # Выборка вакансий по ключевому слову
                json_manager.select_vacancies_by_word(vacancies_objects_list, "sql", VACANCIES_FILE)
#                answer = '0'
        else:
            print('По запросу ничего не найдено!')
    else:
        print('Запрос не введен.')
