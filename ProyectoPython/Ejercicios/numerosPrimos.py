primos = input()
a=primos.split(",")
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

for i in range(len(a)):
    if is_prime(int(a[i])):
        a[i] = str(int(a[i]) + 1)
    a[i] = int(a[i])
    
print(a)

