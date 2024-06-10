from praktikum.burger import Burger
from unittest.mock import Mock
import pytest
import ingredient_types
from data import DataTest


class TestBurger:

    def test_set_bun_none_true(self):
        burger = Burger()
        assert burger.bun is None

    def test_set_ingredients_empty_true(self):
        burger = Burger()
        assert burger.ingredients == []

    def test_set_bun_true(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.return_value = DataTest.BUN_NAME
        burger.set_buns(mock_bun.return_value)
        assert burger.bun == DataTest.BUN_NAME

    def test_get_price_success(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient]
        assert burger.get_price() == DataTest.BUN_PRICE * 2 + DataTest.INGREDIENT_PRICE

    def test_get_receipt_success(self, mock_ingredient, mock_bun):
        burger = Burger()
        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient]
        receipt = f'(==== {DataTest.BUN_NAME} ====)\n' \
                  f'= sauce {ingredient_types.INGREDIENT_TYPE_FILLING} =\n' \
                  f'(==== {DataTest.BUN_NAME} ====)\n' \
                  f'\nPrice: {DataTest.BUN_PRICE * 2 + DataTest.INGREDIENT_PRICE}'
        assert receipt == burger.get_receipt()

    @pytest.mark.parametrize('ingredient', DataTest.INGREDIENT_FOR_BURGERS)
    def test_add_ingredient(self, ingredient):
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.return_value = ingredient
        burger.add_ingredient(mock_ingredient.return_value)
        assert burger.ingredients == [ingredient]

    def test_move_ingredient(self):
        burger = Burger()
        burger.ingredients = DataTest.INGREDIENT_FOR_BURGERS_FOR_MOVE_INGRIDIENTS
        burger.move_ingredient(0, 2)
        assert burger.ingredients == DataTest.INGREDIENT_FOR_BURGERS_MOVED
