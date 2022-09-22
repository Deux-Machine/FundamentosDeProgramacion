#Solo se permite introducir S o N
"@Author Sebastian Alvarez"


e = input(str("Ingrese S o N: "))

a1 = "s"
a2 = "S"
b1 = "N"
b2 = "n"

while e != None:
    
    if e == a1 or e == a2:
        print("Correcto")
        break 
    elif e == b1 or e == b2:
        print("Correcto")
        break 
    else:
        print("Letra invalida, intenta de nuevo")
        e = input("Ingrese S o N: ")