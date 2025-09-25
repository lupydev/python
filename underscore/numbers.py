"""
_ no toma ningun valor, lo que nos ayuda es poder entender mejor el tamaño del numero.
"""

number: int = 1000000000000
big_number: int = 1_000_000_000_000

print(
    "number is equal to big_number"
    if number == big_number
    else "number is not equal to big_number"
)
