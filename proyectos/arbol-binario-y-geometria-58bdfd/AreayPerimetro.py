import math

while True:
    opcion = int(input("Ingresa la figura a calcular:\n 1. Cuadrado\n 2. Circulo \n 3. Triangulo \n 4. Salir \n"))
    area = None
    perimetro = None

    match opcion:
        case 1:
            lado = float(input("Ingresa la medida de un lado: "))
            area = lado * lado
            perimetro = lado * 4
        case 2:
            radio = float(input("Ingresa el radio del circulo: "))
            area = math.pi * (radio * radio)
            perimetro = radio * 2 * math.pi
        case 3:
            lado1 = float(input("Ingresa la medida del primer lado: "))
            lado2 = float(input("Ingresa la medida del segundo lado: "))
            lado3 = float(input("Ingresa la medida del tercer lado: "))
            perimetro = lado1 + lado2 + lado3
            s = perimetro / 2
            area = math.sqrt(s * (s - lado1) * (s - lado2) * (s - lado3))
        case 4:
            break
        case _:
            print("Esa no es una opcion valida")

    if area is not None and perimetro is not None:
        print(f"El area de la figura es: {area}, y su perimetro es: {perimetro}")
    
