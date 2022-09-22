#Impresion y conteo de los multiplos de tres hasta numero ingresado por consola
"@Author Sebastian Alvarez"

numero = int(input("Ingrese el numero de conteo: "))

i = 0
conteo_multiplos = 0

while i != numero:
    i += 3
    conteo_multiplos += 1
    print(i)

    if i >= numero:
        print(f"El numero {numero} tiene {conteo_multiplos} multiplos")
        break
