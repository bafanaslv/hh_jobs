from config import ROOT_DIR
from src.functions import create_vacancies_list
from src.class_json_saver import JSONSaver

VACANCIES_FILE = ROOT_DIR+'/data/vacancies.json'  # json-файл с вакансиями
MY_VACANCIES_FILE = ROOT_DIR+'/data/my_vacancies.json'  # json-файл с моими вакасиями для добавления
URL_GET = "https://api.hh.ru/vacancies"  # адрес HH для отправки запроса

if __name__ == '__main__':
    # vacancy_text - текст запроса на HH
    vacancy_text = input(f'Введите поисковый запрос:\n')
    if len(vacancy_text) > 0:
        # параметры запроса
        params = {'text': vacancy_text, 'area': '113', 'currency': 'RUR', 'per_page': 100, 'page': 0}
        page_quantity = 2  # количество выбираемых страниц

        # create_vacancies_list - функция для формирования списка объектов вакансий vacancies_objects_list
        vacancies_objects_list = create_vacancies_list(params, page_quantity, URL_GET)

        # Создаем объект manager и одновременно получаем список словарей вакансий в новом усеченном формате
        # и сохраняем его а json-файле VACANCIES_FILE
        json_manager = JSONSaver(vacancies_objects_list, VACANCIES_FILE)

        if len(vacancies_objects_list) > 0:
            print("1.Вывести все вакансии\n"
                  "2.Получить топ N вакансий по нижнему уровню зарплаты\n"
                  "3.Получить топ N вакансий по верхнему уровню зарплаты\n"
                  "4.Получить вакансии по региону\n"
                  "5.Получить вакансии с ключевым словом в описании")
            answer = input()  # ввод номера опции выбора
            if answer not in ['1', '2', '3', '4', '5']:
                print('Не выбрана ни одна опция !')
            elif answer == '1':
                # Вывод всех найденных вакансий.
                json_manager.print_vacancies(vacancies_objects_list)
            elif answer == '2' or answer == '3':
                # Выборка топ N вакансий по нижнему уровню зарплаты и вывод.
                sel_obj_list = json_manager.vacancies_top_salary(vacancies_objects_list, 10, VACANCIES_FILE, answer)
                json_manager.print_vacancies(sel_obj_list)
            elif answer == '4':
                # Выборка вакансий по региону и вывод.
                vacancy_text = input(f'Введите нименование региона:\n')
                sel_obj_list = json_manager.select_vacancies_by_region(vacancies_objects_list, vacancy_text, VACANCIES_FILE)
                json_manager.print_vacancies(sel_obj_list)
            elif answer == '5':
                # Выборка вакансий по ключевому слову и вывод.
                vacancy_text = input(f'Введите ключевое слово:\n')
                sel_obj_list = json_manager.select_vacancies_by_word(vacancies_objects_list, vacancy_text, VACANCIES_FILE)
                json_manager.print_vacancies(sel_obj_list)
        else:
            print('По запросу ничего не найдено!')
    else:
        print('Не выбрана ни одна опция !')
