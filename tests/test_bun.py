import ingredient_types
from praktikum.bun import Bun
from unittest.mock import Mock
from data import DataTest


class TestBun:

    bun = Bun(DataTest.BUN_NAME, DataTest.BUN_PRICE)

    def test_name_of_bun_true(self):
        assert self.bun.name == DataTest.BUN_NAME

    def test_price_of_bun_true(self):
        assert self.bun.price == DataTest.BUN_PRICE

    def test_get_type_of_name_of_bun_true(self):
        assert type(self.bun.get_name()) == str

    def test_get_type_of_price_of_bun_true(self):
        assert type(self.bun.get_price()) == float

    def test_get_name_of_bun_true(self, mock_bun):
        assert self.bun.get_name() == DataTest.BUN_NAME

    def test_get_price_of_bun_true(self, mock_bun):
        assert self.bun.get_price() == DataTest.BUN_PRICE


