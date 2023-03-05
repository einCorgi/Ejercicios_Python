def multiplication(*args):  # The args parameter can receive A TUPLE
    result = 1
    for i in args:
        result *= i
    return result  # I must put attention to this detail, the return function...
    # The identation IS A MUST when trying to get the result we wanted ;(


print(multiplication(2, 3, 4, 5, 6))
