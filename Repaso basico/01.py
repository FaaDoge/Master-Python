# Mostrar un encabezado y un mensaje inicial
print("#######")
print("HOLA MUNDO")

# Comentarios
"""
Comentarios adicionales
"""

# Definir y mostrar variables
suma = 20
nombre = "Ezz"
print(suma, nombre)  # No concatenamos; pasamos parámetros

apellido = "Modesto"
print(nombre, apellido)
print(f"{nombre} {apellido}")  # Interpolación de cadenas con f-strings
print("Hola me llamo {} {}".format(nombre, apellido))

# TIPOS DE DATOS

# Dato nulo o sin valor asignado
nada = None
# Mostrar el tipo de dato
print(type(nada))

# Declaración de diferentes tipos de datos
cadena = "texto"
caracter = 'F'
entero = 21
decimal = 0.75
booleano = False
flotante = 1.2  # Número decimal
lista = [10, 23, 1, 3, 54, 24]
lista_variada = [123, "@#fdsad", 2.3, "3"]
tupla = (23, 324, 324, 234, 3)  # Estructura inmutable
diccionario = {  # Clave-valor, similar a un JSON
    "nombre": "Fabri",
    "apellido": "Sanchez"
}

rango = range(9)  # Tipo de dato rango

"""
Otros tipos de datos:
- Set
- Frozenset
- byte
- bytearray
- memoryview
"""

# Conversión de tipos de datos
print(nombre + " " + str(suma))  # Convertir entero a string

# Conversión entre tipos
# int() - convertir a entero
# float() - convertir a decimal (float)
# ... y otros según el tipo de dato

# Caracteres especiales y escapes
# Uso de comillas dentro de una cadena:
# Ejemplo: "\"texto\"" o ' "texto" '

# Saltos de línea y tabulaciones
"\n"  # Salto de línea
"\t"  # Tabulación
"\r"  # Retorno de carro, elimina el texto a la izquierda

# Operadores aritméticos básicos
"""
Operadores:
- Resta (-)
- Suma (+)
- División (/)
- Multiplicación (*)
- Módulo (%) - Resto de la división
"""

# Operadores de asignación
"""
Operadores de asignación:
- Asignación simple (=)
- Suma y asignación (+=)
- Resta y asignación (-=)
"""

# Incremento y decremento
num = 10
num += 1
num -= 1

# Entrada y salida de datos
nombre = input("Introduce tu nombre: ")
print(f"Tu nombre es {nombre}")

numero2 = int(input("Introduce un número: "))
print(f"Tu número es {numero2}")

# Condicionales
if numero2 > 1:
    print("Es mayor que 1")
elif numero2 == 0:
    print("Es igual a 0")
else:
    print("Es menor que 1")

# Operadores de comparación
"""
Operadores de comparación:
- Igualdad (==)
- Mayor o igual (>=)
- Menor o igual (<=)
- Menor que (<)
- Mayor que (>)
- Diferente (!=)
"""

# Condicionales anidados
if nombre == "Fabri":
    if numero2 > 2:
        print(nombre, numero2)
else:
    print("No coincide con ninguno")


# Operadores Logicos

'''
or
and
!
not

'''