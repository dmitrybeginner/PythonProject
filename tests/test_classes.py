import pytest
from src.product import Product
from src.category import Category
from src.category_iterator import CategoryIterator


@pytest.fixture
def sample_product():
    return Product("Test Product", "Desc", 100, 5)


@pytest.fixture
def sample_category(sample_product):
    return Category("Test Category", "Test Desc", [sample_product])


def test_product_str(sample_product):
    assert str(sample_product) == "Test Product, 100 руб. Остаток: 5 шт."


def test_product_repr(sample_product):
    assert repr(sample_product) == "Product('Test Product', 100, 5)"


def test_product_price_setter(sample_product, capsys):
    sample_product.price = -50
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert sample_product.price == 100


def test_product_addition(sample_product):
    p2 = Product("Another", "Desc", 200, 3)
    assert sample_product + p2 == 100 * 5 + 200 * 3


def test_product_addition_invalid_type(sample_product):
    with pytest.raises(TypeError):
        sample_product + "invalid"


def test_category_str(sample_category):
    assert str(sample_category) == "Test Category, количество продуктов: 5 шт."


def test_category_add_product(sample_category):
    initial_count = len(sample_category.get_products_list())
    sample_category.add_product({"name": "New", "price": 300, "quantity": 2})
    assert len(sample_category.get_products_list()) == initial_count + 1


def test_category_add_existing_product(sample_category):
    initial_count = len(sample_category.get_products_list())
    sample_category.add_product({"name": "Test Product", "price": 150, "quantity": 3})
    assert len(sample_category.get_products_list()) == initial_count  # Количество не изменилось
    assert sample_category.get_products_list()[0].quantity == 8  # 5 + 3


def test_category_iteration(sample_category):
    products = list(sample_category)
    assert len(products) == 1
    assert products[0].name == "Test Product"


def test_category_iterator():
    products = [Product("P1", "D1", 100, 2), Product("P2", "D2", 200, 3)]
    category = Category("Test", "Test", products)
    iterator = CategoryIterator(category)

    assert next(iterator).name == "P1"
    assert next(iterator).price == 200
    with pytest.raises(StopIteration):
        next(iterator)
