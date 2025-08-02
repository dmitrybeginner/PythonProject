class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price  # Приватный атрибут
        self.quantity = quantity
        self.__previous_price = price  # Для отслеживания изменений цены

    @property
    def price(self):
        """Геттер для цены"""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Сеттер для цены с проверками"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        # Дополнительное задание: подтверждение понижения цены
        if new_price < self.__price:
            confirmation = input(
                f"Цена понижается с {self.__price} до {new_price}. "
                "Подтвердите изменение (y/n): "
            )
            if confirmation.lower() != 'y':
                print("Изменение цены отменено")
                return

        self.__previous_price = self.__price
        self.__price = new_price

    @classmethod
    def new_product(cls, product_data, products_list=None):
        name = product_data['name']
        description = product_data.get('description', '')
        price = product_data['price']
        quantity = product_data['quantity']

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

    def __repr__(self):
        return f"Product('{self.name}', {self.__price}, {self.quantity})"

    def __add__(self, other):
        """Сложение товаров одного класса (по количеству и цене)"""
        if type(self) != type(other):
            raise TypeError("Нельзя складывать товары разных классов")
        total_quantity = self.quantity + other.quantity
        total_price = self.price * self.quantity + other.price * other.quantity
        return total_price


class Smartphone(Product):
    def __init__(self, name, description, price, quantity,
                 efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        """Сложение только смартфонов (наследуется от Product)"""
        return super().__add__(other)

    def __str__(self):
        base_str = super().__str__()
        return (f"{base_str}\n"
                f"Производительность: {self.efficiency}, "
                f"Модель: {self.model}, "
                f"Память: {self.memory}GB, "
                f"Цвет: {self.color}")


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity,
                 country, germination_period, color):
        if germination_period <= 0:
            raise ValueError("Срок прорастания должен быть положительным числом")
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        """Сложение только газонов (наследуется от Product)"""
        return super().__add__(other)

    def __str__(self):
        base_str = super().__str__()
        return (f"{base_str}\n"
                f"Страна: {self.country}, "
                f"Прорастание: {self.germination_period} дней, "
                f"Цвет: {self.color}")
