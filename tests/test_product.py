import pytest
from src.product import Product


@pytest.fixture
def sample_product():
    return Product("Test", "Description", 100, 5)


def test_product_creation(sample_product):
    assert sample_product.name == "Test"
    assert sample_product.description == "Description"
    assert sample_product.price == 100
    assert sample_product.quantity == 5


def test_product_str(sample_product):
    assert str(sample_product) == "Test, 100 руб. Остаток: 5 шт."


def test_product_repr(sample_product):
    assert repr(sample_product) == "Product('Test', 100, 5)"


def test_price_setter_valid(sample_product, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'y')
    sample_product.price = 150
    assert sample_product.price == 150


def test_price_setter_negative(sample_product, capsys):
    sample_product.price = -50
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert sample_product.price == 100


def test_price_setter_zero(sample_product, capsys):
    sample_product.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert sample_product.price == 100


def test_price_decrease_confirmation_accepted(sample_product, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'y')
    sample_product.price = 90
    assert sample_product.price == 90


def test_price_decrease_confirmation_rejected(sample_product, monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: 'n')
    sample_product.price = 90
    captured = capsys.readouterr()
    assert "Изменение цены отменено" in captured.out
    assert sample_product.price == 100


def test_product_addition(sample_product):
    p2 = Product("Test2", "Desc2", 200, 3)
    assert sample_product + p2 == 100*5 + 200*3


def test_product_addition_invalid_type(sample_product):
    with pytest.raises(TypeError):
        sample_product + "invalid"


def test_new_product_creation():
    product_data = {
        'name': 'New',
        'description': 'New Desc',
        'price': 300,
        'quantity': 2
    }
    product = Product.new_product(product_data)
    assert product.name == "New"
    assert product.price == 300


def test_new_product_update():
    existing = Product("Existing", "Desc", 100, 5)
    updated = Product.new_product(
        {'name': 'Existing', 'price': 150, 'quantity': 3},
        [existing]
    )
    assert updated is existing
    assert updated.price == 150
    assert updated.quantity == 8
