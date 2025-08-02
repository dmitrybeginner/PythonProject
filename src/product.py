from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный базовый класс для всех продуктов"""

    @abstractmethod
    def __init__(self, name, description, price, quantity):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass

    @property
    @abstractmethod
    def price(self):
        pass

    @price.setter
    @abstractmethod
    def price(self, new_price):
        pass


class CreationLoggerMixin:
    """Миксин для логирования создания объектов"""

    def __init__(self, *args, **kwargs):
        print(f"Создан объект {self.__class__.__name__} с параметрами:")
        print(f"Класс: {self.__class__.__name__}")
        print(f"Родительские классы: {self.__class__.__bases__}")
        print(f"Позиционные аргументы: {args}")
        print(f"Именованные аргументы: {kwargs}")
        print("-" * 40)
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f"{self.__class__.__name__}({vars(self)})"


class Product(CreationLoggerMixin, BaseProduct):
    """Основной класс продукта"""

    def __init__(self, name, description, price, quantity):
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")

        super().__init__(
            name=name, description=description, price=price, quantity=quantity
        )
        self.__price = price
        self.__previous_price = price
        self.name = name
        self.description = description
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError("Нельзя складывать товары разных классов")
        return self.price * self.quantity + other.price * other.quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if new_price < self.__price:
            confirmation = input(
                f"Цена понижается с {self.__price} до {new_price}. Подтвердите (y/n): "
            )
            if confirmation.lower() != "y":
                print("Изменение цены отменено")
                return

        self.__previous_price = self.__price
        self.__price = new_price

    @classmethod
    def new_product(cls, product_data, products_list=None):
        name = product_data["name"]
        description = product_data.get("description", "")
        price = product_data["price"]
        quantity = product_data["quantity"]

        if products_list:
            for product in products_list:
                if product.name.lower() == name.lower():
                    product.quantity += quantity
                    product.price = max(product.price, price)
                    if description and not product.description:
                        product.description = description
                    return product

        return cls(name, description, price, quantity)

    @classmethod
    def from_json(cls, data):
        return cls.new_product(data)


class BaseEntity(ABC):
    """Абстрактный базовый класс для сущностей с товарами"""

    @abstractmethod
    def __init__(self, product, quantity):
        pass

    @property
    @abstractmethod
    def total_cost(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Order(BaseEntity):
    """Класс заказа (конкретная реализация)"""

    def __init__(self, product, quantity):
        if quantity <= 0:
            raise ZeroQuantityError(
                "Невозможно создать заказ с нулевым количеством товара"
            )
        self.product = product
        self.quantity = quantity

    @property
    def total_cost(self):
        return self.product.price * self.quantity

    def __str__(self):
        return (
            f"Заказ: {self.product.name}\n"
            f"Количество: {self.quantity}\n"
            f"Итого: {self.total_cost} руб."
        )


class Smartphone(Product):
    """Класс смартфона"""

    def __init__(
        self, name, description, price, quantity, efficiency, model, memory, color
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self):
        base_str = super().__str__()
        return (
            f"{base_str}\n"
            f"Производительность: {self.efficiency}\n"
            f"Модель: {self.model}\n"
            f"Память: {self.memory}GB\n"
            f"Цвет: {self.color}"
        )


class LawnGrass(Product):
    """Класс газонной травы"""

    def __init__(
        self, name, description, price, quantity, country, germination_period, color
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self):
        base_str = super().__str__()
        return (
            f"{base_str}\n"
            f"Страна: {self.country}\n"
            f"Срок прорастания: {self.germination_period} дней\n"
            f"Цвет: {self.color}"
        )


class ZeroQuantityError(Exception):
    """Пользовательское исключение для товаров с нулевым количеством"""

    def __init__(self, message="Товар с нулевым количеством не может быть добавлен"):
        self.message = message
        super().__init__(self.message)
