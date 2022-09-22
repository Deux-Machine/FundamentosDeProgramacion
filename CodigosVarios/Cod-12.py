#Imprime y cuenta los multiplos de 2 o 3 de 1 a 100
"@Author Sebastian Alvarez"

i = 0

multiplos_dos = []
multiplos_tres = []


while i >= 0 and i <= 100:
    i += 1
    
    if i % 2 == 0:
        multiplos_dos.append(i)
        print(f"El numero {i} es mutiplo de 2") 
        
    elif i % 3 == 0:
        multiplos_tres.append(i)
        print(f"El numero {i} es mutiplo de 3")
        
    elif i % 2 and i % 3:
        print(f"El numero {i} es mutiplo de 2 y 3")

print("Hay presente", len(multiplos_dos), "Multiplos de 2")
print("Hay presente", len(multiplos_tres), "Multiplos de 3")