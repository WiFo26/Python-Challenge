listado = input().split(",")
cantidad = int(listado[1])
precios = list(map(int,listado[2:]))
precios = sorted(precios)
precioFinal = 0
for i in range(cantidad):
    precioFinal += precios[i]
print(f"{listado[0]}: ${precioFinal}")