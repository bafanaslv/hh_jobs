import pytest
from src.class_vacancy import Vacancy

prod1 = {
    "name": "Samsung Galaxy C23 Ultra",
    "description": "256GB, Серый цвет, 200MP камера",
    "price": 180000.0,
    "quantity": 5,
    "color": "Серый",
    "capacity": 128.5,
    "model": "C23 Ultra",
    "memory": 64
}
prod2 = {
    "name": "Iphone 15",
    "description": "512GB, Gray space",
    "price": 210000.0,
    "quantity": 8,
    "color": "Gray",
    "capacity": 200.5,
    "model": "15",
    "memory": 64
}
prod3 = {
    "name": "Трава",
    "description": "Газонная",
    "price": 2100.0,
    "quantity": 8,
    "color": "зеленый",
    "country": "Россия",
    "germination": 2
}


@pytest.fixture
def test_product_object1():
    """Создается экземпляр класса Product."""
    return SmartPhone(prod1["name"],
                      prod1["description"],
                      prod1["price"],
                      prod1["quantity"],
                      prod1["color"],
                      prod1["capacity"],
                      prod1["model"],
                      prod1["memory"])


@pytest.fixture
def test_product_object2():
    """Создается экземпляр класса Product."""
    return SmartPhone(prod2["name"],
                      prod2["description"],
                      prod2["price"],
                      prod2["quantity"],
                      prod2["color"],
                      prod2["capacity"],
                      prod2["model"],
                      prod2["memory"])


@pytest.fixture
def test_lawn_object():
    """Создается экземпляр класса Product."""
    return LawnGrass(prod3["name"],
                     prod3["description"],
                     prod3["price"],
                     prod3["quantity"],
                     prod3["color"],
                     prod3["country"],
                     prod3["germination"])


@pytest.fixture
def class_product():
    return SmartPhone("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера",
                      180000.0, 5, "Белый", 234.4, "Ultra", 128)


def test_create_category_objects(test_product_object1):
    """Проверка инициализацииy класса Product."""
    assert test_product_object1.name == "Samsung Galaxy C23 Ultra"
    assert test_product_object1.description == "256GB, Серый цвет, 200MP камера"
    assert test_product_object1.product_price == 180000.0
    assert test_product_object1.quantity == 5


def test_products_add(test_product_object1, test_product_object2, test_lawn_object):
    """Проверка сложение двух товаров."""
    assert test_product_object1 + test_product_object2 == 2580000.0
    with pytest.raises(TypeError):
        test_product_object1 + test_lawn_object


def test_new_product(class_product):
    """Проверка метода добавления нового товара в классе Product."""
    new_product = class_product.new_product(prod2)
    assert new_product.name == "Iphone 15"
    assert new_product.description == "512GB, Gray space"
    assert new_product.product_price == 210000.0
    assert new_product.quantity == 8
