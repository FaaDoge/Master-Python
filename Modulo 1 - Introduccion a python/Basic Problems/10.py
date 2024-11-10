# Exercise 10
# Problem: Check if `nombre` contains more than 3 characters, and if `apellido` has more than 5.
nombre = "Fabri"
apellido = "Sanchez"
if len(nombre) > 3:
    if len(apellido) > 5:
        print(f"{nombre} {apellido} has more than 3 characters in the name and more than 5 in the surname.")
    else:
        print(f"{nombre} has more than 3 characters, but {apellido} does not have more than 5.")
else:
    print(f"{nombre} has 3 or fewer characters.")