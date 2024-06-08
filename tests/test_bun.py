import ingredient_types
from praktikum.bun import Bun
from unittest.mock import Mock


class TestBun:

    bun = Bun(ingredient_types.BUN_NAME, ingredient_types.BUN_PRICE)

    def test_name_of_bun_true(self):
        assert self.bun.name == ingredient_types.BUN_NAME

    def test_price_of_bun_true(self):
        assert self.bun.price == ingredient_types.BUN_PRICE

    def test_get_type_of_name_of_bun_true(self):
        assert type(self.bun.get_name()) == str

    def test_get_type_of_price_of_bun_true(self):
        assert type(self.bun.get_price()) == float

    def test_get_name_of_bun_true(self, mock_bun):
        bun = Bun(mock_bun.get_name.return_value, mock_bun.get_price.return_value)
        assert bun.get_name() == ingredient_types.BUN_NAME

    def test_get_price_of_bun_true(self, mock_bun):
        bun = Bun(mock_bun.get_name.return_value, mock_bun.get_price.return_value)
        assert bun.get_price() == ingredient_types.BUN_PRICE


