Проект предназначен для выборки вакансий с ресурса Head Hanter по текстовому запросу и только в российских рублях по зарплате если она указана. Результатом запроса является json-файл в усеченном формате с полями наиболее 
уктуальными в запросах. Название вакансии, регион, требования к соискатетелю, должностные обязанности, работодатель, описание вакансии на сайте работодателя, размер зарплаты. 
Пользователю предоставлено меню с различными опциями для выбора вакансий из полученного запроса. Выборка происходит из списка объектов полученных при формировании json-файла и выводится на экран в удобном для пользователя виде.
В приложении так же реализована возможность удаления из первоначально полученного json-файла региона по запросу пользователя, а также добавление в первоначальный json-файл своего json-файла с вакансиями.
Созданы тесты валидации поля должностных обязанностей (responsibility) и диапазона зарплат (salary_form & salary_to), а также тесты проверки вхождения зарплат в некоторый диапазон. 
