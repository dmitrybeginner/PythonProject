import pytest
from src.product import Product, Smartphone, LawnGrass


@pytest.fixture
def sample_smartphone():
    return Smartphone(
        "Galaxy S23", "Флагман", 79990, 10,
        "Высокая", "S23 Ultra", 512, "Черный"
    )


@pytest.fixture
def sample_lawn_grass():
    return LawnGrass(
        "Газон Премиум", "Мягкий газон", 1200, 50,
        "Россия", 14, "Зеленый"
    )


def test_smartphone_creation(sample_smartphone):
    """Тест создания смартфона и его свойств"""
    assert sample_smartphone.name == "Galaxy S23"
    assert sample_smartphone.memory == 512
    assert "Производительность: Высокая" in str(sample_smartphone)


def test_lawn_grass_creation(sample_lawn_grass):
    """Тест создания газона и его свойств"""
    assert sample_lawn_grass.country == "Россия"
    assert sample_lawn_grass.germination_period == 14
    assert "Прорастание: 14 дней" in str(sample_lawn_grass)


def test_inheritance_methods(sample_smartphone):
    """Тест наследования от Product и наличия методов"""
    assert isinstance(sample_smartphone, Product)
    assert hasattr(sample_smartphone, "__add__")  # Проверка магического метода


@pytest.mark.parametrize("name, price", [
    ("iPhone 15", 89990),
    ("Xiaomi Note 12", 25000),
])
def test_smartphone_price(name, price):
    """Параметризованный тест цен смартфонов"""
    phone = Smartphone(
        name, "Смартфон", price, 5,
        "Средняя", "Standard", 128, "Синий"
    )
    assert phone.price == price


def test_lawn_grass_invalid_germination_period():
    """Тест на некорректный срок прорастания (должен вызывать ошибку)."""
    with pytest.raises(ValueError, match="Срок прорастания должен быть положительным числом"):
        LawnGrass(
            "Газон", "Тест", 1000, 10,
            "Россия", -5, "Зеленый"  # Отрицательный срок прорастания
        )


def test_add_smartphones(sample_smartphone):
    """Тест сложения смартфонов"""
    phone2 = Smartphone(
        "iPhone 15", "Флагман", 89990, 2,
        "Высокая", "15 Pro", 256, "Титан"
    )
    total = sample_smartphone + phone2
    assert total == 79990 * 10 + 89990 * 2  # Правильный расчет


def test_add_lawn_grass(sample_lawn_grass):
    """Тест сложения газонов"""
    grass2 = LawnGrass(
        "Газон Стандарт", "Обычный", 800, 30,
        "Россия", 10, "Зеленый"
    )
    total = sample_lawn_grass + grass2
    assert total == 1200 * 50 + 800 * 30


def test_add_different_classes(sample_smartphone, sample_lawn_grass):
    """Тест ошибки при сложении разных классов"""
    with pytest.raises(TypeError, match="Нельзя складывать товары разных классов"):
        sample_smartphone + sample_lawn_grass


def test_add_products_same_class():
    """Сложение товаров одного класса (разрешено)."""
    phone1 = Smartphone("Phone A", "Desc", 50000, 2, "High", "X", 128, "Black")
    phone2 = Smartphone("Phone B", "Desc", 70000, 3, "High", "Y", 256, "White")

    grass1 = LawnGrass("Grass A", "Desc", 1000, 5, "Russia", 10, "Green")
    grass2 = LawnGrass("Grass B", "Desc", 1500, 4, "USA", 12, "Blue")

    # Сложение смартфонов
    assert phone1 + phone2 == 50000 * 2 + 70000 * 3  # 100000 + 210000 = 310000

    # Сложение газонов
    assert grass1 + grass2 == 1000 * 5 + 1500 * 4    # 5000 + 6000 = 11000


def test_add_products_different_classes():
    """Попытка сложить товары разных классов (должна вызывать TypeError)."""
    phone = Smartphone("Phone", "Desc", 50000, 2, "High", "X", 128, "Black")
    grass = LawnGrass("Grass", "Desc", 1000, 5, "Russia", 10, "Green")

    with pytest.raises(TypeError, match="Нельзя складывать товары разных классов"):
        phone + grass