import pytest
from src.models import Product, Category


# Фикстуры для создания объектов
@pytest.fixture
def product1() -> Product:
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def product2() -> Product:
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def product3() -> Product:
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


@pytest.fixture
def category(product1: Product, product2: Product, product3: Product) -> Category:
    return Category(
        "Смартфоны",
        "Смартфоны как средство коммуникации",
        [product1, product2, product3]
    )


# Тесты для класса Product
def test_product_initialization(product1: Product) -> None:
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.price == 180000.0
    assert product1.quantity == 5


# Тесты для класса Category
def test_category_initialization(category: Category) -> None:
    assert category.name == "Смартфоны"
    assert category.description == "Смартфоны как средство коммуникации"
    assert len(category.products) == 3


def test_category_product_count(category: Category) -> None:
    assert Category.product_count == 3


def test_category_count(category: Category) -> None:
    assert Category.category_count == 1
