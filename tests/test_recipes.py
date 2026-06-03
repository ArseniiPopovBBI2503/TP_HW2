import pytest
from src.Ingredient import Ingredient
from src.Recipe import Recipe 
from src.ShoppingList import ShoppingList

def test_ingredient_init():
    flour = Ingredient("Мука", 500, "г")
    assert flour.name == "Мука"
    assert flour.quantity == 500.0
    assert flour.unit == "г"

def test_ingredient_wrong_quantity():
    with pytest.raises(ValueError):
        Ingredient("Мука", -1000, "г")

def test_ingredient_str():
    flour = Ingredient("Мука", 500, "г")
    assert str(flour) == "Мука: 500.0 г"

def test_ingredient_repr():
    flour = Ingredient("Мука", 500, "г")
    assert repr(flour) == "Ingredient('Мука', 500.0, 'г')"

def test_ingredient_eq_different_units():
    flour1 = Ingredient("Мука", 1000, "г")
    flour2 = Ingredient("Мука", 1, "кг")
    assert flour1 != flour2

def test_ingredient_eq_different_names():
    flour = Ingredient("Мука", 500, "г")
    sugar = Ingredient("Сахар", 500, "г")
    assert flour != sugar

def test_ingredient_eq_same():
    flour1 = Ingredient("Мука", 500, "г")
    flour2 = Ingredient("Мука", 1000, "г")
    assert flour1 == flour2


def test_recipe_empty_init():
    pizza = Recipe("Пицца")
    assert pizza.title == "Пицца"
    assert pizza.ingredients == []

def test_recipe_init():
    flour = Ingredient("Мука", 500, "г")
    sugar = Ingredient("Сахар", 200, "г")
    eggs = Ingredient("Яйцо куриное", 3, "шт")
    cake = Recipe("Торт", [flour, sugar, eggs])
    assert cake.title == "Торт"
    assert cake.ingredients == [flour, sugar, eggs]

def test_recipe_add_new_ingredient():
    flour = Ingredient("Мука", 500, "г")
    sugar = Ingredient("Сахар", 200, "г")
    cake = Recipe("Торт", [flour])
    assert cake.ingredients == [flour]
    cake.add_ingredient(sugar)
    assert cake.ingredients == [flour, sugar]
    
def test_recipe_same_ingredient():
    flour1 = Ingredient("Мука", 500, "г")
    cake = Recipe("Торт", [flour1])
    assert cake.ingredients == [flour1]
    flour2 = Ingredient("Мука", 500, "г")
    cake.add_ingredient(flour2)
    assert cake.ingredients == [Ingredient("Мука", 1000, "г")]

def test_scale_check_object():
    recipe = Recipe("Пицца")
    cheese = Ingredient("Сыр", 500, "г")
    recipe.add_ingredient(cheese)
    new_recipe = recipe.scale(2.0)
    assert new_recipe is not recipe

def test_scale_check_multiply():
    cake_recipe = Recipe("Торт")
    flour = Ingredient("Мука", 500, "г")
    cake_recipe.add_ingredient(flour)
    new_recipe = cake_recipe.scale(2.0)
    assert new_recipe.ingredients[0].quantity == 1000.0

def test_recipe_wrong_scale():
    recipe = Recipe("Торт")
    flour = Ingredient("Мука", "500", "г")
    recipe.add_ingredient(flour)
    with pytest.raises(ValueError):
        recipe.scale(-1.0)
    with pytest.raises(ValueError):
        recipe.scale(0)

def test_recipe_len():
    flour = Ingredient("Мука", 500, "г")
    sugar = Ingredient("Сахар", 200, "г")
    eggs = Ingredient("Яйцо куриное", 3, "шт")
    cake = Recipe("Торт", [flour, sugar, eggs])
    cake.add_ingredient(Ingredient("Мука", 1, "г"))
    assert len(cake) == 3

def test_ShoppingList_add_recipe_wrong_portions():
    shopping_list = ShoppingList()
    recipe = Recipe("Торт")
    with pytest.raises(ValueError):
        shopping_list.add_recipe(recipe, -1.0)
    with pytest.raises(ValueError):
        shopping_list.add_recipe(recipe, 0)

def test_ShoppingList_add_recipe():
    shopping_list = ShoppingList()
    recipe = Recipe("Торт")
    flour = Ingredient("Мука", 500, "г")
    sugar = Ingredient("Сахар", 400, "г")
    recipe.add_ingredient(flour)
    recipe.add_ingredient(sugar)
    shopping_list.add_recipe(recipe, 2.0)
    assert shopping_list.get_list() == [Ingredient("Мука", 1000.0, "г"), Ingredient("Сахар", 800.0, "г")]



