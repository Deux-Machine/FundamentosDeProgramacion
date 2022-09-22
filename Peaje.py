#Control de parqueadero
print("""TARIFARIO
Carro: 3mil por hora
Moto:  2mil por hora
Cicla: 1mil por hora
Lavado auto (extra): 20mil, se obsequian dos horas gratis""")

ingresos = input("\r\nIndique si es Entrada (E) o Salida (S): ")

#Diccionario que almacena multiusuario
diccUsuario = {}

while ingresos == ingresos:

    #Primer condicional principal que se ejecuta si es Entrada (E)
    if ingresos == "E" or ingresos == "e":
        tipoVehiculo = (int(input("""\r\nSeleccione por favor el tipo de vehiculo.
        1.Carro
        2.Moto
        3.Bicicleta
        Indique el numero: """)))

        #Se ejecutara si el vehiculo es un CARRO
        if tipoVehiculo == 1:
            placa = input("\r\nIngrese el numero de placa: ")
            horaIngreso = int(input("\r\nIndique hora de ingreso: "))
            servicioExtra = str(input("\r\nEl usuario hara uso de servicios extra, Si/No: "))
            #Se ejecutara si se accede al servicio extra
            if servicioExtra == "Si" or servicioExtra == "si":
                usoServicio = input("\r\nIngrese numero de celular: ")
                arreglo = {placa : [tipoVehiculo, horaIngreso, servicioExtra, usoServicio]}
                diccUsuario.update(arreglo)
                print("Cliente Guardado")
                print(diccUsuario)
                ingresos = input("\r\nIndique si es Entrada (E) o Salida (S): ")
            #Se ejecutara si NO se accede al servicio extra
            elif servicioExtra == "No" or servicioExtra == "no":
                arreglo = {placa : [tipoVehiculo, horaIngreso, servicioExtra]}
                diccUsuario.update(arreglo)
                print("Maldito hambriento y chichipato")
                ingresos = input("\r\nIndique si es Entrada (E) o Salida (S): ")

        #Se ejecutara si el vehiculo es una MOTO
        elif tipoVehiculo == 2:
            placa = input("\r\nIngrese el numero de placa: ")
            horaIngreso = int(input("\r\nIndique hora de ingreso: "))
            #Se ejecutara si se accede al servicio extra
            servicioExtra = input("\r\nEl usuario hara uso de servicios extra, Si/No: ")
            if servicioExtra == "Si" or servicioExtra == "si":
                usoServicio = input("\r\nIngrese numero de celular: ")
                arreglo = {placa : [tipoVehiculo, horaIngreso, servicioExtra, usoServicio]}
                diccUsuario.update(arreglo)
                print("Cliente Guardado")
                ingresos = input("\r\nIndique si es Entrada (E) o Salida (S): ")
            #Se ejecutara si NO se accede al servicio extra                
            elif servicioExtra == "No" or servicioExtra == "no":
                arreglo = {placa : [tipoVehiculo, horaIngreso, servicioExtra]}
                diccUsuario.update(arreglo)
                print("Maldito hambriento y chichipato")
                ingresos = input("\r\nIndique si es Entrada (E) o Salida (S): ")

        #Se ejecutara si el vehiculo es una BICICLETA
        elif tipoVehiculo == 3:
            cedula = int(input("\r\nIngrese el numero de cedula: "))
            horaIngreso = int(input("\r\nIndique hora de ingreso: "))
            servicioExtra = input("\r\nEl usuario hara uso de servicios extra, Si/No: ")
            #Se ejecutara si se accede al servicio extra
            if servicioExtra == "Si" or servicioExtra == "si":
                usoServicio = input("\r\nIngrese numero de celular: ")
                arreglo = {cedula : [tipoVehiculo, horaIngreso, servicioExtra, usoServicio]}
                diccUsuario.update(arreglo)
                print("Cliente Guardado")
                ingresos = input("\r\nIndique si es Entrada (E) o Salida (S): ")
            #Se ejecutara si NO se accede al servicio extra                 
            elif servicioExtra == "No" or servicioExtra == "no":
                arreglo = {cedula : [tipoVehiculo, horaIngreso, servicioExtra]}
                diccUsuario.update(arreglo)
                print("Maldito hambriento y chichipato")
                ingresos = input("\r\nIndique si es Entrada (E) o Salida (S): ")
    
      
    #Segundo condicional principal que se ejecuta si es Salida (S)
    if ingresos == "S" or ingresos == "s":
        placa = input("\r\nIngrese el numero de placa que sea buscar: ")
        horaSalida = int(input("\r\nIndique hora de salida: "))
        
        #Ciclo que permite iterar dentro del diciconario para buscar la placa
        if placa is not diccUsuario:
            for placa in diccUsuario:
                    diccUsuario[placa].append(horaSalida)
                    break
        
        #Condicional, se ejecuta si el vehiculo es CARRO y NO se aplica descuento
        if diccUsuario[placa][0] == 1 and (diccUsuario[placa][2] == "No" or diccUsuario[placa][2] == "no"):
            diferenciaTiempo = diccUsuario[placa][1] - diccUsuario[placa][3]
            valorTarifa = 3 * (diferenciaTiempo * -1)
            print(f'''El carro {placa} estuvo {diferenciaTiempo * -1} hora(s), TOTAL: ${valorTarifa} COP.
            NO APLICA DESCUENTO''')
            ingresos = input("\r\nIndique si es Entrada (E) o Salida (S): ")

        #Condicional, se ejecuta si el vehiculo es CARRO y si se aplica descuento
        elif diccUsuario[placa][0] == 1 and (diccUsuario[placa][2] == "Si" or diccUsuario[placa][2] == "si"):
            diferenciaTiempo = diccUsuario[placa][1] - diccUsuario[placa][4]
            descuento = (diferenciaTiempo * -1) - 2
            valorTarifa = 3 * descuento
            print(f'''El carro {placa} estuvo {diferenciaTiempo * -1} hora(s), TOTAL: ${valorTarifa} COP.
            SE APLICA DESCUENTO''')
            ingresos = input("\r\nIndique si es Entrada (E) o Salida (S): ")
        
        #Condicional, se ejecuta si el vehiculo es una MOTO y NO se aplica descuento
        elif diccUsuario[placa][0] == 2 and (diccUsuario[placa][2] == "No" or diccUsuario[placa][2] == "no"):
            diferenciaTiempo = diccUsuario[placa][1] - diccUsuario[placa][3]
            valorTarifa = 2 * (diferenciaTiempo * -1)
            print(f'''La moto {placa} estuvo {diferenciaTiempo * -1} hora(s), TOTAL: ${valorTarifa} COP.
            NO APLICA DESCUENTO''')
            ingresos = input("\r\nIndique si es Entrada (E) o Salida (S): ")
        
        #Condicional, se ejecuta si el vehiculo es una MOTO y se aplica descuento
        elif diccUsuario[placa][0] == 2 and (diccUsuario[placa][2] == "Si" or diccUsuario[placa][2] == "si"):
            diferenciaTiempo = diccUsuario[placa][1] - diccUsuario[placa][4]
            descuento = (diferenciaTiempo * -1) - 2
            valorTarifa = 3 * descuento
            print(f'''La Moto {placa} estuvo {diferenciaTiempo * -1} hora(s), TOTAL: ${valorTarifa} COP.
            SE APLICA DESCUENTO''')
            ingresos = input("\r\nIndique si es Entrada (E) o Salida (S): ")

        #Condicional, se ejecuta si el vehiculo es una Bicicleta y NO se aplica descuento
        elif diccUsuario[placa][0] == 3 and (diccUsuario[placa][2] == "No" or diccUsuario[placa][2] == "no"):
            diferenciaTiempo = diccUsuario[placa][1] - diccUsuario[placa][3]
            valorTarifa = 1 * (diferenciaTiempo * -1)
            print(f'''La moto {cedula} estuvo {diferenciaTiempo * -1} hora(s), TOTAL: ${valorTarifa} COP.
            NO APLICA DESCUENTO''')
            ingresos = input("\r\nIndique si es Entrada (E) o Salida (S): ")
        
        #Condicional, se ejecuta si el vehiculo es una Bicicleta y se aplica descuento
        elif diccUsuario[placa][0] == 3 and (diccUsuario[placa][2] == "Si" or diccUsuario[placa][2] == "si"):
            diferenciaTiempo = diccUsuario[cedula][1] - diccUsuario[cedula][4]
            descuento = (diferenciaTiempo * -1) - 2
            valorTarifa = 1 * descuento
            print(f'''La Bicicleta {cedula} estuvo {diferenciaTiempo * -1} hora(s), TOTAL: ${valorTarifa} COP.
            SE APLICA DESCUENTO''')
            ingresos = input("\r\nIndique si es Entrada (E) o Salida (S): ")
