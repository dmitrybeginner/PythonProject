import json
import pytest
from src.data_loader import load_categories_from_json
from src.category import Category


@pytest.fixture
def sample_json(tmp_path):
    data = [
        {
            "name": "Test Category",
            "description": "Test description",
            "products": [
                {
                    "name": "Test Product",
                    "description": "Test product desc",
                    "price": 100.0,
                    "quantity": 5
                }
            ]
        }
    ]
    file_path = tmp_path / "test_products.json"
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)
    return file_path


def test_json_loading(sample_json):
    # Сброс счетчиков
    Category.total_categories = 0
    Category.total_products = 0

    categories = load_categories_from_json(sample_json)

    assert len(categories) == 1
    assert categories[0].name == "Test Category"
    assert len(categories[0].get_products_list()) == 1
    assert categories[0].get_products_list()[0].name == "Test Product"
    assert Category.total_categories == 1
    assert Category.total_products == 1
