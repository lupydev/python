"""
El método __getitem__ es el método que se ejecuta cuando se accede a un elemento de la instancia de la clase.
"""

from typing import Any


class CustomList:
    def __init__(self, collection: list) -> None:
        self._collection = collection
        self.index = 0

    def __getitem__(self, index: int) -> Any:
        return self._collection[index]


custom_list = CustomList([1, 2, 3, 4, 5])

print(custom_list[0])
print(custom_list[1])
print(custom_list[2])
print(custom_list[3])
print(custom_list[4])
