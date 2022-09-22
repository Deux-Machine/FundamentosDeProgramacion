#Identifica si el numero por teclado es par o impar
"@Author Sebastian Alvarez"



numero = int(input("Ingrese el numero: "))


while numero != None:

    if numero % 2 == 0:
        print(f"El numero {numero} es par")
        numero = int(input("Ingrese otro numero: "))
    else:
        print(f"El numero {numero} es impar")
        numero = int(input("Ingrese otro numero: "))