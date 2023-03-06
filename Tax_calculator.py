# Let´s define our function
def CalculadoraDeImpuestos():
    pago_sin_impuesto = float(input("Proporcione el pago sin impuesto: "))
    impuesto = float(input("Proporcione el monto del impuesto: "))

    pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto / 100)
    print(f"Pago con impuesto: {pago_total}")


CalculadoraDeImpuestos()
