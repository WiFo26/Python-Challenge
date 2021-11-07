poblaList1 = False
buzz = []
zurg = []
while not poblaList1:
    addSoldier = input()
    if addSoldier == "end" and len(buzz) == 0:
        print("Por favor ingrese un soldado para el primer ejercito.")
    elif addSoldier == "end" and len(buzz) != 0:
        poblaList1 = True
        poblaList2 = False
        while not poblaList2:
            addSoldier2 = input()
            if addSoldier2 == "end" and len(zurg) == 0:
                print("Por favor ingrese un soldado para el segundo ejercito.")
            elif addSoldier2 == "end" and len(zurg) != 0:
                battleOver = False
                while not battleOver:
                    if buzz[0] > zurg[0]:
                        print("Buzz ha ganado esta ronda!")
                        zurg.pop(0)
                        buzz[0] -= 1
                    else:
                        print("Zurg ha ganado esta ronda!")
                        buzz.pop(0)
                        zurg[0] -= 1
                    if len(buzz) == 0:
                        print("El malvado emperador Zurg tomara control de la Unimente!")
                        break
                    elif len(zurg) == 0:
                        print("Buzz ha vencido!")
                        break
                break
            else:
                zurg.append(int(addSoldier2))
    else:
        buzz.append(int(addSoldier))
