from Ingredient import Ingredient
from Recipe import Recipe

class DietaryRecipe(Recipe):
    def __init__(self, title: str, diet_type: str,ingredients: list[Ingredient] = None):
        super().__init__(title, ingredients)
        self.diet_type = diet_type
    
    def scale(self, ratio: float) -> DietaryRecipe:
        new_scale = super().scale(ratio)
        new_scale.__class__ = DietaryRecipe
        new_scale.diet_type = self.diet_type
        return new_scale
        
    def __str__(self):
        return f"[{self.diet_type}] Блюдо: {self.title}\n" + "Ингридиенты: " + "\n".join(str(ingredient) for ingredient in self.ingredients)

        
