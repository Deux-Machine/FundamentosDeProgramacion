#Impresion de numeros impares entre 0 al 100 y su cantidad
"@Author Sebastian Alvarez"

i = 0
dic = []

conteo_impares = 0

while i >= 0:
    i += 1
    dic.append(i)

    if i == 100:
        for i in dic:
            if i % 2 != 0:
                conteo_impares += 1
                print(f"El numero {i} es impar")
        print(f"Hay {conteo_impares} impares en total")
        break
