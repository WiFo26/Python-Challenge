print("###### Conversor De Monedas (Soles-Dolares) #####")
isOver = False
while not isOver:
    print("Elija el tipo de moneda que tiene: ")
    print("1.-Soles \n2.-Dolares")
    currencyChoosen = input("Opción seleccionada: ")
    quantity = int(input("Ingrese la cantidad de monedas: "))
    change = 0
    currency = ''
    if currencyChoosen == '1':
        change = quantity * 0.25
        if change <= 1:
            currency = 'Dolar.'
        else:
            currency = 'Dolares.'    
    else:
        change = quantity * 4
        if change <= 1:
            currency = 'Sol.'
        else:
            currency = 'Soles.'  
    print(f"Usted tiene {change} {currency}")
    wantToContinue = input ('Desea continuar? Escriba "S" Sí o "N" No.\n')
    if wantToContinue == 'S':
        isOver = False
    else:
        isOver = True