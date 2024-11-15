# Listas dentro de listas con varias dimensiones
# Ejemplo: Lista de contactos donde cada contacto es una lista con nombre y correo electrónico

print("LISTA DE CONTACTOS")
contactos = [
    ['Antonio', 'antonio@gmail.com', '555-1234'],
    ['Luis', 'luis@gmail.com', '555-5678'],
    ['Jose', 'jose@gmail.com', '555-8765']
]

# Imprimir toda la lista de contactos
print("Contactos completos:", contactos)

# 1. Recorrer Lista Multidimensional y Mostrar Cada Dato
for contacto in contactos:
    for detalle in contacto:
        print("Detalle de contacto:", detalle)

# 2. Imprimir Datos en Formato Estructurado
# Accediendo a cada campo por posición
for contacto in contactos:
    nombre = contacto[0]
    email = contacto[1]
    telefono = contacto[2]
    print(f"Nombre: {nombre}, Email: {email}, Teléfono: {telefono}")

# 3. Usar `enumerate` para Mostrar el Índice del Contacto y sus Detalles
for index, contacto in enumerate(contactos):
    print(f"Contacto #{index + 1}:")
    for detalle in contacto:
        print("   ", detalle)

# 4. Agregar un Nuevo Contacto a la Lista
nuevo_contacto = ['Maria', 'maria@gmail.com', '555-9999']
contactos.append(nuevo_contacto)
print("\nLista de contactos después de agregar a Maria:", contactos)

# 5. Acceder a Elementos Específicos
# Por ejemplo, obtener el email de Luis
email_luis = contactos[1][1]  # Segunda lista, segundo elemento
print("El email de Luis es:", email_luis)

# 6. Modificar Información de un Contacto
# Cambiar el teléfono de José
contactos[2][2] = '555-4321'
print("Lista de contactos después de actualizar el teléfono de José:", contactos)

# 7. Eliminar un Contacto Completo
# Eliminar a Antonio
del contactos[0]
print("Lista de contactos después de eliminar a Antonio:", contactos)

# 8. Filtrar Contactos Basado en Condiciones
# Crear una lista con solo los contactos cuyo email contiene "gmail"
contactos_gmail = [contacto for contacto in contactos if "gmail" in contacto[1]]
print("Contactos con emails de Gmail:", contactos_gmail)

# 9. Uso de `index` para Buscar la Posición de un Contacto
# Encontrar el índice de un contacto con nombre "Luis"
for i, contacto in enumerate(contactos):
    if contacto[0] == "Luis":
        print("Índice de Luis en la lista de contactos:", i)

# 10. Crear una Lista de Listas a Partir de Varias Listas Separadas
# Usando `zip` para crear contactos a partir de listas de nombres, emails y teléfonos
nombres = ["Pedro", "Ana", "Clara"]
emails = ["pedro@gmail.com", "ana@hotmail.com", "clara@yahoo.com"]
telefonos = ["555-1010", "555-2020", "555-3030"]

nuevos_contactos = list(zip(nombres, emails, telefonos))
print("Nuevos contactos creados usando zip:", nuevos_contactos)

# 11. Recorrer Contactos con Función Formateada
# Crear una función para imprimir cada contacto en un formato específico
def imprimir_contacto(contacto):
    nombre, email, telefono = contacto
    print(f"Nombre: {nombre} | Email: {email} | Teléfono: {telefono}")

# Usar la función en cada contacto
print("\nLista de contactos formateada:")
for contacto in contactos:
    imprimir_contacto(contacto)
