#  Basically, a recursive function is a function that can call itself in order to complete a certain task
def recursiveFunction(argument):
    if argument == 1:
        return 1
    else:
        return argument * recursiveFunction(argument - 1)


def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)


def Descendiente(numero):
    if numero == 1:
        print(1)
    else:
        print(numero)
        return Descendiente(numero-1)


def SegundoDescendiente(numero):
    if numero == 1:
        print(1)
    elif numero <= 0:
        print("valor incorrecto")
    else:
        print(numero)
        return SegundoDescendiente(numero-1)


print(recursiveFunction(5))
print(factorial(5))
Descendiente(5)
SegundoDescendiente(7)
