import pytest
from src.product import Product
from src.category import Category


@pytest.fixture
def sample_products():
    return [
        Product("Product1", "Desc1", 100, 5),
        Product("Product2", "Desc2", 200, 3)
    ]


@pytest.fixture
def empty_category():
    return Category("Empty", "Empty Desc", [])


def test_category_creation(sample_products):
    category = Category("Test", "Test Desc", sample_products)
    assert category.name == "Test"
    assert len(category.get_products_list()) == 2


def test_category_str(sample_products):
    category = Category("Test", "Test Desc", sample_products)
    assert str(category) == "Test, количество продуктов: 8 шт."


def test_empty_category_str(empty_category):
    assert str(empty_category) == "Empty, количество продуктов: 0 шт."


def test_add_product_dict(empty_category):
    empty_category.add_product({
        'name': 'New',
        'price': 300,
        'quantity': 2
    })
    assert len(empty_category.get_products_list()) == 1


def test_add_product_object(empty_category):
    product = Product("New", "Desc", 300, 2)
    empty_category.add_product(product)
    assert len(empty_category.get_products_list()) == 1


def test_add_existing_product(sample_products):
    category = Category("Test", "Test Desc", sample_products)
    initial_count = len(category.get_products_list())
    category.add_product({
        'name': 'Product1',
        'price': 150,
        'quantity': 2
    })
    assert len(category.get_products_list()) == initial_count
    assert category.get_products_list()[0].quantity == 7


def test_add_invalid_product(empty_category):
    with pytest.raises(TypeError):
        empty_category.add_product("invalid product")


def test_products_property(sample_products):
    category = Category("Test", "Test Desc", sample_products)
    products_str = category.products
    assert "Product1, 100 руб. Остаток: 5 шт." in products_str
    assert "Product2, 200 руб. Остаток: 3 шт." in products_str


def test_from_json():
    data = {
        'name': 'Test',
        'description': 'Test Desc',
        'products': [
            {
                'name': 'Test Product',
                'price': 100,
                'quantity': 5
            }
        ]
    }
    category = Category.from_json(data)
    assert category.name == "Test"
    assert len(category.get_products_list()) == 1
