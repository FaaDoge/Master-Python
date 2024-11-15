nombre = " Fabry "
lista = [3, 1, 4, 1, 5, 9]
numeros = [1, 2, 3, 4]
datos = {"nombre": "Fabry", "edad": 25}

# 1. Funciones de entrada/salida
print("Ejemplo de print con sep y end", sep=" - ", end=".\n")  # Imprime con separador y fin personalizado

edad = input("Ingresa tu edad: ")  # Entrada del usuario
print(f"Edad ingresada: {edad}")

# 2. Funciones de tipo y conversión de tipos
# Identificación de tipo
print("Es string:", isinstance(nombre, str))
print("Tipo de 'nombre':", type(nombre))  # Tipo de variable

# Conversión de tipos
print("Convertir a int:", int("123"))  # Convierte cadena a entero
print("Convertir a float:", float("45.67"))  # Convierte cadena a flotante
print("Convertir a bool:", bool(""))  # False, cadena vacía
print("Convertir a str:", str(123))  # Convierte entero a cadena

# 3. Manipulación de cadenas
print("Cadena sin espacios:", nombre.strip())  # Eliminar espacios alrededor
print("Todo en mayúsculas:", nombre.upper())  # Convertir a mayúsculas
print("Todo en minúsculas:", nombre.lower())  # Convertir a minúsculas
print("Longitud de nombre:", len(nombre))  # Longitud de cadena
print("Empieza con 'F':", nombre.strip().startswith("F"))  # Comprueba el inicio
print("Termina con 'y':", nombre.strip().endswith("y"))  # Comprueba el fin
print("Primera ocurrencia de 'a':", nombre.find("a"))  # Índice de la primera ocurrencia
print("Cantidad de 'a':", nombre.count("a"))  # Contar ocurrencias
print("Separar por espacios:", nombre.split())  # Separar en lista de palabras

# 4. Funciones matemáticas
import math

print("Valor absoluto de -5:", abs(-5))  # Valor absoluto
print("Redondeo de 3.14159:", round(3.14159, 2))  # Redondear a 2 decimales
print("Raíz cuadrada de 16:", math.sqrt(16))  # Raíz cuadrada
print("Potencia de 2^3:", pow(2, 3))  # Potencia
print("Número máximo:", max(10, 20, 30))  # Máximo
print("Número mínimo:", min(10, 20, 30))  # Mínimo

# 5. Funciones de listas y colecciones
print("Longitud de la lista:", len(lista))  # Longitud de lista
print("Elemento máximo en lista:", max(lista))  # Elemento máximo en lista
print("Elemento mínimo en lista:", min(lista))  # Elemento mínimo en lista
print("Suma de elementos de la lista:", sum(lista))  # Suma de los elementos

lista.append(10)  # Agregar elemento al final
print("Lista después de append:", lista)
lista.pop()  # Eliminar último elemento
print("Lista después de pop:", lista)

# 6. Funciones de conjunto (set)
conjunto = set(lista)
print("Conjunto único (sin duplicados):", conjunto)

# 7. Funciones avanzadas de orden superior
# Map para transformar cada elemento
dobles = list(map(lambda x: x * 2, numeros))
print("Dobles de la lista:", dobles)

# Filter para filtrar elementos
pares = list(filter(lambda x: x % 2 == 0, numeros))
print("Números pares de la lista:", pares)

# Zip para combinar listas en pares
lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']
combinado = list(zip(lista1, lista2))
print("Listas combinadas con zip:", combinado)

# Enumerate para obtener índice y valor de cada elemento
for indice, valor in enumerate(lista1):
    print(f"Índice {indice} - Valor {valor}")

# 8. Funciones de control de flujo
print("Todos son verdaderos:", all([True, True, False]))  # Verifica si todos son True
print("Al menos uno es verdadero:", any([True, False, False]))  # Verifica si algún valor es True

# 9. Funciones para manejo de diccionarios
print("Valor de 'edad' en el diccionario:", datos.get("edad", "Desconocido"))  # Obtener valor con valor predeterminado
datos.update({"pais": "Argentina"})  # Agregar clave y valor
print("Diccionario actualizado:", datos)

# 10. Funciones de manejo de archivos
with open("archivo.txt", "w") as archivo:
    archivo.write("Este es un archivo de ejemplo.")  # Escribir en archivo

with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()  # Leer archivo
    print("Contenido del archivo:", contenido)

# 11. Funciones de manipulación de objetos
class Persona:
    pass

persona = Persona()
print("Atributos y métodos de un objeto:", dir(persona))  # Lista de atributos y métodos
print("Es instancia de Persona:", isinstance(persona, Persona))  # Verifica si es instancia de clase

# 12. Funciones de memoria y sistema
print("ID de variable 'nombre':", id(nombre))  # ID de objeto en memoria
print("Tamaño en bytes de 'nombre':", nombre.__sizeof__())  # Tamaño en bytes del objeto
print("Variables globales en el entorno:", globals())  # Variables globales disponibles

# 13. Otras funciones útiles
rango = range(1, 10, 2)
print("Lista de un rango de 1 a 10 con paso de 2:", list(rango))  # Crear una lista de rango
print("Objeto hash de 'nombre':", hash(nombre))  # Hash del objeto

# Búsqueda y orden
lista = [("a", 5), ("b", 1), ("c", 3)]
ordenado_por_valor = sorted(lista, key=lambda x: x[1])
print("Lista de tuplas ordenada por valor:", ordenado_por_valor)

# Funciones para comparar y evaluar expresiones
print("Resultado de eval('3 + 5'):", eval("3 + 5"))  # Evalúa una expresión
#print("Comparación de 5 y 3:", cmp(5, 3)) if 'cmp' in dir() else print("cmp no está en Python 3")

# Funciones para manejo de iteradores
iterador = iter(lista1)  # Crear un iterador
print("Primer elemento del iterador:", next(iterador))  # Obtener el siguiente elemento del iterador

# Funciones para manipulación de bytearray
bytearray_obj = bytearray("Hola", "utf-8")
print("Bytearray de 'Hola':", bytearray_obj)
print("Convertido a string:", bytearray_obj.decode("utf-8"))

# Funciones para trabajar con conjuntos
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union = set1.union(set2)
interseccion = set1.intersection(set2)
print("Unión de dos conjuntos:", union)
print("Intersección de dos conjuntos:", interseccion)

# Funciones de introspección
import inspect

def ejemplo_funcion():
    pass

print("Nombre de la función:", ejemplo_funcion.__name__)
print("Información de la función:", inspect.signature(ejemplo_funcion))

# Funciones para creación de números complejos
complejo = complex(3, 4)
print("Número complejo:", complejo)
print("Parte real:", complejo.real)
print("Parte imaginaria:", complejo.imag)