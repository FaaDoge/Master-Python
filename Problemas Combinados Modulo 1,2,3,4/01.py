'''
Hacer una lista de 8 numeros enteros
- Recorrer la lista y mostrarla
- Hacer funcion que recorra listas de numeros y devuelva un string
- Ordenarla y mostrarla
- Mostar su longitud
- Buscar algun elemento

'''
lista = [1,4,5,7,12,45,6,34]

def recorrerString():
    resultado = ""
    for item in lista:
        resultado+=str(item)+", "
    return resultado

while True:
    print("SELECCIONE LA OPCION DESEADA")
    print("1. Recorrer la lista y mostrarla")
    print("2. Hacer funcion que recorra listas de numeros y devuelva un string")
    print("3. Ordenarla y mostrarla")
    print("4. Mostar su longitud")
    print("5. Buscar algun elemento")
    op=int(input("\n"))
    if op == 1:
        print("OPCION 1")
        for item in lista:
            print(item)
    elif op == 2:
        print("OPCION 2")
        resultado = recorrerString()
        print(resultado)
    elif op == 3:
        print("OPCION 3")
        lista.sort()
        print(lista)
    elif op == 4:
        print("OPCION 4")
        print(len(lista))
    elif op == 5:
        print("OPCION 5")
        busqueda = int(input("ingrese numero a buscar "))
        if busqueda in lista:
            print(f"existe {busqueda} en la lista en la posicion {lista.index(busqueda)}")
        else:
            print(f"No existe {busqueda} en la lista")
    elif op == 0:
        break