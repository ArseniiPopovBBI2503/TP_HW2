from src.Ingredient import Ingredient
class Recipe:
    def __init__(self, title: str, ingredients: list[Ingredient] = None) -> None:
        self.title = title
        if ingredients is None:
            self.ingredients = []
        else:
            self.ingredients = ingredients
    
    def add_ingredient(self, ingredient: Ingredient):
        is_in_ingredients = False
        for ingr in self.ingredients:
            if ingr.__eq__(ingredient):
                ingr.quantity += ingredient.quantity
                is_in_ingredients = True
                break
        if not is_in_ingredients:
            self.ingredients.append(ingredient)
        
    @staticmethod
    def is_valid_ratio(ratio) -> bool:
        if float(ratio) > 0:
            return True
        return False
    
    def scale(self, ratio: float) -> Recipe:
        if not self.is_valid_ratio(ratio):
            raise ValueError("Коэффициент масштабирования должен быть положительным")
        new_recipe = Recipe(self.title)
        for ingredient in self.ingredients:
            new_quantity = ingredient.quantity * ratio
            new_ingredient = Ingredient(ingredient.name, new_quantity, ingredient.unit)
            new_recipe.add_ingredient(new_ingredient)
        return new_recipe
    
    def __len__(self):
        return len(self.ingredients)
    
    def __str__(self):
        return f"Блюдо: {self.title}\n" + "Ингридиенты: " + "\n".join(str(ingredient) for ingredient in self.ingredients)
