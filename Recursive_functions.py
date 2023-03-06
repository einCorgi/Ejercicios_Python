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


print(recursiveFunction(5))
print(factorial(5))
