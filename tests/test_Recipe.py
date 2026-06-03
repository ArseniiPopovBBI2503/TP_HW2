import pytest 
from src.Ingredient import Ingredient
from src.Recipe import Recipe

def test_recipe_init():
    flour = Ingredient("Мука", 500, "г")
    sugar = Ingredient("Сахар", 200, "г")
    eggs = Ingredient("Яйцо куриное", 3, "шт")
    cake = Recipe("Торт", [flour, sugar, eggs])
    assert cake.title == "Торт"
    assert cake.ingredients == [flour, sugar, eggs]

def test_recipe_add_ingredient():
    flour = Ingredient("Мука", 500, "г")
    sugar = Ingredient("Сахар", 200, "г")
    cake = Recipe("Торт", [flour])
    cake.add_ingredient(sugar)
    assert cake.ingredients == [flour, sugar]
    flour_add = Ingredient("Мука", 200, "г")
    cake.add_ingredient(flour_add)
    assert cake.ingredients == [Ingredient("Мука", 700, "г"), sugar]
    eggs_add = Ingredient("Яйцо куриное", 3, "шт")
    cake.add_ingredient(eggs_add)
    assert cake.ingredients == [Ingredient("Мука", 700, "г"), sugar, eggs_add]