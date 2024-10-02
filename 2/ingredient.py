class Ingredient:
    def __init__(self, name, weight_raw, weight_cooked, cost) -> None:
        self._name = name
        self._weight_raw = weight_raw
        self._weight_cooked = weight_cooked
        self._cost = cost

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str): raise TypeError
        if value.strip() == '': raise ValueError("Name can't be empty")
        self._name = value

    @property
    def weight_raw(self):
        return self._weight_raw
    
    @weight_raw.setter
    def weight_raw(self, value):
        if not isinstance(value, int): raise TypeError
        if isinstance(value, bool): raise TypeError
        if value <= 0: raise ValueError("Raw weight can't be lower than 0")
        self._weight_raw = value

    @property
    def weight_cooked(self):
        return self._weight_cooked
    
    @weight_cooked.setter
    def weight_cooked(self, value):
        if not isinstance(value, int): raise TypeError
        if isinstance(value, bool): raise TypeError
        if value <= 0: raise ValueError("Cooked weight can't be lower than 0")
        self._weight_cooked = value

    @property
    def cost(self):
        return self._cost
    
    @cost.setter
    def cost(self, value):
        if not isinstance(value, int): raise TypeError
        if isinstance(value, bool): raise TypeError
        if value <= 0: raise ValueError("Cost can't be lower than 0")
        self._cost = value