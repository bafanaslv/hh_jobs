import pytest
from src.class_vacancy import Vacancy


test_salary_item1 = {
    "from": 350000,
    "to": 450000,
    "currency": "RUR"
}
test_salary_item2 = {
    "from": None,
    "to": 450000,
    "currency": "RUR"
}
test_salary_item3 = {
    "from": 100000,
    "to": None,
    "currency": "RUR"
}
test_salary_item4 = None

test_snippet1 = {
    "requirement": "Тест1",
    "responsibility": "Тест1"
}
test_snippet2 = {
    "requirement": "Test1",
    "responsibility": None
}
test_snippet3 = None


@pytest.fixture
def test_vacancy_object():
    """Создаем экземпляр класса Vacancy."""
    return Vacancy


def test_test_snippet(test_vacancy_object):
    """ВАлидация должностных обязанностей."""
    assert test_vacancy_object.responsibility_valid(test_snippet1) == "Тест1"
    assert test_vacancy_object.responsibility_valid(test_snippet2) == "не указан"
    assert test_vacancy_object.responsibility_valid(test_snippet3) == ""


def test_salary_valid(test_vacancy_object):
    """Валидация зарплаты."""
    assert test_vacancy_object.salary_valid(test_salary_item1) == (350000, 450000, "руб.")
    assert test_vacancy_object.salary_valid(test_salary_item2) == (0, 450000, "руб.")
    assert test_vacancy_object.salary_valid(test_salary_item3) == (100000, 0, "руб.")
    assert test_vacancy_object.salary_valid(test_salary_item4) == (0, 0, "")
