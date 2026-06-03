import pytest 
from src.Ingredient import Ingredient
from src.Recipe import Recipe

def test_recipe_empty_init():
    pizza = Recipe("Пицца")
    assert pizza.title == "Пицца"
    assert pizza.ingredients == None

def test_recipe_init():
    flour = Ingredient("Мука", 500, "г")
    sugar = Ingredient("Сахар", 200, "г")
    eggs = Ingredient("Яйцо куриное", 3, "шт")
    cake = Recipe("Торт", [flour, sugar, eggs])
    assert cake.title == "Торт"
    assert cake.ingredients == [flour, sugar, eggs]

def test_recipe_len():
    flour = Ingredient("Мука", 500, "г")
    sugar = Ingredient("Сахар", 200, "г")
    eggs = Ingredient("Яйцо куриное", 3, "шт")
    cake = Recipe("Торт", [flour, sugar, eggs])
    assert len(cake) == 3

def test_recipe_add_same_ingredient():
    flour = Ingredient("Мука", 500, "г")
    sugar = Ingredient("Сахар", 200, "г")
    cake = Recipe("Торт", [flour])
    assert cake.ingredients == [flour]
    cake.add_ingredient(sugar)
    assert cake.ingredients == [flour, sugar]
    
def test_recipe_new_ingredient():
    flour = Ingredient("Мука", 500, "г")
    cake = Recipe("Торт", [flour])
    assert cake.ingredients == [flour]
    eggs_add = Ingredient("Яйцо куриное", 3, "шт")
    cake.add_ingredient(eggs_add)
    assert cake.ingredients == [flour, eggs_add]

def test_recipe_wrong_scale():
    recipe = Recipe("Торт")
    flour = Ingredient("Мука", "500", "г")
    recipe.add_ingredient(flour)
    with pytest.raises(ValueError):
        recipe.scale(-1.0)
    with pytest.raises(ValueError):
        recipe.scale(0)


def test_recipe_scale():
    recipe = Recipe("Торт")
    flour = Ingredient("Мука", "500", "г")
    recipe.add_ingredient(flour)
    new_recipe = recipe.scale(2.0)
    assert new_recipe is not recipe

    assert isinstance(new_recipe, Recipe)

    assert recipe.ingredients == [flour]

