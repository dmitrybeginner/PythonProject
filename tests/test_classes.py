import pytest
from src.product import Product
from src.category import Category


@pytest.fixture
def sample_products():
    return [
        Product("Product 1", "Description 1", 100.0, 5),
        Product("Product 2", "Description 2", 200.0, 10)
    ]


@pytest.fixture
def sample_category(sample_products):
    return Category("Test Category", "Test description", sample_products)


def test_product_initialization():
    product = Product("Test Product", "Test description", 150.0, 7)
    assert product.name == "Test Product"
    assert product.description == "Test description"
    assert product.price == 150.0
    assert product.quantity == 7


def test_category_initialization(sample_products):
    category = Category("Test Category", "Test description", sample_products)
    assert category.name == "Test Category"
    assert category.description == "Test description"
    assert len(category.products) == 2
    assert category.products[0].name == "Product 1"
    assert category.products[1].price == 200.0


def test_category_counters(sample_category):
    assert Category.total_categories == 1
    assert Category.total_products == 2

    new_product = Product("New Product", "New description", 300.0, 3)
    _ = Category("New Category", "New description", [new_product])

    assert Category.total_categories == 2
    assert Category.total_products == 3


def test_empty_category():
    Category.total_categories = 0
    Category.total_products = 0

    empty_category = Category("Empty", "No products", [])

    assert Category.total_categories == 1
    assert Category.total_products == 0
    assert len(empty_category.products) == 0


def test_duplicate_products_in_categories():
    Category.total_categories = 0
    Category.total_products = 0

    product = Product("Shared", "Shared product", 100.0, 5)

    _ = Category("Cat 1", "Description", [product])
    _ = Category("Cat 2", "Description", [product])

    assert Category.total_categories == 2
    assert Category.total_products == 2
