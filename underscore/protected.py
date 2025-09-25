"""
Los atributos protegidos son aquellos que no son privados, pero no se deben usar fuera de la clase. Normalmente se usan para atributos que no se deben modificar fuera de la clase y se representan con un underscore. esto es una convención.
"""

from uuid import uuid4


class User:
    def __init__(self, name: str, email: str, password: str):
        self._id = uuid4()
        self.name = name
        self.email = email
        self.password = password

    def __str__(self):
        return f"User(id={self._id}, name={self.name}, email={self.email}, password={self.password})"


user = User(
    name="John Doe",
    email="john.doe@example.com",
    password="123456",
)
print(user)
print(user._id)

"""
Los atributos privados son aquellos que no se deben usar fuera de la clase. Normalmente se usan para atributos que no se deben modificar fuera de la clase y se representan con dos underscores. esto es una convención.
"""


class Car:
    def __init__(self, brand: str, model: str, year: int):
        self.__id = uuid4()
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self):
        return f"Car(id={self.__id}, brand={self.brand}, model={self.model}, year={self.year})"

    def __get_id(self):
        """
        Este método es privado y no se debe usar fuera de la clase.
        """
        return self.__id


car = Car(brand="Toyota", model="Corolla", year=2020)
print(car)
print(car.__get_id())  # AttributeError: 'Car' object has no attribute '__get_id'
