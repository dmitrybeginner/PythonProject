import pytest
from src.product import Product
from src.category import Category
from src.category_iterator import CategoryIterator


@pytest.fixture
def sample_category():
    products = [
        Product("P1", "D1", 100, 2),
        Product("P2", "D2", 200, 3)
    ]
    return Category("Test", "Test Desc", products)


def test_iterator_creation(sample_category):
    iterator = CategoryIterator(sample_category)
    assert iterator is not None


def test_iterator_next(sample_category):
    iterator = CategoryIterator(sample_category)
    assert next(iterator).name == "P1"
    assert next(iterator).price == 200


def test_iterator_stop(sample_category):
    iterator = CategoryIterator(sample_category)
    next(iterator)
    next(iterator)
    with pytest.raises(StopIteration):
        next(iterator)


def test_empty_category_iteration():
    empty_category = Category("Empty", "Empty Desc", [])
    iterator = CategoryIterator(empty_category)
    with pytest.raises(StopIteration):
        next(iterator)


def test_iterator_repr(sample_category):
    iterator = CategoryIterator(sample_category)
    assert repr(iterator) == f"CategoryIterator({sample_category})"
