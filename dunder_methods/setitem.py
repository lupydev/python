"""
El método __setitem__ es el método que se ejecuta cuando se asigna un valor a un elemento de la instancia de la clase.
"""

from typing import Any


class CustomList:
    def __init__(self, collection: list) -> None:
        self._collection = collection
        self.index = 0

    def __getitem__(self, index: int) -> Any:
        return self._collection[index]

    def __setitem__(self, index: int, value: Any) -> None:
        self._collection[index] = value


custom_list = CustomList([1, 2, 3, 4, 5])

custom_list[0] = 10
print(custom_list[0])
