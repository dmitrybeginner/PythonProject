import pytest
from io import StringIO
from src.product import Product, Order, ZeroQuantityError
from src.category import Category


@pytest.fixture
def sample_product():
    return Product("Test Product", "Test Desc", 100, 5)


@pytest.fixture
def sample_category(sample_product):
    return Category("Test Category", "Test Description", [sample_product])


def test_price_getter(sample_product):
    """Тест геттера цены"""
    assert sample_product.price == 100


def test_negative_price_setter(sample_product, capsys):
    """Тест установки отрицательной цены"""
    sample_product.price = -50
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert sample_product.price == 100


def test_zero_price_setter(sample_product, capsys):
    """Тест установки нулевой цены"""
    sample_product.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert sample_product.price == 100


def test_valid_price_setter(sample_product):
    """Тест корректного изменения цены"""
    sample_product.price = 150
    assert sample_product.price == 150


def test_price_decrease_confirmation(sample_product, monkeypatch):
    """Тест подтверждения понижения цены"""
    monkeypatch.setattr("sys.stdin", StringIO("n\n"))
    sample_product.price = 80
    assert sample_product.price == 100

    monkeypatch.setattr("sys.stdin", StringIO("y\n"))
    sample_product.price = 80
    assert sample_product.price == 80


def test_category_operations(sample_category):
    """Проверка операций с категорией"""
    assert "Test Product, 100 руб. Остаток: 5 шт." in sample_category.products
    sample_category.add_product({"name": "New", "price": 200, "quantity": 3})
    assert len(sample_category.get_products_list()) == 2


def test_creation_logger_mixin(capsys):
    """Тест вывода информации при создании продукта"""
    product = Product("Тестовый продукт", "Описание", 1000, 5)
    captured = capsys.readouterr()
    assert "Создан объект Product с параметрами:" in captured.out
    assert "Класс: Product" in captured.out


def test_product_repr():
    """Тест строкового представления продукта"""
    product = Product("Телефон", "Смартфон", 15000, 3)
    # Изменено: проверяем внутреннее представление с приватными атрибутами
    assert "_Product__price': 15000" in repr(product)
    assert "'name': 'Телефон'" in repr(product)


def test_order_creation(sample_product):
    """Тест создания заказа"""
    order = Order(sample_product, 3)
    assert order.quantity == 3
    assert order.total_cost == 300
    assert "Заказ: Test Product" in str(order)


def test_category_as_base_entity(sample_product):
    """Тест Category как наследника BaseEntity"""
    cat = Category("Test", "Desc", [sample_product])
    assert cat.total_cost == 500
    assert "Категория: Test" in str(cat)


def test_zero_quantity_creation():
    """Тест создания товара с нулевым количеством"""
    with pytest.raises(
        ValueError, match="Товар с нулевым количеством не может быть добавлен"
    ):
        Product("Нулевой товар", "Описание", 100, 0)


def test_category_average_price(sample_product):
    """Тест расчета средней цены"""
    category = Category("Тест", "Описание", [sample_product])
    assert category.average_price() == 100.0

    empty_category = Category("Пустая", "Описание", [])
    assert empty_category.average_price() == 0.0

    products = [
        Product("Товар1", "", 200, 5),
        Product("Товар2", "", 300, 3),
        Product("Товар3", "", 100, 2),
    ]
    category_with_multiple = Category("Мульти", "Описание", products)
    assert category_with_multiple.average_price() == 200.0


def test_zero_quantity_exception(capsys):
    """Тест обработки товара с нулевым количеством в категории"""
    category = Category("Тест", "Описание", [])

    category.add_product({"name": "Нормальный", "price": 100, "quantity": 1})
    captured = capsys.readouterr()
    assert "Товар Нормальный успешно добавлен" in captured.out
    assert "Обработка добавления товара завершена" in captured.out

    category.add_product({"name": "Нулевой", "price": 100, "quantity": 0})
    captured = capsys.readouterr()
    assert "Ошибка: Товар с нулевым количеством не может быть добавлен" in captured.out
    assert "Обработка добавления товара завершена" in captured.out


def test_order_zero_quantity_exception():
    """Тест создания заказа с нулевым количеством"""
    product = Product("Тест", "Описание", 100, 5)

    with pytest.raises(ZeroQuantityError) as exc_info:
        Order(product, 0)

    assert (
        str(exc_info.value) == "Невозможно создать заказ с нулевым количеством товара"
    )


def test_custom_exception_inheritance():
    assert issubclass(ZeroQuantityError, Exception)


if __name__ == "__main__":
    pytest.main()
