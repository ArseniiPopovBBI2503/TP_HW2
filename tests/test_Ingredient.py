import pytest 
from src.Ingredient import Ingredient

def test_ingredient_init():
    flour = Ingredient("Мука", 500, "г")
    assert flour.name == "Мука"
    assert flour.quantity == 500
    assert flour.unit == "г"

def test_ingredient_wrong_quantity():
    with pytest.raises(ValueError):
        Ingredient("Мука", -1000, "г")

def test_ingredient_str():
    flour = Ingredient("Мука", 500, "г")
    assert str(flour) == "Мука: 500 г"

def test_ingredient_repr():
    flour = Ingredient("Мука", 500, "г")
    assert repr(flour) == "Ingredient('Мука', 500, 'г')"

def test_ingredient_equality():
    flour1 = Ingredient("Мука", 500, "г")
    flour2 = Ingredient("Мука", 500, "г")
    flour3 = Ingredient("Мука", 1, "кг")
    sugar = Ingredient("Сахар", 200, "г")
    assert flour1 == flour2
    assert flour1 != flour3
    assert flour1 != sugar
    