from src.product import Product
from src.category import Category
from src.data_loader import load_categories_from_json


def main():
    try:
        # 1. Демонстрация работы с продуктами
        print("=== Демонстрация работы с продуктами ===")
        p1 = Product("iPhone 15", "Флагманский смартфон", 79990, 10)
        p2 = Product("MacBook Pro", "Профессиональный ноутбук", 149990, 5)

        print("\nСозданные продукты:")
        print(p1)
        print(p2)

        # Тестирование сложения продуктов
        print(f"\nОбщая стоимость товаров: {p1 + p2} руб.")

        # Тестирование изменения цены
        print("\nПопытка установить отрицательную цену:")
        p1.price = -50000  # Должно вывести сообщение об ошибке
        print(f"Текущая цена iPhone: {p1.price} руб.")  # Цена не изменилась

        # 2. Демонстрация работы с категориями
        print("\n=== Демонстрация работы с категориями ===")
        electronics = Category("Электроника", "Техника и гаджеты", [p1, p2])

        print("\nКатегория:")
        print(electronics)

        print("\nТовары в категории:")
        print(electronics.products)

        # Добавление нового товара
        print("\nДобавляем новый товар:")
        electronics.add_product({
            "name": "AirPods Pro",
            "price": 19990,
            "quantity": 15
        })
        print(electronics)

        # Демонстрация итерации по товарам
        print("\nПеребор товаров в цикле:")
        for product in electronics:
            print(f"- {product.name}: {product.price} руб.")

        # 3. Загрузка данных из JSON
        print("\n=== Загрузка данных из JSON ===")
        categories = load_categories_from_json('products.json')

        for category in categories:
            print(f"\nКатегория: {category.name}")
            print("Товары:")
            for product in category:
                print(f"  - {product}")

    except FileNotFoundError:
        print("\nОшибка: файл products.json не найден!")
    except Exception as e:
        print(f"\nПроизошла ошибка: {str(e)}")

    # Вывод итоговой статистики
    print("\n=== Итоговая статистика ===")
    print(f"Всего категорий: {Category.total_categories}")
    print(f"Всего товаров: {Category.total_products}")


if __name__ == "__main__":
    # Сброс счетчиков перед запуском
    Category.total_categories = 0
    Category.total_products = 0
    main()
