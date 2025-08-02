from src.category import Category
from src.product import Product, Smartphone, LawnGrass
from src.data_loader import load_categories_from_json


def main():
    try:
        # 1. Демонстрация создания нового товара
        print("=== Создание новых товаров ===")
        product_data = {
            'name': 'Xiaomi Redmi Note 12',
            'description': 'Смартфон',
            'price': 25000,
            'quantity': 10
        }

        # Создаем новый товар
        new_product = Product.new_product(product_data)
        print(f"Создан товар: {new_product.name}, {new_product.price} руб.")

        # 2. Демонстрация обновления существующего товара
        print("\n=== Обновление существующего товара ===")
        existing_products = [new_product]
        updated_product = Product.new_product(
            {'name': 'Xiaomi Redmi Note 12', 'price': 27000, 'quantity': 5},
            existing_products
        )
        print(
            f"Обновленный товар: {updated_product.name}, {updated_product.price} руб., Остаток: {updated_product.quantity} шт.")

        # 3. Работа с категориями
        print("\n=== Работа с категориями ===")
        electronics = Category("Электроника", "Техника", [])

        # Добавляем товар через словарь
        electronics.add_product({
            'name': 'Наушники Sony',
            'price': 15000,
            'quantity': 8
        })

        # Добавляем такой же товар с другой ценой и количеством
        electronics.add_product({
            'name': 'Наушники Sony',
            'price': 13000,
            'quantity': 4
        })

        print("\nТовары в категории:")
        print(electronics.products)

        # 4. Загрузка из JSON
        print("\n=== Загрузка из JSON ===")
        categories = load_categories_from_json('products.json')
        for category in categories:
            print(f"\nКатегория: {category.name}")
            print(category.products)

        # 5. Статистика
        print("\n=== Статистика ===")
        print(f"Всего категорий: {Category.total_categories}")
        print(f"Всего товаров: {Category.total_products}")

    except Exception as e:
        print(f"Ошибка: {e}")


def demonstrate_inheritance():
    print("\n=== Демонстрация наследования ===")

    # Создаем продукты разных типов
    regular_product = Product("Коврик", "Для мыши", 500, 100)
    smartphone = Smartphone(
        "iPhone 15", "Флагман Apple", 89990, 15,
        "Высокая", "15 Pro", 256, "Титан"
    )
    grass = LawnGrass(
        "Газон Люкс", "Премиум качество", 1500, 200,
        "Германия", 21, "Изумрудный"
    )

    # Создаем категорию с разными типами товаров
    mixed_category = Category("Разные товары", "Разнообразный ассортимент", [
        regular_product,
        smartphone,
        grass
    ])

    # Демонстрация работы
    print("\nТовары в категории:")
    for product in mixed_category:
        print(f"\n{product}\n{'-' * 30}")

    # Проверка наследования функционала
    print(f"\nСуммарная стоимость (коврик + газон): {regular_product + grass} руб.")


if __name__ == "__main__":
    Category.total_categories = 0
    Category.total_products = 0
    main()
    demonstrate_inheritance()
