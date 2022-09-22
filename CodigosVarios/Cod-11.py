#Imprime numeros del 1 al 100 y suma pares e impares
"@Author Sebastian Alvarez"

i = 0
dic = []

suma_pares = []
sum_impares = []

while i >= 0:
    i += 1
    dic.append(i)
    print(i)

    if i == 100:
        for x in dic:
            if x % 2 == 0:
                suma_pares.append(x)
                total1 = sum(suma_pares)
            elif x % 2 != 0:
                sum_impares.append(x)
                total2 = sum(sum_impares)

        print(f"La suma de pares es {total1}")
        print(f"La suma de impares es {total2}")
        break
