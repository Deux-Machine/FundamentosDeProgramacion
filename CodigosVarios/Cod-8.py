#Identifica si el  numero es negativo o positivo
"@Author Sebastian Alvarez"


numero = int(input("Introduzca el numero: "))



while numero != None:
    if numero < 0:
        print(f"El numero {numero} es negativo")
        numero = int(input("Introduzca otro numero: "))
    elif numero > 0:
        print(f"El numero {numero} es positivo")
        numero = int(input("Introduzca otro numero: "))