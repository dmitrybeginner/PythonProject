import pytest
from io import StringIO
from src.product import Product, Order, Smartphone, LawnGrass
from src.category import Category


@pytest.fixture
def sample_product():
    return Product("Test Product", "Test Desc", 100, 5)


@pytest.fixture
def sample_category(sample_product):
    return Category("Test Category", "Test Description", [sample_product])


def test_price_getter(sample_product):
    assert sample_product.price == 100


def test_negative_price_setter(sample_product, capsys):
    sample_product.price = -50
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert sample_product.price == 100


def test_zero_price_setter(sample_product, capsys):
    sample_product.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert sample_product.price == 100


def test_valid_price_setter(sample_product):
    sample_product.price = 150
    assert sample_product.price == 150


def test_price_decrease_confirmation(sample_product, monkeypatch):
    monkeypatch.setattr('sys.stdin', StringIO('n\n'))
    sample_product.price = 80
    assert sample_product.price == 100

    monkeypatch.setattr('sys.stdin', StringIO('y\n'))
    sample_product.price = 80
    assert sample_product.price == 80


def test_category_operations(sample_category):
    assert "Test Product, 100 руб. Остаток: 5 шт." in sample_category.products
    sample_category.add_product({'name': 'New', 'price': 200, 'quantity': 3})
    assert len(sample_category.get_products_list()) == 2


def test_creation_logger_mixin(capsys):
    product = Product("Тестовый продукт", "Описание", 1000, 5)
    captured = capsys.readouterr()
    assert "Создан объект Product с параметрами:" in captured.out
    assert "Класс: Product" in captured.out


def test_product_repr():
    product = Product("Телефон", "Смартфон", 15000, 3)
    assert "Product({" in repr(product)
    assert "'name': 'Телефон'" in repr(product)


def test_order_creation(sample_product):
    order = Order(sample_product, 3)
    assert order.quantity == 3
    assert order.total_cost == 300
    assert "Заказ: Test Product" in str(order)


def test_category_as_base_entity(sample_product):
    cat = Category("Test", "Desc", [sample_product])
    assert cat.total_cost == 500
    assert "Категория: Test" in str(cat)


def test_category_operations(sample_category):
    """Проверка операций с категорией"""
    assert "Test Product, 100 руб. Остаток: 5 шт." in sample_category.products
    # Добавляем description в тестовые данные
    sample_category.add_product({
        'name': 'New',
        'description': 'New desc',  # Добавлено
        'price': 200,
        'quantity': 3
    })
    assert len(sample_category.get_products_list()) == 2

def test_smartphone_new_product():
    phone_data = {
        'name': 'Galaxy S23',
        'description': 'Flagship smartphone',  # Добавлено
        'price': 799.99,
        'quantity': 5,
        'efficiency': 'Высокая',
        'model': 'S23 Ultra',
        'memory': 512,
        'color': 'Черный'
    }
    phone = Smartphone.new_product(phone_data)
    assert phone.memory == 512
    assert isinstance(phone, Smartphone)

def test_lawn_grass_new_product():
    grass_data = {
        'name': 'Газон Люкс',
        'description': 'Premium grass',  # Добавлено
        'price': 1500,
        'quantity': 20,
        'country': 'Германия',
        'germination_period': 21,
        'color': 'Изумрудный'
    }
    grass = LawnGrass.new_product(grass_data)
    assert grass.germination_period == 21
    assert isinstance(grass, LawnGrass)


if __name__ == "__main__":
    pytest.main()
