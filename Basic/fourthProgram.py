import random
adivina = int(input("Adivina el numero: "))
num = random.randint(1,100)
intentos = 5
isOver = False
while not isOver:
    intentos -= 1
    if intentos > 0:
        if adivina == num:
            print("Felicidades, adivinaste el numero en", intentos, "intentos")
            isOver = True
        elif adivina < num:
            print("El numero es mayor")
            print("Te quedan", intentos, "intentos")
        else:
            print("El numero es menor")
            print("Te quedan", intentos, "intentos")
        adivina = int(input("Adivina el numero: "))
    else:
        print("Perdiste, el numero era", num)
        isOver = True  
    