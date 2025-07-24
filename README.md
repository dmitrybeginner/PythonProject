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