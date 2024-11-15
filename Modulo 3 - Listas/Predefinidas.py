# Funciones predefinidas de listas en Python

# Lista de ejemplo
frutas = ["manzana", "naranja", "pera", "uva"]

# 1. `append()` - Agregar un elemento al final de la lista
frutas.append("plátano")
print("Después de append:", frutas)

# 2. `extend()` - Agregar múltiples elementos de una lista a otra
frutas.extend(["kiwi", "mango"])
print("Después de extend:", frutas)

# 3. `insert()` - Insertar un elemento en una posición específica
frutas.insert(1, "cereza")  # Insertar "cereza" en la segunda posición
print("Después de insert:", frutas)

# 4. `remove()` - Eliminar la primera ocurrencia de un elemento
frutas.remove("naranja")
print("Después de remove:", frutas)

# 5. `pop()` - Eliminar y devolver el último elemento o el elemento en el índice especificado
ultimo_elemento = frutas.pop()
print("Elemento eliminado con pop:", ultimo_elemento)
print("Después de pop:", frutas)

# 6. `clear()` - Eliminar todos los elementos de la lista
frutas.clear()
print("Después de clear:", frutas)

# 7. `index()` - Obtener el índice del primer elemento encontrado
frutas = ["manzana", "naranja", "pera", "uva"]
indice_pera = frutas.index("pera")
print("Índice de 'pera':", indice_pera)

# 8. `count()` - Contar cuántas veces aparece un elemento en la lista
frutas = ["manzana", "naranja", "pera", "naranja", "uva"]
conteo_naranja = frutas.count("naranja")
print("Número de veces que aparece 'naranja':", conteo_naranja)

# 9. `sort()` - Ordenar los elementos de la lista (modifica la lista en el lugar)
frutas.sort()
print("Después de sort:", frutas)

# 10. `reverse()` - Invertir el orden de los elementos de la lista
frutas.reverse()
print("Después de reverse:", frutas)

# 11. `copy()` - Crear una copia superficial de la lista
frutas_copy = frutas.copy()
print("Copia de la lista:", frutas_copy)

# 12. `len()` - Obtener la longitud de la lista
longitud_frutas = len(frutas)
print("Longitud de la lista:", longitud_frutas)

# 13. `sum()` - Sumar los elementos de una lista (para listas numéricas)
numeros = [1, 2, 3, 4, 5]
suma = sum(numeros)
print("Suma de los números:", suma)

# 14. `min()` - Obtener el elemento mínimo de la lista
minimo = min(numeros)
print("Mínimo de la lista:", minimo)

# 15. `max()` - Obtener el elemento máximo de la lista
maximo = max(numeros)
print("Máximo de la lista:", maximo)

# 16. `all()` - Verificar si todos los elementos de la lista son verdaderos (usado en listas booleanas)
booleanos = [True, True, True]
resultado_all = all(booleanos)
print("¿Todos son verdaderos?", resultado_all)

# 17. `any()` - Verificar si al menos un elemento de la lista es verdadero
booleanos = [False, False, True]
resultado_any = any(booleanos)
print("¿Al menos uno es verdadero?", resultado_any)

# 18. `sorted()` - Devolver una nueva lista ordenada sin modificar la original
frutas_ordenadas = sorted(frutas)
print("Lista ordenada sin modificar la original:", frutas_ordenadas)

# 19. `reversed()` - Devolver una nueva lista con los elementos invertidos
frutas_invertidas = list(reversed(frutas))
print("Lista invertida:", frutas_invertidas)

# 20. `list()` - Convertir un iterable en una lista
rango = list(range(5))
print("Lista creada con list() a partir de un rango:", rango)

# 21. `zip()` - Combinar varias listas en una lista de tuplas
nombres = ["Pedro", "Ana", "Juan"]
edades = [25, 30, 22]
combinados = list(zip(nombres, edades))
print("Listas combinadas con zip:", combinados)

# 22. `filter()` - Filtrar elementos según una condición (devolver solo los que cumplen la condición)
numeros_filtrados = list(filter(lambda x: x > 2, numeros))
print("Numeros mayores que 2:", numeros_filtrados)

# 23. `map()` - Aplicar una función a todos los elementos de la lista
numeros_cuadrados = list(map(lambda x: x**2, numeros))
print("Números elevados al cuadrado:", numeros_cuadrados)

# 24. `enumerate()` - Recorrer la lista y obtener tanto el índice como el valor
for index, fruta in enumerate(frutas):
    print(f"Índice {index}: {fruta}")

# 25. `list comprehension` - Crear una nueva lista a partir de una expresión concisa
frutas_mayusculas = [fruta.upper() for fruta in frutas if len(fruta) > 5]
print("Frutas con más de 5 caracteres en mayúsculas:", frutas_mayusculas)

# 26. in - Buscar un elemento
print('Manzana' in frutas)

