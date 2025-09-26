"""
El método __init__ es el constructor de la clase. Se ejecuta automaticamente cuando se crea una instancia de la clase.
Toma los argumentos que se pasan a la clase y los asigna a los atributos de la instancia.
"""


class User:
    def __init__(self, name: str, email: str, password: str):
        """
        Este método es el constructor de la clase.
        """
        self.name = name
        self.email = email
        self.password = password


user = User(name="John Doe", email="john.doe@example.com", password="123456")
print(user)
