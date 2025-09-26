"""
El método __str__ es el método que se ejecuta cuando se imprime una instancia de la clase.
"""


class User:
    def __init__(self, name: str, email: str, password: str):
        self.name = name
        self.email = email
        self.password = password

    def __str__(self):
        return f"User(name={self.name}, email={self.email}, password={self.password})"


user = User(name="John Doe", email="john.doe@example.com", password="123456")
print(user)
