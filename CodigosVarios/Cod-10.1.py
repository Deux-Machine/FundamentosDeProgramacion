#Indica que el numero ingresado es multiplo de 3
"@Author Sebastian Alvarez"

numero = int(input("Ingrese el numero para saber si es multiplo de 3: "))



while numero >= 0:

    if numero % 3 == 0:
        print(f"El numero {numero} es mutiplo de 3")
        numero = int(input("Ingrese otro numero: "))
    else:
        print(f"El numero {numero} NO es mutiplo de 3")
        numero = int(input("Ingrese otro numero: "))