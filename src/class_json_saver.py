import json


class JSONSaver:
    def save_json_file(self, vacancies, json_file):
        with open(json_file, 'w', encoding="UTF-8") as file:
            vacancies_json = json.dumps(vacancies, ensure_ascii=False, indent=4)
            file.write(vacancies_json)
