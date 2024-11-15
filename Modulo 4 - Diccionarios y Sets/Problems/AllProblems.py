# 1. Buscar un valor en un diccionario
def buscar_en_diccionario(diccionario, clave):
    return diccionario.get(clave, "No encontrado")


# 2. Contar ocurrencias de palabras
def contar_palabras(lista_palabras):
    ocurrencias = {}
    for palabra in lista_palabras:
        ocurrencias[palabra] = ocurrencias.get(palabra, 0) + 1
    return ocurrencias


# 3. Obtener las claves de un diccionario
def obtener_claves(diccionario):
    return list(diccionario.keys())


# 4. Filtrar valores de un diccionario
def filtrar_por_valor(diccionario, umbral):
    return {k: v for k, v in diccionario.items() if v > umbral}


# 5. Invertir un diccionario (intercambiar claves y valores)
def invertir_diccionario(diccionario):
    return {v: k for k, v in diccionario.items()}


# 6. Comprobar si una clave está presente en un diccionario
def clave_presente(diccionario, clave):
    return clave in diccionario


# 7. Unir dos diccionarios
def unir_diccionarios(dic1, dic2):
    return {**dic1, **dic2}


# 8. Obtener el valor máximo de un diccionario
def maximo_diccionario(diccionario):
    return max(diccionario.values()) if diccionario else None


# 9. Obtener el promedio de los valores en un diccionario
def promedio_valores(diccionario):
    if not diccionario:
        return 0
    return sum(diccionario.values()) / len(diccionario)


# 10. Eliminar una clave de un diccionario
def eliminar_clave(diccionario, clave):
    diccionario.pop(clave, None)
    return diccionario


# 11. Crear un diccionario con el índice de las palabras en una lista
def diccionario_indice(lista):
    return {palabra: i for i, palabra in enumerate(lista)}


# 12. Verificar si un valor existe en algún diccionario
def valor_en_diccionario(diccionario, valor):
    return valor in diccionario.values()


# 13. Resolver el problema de las parejas de claves y valores iguales
def pareja_clave_valor_igual(diccionario):
    return [k for k, v in diccionario.items() if k == v]


# 14. Ordenar un diccionario por sus valores
def ordenar_diccionario_por_valor(diccionario):
    return dict(sorted(diccionario.items(), key=lambda item: item[1]))


# 15. Contar los elementos únicos en un diccionario
def contar_unicos(diccionario):
    return len(set(diccionario.values()))


# 16. Encontrar el número de elementos comunes entre dos diccionarios
def elementos_comunes(dic1, dic2):
    return len(set(dic1.values()) & set(dic2.values()))


# 17. Resolver el problema de encontrar la diferencia entre dos sets
def diferencia_sets(set1, set2):
    return set1 - set2


# 18. Crear un set de números aleatorios sin repeticiones
def crear_set_aleatorio(n):
    import random
    return set(random.sample(range(1, 100), n))


# 19. Comprobar si un set es un subconjunto de otro
def es_subconjunto(set1, set2):
    return set1.issubset(set2)


# 20. Eliminar elementos duplicados de una lista usando un set
def eliminar_duplicados(lista):
    return list(set(lista))


# 21. Comprobar si un valor pertenece a un set
def pertenece_set(s, valor):
    return valor in s


# 22. Crear un set de tuplas a partir de una lista de tuplas
def crear_set_tuplas(lista):
    return set(lista)


# 23. Verificar si un set tiene elementos comunes con otro set
def tiene_comunes(set1, set2):
    return not set1.isdisjoint(set2)


# 24. Resolver el problema de encontrar los elementos únicos en una lista de sets
def elementos_unicos_lista_sets(lista_sets):
    return set.union(*lista_sets)


# 25. Encontrar la intersección de dos sets
def interseccion_sets(set1, set2):
    return set1 & set2


# 26. Contar cuántos elementos en un set son mayores a un valor dado
def contar_mayores_a(set1, valor):
    return sum(1 for x in set1 if x > valor)


