# Ejercicio 1: Suma de elementos de la lista
def suma_lista(lista):
    return sum(lista)

# Ejercicio 2: Producto de elementos de la lista
def producto_lista(lista):
    producto = 1
    for num in lista:
        producto *= num
    return producto

# Ejercicio 3: Encontrar el número máximo
def maximo_lista(lista):
    return max(lista)

# Ejercicio 4: Encontrar el número mínimo
def minimo_lista(lista):
    return min(lista)

# Ejercicio 5: Contar las ocurrencias de un número
def contar_ocurrencias(lista, numero):
    return lista.count(numero)

# Ejercicio 6: Eliminar duplicados
def eliminar_duplicados(lista):
    return list(set(lista))

# Ejercicio 7: Sumar los números en las posiciones impares
def suma_posiciones_impares(lista):
    return sum(lista[i] for i in range(1, len(lista), 2))

# Ejercicio 8: Lista de números mayores que un valor dado
def mayores_que(lista, valor):
    return [x for x in lista if x > valor]

# Ejercicio 9: Encontrar los 3 números más grandes
def tres_maximos(lista):
    return sorted(lista, reverse=True)[:3]

# Ejercicio 10: Verificar si una lista es palíndroma
def es_palindromo(lista):
    return "YES" if lista == lista[::-1] else "NO"

# Ejercicio 11: Intersección de dos listas
def interseccion_listas(lista1, lista2):
    return list(set(lista1) & set(lista2))

# Ejercicio 12: Mover ceros al final
def mover_ceros(lista):
    lista_no_ceros = [x for x in lista if x != 0]
    lista_ceros = [0] * (len(lista) - len(lista_no_ceros))
    return lista_no_ceros + lista_ceros

# Ejercicio 13: Multiplicar dos listas elemento por elemento
def multiplicar_listas(lista1, lista2):
    return [a * b for a, b in zip(lista1, lista2)]

# Ejercicio 14: Encontrar el número más frecuente
from collections import Counter
def mas_frecuente(lista):
    return Counter(lista).most_common(1)[0][0]

# Ejercicio 15: Resolver el problema de la mochila (Knapsack problem)
def mochila(pesos, valores, capacidad):
    n = len(pesos)
    dp = [[0] * (capacidad + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacidad + 1):
            if pesos[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - pesos[i - 1]] + valores[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][capacidad]

# Ejercicio 16: Buscar el subarray con la suma máxima
def subarray_maximo(arr):
    max_suma = arr[0]
    suma_actual = arr[0]
    for i in range(1, len(arr)):
        suma_actual = max(arr[i], suma_actual + arr[i])
        max_suma = max(max_suma, suma_actual)
    return max_suma

# Ejercicio 17: Buscar el índice de un valor en una lista
def buscar_indice(lista, valor):
    try:
        return lista.index(valor)
    except ValueError:
        return -1

# Ejercicio 18: Crear una lista de pares de índice y valor
def lista_de_pares(lista):
    return [(i, lista[i]) for i in range(len(lista))]

# Ejercicio 19: Eliminar el elemento que aparece más veces
def eliminar_mas_frecuente(lista):
    cuenta = Counter(lista)
    mas_frecuente = cuenta.most_common(1)[0][0]
    lista.remove(mas_frecuente)
    return lista

# Ejercicio 20: Verificar si una lista tiene elementos únicos
def tiene_elementos_unicos(lista):
    return len(lista) == len(set(lista))

# Ejercicio 21: Encontrar el segundo número más grande
def segundo_maximo(lista):
    lista_unica = list(set(lista))
    lista_unica.sort()
    return lista_unica[-2] if len(lista_unica) > 1 else None

# Ejercicio 22: Unir varias listas en una
def unir_listas(*listas):
    return [item for sublista in listas for item in sublista]

# Ejercicio 23: Dividir una lista en dos sublistas
def dividir_lista(lista):
    mitad = len(lista) // 2
    return lista[:mitad], lista[mitad:]

# Ejercicio 24: Verificar si una lista contiene solo números positivos
def contiene_solo_positivos(lista):
    return all(x > 0 for x in lista)

# Ejercicio 25: Comparar dos listas si son iguales
def son_iguales(lista1, lista2):
    return lista1 == lista2

# Ejercicio 26: Encontrar el índice donde comienza la subsecuencia
def subsecuencia_en_lista(lista, subsecuencia):
    for i in range(len(lista) - len(subsecuencia) + 1):
        if lista[i:i+len(subsecuencia)] == subsecuencia:
            return i
    return -1

# Ejercicio 27: Encontrar la mediana de una lista
def mediana(lista):
    lista.sort()
    n = len(lista)
    if n % 2 == 1:
        return lista[n // 2]
    else:
        return (lista[n // 2 - 1] + lista[n // 2]) / 2

# Ejercicio 28: Calcular el número de combinaciones posibles con 2 elementos de la lista
from math import comb
def combinaciones(lista):
    return comb(len(lista), 2)

# Ejercicio 29: Ordenar una lista de tuplas por el segundo valor
def ordenar_por_segundo(lista):
    return sorted(lista, key=lambda x: x[1])

# Ejercicio 30: Resolver el problema de la suma de subconjuntos (Subset Sum Problem)
def suma_subconjunto(lista, objetivo):
    n = len(lista)
    dp = [[False] * (objetivo + 1) for _ in range(n + 1)]
    dp[0][0] = True
    for i in range(1, n + 1):
        for j in range(objetivo + 1):
            dp[i][j] = dp[i-1][j] or (j >= lista[i-1] and dp[i-1][j-lista[i-1]])
    return dp[n][objetivo]
