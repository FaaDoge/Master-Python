# Ejercicio 1: Función simple que imprime un mensaje
def saludar():
    print("¡Hola, mundo!")

saludar()  # Llamar a la función

# Ejercicio 2: Función con parámetros y valor de retorno
def sumar(a, b):
    return a + b

resultado = sumar(5, 3)
print(f"La suma es: {resultado}")

# Ejercicio 3: Función con un parámetro opcional
def saludar_persona(nombre, saludo="Hola"):
    print(f"{saludo}, {nombre}!")

saludar_persona("Fabricio")  # Usando el valor por defecto
saludar_persona("Jose", "Buenos días")  # Usando un saludo personalizado

# Ejercicio 4: Función que retorna un valor calculado basado en condiciones
def par_o_impar(num):
    if num % 2 == 0:
        return "Es par"
    else:
        return "Es impar"

print(par_o_impar(10))  # Es par
print(par_o_impar(7))   # Es impar

# Ejercicio 5: Función que recibe una lista y devuelve el mayor número
def numero_mayor(lista):
    return max(lista)

print(f"El número mayor en la lista es: {numero_mayor([10, 20, 5, 7])}")

# Ejercicio 6: Función con manejo de errores (división por cero)
def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "No se puede dividir por cero"

print(dividir(10, 2))  # 5.0
print(dividir(10, 0))  # "No se puede dividir por cero"

# Ejercicio 7: Función anónima (lambda) que calcula el cuadrado de un número
cuadrado = lambda x: x ** 2
print(f"Cuadrado de 5: {cuadrado(5)}")  # Devuelve 25

# Ejercicio 8: Función dentro de una función que retorna un valor calculado
def operaciones(a, b):
    def suma(x, y):
        return x + y
    def resta(x, y):
        return x - y
    def multiplicacion(x, y):
        return x * y
    return f"Suma: {suma(a, b)}, Resta: {resta(a, b)}, Multiplicación: {multiplicacion(a, b)}"

print(operaciones(7, 3))

# Ejercicio 9: Función con número variable de parámetros (*args) que devuelve el promedio
def promedio(*numeros):
    return sum(numeros) / len(numeros) if numeros else 0

print(f"Promedio: {promedio(10, 20, 30)}")
print(f"Promedio: {promedio(5, 15, 25, 35)}")

# Ejercicio 10: Función recursiva para calcular el factorial de un número
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(f"Factorial de 5: {factorial(5)}")  # 120

# Ejercicio 11: Función con parámetros keyword (**kwargs) para crear un diccionario dinámico
def crear_usuario(**usuario):
    return usuario

print(crear_usuario(nombre="Fabricio", edad=30, ciudad="Madrid"))

# Ejercicio 12: Función que verifica si un número es primo
def es_primo(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

print(f"Es 7 primo? {es_primo(7)}")  # True
print(f"Es 9 primo? {es_primo(9)}")  # False

# Ejercicio 13: Función que realiza operaciones matemáticas con varios valores usando **kwargs
def operaciones_matematicas(**valores):
    resultado = {
        'suma': sum(valores.values()),
        'promedio': sum(valores.values()) / len(valores) if valores else 0
    }
    return resultado

print(operaciones_matematicas(a=1, b=2, c=3, d=4))  # {'suma': 10, 'promedio': 2.5}

# Ejercicio 14: Función que recibe una lista de diccionarios y retorna el nombre con el número más alto
def obtener_contacto_mayor(contactos):
    mayor = max(contactos, key=lambda x: x['numero'])
    return mayor

contactos = [
    {'nombre': 'Fabricio', 'numero': 23434},
    {'nombre': 'Jose', 'numero': 213456},
    {'nombre': 'Salo', 'numero': 776665},
]
print(obtener_contacto_mayor(contactos))

# Ejercicio 15: Función que maneja un conjunto de operaciones (suma, resta, multiplicación, división) y elige una con base en un parámetro
def operaciones_complejas(a, b, operacion):
    if operacion == "suma":
        return a + b
    elif operacion == "resta":
        return a - b
    elif operacion == "multiplicación":
        return a * b
    elif operacion == "división":
        if b == 0:
            return "Error: División por cero"
        return a / b
    else:
        return "Operación no válida"

print(operaciones_complejas(10, 5, "suma"))  # 15
print(operaciones_complejas(10, 5, "división"))  # 2.0
print(operaciones_complejas(10, 0, "división"))  # Error: División por cero
