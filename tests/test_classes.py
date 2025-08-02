import pytest
from io import StringIO
from src.product import Product, Smartphone, LawnGrass
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
    assert sample_product.price == 100  # Цена не изменилась


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
    # Симулируем ввод 'n' (отмена)
    monkeypatch.setattr('sys.stdin', StringIO('n\n'))
    sample_product.price = 80
    assert sample_product.price == 100  # Цена не изменилась

    # Симулируем ввод 'y' (подтверждение)
    monkeypatch.setattr('sys.stdin', StringIO('y\n'))
    sample_product.price = 80
    assert sample_product.price == 80  # Цена изменилась


def test_category_operations(sample_category):
    """Проверка, что старые тесты работают"""
    assert "Test Product, 100 руб. Остаток: 5 шт." in sample_category.products
    sample_category.add_product({'name': 'New', 'price': 200, 'quantity': 3})
    assert len(sample_category.get_products_list()) == 2


def test_add_invalid_product(sample_category):
    """Попытка добавить не-продукт (должна вызывать TypeError)"""
    with pytest.raises(TypeError, match="Можно добавлять только объекты Product или его наследников"):
        sample_category.add_product("Это не продукт")  # Строка вместо продукта

    with pytest.raises(TypeError):
        sample_category.add_product(123)  # Число вместо продукта

    with pytest.raises(TypeError):
        sample_category.add_product([])  # Список вместо продукта


def test_add_valid_subclasses(sample_category):
    """Проверка добавления Smartphone и LawnGrass"""
    smartphone = Smartphone(
        "iPhone 15", "Флагман", 89990, 5,
        "Высокая", "15 Pro", 256, "Титан"
    )
    lawn_grass = LawnGrass(
        "Газон Люкс", "Премиум", 1500, 10,
        "Германия", 21, "Изумрудный"
    )

    sample_category.add_product(smartphone)  # ОК
    sample_category.add_product(lawn_grass)  # ОК

    assert len(sample_category.get_products_list()) == 3  # Был 1 продукт + 2 новых


def test_add_product_with_invalid_type(sample_category, capsys):
    """Попытка добавить в категорию объект, не являющийся Product или его наследником."""
    invalid_objects = ["Not a product", 123, None, {"name": "Dict but not Product"}]

    for obj in invalid_objects:
        with pytest.raises(TypeError, match="Можно добавлять только объекты Product или его наследников"):
            sample_category.add_product(obj)

    # Проверяем, что количество продуктов не изменилось
    assert len(sample_category.get_products_list()) == 1


def test_add_product_with_invalid_type(sample_category):
    """Попытка добавить в категорию объект, не являющийся Product или его наследником."""
    invalid_objects = ["Not a product", 123, None, {"name": "Dict but not Product"}]  # Невалидные данные

    for obj in invalid_objects:
        with pytest.raises((TypeError, ValueError)):
            sample_category.add_product(obj)

    # Проверяем, что количество продуктов не изменилось
    assert len(sample_category.get_products_list()) == 1


if __name__ == "__main__":
    pytest.main()
