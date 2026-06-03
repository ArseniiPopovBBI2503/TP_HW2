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
    