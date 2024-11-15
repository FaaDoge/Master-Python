'''
Los diccionarios en Python son colecciones de pares clave-valor. Se utilizan 
cuando necesitas asociar valores con claves únicas. Es similar a un "array asociativo" 
en otros lenguajes o un JSON. 

'''

# Definición de un diccionario
persona = {
    'nombre': 'Fabricio',
    'apellidos': 'Sanchez',
    'edad': 30
}

# Acceder a un valor usando la clave
print("Nombre:", persona['nombre'])

# Métodos y operaciones comunes en diccionarios

# 1. `get()` - Obtener el valor asociado a una clave, devuelve None si la clave no existe
edad = persona.get('edad')
print("Edad:", edad)

# 2. `get()` con valor por defecto - Si la clave no existe, se puede devolver un valor por defecto
ciudad = persona.get('ciudad', 'Desconocida')  # Si 'ciudad' no existe, devuelve 'Desconocida'
print("Ciudad:", ciudad)

# 3. `keys()` - Obtener todas las claves del diccionario
claves = persona.keys()
print("Claves:", claves)

# 4. `values()` - Obtener todos los valores del diccionario
valores = persona.values()
print("Valores:", valores)

# 5. `items()` - Obtener los pares clave-valor del diccionario como una lista de tuplas
items = persona.items()
print("Pares clave-valor:", items)

# 6. `update()` - Actualizar el diccionario con nuevos pares clave-valor
persona.update({'email': 'fabricio@mail.com', 'edad': 31})
print("Después de update:", persona)

# 7. `pop()` - Eliminar y devolver el valor asociado a una clave
apellidos = persona.pop('apellidos')
print("Apellido eliminado:", apellidos)
print("Diccionario después de pop:", persona)

# 8. `popitem()` - Eliminar y devolver un par clave-valor arbitrario
item_eliminado = persona.popitem()
print("Elemento eliminado con popitem:", item_eliminado)
print("Diccionario después de popitem:", persona)

# 9. `clear()` - Eliminar todos los elementos del diccionario
persona.clear()
print("Diccionario después de clear:", persona)

# 10. `del` - Eliminar un par clave-valor usando la clave directamente
persona = {'nombre': 'Fabricio', 'apellidos': 'Sanchez', 'edad': 30}
del persona['edad']
print("Después de del:", persona)

# 11. `copy()` - Crear una copia superficial del diccionario
persona_copy = persona.copy()
print("Copia del diccionario:", persona_copy)

# 12. `len()` - Obtener el número de elementos (pares clave-valor) en el diccionario
tamaño = len(persona)
print("Número de elementos:", tamaño)

# 13. `in` - Verificar si una clave existe en el diccionario
tiene_nombre = 'nombre' in persona
print("¿Contiene 'nombre'?", tiene_nombre)

# 14. `setdefault()` - Obtener el valor asociado a una clave, si no existe, añadir la clave con un valor por defecto
telefono = persona.setdefault('telefono', 'No disponible')
print("Teléfono:", telefono)

# 15. `fromkeys()` - Crear un nuevo diccionario con claves dadas y un valor por defecto
nuevas_claves = ['id', 'nombre', 'edad']
nuevo_dict = dict.fromkeys(nuevas_claves, 'Desconocido')
print("Nuevo diccionario con fromkeys:", nuevo_dict)


# Diccionario de ejemplo
persona = {
    'nombre': 'Fabricio',
    'apellidos': 'Sanchez',
    'edad': 30,
    'email': 'fabricio@mail.com'
}

# 1. Recorrer solo las claves
print("Recorrer solo las claves:")
for clave in persona:
    print(clave)

# 2. Recorrer claves y valores usando `items()`
print("\nRecorrer claves y valores con items():")
for clave, valor in persona.items():
    print(f"{clave}: {valor}")

# 3. Recorrer solo los valores usando `values()`
print("\nRecorrer solo los valores con values():")
for valor in persona.values():
    print(valor)

# 4. Recorrer solo las claves usando `keys()`
print("\nRecorrer solo las claves con keys():")
for clave in persona.keys():
    print(clave)

# 5. Recorrer usando `enumerate()` para obtener el índice y la clave
print("\nRecorrer con enumerate() para obtener índice y clave:")
for idx, clave in enumerate(persona.keys()):
    print(f"Índice {idx}: {clave}")

# 6. Recorrer usando `zip()` para combinar claves y valores
print("\nRecorrer con zip() para combinar claves y valores:")
for clave, valor in zip(persona.keys(), persona.values()):
    print(f"{clave}: {valor}")

