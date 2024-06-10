import pytest
from praktikum.burger import Burger
from praktikum.database import Database
from unittest.mock import Mock
import ingredient_types
from data import DataTest



@pytest.fixture(scope='function')
def mock_burger_price():
    burger_price = Mock()
    burger_price.get_price.return_value = 200.0
    return burger_price


@pytest.fixture(scope='function')
def mock_bun():
    mock_bun = Mock()
    mock_bun.get_name.return_value = DataTest.BUN_NAME
    mock_bun.get_price.return_value = DataTest.BUN_PRICE
    return mock_bun


@pytest.fixture(scope='function')
def mock_ingredient():
    mock_ingredient = Mock()
    mock_ingredient.get_type.return_value = ingredient_types.INGREDIENT_TYPE_SAUCE
    mock_ingredient.get_name.return_value = ingredient_types.INGREDIENT_TYPE_FILLING
    mock_ingredient.get_price.return_value = DataTest.INGREDIENT_PRICE
    return mock_ingredient
