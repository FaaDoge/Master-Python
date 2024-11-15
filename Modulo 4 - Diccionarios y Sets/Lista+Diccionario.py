# Lista de contactos (diccionarios)
contactos = [
    {'nombre': 'Fabricio', 'numero': 23434},
    {'nombre': 'Jose', 'numero': 213456},
    {'nombre': 'Salo', 'numero': 776665}
]

contactos[0]['nombre'] = 'antonio'


# 1. Imprimir toda la lista de contactos
print("Lista de contactos:")
print(contactos)

# 2. Acceder a un contacto específico por su índice
print("\nAccediendo a un contacto específico por índice:")
contacto_especifico = contactos[1]  # Accede al segundo contacto (Jose)
print(f"Nombre: {contacto_especifico['nombre']}, Número: {contacto_especifico['numero']}")

# 3. Acceder a un contacto específico utilizando un bucle (por ejemplo, buscando por nombre)
print("\nAccediendo a un contacto específico buscando por nombre:")
for contacto in contactos:
    if contacto['nombre'] == 'Jose':
        print(f"Nombre: {contacto['nombre']}, Número: {contacto['numero']}")

# 4. Recorrer toda la lista de contactos
print("\nRecorriendo toda la lista de contactos:")
for contacto in contactos:
    print(f"Nombre: {contacto['nombre']}, Número: {contacto['numero']}")

# 5. Acceder a un contacto y modificar su número (por ejemplo, cambiar el número de 'Salo')
print("\nModificando el número de Salo:")
for contacto in contactos:
    if contacto['nombre'] == 'Salo':
        contacto['numero'] = 999999  # Cambiar el número de Salo
        print(f"Nuevo número de Salo: {contacto['numero']}")

# 6. Eliminar un contacto de la lista (por ejemplo, eliminar 'Fabricio')
print("\nEliminando el contacto de Fabricio:")
contactos = [contacto for contacto in contactos if contacto['nombre'] != 'Fabricio']
print("Lista después de eliminar Fabricio:")
print(contactos)

# 7. Añadir un nuevo contacto a la lista
nuevo_contacto = {'nombre': 'Ana', 'numero': 123456}
contactos.append(nuevo_contacto)
print("\nLista después de añadir un nuevo contacto:")
print(contactos)


contacto_especifico = contactos[1]  # Accede al segundo contacto (Jose)

for contacto in contactos:
    if contacto['nombre'] == 'Jose':
        print(f"Nombre: {contacto['nombre']}, Número: {contacto['numero']}")

for contacto in contactos:
    print(f"Nombre: {contacto['nombre']}, Número: {contacto['numero']}")

for contacto in contactos:
    if contacto['nombre'] == 'Salo':
        contacto['numero'] = 999999  # Cambiar el número de Salo

nuevo_contacto = {'nombre': 'Ana', 'numero': 123456}
contactos.append(nuevo_contacto)
