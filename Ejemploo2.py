def calcular_resultado(a, b, c):
    """
    Calcula el resultado de la operación a * b + c.

    :param a: Primer número.
    :param b: Segundo número.
    :param c: Tercer número.
    :return: El resultado de la operación.
    """
    return a * b + c


def main():
    # Solicitar valores al usuario
    a = float(input("Ingrese el primer número (a): "))
    b = float(input("Ingrese el segundo número (b): "))
    c = float(input("Ingrese el tercer número (c): "))

    resultado = calcular_resultado(a, b, c)
    print("El resultado es:", resultado)


if __name__ == "__main__":
    main()
