from src.product import Product, BaseEntity


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
        if isinstance(product_data, dict):
            product = Product.new_product(product_data, self.__products)
        elif isinstance(product_data, Product):
            product = product_data
        else:
            raise TypeError("Можно добавлять только объекты Product или словари с данными")

        if product not in self.__products:
            self.__products.append(product)
            Category.total_products += 1

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
        return (f"Категория: {self.name}\n"
                f"Описание: {self.description}\n"
                f"Товаров: {len(self.__products)}\n"
                f"Общая стоимость: {self.total_cost} руб.")

    @classmethod
    def from_json(cls, data):
        products = [Product.new_product(p) for p in data['products']]
        return cls(
            name=data['name'],
            description=data['description'],
            products=products
        )
