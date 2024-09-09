def multiplicacion( refactor1, factor2):
    producto = refactor1 *refactor1
    return producto

if __main__=="__main__":
    multiplicando = float(input("multiplicando: "))
    multiplicador = float(input("multiplicandor: "))
    resultado = multiplicacion(multiplicando, multiplicador)
    print(f"{multiplicando} * {multiplicador} = {resultado}")