# 27. Realizar la diferencia simétrica entre dos sets
def diferencia_simetrica(set1, set2):
    return set1 ^ set2


# 28. Obtener el valor mínimo de un set
def minimo_set(s):
    return min(s) if s else None


# 29. Resolver el problema del conjunto potencia de un set
def conjunto_potencia(s):
    from itertools import combinations
    conjunto = list(s)
    return [set(comb) for i in range(len(conjunto) + 1) for comb in combinations(conjunto, i)]


# 30. Resolver el problema de los anagramas (verificar si dos sets de caracteres son anagramas)
def son_anagramas(set1, set2):
    return sorted(set1) == sorted(set2)


# Ejemplo de ejecución
if __name__ == "__main__":
    # Ejercicio 1
    dic = {"a": 1, "b": 2, "c": 3}
    print(buscar_en_diccionario(dic, "b"))

    # Ejercicio 2
    lista_palabras = ["apple", "banana", "apple", "apple", "banana"]
    print(contar_palabras(lista_palabras))

    # Ejercicio 3
    diccionario = {"a": 1, "b": 2, "c": 3}
    print(obtener_claves(diccionario))

    # Ejercicio 4
    diccionario_filtrado = filtrar_por_valor(diccionario, 1)
    print(diccionario_filtrado)

    # Ejercicio 5
    diccionario_invertido = invertir_diccionario(diccionario)
    print(diccionario_invertido)

    # Ejercicio 6
    print(clave_presente(diccionario, "b"))

    # Ejercicio 7
    dic1 = {"a": 1}
    dic2 = {"b": 2}
    print(unir_diccionarios(dic1, dic2))

    # Ejercicio 8
    print(maximo_diccionario(diccionario))

    # Ejercicio 9
    print(promedio_valores(diccionario))

    # Ejercicio 10
    eliminar_clave(diccionario, "a")
    print(diccionario)

    # Ejercicio 11
    lista = ["apple", "banana", "orange"]
    print(diccionario_indice(lista))

    # Ejercicio 12
    print(valor_en_diccionario(diccionario, 2))

    # Ejercicio 13
    diccionario = {"a": 1, "b": 2, "b": 2}
    print(pareja_clave_valor_igual(diccionario))

    # Ejercicio 14
    print(ordenar_diccionario_por_valor(diccionario))

    # Ejercicio 15
    print(contar_unicos(diccionario))

    # Ejercicio 16
    dic1 = {"a": 1, "b": 2}
    dic2 = {"b": 2, "c": 3}
    print(elementos_comunes(dic1, dic2))

    # Ejercicio 17
    set1 = {1, 2, 3}
    set2 = {2, 3, 4}
    print(diferencia_sets(set1, set2))

    # Ejercicio 18
    print(crear_set_aleatorio(5))

    # Ejercicio 19
    print(es_subconjunto({1, 2}, {1, 2, 3}))

    # Ejercicio 20
    print(eliminar_duplicados([1, 2, 2, 3, 3, 4]))

    # Ejercicio 21
    print(pertenece_set({1, 2, 3}, 2))

    # Ejercicio 22
    print(crear_set_tuplas([(1, 2), (3, 4)]))

    # Ejercicio 23
    print(tiene_comunes({1, 2}, {2, 3}))

    # Ejercicio 24
    print(elementos_unicos_lista_sets([{1, 2}, {2, 3}, {3, 4}]))

    # Ejercicio 25
    print(interseccion_sets({1, 2, 3}, {3, 4, 5}))

    # Ejercicio 26
    print(contar_mayores_a({1, 2, 3, 4, 5}, 3))

    # Ejercicio 27
    print(diferencia_simetrica({1, 2, 3}, {3, 4, 5}))

    # Ejercicio 28
    print(minimo_set({3, 5, 1}))

    # Ejercicio 29
    print(conjunto_potencia({1, 2}))

    # Ejercicio 30
    print(son_anagramas('abc', 'cab'))
