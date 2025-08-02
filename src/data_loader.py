import json
from src.category import Category


def load_categories_from_json(file_path):
    """Загружает данные категорий из JSON-файла"""
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return [Category.from_json(category) for category in data]


load_data = load_categories_from_json
