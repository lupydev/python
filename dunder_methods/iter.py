"""
El método __iter__ es el método que se ejecuta cuando se itera sobre una instancia de la clase.
"""

from typing import Iterator


class CustomList:
    def __init__(self, collection: list) -> None:
        self._collection = collection
        self.index = 0

    def __iter__(self) -> Iterator:
        return iter(self._collection)


custom_list = CustomList([1, 2, 3, 4, 5])

for element in custom_list:
    print(element)
