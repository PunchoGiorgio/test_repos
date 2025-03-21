class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age

class Price:
    def __init__(self, currency, value) -> None:
        self.currency = currency
        self.value = value