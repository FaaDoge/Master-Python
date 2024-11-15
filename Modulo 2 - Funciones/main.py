"""
Una función es un bloque de código que realiza una tarea específica, agrupado bajo un nombre,
y que puede reutilizarse al invocarlo varias veces.
"""

# Definir una función que retorna un valor
def funcionConDevolucion():
    return "Resultado de la función"

# Definir una función que no retorna valor, solo realiza una acción
def funcionSinDevolucion(parametro):
    print("El parámetro recibido es:", parametro)

# Invocar las funciones:
resultado = funcionConDevolucion()  # Llamada a la función que retorna un valor
print("Resultado de la función con retorno:", resultado)

funcionSinDevolucion("Fabricio")  # Llamada a la función sin retorno


# Ejemplo de función con parámetros y retorno de valor
def sumar(a, b):
    return a + b

# Ejemplo de función con parámetros sin retorno de valor
def saludar(nombre, edad):
    print(f"Hola, {nombre}. Tienes {edad} años.")

# Ejemplo de función con parámetros predeterminados
def calcular_precio(precio, descuento=0.1):
    return precio * (1 - descuento)

# Invocación de las funciones con distintos tipos de parámetros:
resultado_suma = sumar(5, 3)  # Parámetros pasados: 5 y 3
print("Resultado de sumar:", resultado_suma)

saludar("Fabricio", 25)  # Parámetros pasados: "Fabricio" y 25

precio_final = calcular_precio(100)  # Parámetro con valor predeterminado (10% de descuento)
print("Precio final con descuento predeterminado:", precio_final)

precio_con_descuento = calcular_precio(100, 0.2)  # Descuento especificado (20%)
print("Precio final con descuento especificado:", precio_con_descuento)

# Parámetros opcionales en una función

def getEmpleado(nombre, id=None):
    print("EMPLEADO:")
    # Verificar si se proporcionó un ID; si no, mostrar solo el nombre
    if id is not None:
        print(f"Nombre: {nombre}, ID: {id}")
    else:
        print(f"Nombre: {nombre} (ID no especificado)")

# Llamada a la función con ambos parámetros
getEmpleado("Fabri", "8382838")

# Llamada a la función solo con el parámetro obligatorio
getEmpleado("Fabri")



# Función principal que contiene una función anidada
def calcular_precio_final(precio_base, descuento):
    # Función anidada para calcular el precio con descuento
    def aplicar_descuento(precio, descuento):
        return precio * (1 - descuento)

    # Función anidada para calcular el impuesto
    def aplicar_impuesto(precio):
        impuesto = 0.15  # 15% de impuesto
        return precio * (1 + impuesto)

    # Calcular el precio después de aplicar el descuento y el impuesto
    precio_con_descuento = aplicar_descuento(precio_base, descuento)
    precio_final = aplicar_impuesto(precio_con_descuento)
    
    return precio_final

# Llamar a la función principal
precio = 100
descuento = 0.2  # 20% de descuento
precio_final = calcular_precio_final(precio, descuento)
print("El precio final después de descuento e impuesto es:", precio_final)

