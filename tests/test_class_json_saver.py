import pytest
from src.class_vacancy import Vacancy
from src.class_json_saver import JSONSaver


@pytest.fixture
def test_vacancy_object():
    """Создаем экземпляр класса Vacancy."""
    return Vacancy


@pytest.fixture
def test_jsonsaver_object():
    """Создаем экземпляр класса JSONSaver."""
    return JSONSaver


@pytest.fixture
def vacancy_object_sample():
    vac_object = Vacancy("0", "Программист", "Казань", "Все",
                         "И даже больше", 100000, 200000,
                         "руб.", "Facebook", "htts:\\www.facebook.com")
    return vac_object


@pytest.fixture
def test_vacancy_object1():
    vac_object = Vacancy("0", "Программист", "Казань", "Все",
                         "И даже больше", 100000, 200000,
                         "руб.", "Facebook", "htts:\\www.facebook.com")
    return vac_object


@pytest.fixture
def test_vacancy_object2():
    vac_object = Vacancy("0", "Программист", "Казань", "Все",
                         "И даже больше", 90000, 210000,
                         "руб.", "Facebook", "htts:\\www.facebook.com")
    return vac_object


@pytest.fixture
def test_vacancy_object3():
    vac_object = Vacancy("0", "Программист", "Казань", "Все",
                         "И даже больше", 0, 200000,
                         "руб.", "Facebook", "htts:\\www.facebook.com")
    return vac_object


@pytest.fixture
def test_vacancy_object4():
    vac_object = Vacancy("0", "Программист", "Казань", "Все",
                         "И даже больше", 100000, 0,
                         "руб.", "Facebook", "htts:\\www.facebook.com")
    return vac_object


@pytest.fixture
def test_vacancy_object5():
    vac_object = Vacancy("0", "Программист", "Казань", "Все",
                         "И даже больше", 90000, 0,
                         "руб.", "Facebook", "htts:\\www.facebook.com")
    return vac_object


@pytest.fixture
def test_vacancy_object6():
    vac_object = Vacancy("0", "Программист", "Казань", "Все",
                         "И даже больше", 0, 210000,
                         "руб.", "Facebook", "htts:\\www.facebook.com")
    return vac_object


def test_lte_salary1(test_jsonsaver_object, test_vacancy_object1, vacancy_object_sample):
    """Проверка вхождения нижней границы зарлаты в диапазо при наличии верхней."""
    assert test_jsonsaver_object.__lte__(test_vacancy_object1, vacancy_object_sample) is True


def test_gte_salary1(test_jsonsaver_object, test_vacancy_object1, vacancy_object_sample):
    """Проверка вхождения верхней границы зарлаты в диапазо при наличии нижней."""
    assert test_jsonsaver_object.__lte__(test_vacancy_object1, vacancy_object_sample) is True


def test_lte_salary2(test_jsonsaver_object, test_vacancy_object2, vacancy_object_sample):
    """Проверка вхождения нижней границы зарлаты в диапазо при наличии верхней."""
    assert test_jsonsaver_object.__lte__(test_vacancy_object2, vacancy_object_sample) is False


def test_gte_salary2(test_jsonsaver_object, test_vacancy_object2, vacancy_object_sample):
    """Проверка вхождения верхней границы зарлаты в диапазо при наличии нижней."""
    assert test_jsonsaver_object.__lte__(test_vacancy_object2, vacancy_object_sample) is False


def test_lte_salary3(test_jsonsaver_object, test_vacancy_object3, vacancy_object_sample):
    """Проверка вхождения нижней границы зарлаты в диапазо при отсуствии верхней."""
    assert test_jsonsaver_object.__lte__(test_vacancy_object3, vacancy_object_sample) is True


def test_gte_salary3(test_jsonsaver_object, test_vacancy_object4, vacancy_object_sample):
    """Проверка вхождения верхней границы зарлаты в диапазо при отсуствии нижней."""
    assert test_jsonsaver_object.__lte__(test_vacancy_object4, vacancy_object_sample) is True


def test_lte_salary4(test_jsonsaver_object, test_vacancy_object5, vacancy_object_sample):
    """Проверка вхождения нижней границы зарлаты в диапазо при отсуствии верхней."""
    assert test_jsonsaver_object.__lte__(test_vacancy_object5, vacancy_object_sample) is False


def test_gte_salary4(test_jsonsaver_object, test_vacancy_object6, vacancy_object_sample):
    """Проверка вхождения верхней границы зарлаты в диапазо при отсуствии нижней."""
    assert test_jsonsaver_object.__lte__(test_vacancy_object6, vacancy_object_sample) is False
