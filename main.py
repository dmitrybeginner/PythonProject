from src.models import Product, Category

if __name__ == "__main__":
    # Создание продуктов
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    # Вывод информации о продуктах
    for product in [product1, product2, product3]:
        print(f"{product.name}: {product.price} руб. (Остаток: {product.quantity} шт.)")

    # Создание категории
    smartphones = Category(
        "Смартфоны",
        "Смартфоны как средство коммуникации",
        [product1, product2, product3]
    )

    # Вывод информации о категории
    print(f"\nКатегория: {smartphones.name}")
    print(f"Товаров в категории: {len(smartphones.products)}")
    print(f"Всего категорий: {Category.category_count}")
    print(f"Всего товаров: {Category.product_count}")
