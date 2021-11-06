
def isPalindrome(inputWord):
    if inputWord == inputWord[::-1]:
        return True
    else:
        return False

print("**********Bienvenido al Detector De Palindromos*************")
isOver = False
while not isOver:
    inputWord = input("Ingrese la palabra u oración: ").lower().replace(" ","")
    if isPalindrome(inputWord):
        "Es palindromo"
    else:
        "No es palindromo"
    wantContinue = input("Desea Continuar? [Y] yes or [N] no")
    if wantContinue == 'N':
        isOver = True

