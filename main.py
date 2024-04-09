from src.class_hh_api import HeadHunterAPI
from src.class_internet_errors import Internet_connection_error
from config import ROOT_DIR

URL_GET = "https://httpbin.org/get"  # используемый адрес для отправки запроса

if __name__ == '__main__':
    try:
        hh_api = HeadHunterAPI(URL_GET)
    except Internet_connection_error:
        print('Отсутсвует подключение к сети Интернет или неверен url - адрес.')
    else:
        print(hh_api.get_vacancies())


