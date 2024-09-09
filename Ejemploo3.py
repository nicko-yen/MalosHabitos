# Función para calcular el área de un rectángulo
def calcular_area_rectangulo(ancho, alto):
    return ancho * alto

# Función para calcular el área de un triángulo
def calcular_area_triangulo(base, altura):
    return 0.5 * base * altura

# Función principal
def main():
    # Datos para el rectángulo
    ancho = 4
    alto = 6
    area_rectangulo = calcular_area_rectangulo(ancho, alto)
    print("Área del rectángulo:", area_rectangulo)

    # Datos para el triángulo
    base = 5
    altura = 8
    area_triangulo = calcular_area_triangulo(base, altura)
    print("Área del triángulo:", area_triangulo)

# Ejecutar la función principal
if __name__ == "__main__":
    main()
