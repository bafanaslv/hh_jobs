import json
class JSONSaver:
    def save_json_file(self, vacancies, json_file):
        with open(json_file, "w", encoding="utf8") as file:
            vacancies_json = json.dumps(vacancies, ensure_ascii=False)
            file.write(vacancies_json)
