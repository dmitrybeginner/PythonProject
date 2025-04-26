from typing import List


class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Инициализация объекта Product.
        """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    # Атрибуты класса
    category_count = 0  # Количество категорий
    product_count = 0   # Количество товаров

    def __init__(self, name: str, description: str, products: List[Product]):
        """
        Инициализация объекта Category.
        """
        self.name = name
        self.description = description
        self.products = products

        # Увеличиваем количество категорий
        Category.category_count += 1

        # Увеличиваем общее количество товаров
        Category.product_count += len(products)
