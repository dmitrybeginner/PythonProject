from src.product import Product


class Category:
    total_categories = 0
    total_products = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products

        Category.total_categories += 1
        Category.total_products += len(products)

    @classmethod
    def from_json(cls, data):
        products = [Product.from_json(p) for p in data['products']]
        return cls(
            name=data['name'],
            description=data['description'],
            products=products
        )
