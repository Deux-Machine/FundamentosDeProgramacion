#Impresion de numeros naturales desde la unidad hasta la entrada por teclado
"@Author Sebastian Alvarez"

numero = int(input("Ingrese el numero de conteo: "))

i = 0

while i != numero:
    i += 1
    print(i)

    if i == numero:
        break

