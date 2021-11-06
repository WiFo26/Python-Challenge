def isPrime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

def run():
    numero  = int(input("Ingrese un numero: "))
    if isPrime(numero):
        print("El numero es primo")
    else:
        print("El numero no es primo")


if __name__ == '__main__':
    run()