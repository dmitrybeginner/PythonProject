# Описание проекта

Реализованы 2 класса:

1. **Product** (товар)
   - name: название
   - description: описание  
   - price: цена
   - quantity: количество

2. **Category** (категория)
   - name: название
   - description: описание
   - products: список товаров
   - total_categories: счетчик категорий
   - total_products: счетчик товаров

Дополнительно:
- Загрузка данных из JSON (data_loader.py)
- Тесты для всех компонентов (tests/)
- Проверка стиля кода (flake8)

### Новая функциональность
- Классы-наследники: `Smartphone` и `LawnGrass`.
- Сложение товаров только одного типа (иначе `TypeError`).
- Защита `Category.add_product` от некорректных типов.


### Реализованная функциональность
- Абстрактный класс `BaseProduct` для продуктов
- Миксин `CreationLoggerMixin` для логирования
- Класс `Order` для работы с заказами
- Наследование: `Smartphone` и `LawnGrass` → `Product` → `BaseProduct`
