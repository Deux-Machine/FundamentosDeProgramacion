#Impresion de numeros pares entre 0 al 100
"@Author Sebastian Alvarez"

i = 0
dic = []

while i >= 0:
    i += 1
    dic.append(i)

    if i == 100:
        for i in dic:
            if i % 2 == 0:
                print(f"El numero {i} es par")
        break
