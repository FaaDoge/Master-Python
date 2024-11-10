aprobados=0
reprobados=0

for i in range (1,16):
    print("Ingresa notas")
    nota=int(input())
    if nota < 51:
        reprobados+=1
    else:
        aprobados+=1

print(f"Aprobados {aprobados} y reprobados {reprobados}")