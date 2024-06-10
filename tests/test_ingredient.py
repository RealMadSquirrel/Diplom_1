from praktikum.ingredient import Ingredient
import ingredient_types
from data import DataTest

class TestIngredient:
    ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_SAUCE, ingredient_types.INGREDIENT_TYPE_FILLING,
                            DataTest.INGREDIENT_PRICE)

    def test_type_of_ingredient_true(self):
        assert self.ingredient.type == ingredient_types.INGREDIENT_TYPE_SAUCE


    def test_name_of_ingredient_true(self):
        assert self.ingredient.name == ingredient_types.INGREDIENT_TYPE_FILLING


    def test_price_of_ingredient_true(self):
        assert self.ingredient.price == DataTest.INGREDIENT_PRICE


    def test_get_price_of_ingredient_true(self):
        assert self.ingredient.get_price() == DataTest.INGREDIENT_PRICE


    def test_get_name_of_ingredient_true(self):
        assert self.ingredient.get_name() == ingredient_types.INGREDIENT_TYPE_FILLING

    def test_get_type_success(self):
        assert self.ingredient.get_type() == ingredient_types.INGREDIENT_TYPE_SAUCE



