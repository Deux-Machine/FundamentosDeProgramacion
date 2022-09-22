#Suma de los primeros 100 numeros
"@Author Sebastian Alvarez"

i = 0
dic = []

while i >= 0:
    i += 1
    dic.append(i)
    #print(i)

    if i == 100:
        sumDic = sum(dic)
        print(f"La suma total es {sumDic}")
        break
