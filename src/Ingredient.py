class Ingredient:
    def __init__(self, name: str, quantity: float, unit: str) -> None:
        self.name = name
        self.quantity = quantity
        self.unit = unit
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def quantity(self) -> float:
        return self._quantity   

    @property
    def unit(self) -> str:
        return self._unit

    @quantity.setter
    def quantity(self, value: float) -> None:
        if value < 0:
            raise ValueError("Количество должно быть положительным")
        self._quantity = value
    
    def __str__(self):
        return f"{self.name}: {self.quantity} {self.unit}"
    
    def __repr__(self):
        return f"Ingredient('{self._name}', {self._quantity}, '{self._unit}')"
    
    def __eq__(self, other):
        if not isinstance(other, Ingredient):
            return False
        return self._name == other._name and self._unit == other._unit