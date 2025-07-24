from src.category import Category
from src.data_loader import load_categories_from_json


def main():
    try:
        categories = load_categories_from_json('products.json')

        print("=" * 50)
        print("ЗАГРУЖЕННЫЕ ДАННЫЕ")
        print("=" * 50)

        for category in categories:
            print(f"\nКатегория: {category.name}")
            print(f"Описание: {category.description}")
            print("-" * 50)

            for product in category.products:
                print(f"\nТовар: {product.name}")
                print(f"Описание: {product.description}")
                print(f"Цена: {product.price} руб.")
                print(f"Количество: {product.quantity} шт.")

        print("\n" + "=" * 50)
        print("СТАТИСТИКА")
        print("=" * 50)
        print(f"Всего категорий: {Category.total_categories}")
        print(f"Всего товаров: {Category.total_products}")

    except FileNotFoundError:
        print("Ошибка: файл products.json не найден!")
    except Exception as e:
        print(f"Ошибка: {str(e)}")


if __name__ == "__main__":
    main()
