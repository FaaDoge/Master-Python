"""
Los sets en Python son colecciones de valores únicos que no tienen índice ni orden.

"""

# Definición de un set
personas = {'Jose', 'Fran', 'Fabri'}
print("Set de personas:", personas)

# 1. `add()` - Agregar un elemento al set (si no existe)
personas.add('Carlos')
print("Después de add:", personas)

# 2. `remove()` - Eliminar un elemento del set
# Si el elemento no existe, generará un KeyError. Usar `discard()` si no estás seguro.
personas.remove('Fran')
print("Después de remove:", personas)

# 3. `discard()` - Eliminar un elemento del set, pero no genera error si el elemento no existe
personas.discard('Maria')  # 'Maria' no está en el set, pero no dará error
print("Después de discard:", personas)

# 4. `pop()` - Eliminar y devolver un elemento aleatorio del set
eliminado = personas.pop()
print("Elemento eliminado con pop:", eliminado)
print("Después de pop:", personas)

# 5. `clear()` - Eliminar todos los elementos del set
personas.clear()
print("Después de clear:", personas)

# 6. `union()` - Crear un nuevo set con la unión de dos sets
otros = {'Ana', 'Luis', 'Carlos'}
union_sets = personas.union(otros)
print("Unión de sets:", union_sets)

# 7. `update()` - Agregar todos los elementos de otro set al set original
personas = {'Jose', 'Fabri'}
personas.update(otros)
print("Después de update:", personas)

# 8. `intersection()` - Obtener un nuevo set con los elementos comunes entre dos sets
personas_comunes = personas.intersection(otros)
print("Intersección de sets:", personas_comunes)

# 9. `difference()` - Obtener un nuevo set con los elementos que están en el primer set pero no en el segundo
diferencia_sets = personas.difference(otros)
print("Diferencia de sets:", diferencia_sets)

# 10. `issubset()` - Verificar si todos los elementos del set están en otro set
es_subconjunto = personas.issubset(otros)
print("Es subconjunto de 'otros'?", es_subconjunto)

# 11. `issuperset()` - Verificar si el set contiene todos los elementos de otro set
es_superconjunto = personas.issuperset(otros)
print("Es superconjunto de 'otros'?", es_superconjunto)

# 12. `isdisjoint()` - Verificar si dos sets no tienen elementos en común
no_comunes = personas.isdisjoint(otros)
print("¿No tienen elementos en común?", no_comunes)

# 13. `copy()` - Crear una copia superficial del set
personas_copy = personas.copy()
print("Copia del set:", personas_copy)

# 14. `len()` - Obtener el número de elementos en el set
tamaño = len(personas)
print("Tamaño del set:", tamaño)

# 15. `in` - Verificar si un elemento está presente en el set
esta_en_personas = 'Jose' in personas
print("¿Jose está en el set?", esta_en_personas)