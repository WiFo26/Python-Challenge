import random

def run():
    name = """Hola mundo 'Como están' Yo "Estoy bien" gracias"""
    password = generatePassword()
    print("Your password is: " + "".join(password))
    print(name)

def generatePassword():
    password = []
    for i in range(15):
        password.append(random.choice(list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()")))
    return password

if __name__ == '__main__':
    run()


