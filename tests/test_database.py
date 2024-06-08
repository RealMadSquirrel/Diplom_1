from praktikum.database import Database


class TestDatabase:
    database = Database()

    def test_type_of_list_buns_is_list(self):
        assert type(self.database.buns) == list

    def test_type_of_list_ingredients_is_list(self):
        assert type(self.database.ingredients) == list

    def test_available_buns_list_len(self):
        assert len(self.database.available_buns()) == 3

    def test_available_ingredients_list_len(self):
        assert len(self.database.available_ingredients()) == 6
