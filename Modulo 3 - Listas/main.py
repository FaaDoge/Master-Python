# 1. Definición y Acceso a Listas
# Las listas son colecciones de datos bajo un único nombre, a las que se puede acceder mediante un índice.

# Crear una lista vacía y agregar elementos
pelicula = "Batman"
peliculas = []  # Lista vacía
peliculas.append(pelicula)  # Agregar un elemento a la lista
print("Lista de películas:", peliculas)

# Crear una lista usando la función list()
cantantes = list(("ADO", "YOASOBI"))  # Lista creada con múltiples elementos
print("Lista de cantantes:", cantantes)

# Crear una lista con la función range() para generar secuencias
years = list(range(2000, 2024))  # Generar una lista con valores del 2000 al 2023
print("Lista de años:", years)

# Lista con elementos de distintos tipos
variada = ["Hoka", 34, False]  # Lista con tipos mixtos
print("Lista variada:", variada)

# 2. Acceso y Manipulación de Elementos de la Lista
print("Primer elemento de 'cantantes':", cantantes[0])  # Acceder al primer elemento
print("Último elemento de 'years':", years[-1])  # Acceder al último elemento usando índice negativo

# Modificar elementos en la lista
cantantes[1] = "Queen"  # Cambiar el segundo elemento
print("Lista de cantantes modificada:", cantantes)

# 3. Métodos Comunes para Manipular Listas
# Agregar elementos al final y en una posición específica
peliculas.append("El Señor de los Anillos")  # Agregar al final
peliculas.insert(1, "Matrix")  # Agregar en posición específica
print("Películas después de agregar elementos:", peliculas)

# Eliminar elementos
peliculas.remove("Matrix")  # Eliminar un elemento por su valor
print("Películas después de eliminar 'Matrix':", peliculas)

peliculas.pop()  # Eliminar el último elemento de la lista
print("Películas después de eliminar el último elemento:", peliculas)

# Ordenar la lista
peliculas.sort()  # Ordenar en orden ascendente
print("Películas ordenadas:", peliculas)

# Revertir el orden de la lista
peliculas.reverse()  # Revertir el orden
print("Películas en orden invertido:", peliculas)

# 4. Otras Operaciones con Listas
# Contar ocurrencias de un valor
frutas = ["manzana", "naranja", "manzana", "pera"]
print("Ocurrencias de 'manzana':", frutas.count("manzana"))

# Encontrar índice de un valor
print("Índice de 'pera':", frutas.index("pera"))

# Copiar una lista
copia_frutas = frutas.copy()  # Copiar lista
print("Copia de frutas:", copia_frutas)

# Extender una lista con otra lista
frutas.extend(["sandía", "fresa"])  # Agregar elementos de otra lista
print("Lista de frutas extendida:", frutas)

# 5. Slicing o Subconjuntos de Listas
# Obtener sublistas usando slicing
print("Primeras dos frutas:", frutas[:2])  # Desde el inicio hasta el segundo elemento
print("Últimas dos frutas:", frutas[-2:])  # Últimos dos elementos
print("Frutas del segundo al cuarto elemento:", frutas[1:4])  # Rango específico

# 6. Comprobar la Existencia de Elementos
# Verificar si un elemento está en la lista
if "manzana" in frutas:
    print("La manzana está en la lista de frutas")

# 7. Longitud de una Lista
# Obtener el número de elementos en la lista
print("Número de frutas:", len(frutas))

# 8. Aplicar Funciones a Listas Numéricas
numeros = [10, 20, 30, 40]
print("Máximo:", max(numeros))  # Valor máximo
print("Mínimo:", min(numeros))  # Valor mínimo
print("Suma de todos los elementos:", sum(numeros))  # Suma total

# 9. Uso de List Comprehensions
# Crear una lista de números pares del 0 al 10
pares = [x for x in range(11) if x % 2 == 0]
print("Números pares del 0 al 10:", pares)

# Crear una lista de cuadrados
cuadrados = [x**2 for x in range(5)]
print("Cuadrados de los primeros cinco números:", cuadrados)

# Crear una lista de cadenas en mayúsculas
mayusculas = [fruta.upper() for fruta in frutas]
print("Frutas en mayúsculas:", mayusculas)

# 10. Funciones de Orden Superior en Listas
# map() para transformar cada elemento
cuadrados = list(map(lambda x: x**2, numeros))
print("Cuadrados usando map():", cuadrados)

# filter() para filtrar elementos
mayores_que_15 = list(filter(lambda x: x > 15, numeros))
print("Números mayores que 15 usando filter():", mayores_que_15)

# reduce() para reducir la lista a un solo valor
from functools import reduce
producto_total = reduce(lambda x, y: x * y, numeros)
print("Producto de todos los elementos usando reduce():", producto_total)