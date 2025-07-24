class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __repr__(self):
        return f"Product('{self.name}', {self.__price}, {self.quantity})"

    def __add__(self, other):
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты класса Product")
        return self.__price * self.quantity + other.__price * other.quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if new_price < self.__price:
            confirm = input(
                f"Цена понижается с {self.__price} до {new_price}. "
                "Подтвердите (y/n): "
            )
            if confirm.lower() != 'y':
                print("Изменение цены отменено")
                return

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
