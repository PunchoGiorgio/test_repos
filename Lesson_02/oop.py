class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

class Price:
    def __init__(self, currency: str, value: int) -> None:
        self.currency: str = currency
        self.value: int = value 
