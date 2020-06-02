from app.service import firebase
from app.model.model_constants import INGREDIENT_ALL_REF, INGREDIENT_REF

db = firebase.Firebase('firebase')


class Ingredient:

    @staticmethod
    def get_all_ingredients():
        return db.get(INGREDIENT_ALL_REF)

    @staticmethod
    def get_ingredient(name: str):
        return db.get(INGREDIENT_REF.format(name))

    @staticmethod
    def add_ingredient(ingredient_dict: dict):
        db.add(INGREDIENT_ALL_REF, ingredient_dict)
        return ingredient_dict

    @staticmethod
    def add_multiple_ingredients(ingredients_dict: dict):
        # TODO check if this works
        for recipe in ingredients_dict:
            db.add(INGREDIENT_ALL_REF, recipe)
            return ingredients_dict

    @staticmethod
    def replace_ingredient(ingredient_dict: dict):
        db.set(INGREDIENT_ALL_REF, ingredient_dict)
        return ingredient_dict

    @staticmethod
    def update_ingredient(ingredient_dict: dict):
        db.update(INGREDIENT_ALL_REF, ingredient_dict)
        return ingredient_dict

    @staticmethod
    def delete_ingredient(name: str):
        db.delete(INGREDIENT_REF.format(name))
        return name



