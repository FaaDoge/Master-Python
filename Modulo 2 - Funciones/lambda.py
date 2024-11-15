# Las funciones lambda son funciones anónimas (sin nombre), útiles para definir operaciones pequeñas en una sola línea.

# Ejemplo básico de una función lambda con una variable externa
variable = "algo"
dimeAlgo = lambda year: f"{variable} en el año {year}"

# Llamar a la función lambda
print(dimeAlgo(2024))

# Ejemplo 1: Lambda con múltiples parámetros para sumar dos números
suma = lambda x, y: x + y
print("Suma de 5 y 3:", suma(5, 3))

# Ejemplo 2: Lambda para verificar si un número es par o impar
es_par = lambda x: "Par" if x % 2 == 0 else "Impar"
print("El número 4 es:", es_par(4))
print("El número 7 es:", es_par(7))

# Ejemplo 3: Lambda para ordenar una lista de tuplas basada en el segundo elemento de cada tupla
lista = [(1, 'b'), (3, 'a'), (2, 'c')]
lista_ordenada = sorted(lista, key=lambda x: x[1])  # Ordenar por el segundo elemento de cada tupla
print("Lista ordenada por segundo elemento:", lista_ordenada)

# Ejemplo 4: Lambda para filtrar una lista y obtener solo los números mayores a 5
numeros = [1, 6, 8, 3, 9, 2]
mayores_a_5 = list(filter(lambda x: x > 5, numeros))
print("Números mayores a 5:", mayores_a_5)

# Ejemplo 5: Lambda en una lista de funciones para realizar operaciones matemáticas
operaciones = [
    lambda x: x + 2,
    lambda x: x * 2,
    lambda x: x ** 2
]

# Aplicar cada operación a un valor
valor = 3
resultados = [operacion(valor) for operacion in operaciones]
print("Resultados de aplicar operaciones a 3:", resultados)
