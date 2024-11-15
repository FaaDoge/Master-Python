# Lista de ejemplo
frutas = ["manzana", "naranja", "pera", "uva"]

# 1. Recorrido Simple Usando un Bucle `for`
for fruta in frutas:
    print("Fruta:", fruta)

# 2. Recorrido Usando `for` con Índices
for i in range(len(frutas)):
    print(f"Fruta en índice {i}:", frutas[i])

# 3. Recorrido Usando `enumerate` para Índice y Valor
for index, fruta in enumerate(frutas):
    print(f"Fruta en índice {index}:", fruta)

# 4. Recorrido Usando `while` con Índices
i = 0
while i < len(frutas):
    print(f"Fruta en índice {i}:", frutas[i])
    i += 1

# 5. Recorrido Inverso Usando Índices Negativos
for i in range(-1, -len(frutas) - 1, -1):
    print("Fruta en recorrido inverso:", frutas[i])

# 6. Recorrido Inverso Usando `reversed`
for fruta in reversed(frutas):
    print("Fruta en orden inverso:", fruta)

# 7. Recorrido Usando Comprensión de Listas
nombres_mayusculas = [fruta.upper() for fruta in frutas]
print("Frutas en mayúsculas:", nombres_mayusculas)

# 8. Filtrado y Recorrido Simultáneo con Comprensión de Listas
frutas_con_a = [fruta for fruta in frutas if "a" in fruta]
print("Frutas con 'a':", frutas_con_a)

# 9. Recorrido de Pares de Elementos con `zip`
precios = [1.5, 2.0, 1.2, 3.0]
for fruta, precio in zip(frutas, precios):
    print(f"{fruta} cuesta {precio}")

# 10. Recorrido Usando `map` para Aplicar Funciones a Cada Elemento
frutas_mayusculas = list(map(lambda x: x.upper(), frutas))
print("Frutas en mayúsculas usando map():", frutas_mayusculas)

# 11. Recorrido Usando `filter` para Filtrar Elementos
frutas_con_a = list(filter(lambda x: "a" in x, frutas))
print("Frutas que contienen 'a' usando filter():", frutas_con_a)

# 12. Recorrido de Lista Anidada
frutas_variantes = [["manzana", "manzana verde"], ["naranja", "naranja roja"], ["pera", "pera amarilla"]]
for grupo in frutas_variantes:
    for variante in grupo:
        print("Variante de fruta:", variante)
