from src.product import Product, BaseEntity, ZeroQuantityError


class Category(BaseEntity):
    """Класс категории товаров"""

    total_categories = 0
    total_products = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

        Category.total_categories += 1
        Category.total_products += len(products)

    def add_product(self, product_data):
        """Добавляет продукт в категорию"""
        try:
            if isinstance(product_data, dict):
                if product_data["quantity"] == 0:
                    raise ZeroQuantityError()
                product = Product.new_product(product_data, self.__products)
            elif isinstance(product_data, Product):
                if product_data.quantity == 0:
                    raise ZeroQuantityError()
                product = product_data
            else:
                raise TypeError(
                    "Необходимо передать объект Product или словарь с данными"
                )

            if product not in self.__products:
                self.__products.append(product)
                Category.total_products += 1
                print(f"Товар {product.name} успешно добавлен")

        except ZeroQuantityError as e:
            print(f"Ошибка: {e}")
        finally:
            print("Обработка добавления товара завершена")

    @property
    def products(self):
        return "\n".join(
            f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт."
            for p in self.__products
        )

    def get_products_list(self):
        return self.__products

    @property
    def total_cost(self):
        return sum(p.price * p.quantity for p in self.__products)

    def __str__(self):
        return (
            f"Категория: {self.name}\n"
            f"Описание: {self.description}\n"
            f"Товаров: {len(self.__products)}\n"
            f"Общая стоимость: {self.total_cost} руб."
        )

    @classmethod
    def from_json(cls, data):
        products = [Product.new_product(p) for p in data["products"]]
        return cls(
            name=data["name"], description=data["description"], products=products
        )

    def average_price(self) -> float:
        try:
            return sum(product.price for product in self.__products) / len(
                self.__products
            )
        except ZeroDivisionError:
            return 0.0
