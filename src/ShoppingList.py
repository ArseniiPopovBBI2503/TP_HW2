from src.Ingredient import Ingredient
from src.Recipe import Recipe

class ShoppingList:
    def __init__(self,):
        self._items = list()
    
    def add_recipe(self, recipe: Recipe, portions: float) -> None:
        if portions <= 0:
            raise ValueError("Количество порций должно быть положительным")
        new_recipe = recipe.scale(portions)
        for ingredient in new_recipe.ingredients:
            self._items.append((ingredient, recipe.title))

    def remove_recipe(self, title:str):
        new_items = list()
        for item in self._items:
            if item[1] != title:
                new_items.append(item)
        self._items = new_items
    
    def get_list(self) -> dict:
        shop_list = {}
        for ingredient, title in self._items:
            key = (ingredient.name, ingredient.unit)
            if key in shop_list:
                shop_list[key].quantity += ingredient.quantity
            else:
                shop_list[key] = Ingredient(ingredient.name, ingredient.quantity, ingredient.unit)
        sorted_items = sorted(shop_list.values(), key=lambda x: x.name)
        return sorted_items

    def __add__(self, other: ShoppingList) -> ShoppingList:
        new_list = ShoppingList()
        new_list._items = self._items + other._items
        return new_list
