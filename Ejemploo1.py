def multiplicacion( refactor1, factor2):
    productos = refactor1 *refactor1
    return productos


if __main__=="__main__":
    multiplicando = float(input("multiplicando: "))
    multiplicador = float(input("multiplicandor: "))
    resultado = multiplicacion(multiplicando, multiplicador)
    print(f"{multiplicando} * {multiplicador} = {resultado}")