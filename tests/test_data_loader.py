import pytest
import json
from src.data_loader import load_categories_from_json


@pytest.fixture
def valid_json(tmp_path):
    data = [{
        "name": "Test",
        "description": "Test Desc",
        "products": [{
            "name": "Test Product",
            "price": 100,
            "quantity": 5
        }]
    }]
    file_path = tmp_path / "test.json"
    file_path.write_text(json.dumps(data), encoding='utf-8')
    return file_path


@pytest.fixture
def invalid_json(tmp_path):
    file_path = tmp_path / "invalid.json"
    file_path.write_text("{invalid json}", encoding='utf-8')
    return file_path


def test_valid_json_loading(valid_json):
    categories = load_categories_from_json(valid_json)
    assert len(categories) == 1
    assert categories[0].name == "Test"


def test_invalid_json_loading(invalid_json):
    with pytest.raises(json.JSONDecodeError):
        load_categories_from_json(invalid_json)


def test_missing_file():
    with pytest.raises(FileNotFoundError):
        load_categories_from_json("nonexistent.json")


def test_empty_json(tmp_path):
    empty_file = tmp_path / "empty.json"
    empty_file.touch()
    with pytest.raises(json.JSONDecodeError):
        load_categories_from_json(empty_file)
