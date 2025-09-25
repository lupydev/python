"""
Unpaking con underscore, es una forma de ignorar un valor de un iterable.
"""

super_tuple: tuple[int, str, float, str] = (1, "2", 3.0, "4")

a, _, c, _ = super_tuple

print(a, c)
print(_)

x, *_, y = super_tuple

print(x, y)
print(_)
